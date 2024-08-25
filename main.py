import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
upload_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if upload_file is not None:
    df = pd.read_excel(upload_file)
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select Columns to Filter by", columns)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Select Values to Filter", unique_value)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x_axis column to plot", columns)
    y_column = st.selectbox("Select y_axis column to plot", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.warning("Please upload an Excel file.")
