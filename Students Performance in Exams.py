import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# read the CSV
df=pd.read_csv("StudentsPerformance.csv")
# Explore the data
pd.set_option('display.max_columns', None)
print(df.head(10))
print(df.describe())
print(df.shape)# 1000 rows =1000 students
print(df.isnull().sum())# zero nulls


#finding the average of scores(math,reading,writing)
print(f"mean of math: {df.loc[:,'math score'].mean()}")
print(f"mean of reading: {df.loc[:,'reading score'].mean()}")
print(f"mean of writing: {df.loc[:,'writing score'].mean()}")

# Create average score col
df['average score'] = df[['math score','reading score','writing score']].mean(1).round(2)
print(df.head(10))
print("-"*100)
# see max and min average score
max_avg_score=df['average score'].max()
print(" Student with highest average score :")
print(df[df['average score']==max_avg_score][['gender','math score','reading score','writing score','average score']])
print("-"*100)
min_avg_score=df['average score'].min()
print(" Student with lowest average score :")
print(df[df['average score']==min_avg_score][['gender','math score','reading score','writing score','average score']])
print("-"*100)

#Comparing average score by gender :
by_gender=df.groupby('gender')['average score'].mean()
sns.catplot(x=by_gender.index, y=by_gender, kind='bar',hue=by_gender.index)
plt.title('Average score per gender',y=0.98)
plt.show()

#Comparing average score of each subject by gender
reshaped_df=df.copy()
reshaped_df=reshaped_df.melt(id_vars='gender',value_vars=['math score','reading score','writing score'],var_name='subject',value_name='avg_score')
g=sns.catplot(x='gender',y='avg_score',hue='gender',data=reshaped_df,kind='bar',col='subject',col_wrap=2)
g.fig.suptitle('Average score per gender',y=1.00,fontsize=14)
g.set_titles('{col_name}',fontsize=12)
plt.show()



#Analyze distributions
g2=sns.displot(x='avg_score',hue='gender',data=reshaped_df,col='subject',kind='hist')
g2.fig.suptitle('Distribution of Average Scores by Gender in Math, Reading, and Writing',y=1.00,fontsize=14)
g2.set_titles('{col_name}',fontsize=12)
plt.show()



# Top 10 students with the highest overall average score
pd.reset_option("display.max_columns")
df.sort_values('average score',ascending=False)
print(df.head(10))

print("-"*100)



