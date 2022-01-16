import pandas as pd
import numpy as np
import streamlit as st

st.title("俺の 1st app")

st.write("データフレーム")
st.write(
    pd.DataFrame({
        "1st column": [1, 2, 3, 4],
        "2st column": [10, 20, 30, 40]
    })
)

"""
# My 1st app
# マジックコマンド
## マジックコマンド
### マジックコマンド
こんな感じでマジックコマンドを使用できる。MarkDown対応。
"""
if st.checkbox("Show DataFrame"):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ["a", "b", "c"]
    )

    st.line_chart(chart_df)
