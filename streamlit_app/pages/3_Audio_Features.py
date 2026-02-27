# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from utils import *

# pca_df = pd.read_csv(r"D:\spotify\data\processed\analytics_ready\audio_feature_pca.csv")

# st.header("🎼 Audio Feature Intelligence")

# fig = px.scatter(
#     pca_df,
#     x="PC1",
#     y="PC2",
#     color="popularity",
#     title="PCA of Spotify Audio Features",
#     color_continuous_scale="viridis"
# )

# st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
from utils import pca_popularity_filter, pca_top_hits

@st.cache_data
def load_data():
    return pd.read_csv(r"D:\spotify\data\processed\analytics_ready\audio_feature_pca.csv")

df = load_data()

st.title("🎼 Audio Feature Intelligence")
st.caption("Exploring how songs cluster sonically and how popularity relates to sound")

st.subheader("🎯 Popularity-Filtered PCA")

threshold = st.slider(
    "Minimum popularity threshold",
    min_value=0,
    max_value=100,
    value=70
)

fig1 = pca_popularity_filter(df, threshold)
st.plotly_chart(fig1, use_container_width=True)

st.markdown(
    "📌 **Insight:** Popular songs tend to cluster within specific regions of the audio feature space."
)

st.subheader("🔥 Top 10% Popular Songs")

fig2 = pca_top_hits(df)
st.plotly_chart(fig2, use_container_width=True)
