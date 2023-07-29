from streamlit.connections import ExperimentalBaseConnection
import cdsapi
import pandas as pd
import xarray as xr
import os
from datetime import datetime

class ClimateDataStoreConnection(ExperimentalBaseConnection[cdsapi.api.Client]):

    def _connect(self) -> cdsapi.api.Client:

        conn = cdsapi.Client()

        return conn
    
    def retrieve(self) -> cdsapi.api.Client.retrieve:

        return self._instance.retrieve
    
    def query(self, query_param):

        def _parse_data(path: str) -> pd.DataFrame:

            data = xr.open_dataset(path)
            df = data.to_dataframe()
            df.reset_index(inplace=True)

            df.index = pd.to_datetime(df['time'])
            df = df.drop(columns=['longitude', 'latitude', 'time'])

            return df

        query_param['product_type'] = 'reanalysis'
        query_param['format'] = 'netcdf'

        # adding time in file name to avoid overlapping
        data_path = 'download_'+str(datetime.now()).replace(":","-")+'.nc'

        ret = self.retrieve()

        ret('reanalysis-era5-single-levels',
            query_param,
            data_path)
        
        final_df = _parse_data(data_path)

        # deleting NetCDF file to free up space
        os.remove(data_path)

        return final_df
        