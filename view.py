import streamlit as st
import streamlit.components.v1 as components

with open('locations.html', 'r') as f:
    html = f.read()

type = st.radio("Choose:", ["Locations", "Route", "Model"])

if type == "Locations":
    components.html("<html><body><h1>Hello, World</h1></body></html>")