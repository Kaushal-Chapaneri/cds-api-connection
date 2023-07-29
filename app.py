import streamlit as st
from datetime import datetime, timedelta
from streamlit_folium import st_folium
import folium
import plotly.express as px

from climate_data_store_connection import ClimateDataStoreConnection

st.set_page_config(page_title="CDS API", page_icon="🌤️")

st.title("ClimateDataStoreConnection")

with st.form("data_fetch_api"):

    col1, col2 = st.columns(2)

    params = st.multiselect(
        'Select Weather Parameters', help="CDS offers many parameter but few selected for demo purpose.",
        options=['Ambient Temperature (°C)', 'Dew Point Temperature (°C)', 'Surface Pressure (kPa)']
    )

    date = st.date_input('Select a date',
                         value=datetime.today() - timedelta(days=6),
                         min_value=datetime.fromisoformat('2023-01-01'),
						 max_value=datetime.today() - timedelta(days=6))
    
    st.write("Click on map to select location")
    
    # https://franekjemiolo.pl/using-selected-position-map-form-streamlit/
    DEFAULT_LATITUDE = 23.25
    DEFAULT_LONGITUDE = 72.45

    m = folium.Map(location=[DEFAULT_LATITUDE, DEFAULT_LONGITUDE], zoom_start=5)

    # The code below will be responsible for displaying 
    # the popup with the latitude and longitude shown
    m.add_child(folium.LatLngPopup())

    f_map = st_folium(m, width=670, height=500)

    selected_latitude = DEFAULT_LATITUDE
    selected_longitude = DEFAULT_LONGITUDE

    if f_map.get("last_clicked"):
        selected_latitude = f_map["last_clicked"]["lat"]
        selected_longitude = f_map["last_clicked"]["lng"]

    submitted = st.form_submit_button("Submit")
    
if submitted:

    st.success(f"Selected location: {selected_latitude}, {selected_longitude}")

    if params:            

        # API understands these names for input
        param_mapping_ip = {
            "Ambient Temperature (°C)":"2m_temperature",
            "Dew Point Temperature (°C)": "2m_dewpoint_temperature",
            "Surface Pressure (kPa)":"surface_pressure"
        }

        # API returns these names in output
        param_mapping_op = {
            "t2m": "Ambient Temperature (°C)",
            "d2m": "Dew Point Temperature (°C)",
            "sp": "Surface Pressure (kPa)"
        }

        # Preparing dictionary to send to API
        data = {
                'product_type': 'reanalysis',
                'format': 'netcdf',

                'variable': [param_mapping_ip[p] for p in params],
                'year': [
                    str(date.year),
                ],
                'month': [
                    str(date.month),
                ],
                'day': [
                    str(date.day),
                ],
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],
                'area': [
                    selected_latitude, selected_longitude, 
                    selected_latitude,selected_longitude,
                ],
                }

        with st.spinner("Fetching weather data..."):

            # Connection to API
            conn = st.experimental_connection("", type=ClimateDataStoreConnection)
            df = conn.query(data)

        with st.spinner("Plotting..."):

            # unit conversion
            if "t2m" in df.columns:
                df["t2m"] = df["t2m"] - 273.15
            if "d2m" in df.columns:
                df["d2m"] = df["d2m"] - 273.15
            if "sp" in df.columns:
                df["sp"] = df["sp"] / 1000

            df.columns = [param_mapping_op[c] for c in df.columns]

            for i in range(df.shape[1]):
                fig = px.line(x=df.index, y=df.iloc[:, i], labels={'x':'Time', 'y':df.columns[i]},
                               title="Time series plot of "+df.columns[i])
                st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("Select minimum 1 weather parameter")
        