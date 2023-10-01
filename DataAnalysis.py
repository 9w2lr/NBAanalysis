import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

from DataLoading import nba_players_with_salary_df

# Visualize correlations
plt.subplots(figsize=(20, 15))
ax = plt.axes()
ax.set_title("NBA Player Correlation Heatmap: 2016-2017 Season (STATS & SALARY)")
corr = nba_players_with_salary_df.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)

# Linear regression and visualization
sns.lmplot(x="SALARY_MILLIONS", y="WINS_RPM", data=nba_players_with_salary_df)
results = smf.ols('W ~POINTS', data=nba_players_with_salary_df).fit()
print(results.summary())
results = smf.ols('W ~WINS_RPM', data=nba_players_with_salary_df).fit()
print(results.summary())
results = smf.ols('SALARY_MILLIONS ~POINTS', data=nba_players_with_salary_df).fit()
print(results.summary())
results = smf.ols('SALARY_MILLIONS ~WINS_RPM', data=nba_players_with_salary_df).fit()
print(results.summary())

# Data visualization using ggplot
from ggplot import *

p = ggplot(nba_players_with_salary_df, aes(x="POINTS", y="WINS_RPM", color="SALARY_MILLIONS")) + geom_point(size=200)
p + xlab("POINTS/GAME") + ylab("WINS/RPM") + ggtitle(
    "NBA Players 2016-2017: POINTS/GAME, WINS REAL PLUS MINUS and SALARY")
