import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 7, 9]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("My First Chart")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

st.pyplot(fig)


st.title("week 1 assignment")
st.write("By Teemu Kuutti")

# Create sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.title("week 2 assignment")
st.write("By Teemu Kuutti")
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 7, 9]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("My First Chart")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

st.pyplot(fig)
