import streamlit as st
import gspread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests, json

st.set_page_config(page_title="Nifty Stuff",
                    page_icon=":bar_chart:",
                    layout="wide")

st.title("Welcome to StreamLit")
