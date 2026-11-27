# ⚽ Football Player Performance Analytics Dashboard

**An interactive dashboard for exploring, comparing, and visualizing football player statistics.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Analysis-150458?logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)

## Overview
This project is a Streamlit-based football statistics dashboard. It provides filters, summary metrics, visual analysis, player comparisons, rankings, and CSV export.

> **Dataset notice:** `football_players.csv` contains fictional demonstration records generated for this starter project. It is not real-world football data and must not be used to make claims about actual players or clubs. Replace it with a properly sourced dataset and document its license before using real data.

## Features
- Filter players by club, position, and age.
- View player count, goals, assists, and average rating.
- Explore goals by club and player distribution by position.
- Inspect goals against expected goals per 90.
- Compare two selected players across key metrics.
- Rank players by goals, assists, rating, xG/90, xA/90, or clean sheets.
- View and download the filtered data as CSV.

## Technology
- Python
- Pandas
- Streamlit
- Plotly

## Project Structure
```text
football-player-performance-analytics/
├── .streamlit/
│   └── config.toml
├── app.py
├── football_players.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Run Locally
1. Install Python 3.10 or newer.
2. Clone this repository:
   ```bash
   git clone https://github.com/kunalpatil-ce/football-player-performance-analytics.git
   cd football-player-performance-analytics
   ```
3. Create and activate a virtual environment (Windows):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the dashboard:
   ```bash
   streamlit run app.py
   ```

## Dataset Schema
The sample CSV includes player, nationality, club, position, age, matches, starts, goals, assists, clean sheets, xG per 90, xA per 90, and rating.

## Limitations
- The included dataset is fictional sample data.
- Metrics and rankings are illustrative, not official player evaluations.
- Real-world analysis requires a reliable dataset, clear metric definitions, and source attribution.

## Future Improvements
- Integrate a licensed, real-world football dataset.
- Add league and season filters when those fields are available.
- Expand position-specific metrics.
- Add tests and data-validation checks.
- Deploy the dashboard online.

## Author
**Kunal Patil** — Computer Engineering Student

- GitHub: [@kunalpatil-ce](https://github.com/kunalpatil-ce)
- LinkedIn: [Kunal Patil](https://linkedin.com/in/kunal-patil-711783332)

## License
Distributed under the MIT License. See [LICENSE](LICENSE).
