import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

# Upload file
upload_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if upload_file is not None:
    try:
        # Read the uploaded Excel file
        if upload_file.name.endswith('.xls'):
            df = pd.read_excel(upload_file, engine='xlrd')
        else:
            df = pd.read_excel(upload_file)
        
        # Display Data Preview
        st.subheader("Data Preview")
        st.write(df.head())
        
        # Display Data Summary
        st.subheader("Data Summary")
        st.write(df.describe())
        
        # Filter Data
        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select Column to Filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select Value to Filter", unique_values)
        
        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)
        
        # Plot Data
        st.subheader("Plot Data")
        x_column = st.selectbox("Select x-axis column to plot", columns)
        y_column = st.selectbox("Select y-axis column to plot", columns)
        
        if st.button("Generate Plot"):
            if pd.api.types.is_numeric_dtype(filtered_df[y_column]):
                st.line_chart(filtered_df.set_index(x_column)[y_column])
            else:
                st.error(f"Cannot plot non-numeric data for {y_column}. Please select a numeric column.")
    
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.warning("Please upload an Excel file.")
