# import pandas as pd
# import numpy as np
# import datetime
# import matplotlib.pyplot as plt
# import seaborn as sns
# from collections import Counter
# df = pd.read_csv(r'C:\Users\Yogesh\Desktop\imdb casestudy\IMDB-Movie-data.csv')

# 1. Display Top 10 Rows of The Dataset
# print(df.head(10))



# 2. Check Last 10 Rows of The Dataset
# print(df.tail(10))



# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
# print(df.shape)



# 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
# print(df.info())




# 5. Check Missing Values In The Dataset
# print(df.isnull().sum())
# sns.heatmap(df.isnull())
# plt.show()
# per_missing = df.isnull().sum()*100/len(df)
# print(per_missing)





# 6. Drop All The  Missing Values
# print(df.dropna(how='any'))




# 7. Check For Duplicate Data
# print(df.duplicated().any()) # nothing duplicate values
# df = df.drop_duplicates()
# print(df)





# 8. Get Overall Statistics About The DataFrame
# print(df.describe(include='all'))




# 9. Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes
# print(df.loc[df['Runtime (Minutes)']>=180][['Title','Runtime (Minutes)']])




# 10. In Which Year There Was The Highest Average Voting?
# print(df.columns)
# df.groupby('Year')['Votes'].mean().sort_values(ascending=False)
# sns.barplot(data=df,x='Year',y='Votes')
# plt.title('Votes by Years')
# plt.show()



# 11. In Which Year There Was The Highest Average Revenue?
# print(df.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False))
# sns.barplot(data=df,x='Year',y='Revenue (Millions)')
# plt.title('Revenue (Millions) by year')
# plt.show()



# 12. Find The Average Rating For Each Director
# print(df[['Director','Rating']])
# print(df.groupby('Director')['Rating'].mean().sort_values(ascending=False))






# 13. Display Top 10 Lengthy Movies Title and Runtime
# df['len'] = len(df['Title'])
# top_10 = df.sort_values(by=['len','Runtime (Minutes)'],ascending=False).head(10)
# print(top_10[['Title','Runtime (Minutes)']])
# sns.barplot(data=top_10,x='Title',y='Runtime (Minutes)')
# plt.show()







# 14. Display Number of Movies Per Year
# print(df.columns)
# print(df.groupby('Year')['Title'].count())
# sns.countplot(data=df,x='Year')
# plt.title('Number of Movies Per Year')
# plt.show()



# 15. Find Most Popular Movie Title (Highest Revenue)
# print(df.sort_values(by='Revenue (Millions)',ascending=False)[['Title','Revenue (Millions)']].head(1))
# print(df.loc[df['Revenue (Millions)'].max()==df['Revenue (Millions)']][['Title','Revenue (Millions)']])





# 16. Display Top 10 Highest Rated Movie Titles And its Directors
# x = df.sort_values(by='Rating',ascending=False)[['Title','Director','Rating']].head(10)
# sns.barplot(data=x,x='Title',y='Rating',hue='Director',dodge=False)
# plt.legend(bbox_to_anchor=(1.05,1),loc=2)
# plt.title('Top 10 Highest Rated Movie Titles')
# plt.show()




# 17. Display Top 10 Highest Revenue Movie Titles
# x = df.sort_values(by='Revenue (Millions)',ascending=False)[['Title','Revenue (Millions)']].head(10)
# sns.barplot(data=x,y='Title',x='Revenue (Millions)')
# plt.title('Top 10 Highest Revenue Movie Titles')
# plt.show()




# 18.  Find Average Rating of Movies Year Wise
# print(df.groupby('Year')[['Rating','Year']].mean())





# 19. Does Rating Affect The Revenue?
# sns.scatterplot(data=df,x='Revenue (Millions)',y='Rating')
# plt.show()



# 20. Classify Movies Based on Ratings [Excellent, Good, and Average]

# def rating(rate):
#     if rate<5:
#         return 'Average'
#     elif 7>rate>=5:
#         return 'Good'
#     else:
#         return 'Excellent'
#
# df['Classify']=df['Rating'].apply(rating)
#
# print(df.groupby('Classify')['Title'].count())



# 21. Count Number of Action Movies
# print(df.columns)
# print(len(df.loc[df['Genre'].str.contains('Action')]))
# def Genre(x):
#     if 'Action' in x:
#         return True
#     else:
#         return False
# df['TF'] = df['Genre'].apply(Genre)
# print(df.loc[df['TF']])



# 22. Find Unique Values From Genre
# l = df['Genre'].str.split(',')
# l1 = []
# for i in l:
#     l1 = l1 + i
# l1 = list(set(l1))
# print(l1)




# 23. How Many Films of Each Genre Were Made?
# print(Counter(l1))

# class solution():
#     def find_minimum(self,arr,n):
#         minimum = -1
#         x = int(min(arr))
#         return minimum+1+x
#     a = int(input('Enter num'))
#     l = input().split()
#     x1 = 1
#     print(find_minimum(x1,l,a))
    # find_minimum(x1, l, a)
