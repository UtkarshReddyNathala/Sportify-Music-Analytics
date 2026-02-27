# streamlit_app/utils.py

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def music_trends_multifeature(yearly_df, features):
    fig = px.line(
        yearly_df,
        x="year",
        y=features,
        markers=True,
        title="Evolution of Key Spotify Audio Features Over Time",
        template="plotly_dark"
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Feature Value",
        legend_title="Audio Feature"
    )
    return fig

def music_trend_highlight(yearly_df, feature, start_year=2020, end_year=2021):
    fig = px.line(
        yearly_df,
        x="year",
        y=feature,
        markers=True,
        title=f"{feature.capitalize()} Trend with Highlighted Period",
        template="plotly_dark"
    )

    fig.add_vrect(
        x0=start_year,
        x1=end_year,
        fillcolor="red",
        opacity=0.15,
        annotation_text="Special Period",
        annotation_position="top left"
    )

    return fig

def genre_distribution_bar(genre_df):
    genre_counts = (
        genre_df["track_genre"]
        .value_counts()
        .reset_index()
    )
    genre_counts.columns = ["track_genre", "count"]

    fig = px.bar(
        genre_counts,
        x="track_genre",
        y="count",
        color="count",
        title="Distribution of Tracks Across Genres",
        template="plotly_dark"
    )

    fig.update_layout(
        xaxis_title="Genre",
        yaxis_title="Number of Tracks"
    )
    return fig

def genre_average_feature_bar(genre_df, feature):
    avg_df = (
        genre_df
        .groupby("track_genre")[feature]
        .mean()
        .reset_index()
        .sort_values(by=feature, ascending=False)
    )

    fig = px.bar(
        avg_df,
        x=feature,
        y="track_genre",
        orientation="h",
        color=feature,
        title=f"Average {feature.capitalize()} by Genre",
        template="plotly_dark"
    )
    return fig

def genre_share_pie(genre_df, top_n=10):
    genre_counts = genre_df["track_genre"].value_counts().head(top_n)

    fig = px.pie(
        values=genre_counts.values,
        names=genre_counts.index,
        title="Top Genres by Dataset Share",
        hole=0.4
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(template="plotly_dark")
    return fig

def chart_vs_nonchart_mean(chart_df, feature):
    mean_df = (
        chart_df
        .groupby("is_chart_song")[feature]
        .mean()
        .reset_index()
    )

    mean_df["is_chart_song"] = mean_df["is_chart_song"].map(
        {True: "Chart", False: "Non-Chart"}
    )

    fig = px.bar(
        mean_df,
        x="is_chart_song",
        y=feature,
        color="is_chart_song",
        text_auto=".2f",
        title=f"Average {feature.capitalize()} — Chart vs Non-Chart",
        template="plotly_dark"
    )
    return fig

def chart_feature_difference(chart_df, features):
    diff_df = (
        chart_df
        .groupby("is_chart_song")[features]
        .mean()
        .T
        .reset_index()
    )

    diff_df.columns = ["feature", "non_chart", "chart"]
    diff_df["difference"] = diff_df["chart"] - diff_df["non_chart"]
    diff_df = diff_df.sort_values("difference", ascending=False)

    fig = px.bar(
        diff_df,
        x="difference",
        y="feature",
        orientation="h",
        text_auto=".3f",
        title="Audio Feature Differences: Chart vs Non-Chart Songs",
        template="plotly_dark"
    )
    return fig

def pca_popularity_filter(pca_df, threshold):
    filtered = pca_df[pca_df["popularity"] >= threshold]

    fig = px.scatter(
        filtered,
        x="PC1",
        y="PC2",
        color="popularity",
        title=f"PCA of Audio Features (Popularity ≥ {threshold})",
        color_continuous_scale="viridis",
        template="plotly_dark"
    )
    return fig

def pca_top_hits(pca_df):
    cutoff = pca_df["popularity"].quantile(0.90)
    top_hits = pca_df[pca_df["popularity"] >= cutoff]

    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        opacity=0.2,
        color_discrete_sequence=["gray"],
        title="Top 10% Popular Songs Highlighted",
        template="plotly_dark"
    )

    fig.add_scatter(
        x=top_hits["PC1"],
        y=top_hits["PC2"],
        mode="markers",
        marker=dict(color="red", size=6),
        name="Top 10% Popular Songs"
    )
    return fig
