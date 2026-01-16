import streamlit as st
import pandas as pd
import numpy as np

st.title("week 1 assignment")
st.write("By Teemu Kuutti")

# Create sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Display chart
st.line_chart(data)

