import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

st.header("st.write")

st.write("Hello, *World!* :sunglasses:")

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

st.write(df)

st.write("Below is a DataFrame:", df, "Above is a DataFrame.")

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ["a", "b", "c"]
)

c = alt.Chart(df2).mark_circle().encode(
    x="a", y="b", size="c", tooltip=["a", "b", "c"]
)
st.write(c)