import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Football Player Analytics", page_icon="⚽", layout="wide")

DATA_PATH = Path(__file__).resolve().parent / "football_players.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    numeric = ["age", "matches", "starts", "goals", "assists", "clean_sheets",
               "xG_per90", "xA_per90", "rating"]
    for col in numeric:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    return data.dropna(subset=["player", "club", "position"])

df = load_data()

st.title("⚽ Football Player Performance Analytics")
st.caption("Explore player statistics, compare performances, and discover insights.")
st.info("Demo dataset: the included player records are fictional sample data created for demonstrating this dashboard. Replace them with a properly sourced dataset before presenting real-world conclusions.")

with st.sidebar:
    st.header("Dashboard Filters")
    clubs = st.multiselect("Club", sorted(df["club"].unique()), default=sorted(df["club"].unique()))
    positions = st.multiselect("Position", sorted(df["position"].unique()), default=sorted(df["position"].unique()))
    min_age, max_age = int(df.age.min()), int(df.age.max())
    age_range = st.slider("Age range", min_age, max_age, (min_age, max_age))

filtered = df[
    df["club"].isin(clubs) &
    df["position"].isin(positions) &
    df["age"].between(age_range[0], age_range[1])
].copy()

if filtered.empty:
    st.warning("No players match the selected filters. Adjust the filters in the sidebar.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Players", f"{len(filtered)}")
c2.metric("Total goals", f"{int(filtered.goals.sum())}")
c3.metric("Total assists", f"{int(filtered.assists.sum())}")
c4.metric("Average rating", f"{filtered.rating.mean():.2f}/10")

st.divider()
overview, compare, rankings = st.tabs(["📊 Overview", "⚖️ Player comparison", "🏆 Rankings"])

with overview:
    left, right = st.columns(2)
    with left:
        goals = filtered.groupby("club", as_index=False)["goals"].sum().sort_values("goals", ascending=False)
        fig = px.bar(goals, x="club", y="goals", title="Goals by club", text="goals")
        fig.update_layout(xaxis_title="", yaxis_title="Goals")
        st.plotly_chart(fig, use_container_width=True)
    with right:
        pos = filtered.groupby("position", as_index=False)["player"].count().rename(columns={"player":"players"})
        fig = px.pie(pos, names="position", values="players", hole=0.48, title="Players by position")
        st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(filtered, x="xG_per90", y="goals", size="assists",
                     color="position", hover_name="player",
                     hover_data=["club", "rating"], title="Goals vs expected goals per 90")
    st.plotly_chart(fig, use_container_width=True)

with compare:
    names = sorted(filtered["player"].unique())
    if len(names) < 2:
        st.warning("Select at least two players using the dashboard filters.")
    else:
        p1 = st.selectbox("First player", names, index=0)
        p2 = st.selectbox("Second player", names, index=1)
        selected = filtered[filtered.player.isin([p1, p2])].set_index("player")
        metrics = ["goals", "assists", "matches", "rating", "xG_per90", "xA_per90"]
        st.dataframe(selected[["club", "position"] + metrics], use_container_width=True)
        chart_data = selected.reset_index().melt(id_vars="player", value_vars=metrics,
                                                 var_name="metric", value_name="value")
        fig = px.bar(chart_data, x="metric", y="value", color="player",
                     barmode="group", title="Side-by-side statistical comparison")
        st.plotly_chart(fig, use_container_width=True)

with rankings:
    metric = st.selectbox("Rank players by", ["goals", "assists", "rating", "xG_per90", "xA_per90", "clean_sheets"])
    top = filtered.sort_values(metric, ascending=False).head(10)
    fig = px.bar(top.sort_values(metric), x=metric, y="player", color="position",
                 orientation="h", title=f"Top players by {metric}")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(top[["player", "club", "position", metric]], use_container_width=True)

st.divider()
st.subheader("Player data")
st.dataframe(filtered.sort_values("rating", ascending=False), use_container_width=True)
st.download_button("⬇️ Download filtered player data",
                   filtered.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_football_players.csv", mime="text/csv")
st.caption("Built with Python, Pandas, Streamlit and Plotly. Sample data is fictional.")
