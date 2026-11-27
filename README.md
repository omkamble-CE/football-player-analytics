# ⚽ Football Player Performance Analytics Dashboard

<p align="center">
  <strong>Turning Football Statistics into Meaningful Performance Insights</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" />
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly" />
  <img src="https://img.shields.io/badge/Status-Development-orange" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---

## 📌 Overview

The **Football Player Performance Analytics Dashboard** is an interactive data analytics application developed using Python and Streamlit to explore, analyze, and visualize football player statistics.

The project transforms structured football data into meaningful insights through statistical analysis, interactive charts, player comparisons, and performance rankings.

It provides an intuitive platform for exploring player contributions, understanding performance patterns, and comparing players across different statistical indicators.

## 🎯 Project Objectives

- Analyze football player statistics using Python.
- Evaluate player performance through different statistical indicators.
- Compare players based on goals, assists, and other metrics.
- Identify top-performing players through statistical rankings.
- Explore player distribution across different playing positions.
- Visualize football statistics through interactive charts.
- Develop an interactive and user-friendly analytics dashboard.

## ✨ Key Features

### 📊 1. Performance Overview

- Total number of players.
- Total goals scored.
- Total assists recorded.
- Average player rating.

### ⚖️ 2. Player Comparison

- Compare two selected football players.
- Analyze goals and assists.
- Compare appearances and player ratings.
- Examine expected goals and expected assists per 90 minutes.

### 🏆 3. Top Player Rankings

- Rank players based on goals.
- Identify top assist providers.
- Explore player ratings.
- Analyze expected goals and expected assists.
- View clean-sheet rankings.

### ⚽ 4. Position-Based Analysis

- Explore forwards, midfielders, defenders, and goalkeepers.
- Visualize player distribution by position.
- Examine statistical differences across playing positions.

### 📈 5. Interactive Data Visualization

- Goals by club bar chart.
- Player distribution pie chart.
- Goals versus expected goals scatter plot.
- Interactive player comparison charts.
- Dynamic performance ranking charts.

### 🔍 6. Dynamic Data Filtering

Filter player records using:

- Club
- Playing position
- Age range

### 📥 7. Data Export

Download filtered football player statistics in CSV format for further analysis.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive charts and visualization |
| Git | Version control |
| GitHub | Source code hosting and project management |

## 📊 Performance Metrics

The dashboard analyzes different categories of football statistics.

**Attacking Performance**
- Goals
- Assists
- Expected Goals (xG per 90)
- Expected Assists (xA per 90)

**Player Statistics**
- Matches played
- Starts
- Age
- Clean sheets
- Player rating

**Comparative Performance**
- Goals and assists comparison
- Player ratings
- Performance rankings
- Expected goals and assists comparison

*The available metrics depend on the columns included in the dataset.*

## 📂 Dataset Information

The project includes a sample football player dataset named `football_players.csv`.

The dataset contains structured player information and statistical attributes, including:

- Player name
- Nationality
- Club
- Playing position
- Age
- Matches played
- Starts
- Goals
- Assists
- Clean sheets
- Expected goals per 90 minutes
- Expected assists per 90 minutes
- Player rating

**Dataset Note:** The included dataset contains fictional demonstration records created for testing and demonstrating the dashboard. It does not represent actual professional football players or official club statistics.

## 🔄 Project Workflow

The application follows a structured data analytics workflow:

1. **Data Collection** – Load structured football player statistics.
2. **Data Loading** – Import the dataset using Pandas.
3. **Data Processing** – Prepare numerical and categorical attributes.
4. **Data Analysis** – Examine player statistics and performance indicators.
5. **Data Visualization** – Generate interactive charts using Plotly.
6. **Dashboard Development** – Display analytical results through Streamlit.
7. **Data Export** – Allow users to download filtered player records.

## 🖥️ Dashboard Preview

The dashboard provides an interactive interface for exploring football player statistics.

**Screenshots will be added after the dashboard is executed and tested.**

## 📁 Project Structure

```text
football-player-performance-analytics/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
│
├── football_players.csv
│
├── requirements.txt
│
├── .gitignore
│
├── README.md
│
└── LICENSE
```

## ⚙️ Installation and Setup

Follow the instructions below to run the project locally.

### Prerequisites

- Python 3.10 or above
- Git
- Visual Studio Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/kunalpatil-ce/football-player-performance-analytics.git
```

### 2. Navigate to the Project Directory

```bash
cd football-player-performance-analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Dashboard

```bash
streamlit run app.py
```

The application will start locally and open in your default web browser.

## 🚀 Future Enhancements

- Integration of real-world football datasets.
- Support for multiple football leagues and seasons.
- Advanced player performance evaluation.
- Additional player comparison metrics.
- Position-specific performance analysis.
- Machine learning-based performance prediction.
- Player scouting and recommendation features.
- Online dashboard deployment.

## 🎓 Project Applications

This project demonstrates practical applications of:

- Python Programming
- Data Analytics
- Data Manipulation
- Statistical Analysis
- Data Visualization
- Interactive Dashboard Development
- Football Performance Analysis

## 👨‍💻 Author

**Om Kamble**

Computer Engineering Student

- GitHub: [kunalpatil-ce](https://github.com/kunalpatil-ce)

## 📄 License

This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>⚽ Football Analytics | Python | Data Science | Performance Insights</strong>
</p>

<p align="center">
  If you find this project interesting, consider giving it a ⭐!
</p>
