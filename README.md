# ClimateDataStoreConnection Example

[CDS](https://cds.climate.copernicus.eu/cdsapp#!/home) Provides Weather data for entire world from 1940 to present (today - 6 days) for free. 
A simple example app for using ClimateDataStoreConnection in Streamlit.

## Demo
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

- Create an account to get API Key [Register](https://cds.climate.copernicus.eu/user/register).
- Follow instructions to Store CDS API key [Linux](https://cds.climate.copernicus.eu/api-how-to#install-the-cds-api-client), [Windows](https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+Windows), [macOS](https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+macOS)

### Run the app

```sh
streamlit run app.py
```
