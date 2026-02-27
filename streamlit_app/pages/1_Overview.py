import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv(r"D:\spotify\data\processed\analytics_ready\yearly_trends.csv")

df = load_data()

st.title("🎧 Spotify Music Analytics Dashboard")
st.caption("Understanding how music characteristics, genres, and popularity evolve over time")

st.markdown(
    """
    This dashboard helps analyze:
    - How audio features evolved over the years  
    - What differentiates chart-topping songs  
    - How genres vary in sound characteristics  
    - How popularity relates to audio features  
    """
)

st.subheader("📅 Coverage & Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Years Covered", f"{df['year'].min()} – {df['year'].max()}")

with col2:
    st.metric("Average Popularity", f"{df['popularity'].mean():.2f}")

st.subheader("📊 Sample Aggregated Data")
st.dataframe(df.head(), use_container_width=True)
