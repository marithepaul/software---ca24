import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Streamlit Setup and User Interaction
st.title("My First Streamlit App")
st.write("This app is a demonstration of various Streamlit features like user input, data manipulation, and visualization.")

# 2. User Input Controls
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100)

st.write(f"Hello {name}, you are {age} years old.")

# 3. Button Interaction
if st.button("Say hello"):
    st.write("Hello there!")

# 4. Data Manipulation and Display
# Creating a simple DataFrame with two columns
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [24, 30, 35, 40, 29]
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here is the DataFrame:")
st.dataframe(df)

# 5. Data Visualization
# Generating a histogram of the 'Age' column
fig, ax = plt.subplots()
ax.hist(df["Age"], bins=5, color='blue', alpha=0.7)
ax.set_title("Histogram of Ages")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")

# Display the plot in Streamlit
st.pyplot(fig)

# 6. Advanced Layouts
col1, col2 = st.columns(2)

with col1:
    st.write("Hello")

with col2:
    st.write("World")

# Expander for additional information
with st.expander("More Information"):
    st.write("This is a sample Streamlit application")
