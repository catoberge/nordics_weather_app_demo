import pandas as pd
import streamlit as st
import pygwalker as pyg

st.set_page_config(
    page_title="Nordics Weather App Demo",
    page_icon=":rainbow:",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data():
    df = pd.read_csv("data/nordics_weather.csv")
    return df


df = load_data()


st.title("Nordics Weather App Demo :rainbow:")
st.subheader("Test av Pygwalker bibliotek")


# Display Pygwalker
def load_config(file_path):
    with open(file_path, "r") as config_file:
        config_str = config_file.read()
    return config_str


config = load_config("config.json")

pyg.walk(df, env="Streamlit", dark="dark", spec=config)
