# NBAanalysis
## NBA Player Power Influence And Performance

### Exploration of How Social Media Can Predict Winning Metrics Better Than Salary

- Data Source:
  - `../input/nba_2017_att_val_elo.csv`
  - `../input/nba_2017_salary.csv`
  - `../input/nba_2017_pie.csv`
  - `../input/nba_2017_real_plus_minus.csv`
  - `../input/nba_2017_br.csv`

### Data Description:

#### Attendance Valuation and ELO Data
- Columns:
  - `TEAM`: Team name
  - `GMS`: Games played
  - `TOTAL`: Total attendance
  - `AVG`: Average attendance per game
  - `PCT`: Percentage of attendance
  - `VALUE_MILLIONS`: Team value in millions
  - `ELO`: ELO rating
  - `CONF`: Conference

#### Salary Data
- Columns:
  - `PLAYER`: Player name
  - `SALARY_MILLIONS`: Salary in millions

#### Player Impact Estimate (PIE) Data
- Columns:
  - `PLAYER`: Player name
  - `PIE`: Player Impact Estimate
  - `PACE`: Pace of the game
  - `W`: Number of wins

#### Real Plus Minus Data
- Columns:
  - `PLAYER`: Player name
  - `GP`: Games played
  - `MPG`: Minutes per game
  - `ORPM`: Offensive Real Plus Minus
  - `DRPM`: Defensive Real Plus Minus
  - `RPM`: Real Plus Minus
  - `WINS_RPM`: Wins contributed by RPM

#### Box Score Statistics Data
- Columns:
  - `PLAYER`: Player name
  - `POSITION`: Player position
  - `AGE`: Player age
  - `MP`: Minutes played per game
  - `FG`: Field goals made per game
  - `FGA`: Field goals attempted per game
  - ... (other statistics columns)

### Data Processing:
- Merged and processed data to create a comprehensive dataset for analysis.
- Removed irrelevant columns and cleaned the data for analysis.

### Data Analysis:
- Explored correlations between various player statistics and salary using a heatmap.
- Analyzed the relationship between social media influence and player performance metrics.

---