import streamlit as st
import pandas as pd
import numpy as np

st.title("Teemu Kuutti's first streamlit app")

import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Streamlit Chart")

# Create sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Display chart
st.line_chart(data)

