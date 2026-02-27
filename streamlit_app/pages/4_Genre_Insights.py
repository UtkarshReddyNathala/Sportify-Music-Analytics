# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from utils import *

# df = pd.read_csv(r"D:\spotify\data\processed\analytics_ready\genre_audio_analysis.csv")

# st.header("🎧 Genre Insights")

# feature = st.selectbox(
#     "Select Feature",
#     ["energy", "danceability", "valence", "acousticness"]
# )

# fig = px.box(
#     df,
#     x="track_genre",
#     y=feature,
#     title=f"{feature.capitalize()} by Genre"
# )

# st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
from utils import (
    genre_distribution_bar,
    genre_average_feature_bar,
    genre_share_pie
)

@st.cache_data
def load_data():
    return pd.read_csv(r"D:\spotify\data\processed\analytics_ready\genre_audio_analysis.csv")

df = load_data()

st.title("🎧 Genre Insights")
st.caption("Comparing how audio features vary across music genres")

st.subheader("📊 Genre Distribution")

fig1 = genre_distribution_bar(df)
st.plotly_chart(fig1, use_container_width=True)

feature = st.selectbox(
    "Select audio feature",
    ["energy", "danceability", "valence", "acousticness"]
)

st.subheader(f"🎚 Average {feature.capitalize()} by Genre")

fig2 = genre_average_feature_bar(df, feature)
st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    "📌 **Insight:** Rock and alternative genres show higher energy, while pop remains more consistent."
)

st.subheader("🥧 Genre Share (Top 10)")

fig3 = genre_share_pie(df, top_n=10)
st.plotly_chart(fig3, use_container_width=True)
