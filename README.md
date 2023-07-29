# ClimateDataStoreConnection Example

[CDS](https://cds.climate.copernicus.eu/cdsapp#!/home){:target="_blank" rel="noopener"} Provides Weather data for entire world from 1940 to present (today - 6 days) for free. 
A simple example app for using ClimateDataStoreConnection in Streamlit.

## Demo [Live](https://cds-api-connection.streamlit.app/){:target="_blank" rel="noopener"}
<img src="demo_app.gif" alt="demo" style="margin-top:50px"></img>

## Setup

### Install Python

Developed and tested with Python3.10

### Install dependencies

Create a python environment.
```sh
pip install -r requirements.txt
```
### Register on CDS

- Create an account to get API Key [Register](https://cds.climate.copernicus.eu/user/register){:target="_blank" rel="noopener"}.
- Follow instructions to Store CDS API key [Linux](https://cds.climate.copernicus.eu/api-how-to#install-the-cds-api-client){:target="_blank" rel="noopener"}, [Windows](https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+Windows){:target="_blank" rel="noopener"}, [macOS](https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+macOS){:target="_blank" rel="noopener"}
- Or set API Key in Environment variables
  ```
  CDSAPI_URL = "https://cds.climate.copernicus.eu/api/v2"
  CDSAPI_KEY = "<api-key>"
  ```

### Run the app

```sh
streamlit run app.py
```
