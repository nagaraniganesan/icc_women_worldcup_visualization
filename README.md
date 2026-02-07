# ICC Women's World Cup Visualization

Data exploration and visualization project focused on ICC Women's World Cup matches and player performances.

## Project Overview

This project analyzes ICC Women's World Cup data using Python to understand how teams and players perform across tournaments.  
It combines match‑level, batting, and bowling statistics to build clear visual stories about results, players, and venues.

## Objectives

- Explore match outcomes and score patterns across tournaments.
- Identify top batters and bowlers using aggregate statistics.
- Analyze how venues and toss decisions influence results.
- Present insights through clean, reproducible visualizations.

## Data

The project uses three CSV files:

- `match_records.csv`  
  - Match date, venue, teams, toss winner, toss decision, winning team, scores, result type, margin, etc.
- `batting_stats.csv`  
  - Player, team, matches, innings, runs, balls, average, strike rate, 4s, 6s, high scores, etc.
- `bowling_stats.csv`  
  - Player, team, matches, overs, maidens, runs, wickets, average, economy, best figures, etc.


### Data Preparation (high level)

In `Data_visualization_project.py`:

- Load CSVs with `pandas` (`match_records.csv`, `batting_stats.csv`, `bowling_stats.csv`).
- Clean and standardize team and venue names.
- Handle missing values where needed (e.g., results or stats).
- Convert date columns to `datetime` to enable time‑based analysis.
- Perform basic feature engineering, such as:
  - Year/tournament extraction from the date.
  - Win/loss indicators for teams.
  - Aggregated batting and bowling metrics per player or team.

## Visualizations

`Data_visualization_project.py` generates multiple plots (edit this list to match your code exactly):

- **Match‑level**
  - Distribution of total scores / first‑innings scores.
  - Results by margin type (runs vs wickets).
  - Team win counts across tournaments.

- **Batting**
  - Top run‑scorers in ICC Women’s World Cup.
  - Strike‑rate vs average scatter plots for key batters.
  - Boundaries (4s/6s) comparison between players.

- **Bowling**
  - Top wicket‑takers.
  - Economy rate vs wickets taken.
  - Best bowling figures visual summary.

- **Toss & venue**
  - Toss decision vs match result.
  - Venue‑wise win percentages for major teams.





