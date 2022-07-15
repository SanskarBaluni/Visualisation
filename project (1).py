#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly
import plotly.express as px 
import plotly.graph_objects as go
plt.rcParams['figure.figsize']=17,8

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

import folium


# In[3]:


pyo.init_notebook_mode(connected=True)
cf.go_offline()


# In[4]:


df=pd.read_excel(r"D:\Edge Download\Covid cases in India.xlsx")


# In[5]:


df


# In[6]:


df.drop(['S. No.'],axis=1,inplace=True)


# In[7]:


df


# In[8]:


df['Total Cases']=df['Total Confirmed cases (Indian National)']+df['Total Confirmed cases ( Foreign National )']


# In[9]:


df


# In[10]:


total_cases_overall=df['Total Cases'].sum()
print('Total number of cases till now in India is',total_cases_overall)


# In[11]:


df['Active Cases']=df['Total Cases']-(df['Death']+df['Cured'])


# In[12]:


df


# In[13]:


df.style.background_gradient(cmap='Reds')


# In[ ]:





# In[14]:


Total_Active_Cases=df.groupby('Name of State / UT')['Active Cases'].sum().sort_values(ascending=False).to_frame()


# In[15]:


Total_Active_Cases


# In[16]:


Total_Active_Cases.style.background_gradient(cmap='Reds')


# In[ ]:





# In[ ]:





# In[17]:


############################## Graphical representation


# In[18]:


df.plot(kind='bar',x='Name of State / UT',y='Total Cases')
df.iplot(kind='bar',x='Name of State / UT',y='Total Cases')


# In[19]:


#matplotlib

plt.bar(df['Name of State / UT'],df['Total Cases'])


# In[20]:


px.bar(df,x='Name of State / UT',y='Total Cases')


# In[21]:


#pandas
df.plot(kind='scatter',x='Name of State / UT',y='Total Cases')


# In[22]:


#plotly
plt.scatter(df['Name of State / UT'],df['Total Cases'])


# In[23]:


#plotly scatter plot
df.iplot(kind='scatter',x='Name of State / UT',y='Total Cases',mode='markers+lines',title='My Graph',xTitle='Name of State / UT',yTitle='Total Cases',colors='red',size=20)

#plotly express scatter graph
px.scatter(df,x='Name of State / UT',y='Total Cases')


# In[ ]:





# In[24]:


#oo vis


# In[25]:


#matplotlib
fig=plt.figure(figsize=(20,10),dpi=200)
axes=fig.add_axes([0,0,1,1])
axes.bar(df['Name of State / UT'],df['Total Cases'])
axes.set_title("total Cases in India")
axes.set_xlabel("Name of States/ UT")
axes.set_ylabel("total Cases")
plt.show()

#plotly
fig=go.Figure()
fig.add_trace(go.Bar(x=df['Name of State / UT'],y=df['Total Cases']))
fig.update_layout(title='Total Cases in India',xaxis=dict(title='Name of State / UT'),yaxis=dict(title='Total Cases'))


# In[ ]:





# In[26]:


Indian_Cord=pd.read_excel(r"D:\Edge Download\Indian Coordinates.xlsx")


# In[27]:


Indian_Cord


# In[28]:


Indian_Cord.drop(['Unnamed: 3'],axis=1,inplace=True)


# In[29]:


Indian_Cord


# In[30]:


df_full=pd.merge(Indian_Cord,df,on='Name of State / UT')


# In[ ]:





# df_full

# In[31]:


map=folium.Map(location=[20,70],zoom_start=4,tiles='Stamenterrain')
for lat,long,value,name in zip(df_full['Latitude'],df_full['Longitude'],df_full['Total Cases'],df_full['Name of State / UT']):
    folium.CircleMarker([lat,long],radius=value*0.4,popup=('<strong>State</strong>: '+str(name).capitalize()+'<br>''</strong>: '+ str(value)+'<br'),color='red',fill_color='red',fill_opacity=0.3).add_to(map)


# map

# In[ ]:





# In[32]:


#how corona virus is rising globally


# In[33]:


dbd_India=pd.read_excel(r"D:\Edge Download\per_day_cases.xlsx",parse_dates=True,sheet_name="India")
dbd_Italy=pd.read_excel(r"D:\Edge Download\per_day_cases.xlsx",parse_dates=True,sheet_name="Italy")
dbd_Korea=pd.read_excel(r"D:\Edge Download\per_day_cases.xlsx",parse_dates=True,sheet_name="Korea")
dbd_Wuhan=pd.read_excel(r"D:\Edge Download\per_day_cases.xlsx",parse_dates=True,sheet_name="Wuhan")


# In[34]:


dbd_India


# In[ ]:





# In[35]:


#matplotlib
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(dbd_India["Date"],dbd_India["Total Cases"],color='blue')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()


# In[ ]:





# In[40]:


#plotly Express
fig=px.bar(dbd_India,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()


# In[37]:




fig=px.bar(dbd_Italy,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Italy')
fig.show()

fig=px.bar(dbd_Korea,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Korea')
fig.show()

fig=px.bar(dbd_Wuhan,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Wuhan')
fig.show()


# In[ ]:





# In[42]:


#plotly
dbd_India.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers')


# In[ ]:





# In[ ]:





# In[ ]:




