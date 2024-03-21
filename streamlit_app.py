import streamlit as st
import pandas as pd

# Function to load data from uploaded file
def load_data(file):
    try:
        data = pd.read_csv(file) if file.name.endswith('csv') else pd.read_excel(file)
        return data
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Main function to run the Streamlit app
def main():
    st.title('CSV and XLS Data Visualizer')
    
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        if data is not None:
            st.write("### Data Preview:")
            st.write(data)
            
            # Add interactive visualizations here
            
        else:
            st.error("Failed to load data from the file.")
    
if __name__ == '__main__':
    main()
