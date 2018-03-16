# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:08:13 2018

@author: Pranav
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing dataset
dataset=pd.read_csv('Movie-Ratings.csv')
movies=dataset
plt.hist(movies[movies.Genre=='Action'].BudgetMillions)
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 
       'BudgetMillions', 'Year'] 
movies.Film = movies.Film.astype('category') 
 
movies.info() #ntc it is now category #factors in R 
 
movies.Genre = movies.Genre.astype('category') 
movies.Year = movies.Year.astype('category')
movies.describe() 
import seaborn as sns 
%matplotlib inline 
import warnings 
warnings.filterwarnings('ignore') 
vis1 = sns.lmplot(data=movies,x='CriticRating',y='AudienceRating',
     fit_reg=False,hue='Genre',size=7,aspect=1)
vis1 = sns.lmplot(data=movies,x='CriticRating',y='AudienceRating',
     fit_reg=False,hue='Genre',size='BudgetMillions',aspect=1) 
list1=[]
h = plt.hist(list1,bins=30, stacked=True,rwidth=1,label=mylabels)
k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating, shade=True) k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating, shade=True,shade_lowest=False)#shows
k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating, shade=True,shade_lowest=False, cmap='Reds')
k1 = sns.kdeplot(movies.BudgetM
illions,movies.AudienceRating) 
z = sns.violinplot(data=movies,x='Genre',y='CriticRating') 
z = sns.violinplot(data=movies,x='Genre',y='CriticRating') 
z = sns.boxplot(data=movies,x='Genre',y='CriticRating') 
g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre') 
g1.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat: 
 ax.plot((0,100),(0,100),c="gray",ls="--") 
g.add_legend() 
