# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from utils import *


# df = pd.read_csv(r"D:\spotify\data\processed\analytics_ready\yearly_trends.csv")

# st.header("📈 Music Trends Over Time")

# feature = st.selectbox(
#     "Select Audio Feature",
#     ["danceability", "energy", "valence", "tempo"]
# )

# fig = px.line(
#     df,
#     x="year",
#     y=feature,
#     title=f"{feature.capitalize()} Over Time"
# )

# st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
from utils import music_trends_multifeature, music_trend_highlight

@st.cache_data
def load_data():
    return pd.read_csv(r"D:\spotify\data\processed\analytics_ready\yearly_trends.csv")

df = load_data()

st.title("📈 Music Trends Over Time")
st.caption("How core Spotify audio features have evolved year by year")

features = ["danceability", "energy", "valence", "tempo"]

st.subheader("🎵 Multi-Feature Trend Comparison")

selected_features = st.multiselect(
    "Select audio features",
    features,
    default=["danceability", "energy"]
)

if selected_features:
    fig = music_trends_multifeature(df, selected_features)
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
    "📌 **Insight:** Energy and danceability peaked in the early 2010s, dipped around 2020, and are now rebounding."
)

st.subheader("🕒 Feature Trend Highlight")

highlight_feature = st.selectbox(
    "Highlight a feature",
    features
)

fig2 = music_trend_highlight(df, highlight_feature)
st.plotly_chart(fig2, use_container_width=True)

