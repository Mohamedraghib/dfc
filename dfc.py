import streamlit as st
import pandas as pd

# Load the Excel file
file_path = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if file_path:
    df = pd.read_excel(file_path)

    # Display the DataFrame
    st.write("DataFrame:")
    st.dataframe(df)

    # Sidebar for filters
    st.sidebar.header("Filter Options")

    # Select columns to filter
    columns = st.sidebar.multiselect("Select columns to filter by", df.columns)

    # Dictionary to store selected values for each column
    filters = {}

    for column in columns:
        unique_values = df[column].unique()
        selected_values = st.sidebar.multiselect(f"Select values for '{column}'", unique_values)
        filters[column] = selected_values

    # Filter DataFrame based on selected values
    if filters:
        filtered_df = df.copy()
        for column, selected_values in filters.items():
            if selected_values:
                filtered_df = filtered_df[filtered_df[column].isin(selected_values)]

        st.write("Filtered DataFrame:")
        st.dataframe(filtered_df)
