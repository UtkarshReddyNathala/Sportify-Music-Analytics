import streamlit as st

st.set_page_config(
    page_title="Spotify Music Analytics",
    page_icon="🎧",
    layout="wide"
)

# -------------------- SIDEBAR --------------------
st.sidebar.title("🎧 Spotify Insights")
st.sidebar.caption("Interactive analysis of global music trends")

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit • Plotly • Pandas")

# -------------------- MAIN PAGE CONTENT --------------------
st.title("🎧 Spotify Music Analytics Dashboard")
st.caption(
    "A data-driven exploration of global music trends, audio features, genres, and chart performance using Spotify data."
)

st.markdown("---")

# -------------------- PROJECT OVERVIEW --------------------
st.subheader("📌 Project Overview")

st.markdown(
    """
This project analyzes **Spotify music data from 2009 to 2023** to understand how songs evolve over time,
what differentiates **chart-topping tracks**, and how **genres vary in their audio characteristics**.

The goal is to combine **data analytics, visualization, and exploratory intelligence**
to answer questions such as:
- How has popular music changed over the years?
- What audio features are common in hit songs?
- How do different genres differ sonically?
- How does popularity relate to sound patterns?
"""
)

# -------------------- DATA USED --------------------
st.subheader("📊 Datasets Used")

st.markdown(
    """
The analysis is built using multiple Spotify datasets sourced from Kaggle, including:

- **Spotify Global Music Dataset (2009–2025)**  
  → Track metadata, popularity, release information

- **Spotify Audio Features Dataset**  
  → Danceability, energy, valence, tempo, loudness, acousticness, and more

- **Spotify Top Charts Dataset**  
  → Used to label songs as *chart* vs *non-chart*

- **Genre-Enriched Track Dataset**  
  → Enables genre-wise analysis and comparison
"""
)

# -------------------- ANALYTICS PERFORMED --------------------
st.subheader("🧠 Analytics & Techniques Applied")

st.markdown(
    """
This project applies a range of analytical and visualization techniques:

### 📈 Trend Analysis
- Year-wise aggregation of audio features
- Identification of long-term shifts in musical characteristics

### 🎵 Audio Feature Intelligence
- Dimensionality reduction using **PCA**
- Visual clustering of songs in audio feature space
- Popularity-based filtering and analysis

### 🎧 Genre-Level Insights
- Genre distribution analysis
- Comparison of average and distributional audio features across genres

### 🔥 Chart vs Non-Chart Comparison
- Binary classification of songs as charting or non-charting
- Feature-wise comparison to identify what differentiates hit songs
"""
)

# -------------------- INSIGHTS --------------------
st.subheader("🔍 What Insights Can You Explore?")

st.markdown(
    """
Using the interactive pages in this dashboard, you can explore insights such as:

- 📉 How danceability and energy dipped during the 2020 period and rebounded later  
- 🎶 Why chart-topping songs tend to be more energetic and louder  
- 🎸 How rock and alternative genres differ from pop in energy distribution  
- 🎯 Where popular songs cluster in audio feature space  
"""
)

# -------------------- NAVIGATION GUIDE --------------------
st.subheader("🧭 How to Navigate the Dashboard")

st.markdown(
    """
Use the sidebar to explore different sections:

- **Overview** → High-level summary and dataset snapshot  
- **Music Trends** → Audio feature evolution over time  
- **Audio Features** → PCA-based audio intelligence  
- **Genre Insights** → Genre-wise comparison and distribution  
- **Chart Insights** → What makes a song chart-worthy  
"""
)

st.markdown("---")

st.caption(
    "This dashboard was designed as a portfolio-grade data analytics project, "
    "focusing on clean architecture, reproducible analysis, and insightful visualization."
)
