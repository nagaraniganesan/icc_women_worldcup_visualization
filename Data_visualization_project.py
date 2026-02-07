import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_batting=pd.read_csv("batting_stats.csv")
df_bowling=pd.read_csv('bowling_stats.csv')
df_matchrecords=pd.read_csv('match_records.csv')

sns.set(style="whitegrid",palette="magma")

plt.figure(figsize=(15,12))

#barplot
plt.subplot(2,2,1)
top_bat=df_batting.nlargest(10,'Runs')
sns.barplot(data=df_batting,x="Runs",y="Player",hue="Country",dodge=False,palette='viridis')
plt.title("Top 10 Run Scorers")

#Scatter

plt.subplot(2,2,2)
sns.scatterplot(data=df_batting,x="Strike_rate",y="Runs",hue="Country",s=100)
plt.title("Runs vs Strike Rate by Country",fontsize=14)
plt.legend(loc='upper right')

#Bowling_Stats-Bar_plot

plt.subplot(2,2,3)
top_bowl=df_bowling.nlargest(10,'Wickets')
sns.barplot(data=top_bowl,x="Wickets",y="Player",hue="Country",dodge=False)
plt.title("Top 10 Wicket Takers",fontsize=14)
plt.legend(loc='lower right')


#Scatter_plt:
plt.subplot(2,2,4)
sns.scatterplot(data=df_bowling,x="Economy",y="Wickets",hue="Country",s=100)
plt.title("Wickets vs Economy Rate")
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

#violin plot:

plt.figure(figsize=(10,5))
sns.violinplot(data=df_bowling,x="Country",y="Economy",hue='Country',palette='viridis',legend=False)
plt.title("Economy Rate Distribution by Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Box_plot:

plt.figure(figsize=(10,5))
sns.boxplot(data=df_batting,x="Country",y="Runs",palette='Set3')
plt.title("BATTING:Runs Distribution by Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Histogram

plt.figure(figsize=(8, 6))
sns.histplot(df_bowling['Economy'], bins=10, kde=True, color='darkgreen')
plt.title('BOWLING: Distribution of Economy Rate', fontsize=14)
plt.xlabel('Economy Rate')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

#Count plot

plt.figure(figsize=(8,6))
sns.countplot(data=df_matchrecords, x="toss_decision", hue="result",palette='magma')
plt.title("Toss Decision vs Match Result")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Pair plot
plt.figure(figsize=(10,6))
num_bat_cols = ['Runs', 'Average', 'Strike_rate', 'Fours', 'Sixes']
sns.pairplot(df_batting[num_bat_cols + ['Country']], hue='Country')
plt.suptitle("Batting Stats Relationships", y=1.02)
plt.show()

#Heatmap: Team performance
pivot_runs = df_matchrecords.pivot_table(values='1st_score', index='team1', columns='match_type', aggfunc='mean')
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_runs, annot=True, cmap='YlOrRd', fmt='.0f')
plt.title("Average 1st Innings Score by Team & Match Type")
plt.tight_layout()
plt.show()








