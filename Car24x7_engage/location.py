import requests
import pandas as pd
import numpy as np
import streamlit as st
from multipage_streamlit import State


#st.set_page_config(layout="wide")


def app():
   car_manufacturer_data=pd.read_csv("C:/Users/Asus/Downloads/Book3.csv")
   st.title("Competitons in Locality")
   st.write(car_manufacturer_data)
   r=requests.get('https://get.geojs.io/')

   ip_request=requests.get('https://get.geojs.io/v1/ip.json')
   ipAdd=ip_request.json()['ip']

   url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
   geo_request=requests.get(url)
   geo_data=geo_request.json()



   region=geo_data['region']
   city=geo_data['city']
   latitude=geo_data['latitude']
   longitude=geo_data['longitude']
   ans=[]
   ans.append(float(latitude))
   ans.append(float(longitude))

#st.subheader("---->Your Current Location is     :"+region)
#st.subheader("---->Your Current City is:"+city)

   st.sidebar.title("Current Location")
   st.sidebar.subheader(region)
   st.sidebar.subheader(city)


   car_manufacturer_data=car_manufacturer_data.loc[car_manufacturer_data['State']==region]
   num=car_manufacturer_data.Manufacturer.count()

   st.subheader("Companies in Town")
   st.write(car_manufacturer_data.Manufacturer)

   df=pd.DataFrame([ans],columns=['lat','lon'])
   st.map(df)

