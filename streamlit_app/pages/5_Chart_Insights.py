# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from utils import *

# df = pd.read_csv(r"D:\spotify\data\processed\analytics_ready\chart_vs_nonchart.csv")

# st.header("🔥 Chart vs Non-Chart Songs")

# feature = st.selectbox(
#     "Select Feature",
#     ["energy", "danceability", "valence", "loudness"]
# )

# fig = px.box(
#     df,
#     x="is_chart_song",
#     y=feature,
#     title=f"{feature.capitalize()} Comparison"
# )

# fig.update_xaxes(
#     tickvals=[False, True],
#     ticktext=["Non-Chart", "Chart"]
# )

# st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
from utils import (
    chart_vs_nonchart_mean,
    chart_feature_difference
)

@st.cache_data
def load_data():
    return pd.read_csv(r"D:\spotify\data\processed\analytics_ready\chart_vs_nonchart.csv")

df = load_data()

st.title("🔥 Chart vs Non-Chart Analysis")
st.caption("Understanding how hit songs differ from non-charting tracks")

features = ["energy", "danceability", "valence", "loudness", "tempo"]

col1, col2 = st.columns([1, 2])

with col1:
    feature = st.selectbox("Select feature", features)

with col2:
    fig1 = chart_vs_nonchart_mean(df, feature)
    st.plotly_chart(fig1, use_container_width=True)

st.markdown(
    "📌 **Insight:** Chart-topping songs consistently show higher energy and loudness on average."
)

st.subheader("📈 Feature Impact Ranking")

fig2 = chart_feature_difference(df, features)
st.plotly_chart(fig2, use_container_width=True)
