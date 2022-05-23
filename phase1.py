#!/usr/bin/env python
# coding: utf-8

# # Analysis of Various Movies

# In[385]:


#importing 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[386]:


#loading data with pandas
df_b = pd.read_csv('imdb.title.basics.csv.gz')
df_r = pd.read_csv('imdb.title.ratings.csv.gz')
df_g = pd.read_csv('bom.movie_gross.csv.gz')


# In[387]:


df_b.head(5)


# ### Most produced genres
# 

# In[388]:


s = df_b.genres.value_counts().head(12)
s


# In[389]:


#check for missing values
df_b.info()


# In[390]:


df_b.isna()


# In[391]:


df_b.head()


# In[392]:


#drop rows with genre as NAN
df_b.dropna(subset = ['genres'],inplace = True)
df_b["genres"].isna().sum()


# In[393]:


grouped_data = df_b.groupby("genres").count().sort_values(by = 'tconst',ascending = False)
grouped_data.reset_index(inplace = True)
grouped_data


# In[394]:


#top 10 produce genres 

top_10_genres = grouped_data[:10]
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(height = top_10_genres['original_title'] , x=top_10_genres['genres'] )
ax.tick_params(axis = "x",labelrotation = 90)
ax.set_title('Most produced genres')
ax.set_xlabel('Genres')
ax.set_ylabel('num_of_times_produced')


# In[395]:


#checking data
df_r.info()
df_b.info()


# ### Genres with high average ratings

# In[396]:


#joining two dataframes
r_b = df_b.merge(df_r, on="tconst", how="inner")
r_b


# In[397]:


#checking if the values have merged properly
r_b['tconst'].value_counts()


# In[398]:


#setting he dataframe to a descending order
grouped =r_b.sort_values(by = 'averagerating',ascending = False)
grouped.reset_index(inplace = True)
grouped


# In[399]:


#getting the top 10 highly rated genres
top_10_avgrates = grouped[:300]
#top_10_avgrates


# In[400]:


#ploting a genre avg rating graph
fig ,ax = plt.subplots(figsize = (15,5))
ax.bar(height = top_10_avgrates['averagerating'],x= top_10_avgrates['genres'])
ax.set_title('Genre avg ratings')
ax.set_xlabel('Genres')
ax.tick_params(axis = 'x',labelrotation = 90)
ax.set_ylabel('Ratings')


# ### Movies that have made the most profits

# In[401]:


#checking for missing values
df_g.isna().sum()


# In[402]:


#dropping rows with gross missing value
df_g.dropna(subset = ['foreign_gross','domestic_gross'] ,axis = 0,inplace = True)


# In[403]:


#removing commas from foreign gross column
df_g['foreign_gross'] =  [gross.replace(',', '') for gross in df_g['foreign_gross'] ]
df_g['foreign_gross']


# In[404]:


#changing foreign gross datatype o float
df_g = df_g.astype({'foreign_gross' :float} , errors = 'raise')
df_g.info()


# In[405]:


#adding domestic and foreign gross
df_g['sum_gross'] = df_g['domestic_gross'] + df_g['foreign_gross']
df_g['sum_gross']


# In[406]:


#viewing the dataframe with new column
df_g.head(5)


# In[418]:


#sorting the new dataframe
df_g.sort_values(by = 'sum_gross', ascending = False ,inplace = True)
df_g.head(20)


# In[419]:


#getting movies with most total gross
top_30_gross = df_g[:30]



# In[420]:


#graph for movies with most gross
fig ,ax = plt.subplots(figsize = (10,5)) 
ax.bar(height = top_30_gross['sum_gross'], x =top_30_gross['title'] )
ax.set_title('top 30 with highest profit')
ax.tick_params(axis = "x",labelrotation = 90)
ax.set_xlabel('movie_title')
ax.set_ylabel('total profits')


# In[410]:


df_r['tconst'] = df_r['tconst'].astype(str)
df_b['tconst'] = df_b['tconst'].astype(str)
df_b.info()


# ### Relationship between  average rating and number of votes

# In[411]:


r_b


# In[412]:


#plot a graph
fig, ax =plt.subplots(figsize= (10,5))
ax.scatter(
y = r_b['numvotes'],
x = r_b['averagerating'],
    
)
ax.set_title('average rating vs num of votes')
ax.set_xlabel('avg rating')
ax.set_ylabel('num of votes')


# In[413]:


'''
number of votes are quite high at 7.8 to 9 avg rate
'''


# ### genres that have very few number avg ratings

# In[364]:


r_b.info()


# In[366]:


#sort the dataframe in ascending order
low_rates = r_b.sort_values(by = 'averagerating',ascending = True)
low_rates.reset_index(inplace = True)
low_rates


# In[379]:


low = low_rates[:100]


# In[421]:


#plot graph for movies with low avg rate
fig ,ax = plt.subplots(figsize = (10,5))
ax.bar(height = low['averagerating'],x = low['genres'])
ax.set_ylim(0,5)
ax.tick_params(axis = 'x',labelrotation = 90)
ax.set_ylabel('average rating')
ax.set_xlabel('genres')
ax.set_title('movies with minimal average rating')


# In[ ]:


'''
genres not to venture in

'''


# ### What runtime gets high avg ratings

# In[165]:


r_b


# In[277]:


#checking for missing values
r_b.info()


# In[278]:


#drop rows with missing values 
r_b.dropna(subset = ['runtime_minutes'],axis= 0,how = 'any', inplace = True)


# In[293]:


#sorting the dataframes by avg rating
num_t = r_b.sort_values(by = 'averagerating',ascending = False)
num_t


# In[327]:


fav_run_time = num_t[:10000]


# In[328]:


# Creating histogram

fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(x = fav_run_time['runtime_minutes'],y =fav_run_time['averagerating'])
ax.set_title('run time impact vs averagerating')
ax.set_xlabel('runtime(minutes)')
ax.set_ylabel('average ratings')


# In[ ]:


'''
most movies with high ratings as from 9.6 to 10 range from 54 minutes to 105 minutes
'''


# In[ ]:




