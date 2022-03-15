import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **Exploratory Data Analysis (EDA) Application**

This is an **Exploratory Data Analysis (EDA) Application** created in Streamlit using the **pandas-profiling** library.
''')

# Upload CSV data
with st.sidebar.header('Upload your CSV data file'):
    uploaded_file = st.sidebar.file_uploader("Upload file to analyze", type=["csv"])

st.sidebar.markdown("""
This application is built using Python and Streamlit by: 
[Aweda Oluwanifemi](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/), Twitter: [@Adenifesimi1](https://twitter.com/adenifesimi1)

\nTutorials from [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
