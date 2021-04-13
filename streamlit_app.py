import pickle
import re

import altair as alt
import lightgbm
import lime
import lime.lime_tabular
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import shap
import streamlit as st
import streamlit.components.v1 as components
from lightgbm import LGBMClassifier
# from lightgbm_with_simple_features import *
from PIL import Image
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Streamlit Deployment Test", page_icon='✅')
st.title('🔨 Selenium Test for Streamlit Sharing Deployment')
