# -*- coding: utf-8 -*-
"""
Dashboard Infographic Visualization

#Student name - Marasingha Arachchilage Sanduni Sakunthala Jayathilaka #STuden ID - 22031451

#Data set Name - Agriculture Crop Production In India #Data set source - https://www.kaggle.com/datasets/srinivas1/agricuture-crops-production-in-india

"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read data 
data = pd.read_csv("datafile (1).csv")
data.head()

crop_production_data = pd.read_csv("datafile (2).csv")
crop_production_data.head()

#create plots

fig,axs = plt.subplots(figsize=(10,6))
crop_wise_yield = data.groupby(['Crop']).sum()['Yield (Quintal/ Hectare) ']
plt.plot(crop_wise_yield)
crop_wise_production = data.groupby(['Crop']).sum()['Cost of Production (`/Quintal) C2']/10
plt.plot(crop_wise_production)
plt.xticks(rotation ='vertical')
plt.legend()

# Add title and axis labels
plt.title('Crop-wise Yield and Cost of Production')
plt.xlabel('Crop')
plt.ylabel('Yield (Quintal/Hectare) / Cost of Production (`/Quintal) C2')
# cost of production is 10 times as indicated
# this shows maximum yield/hectare is of SUGARCANE
# sugarcane has low cost of production/quintal

state_crop_yield = data.groupby(['State'])
index = list(state_crop_yield.indices.keys())
state_crop_yield.sum()[['Cost of Production (`/Quintal) C2', 'Yield (Quintal/ Hectare) ']].plot(kind='bar',figsize=(12,7))

# Add axis labels and title
plt.title('State based Yield and Cost of Production 2001-2014')
plt.xlabel('Yield (Quintal/ Hectare) / Cost of Production (`/Quintal) C2')
plt.ylabel('Crop Yield and Cost of Production by State')

recommended_zone = pd.read_csv('datafile (3).csv')

recommended_zone.drop('Unnamed: 4',axis=1,inplace=True)
recommended_zone.dropna(inplace=True)
recommended_zone.info()
recommended_zone.head()

def state1(row):
    if 'Andhra Pradesh' in row['Recommended Zone']:
        return 1
def state2(row):
    if 'Tamil Nadu' in row['Recommended Zone']:
        return 1
def state3(row):
    if 'Gujarat' in row['Recommended Zone']:
        return 1
def state4(row):
    if 'Orissa' in row['Recommended Zone']:
        return 1
def state5(row):
    if 'Punjab' in row['Recommended Zone']:
        return 1
def state6(row):
    if 'Haryana' in row['Recommended Zone']:
        return 1
def state7(row):
    if 'Uttar Pradesh' in row['Recommended Zone']:
        return 1
def state8(row):
    if 'Rajasthan' in row['Recommended Zone']:
        return 1
def state9(row):
    if 'Karnataka' in row['Recommended Zone']:
        return 1
def state10(row):
    if 'Madhya Pradesh' in row['Recommended Zone']:
        return 1
def state11(row):
    if 'West Bengal' in row['Recommended Zone']:
        return 1
    
recommended_zone['Andhra Pradesh'] = recommended_zone.apply(state1,axis=1)
recommended_zone['Tamil Nadu']=recommended_zone.apply(state2,axis=1)
recommended_zone['Gujarat']=recommended_zone.apply(state3,axis=1)
recommended_zone['Orissa']=recommended_zone.apply(state4,axis=1)
recommended_zone['Punjab']=recommended_zone.apply(state5,axis=1)
recommended_zone['Haryana']=recommended_zone.apply(state6,axis=1)
recommended_zone['Uttar Pradesh']=recommended_zone.apply(state7,axis=1)
recommended_zone['Rajasthan']=recommended_zone.apply(state8,axis=1)
recommended_zone['Karnataka']=recommended_zone.apply(state9,axis=1)
recommended_zone['Madhya Pradesh']=recommended_zone.apply(state10,axis=1)
recommended_zone['West Bangal']=recommended_zone.apply(state11,axis=1)
# Added the eleven states as columns in the dataframe  

recommended_zone.fillna(0).head()

dataframe = recommended_zone.groupby('Crop').sum().plot(kind='bar',figsize=(15,7))
dataframe
# Add axis labels and title
plt.xlabel('Crop')
plt.ylabel('Count')
plt.title('Recommended Zones by Crop')

# wheat is almost sown in all the mentioned states
# suitable zones for paddy is Orissa and west Bengal

dataframe = pd.DataFrame(recommended_zone.groupby('Season/ duration in days').count().reset_index())
dataframe1 = pd.DataFrame([dataframe.loc[1:27].sum(),dataframe.loc[29:37].sum()])
dataframe1.drop('Season/ duration in days',axis=1,inplace=True)
dataframe1 = dataframe1.assign(Duration = ['100-190','70-100'])

ax = dataframe1[['Andhra Pradesh', 'Tamil Nadu', 'Gujarat', 'Orissa', 'Punjab', 'Haryana', 'Uttar Pradesh', 'Rajasthan',
                 'Karnataka', 'Madhya Pradesh', 'West Bangal', 'Duration']].plot(x='Duration', kind='bar', figsize=(12,7))

# Add axis labels and title
ax.set_xlabel('Duration in Days')
ax.set_ylabel('Count')
ax.set_title('Recommended Zones by Season Duration')
# most favorable state for growing crops in 100-190 days is UP and Rajasthan
# for 70-100 days it is Gujarat

dataframe1
crop_production_data.head()

crop_production_data.columns = ['Crop', 'Production 2006-07', 'Production 2007-08',
       'Production 2008-09', 'Production 2009-10', 'Production 2010-11',
       'Area 2006-07', 'Area 2007-08', 'Area 2008-09', 'Area 2009-10',
       'Area 2010-11', 'Yield 2006-07', 'Yield 2007-08', 'Yield 2008-09',
       'Yield 2009-10', 'Yield 2010-11']

plt.subplots(figsize=(15,6))
plt.scatter(x='Crop',y='Production 2006-07',data = crop_production_data)

# Add axis labels and title
plt.xlabel('Crop')
plt.ylabel('Production 2006-07')
plt.title('Crop Production Data for 2006-07')
plt.xticks(rotation=90)
plt.show()

#Development of the final dashboard visualization
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Define the grid specification
fig = plt.figure(figsize=(18, 18))
#gs = gridspec.GridSpec(3, 2, height_ratios=[2, 2, 2])
gs = gridspec.GridSpec(3, 2, height_ratios=[3, 3, 4])
# Plot 1
ax1 = fig.add_subplot(gs[0, 0])
crop_wise_yield = data.groupby(['Crop']).sum()['Yield (Quintal/ Hectare) ']
plt.plot(crop_wise_yield)
crop_wise_production = data.groupby(['Crop']).sum()['Cost of Production (`/Quintal) C2']/10
plt.plot(crop_wise_production)
plt.xticks(rotation ='vertical')
ax1.set_title('Crop-wise Yield and Cost of Production')
ax1.set_xlabel('Crop')
ax1.set_ylabel('Amojnt')
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Plot 2
ax2 = fig.add_subplot(gs[0, 1])
state_crop_yield = data.groupby(['State']).sum()[['Cost of Production (`/Quintal) C2', 'Yield (Quintal/ Hectare) ']]
state_crop_yield.plot(kind='bar', ax=ax2, figsize=(12,7))
ax2.set_title('State based Yield and Cost of Production 2001-2014')
ax2.set_xlabel('State')
ax2.set_ylabel('Amount')
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Plot 3
ax3 = fig.add_subplot(gs[1, 0])
dataframe = recommended_zone.groupby('Crop').sum().plot(kind='bar', ax=ax3, figsize=(15,7))
ax3.set_title('Recommended Zones by Crop')
ax3.set_xlabel('Crop')
ax3.set_ylabel('Count')
ax3.legend(loc='upper right', bbox_to_anchor=(-0.1, 1))

# Plot 4
ax4 = fig.add_subplot(gs[1, 1])
dataframe1[['Andhra Pradesh', 'Tamil Nadu', 'Gujarat', 'Orissa', 'Punjab', 'Haryana', 'Uttar Pradesh', 'Rajasthan',
            'Karnataka', 'Madhya Pradesh', 'West Bangal']].plot(kind='bar', ax=ax4, figsize=(12,7))
ax4.set_title('Recommended Zones by Duration in Days')
ax4.set_xlabel('Duration in Days')
ax4.set_ylabel('Count')
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Plot 5
ax5 = fig.add_subplot(gs[2, :])
plt.scatter(x='Crop', y='Production 2006-07', data=crop_production_data)
ax5.set_title('Crop Production Data for 2006-07')
ax5.set_xlabel('Crop')
ax5.set_ylabel('Production 2006-07')
plt.xticks(rotation=90)

# Add a title and subtitle to the grid


# Add a title and subtitle to the grid
fig.suptitle('Agriculture Crop Production in India', fontsize=24, y=1.05)

# Add a title and subtitle to the grid
#fig.suptitle('Agriculture Crop Production in India', fontsize=24, fontweight='bold')
fig.text(0.5, 0.95, 'An Infographic Visualization Dashboard produced by Marasingha Arachchilage Sanduni Sakunthala Jayathilaka', ha='center', fontsize=16)

# Add a description of the data set
fig.text(0.01, -0.2, 'Data set source: https://www.kaggle.com/datasets/srinivas1/agricuture-crops-production-in-india', fontsize=12)


# Adjust the layout
plt.tight_layout()
fig.subplots_adjust(hspace=1)

# Show the plot
plt.show()

