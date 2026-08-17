"""
   NETFLIX USER DATA ANALYSIS 
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# LOAD DATA
df = pd.read_csv("netflix_users.csv")

print('--- CHECK DATA AND COLUMN INFORMATIOM---\n')
print(df.head())
print(df.info())
print('-' * 50)

print('---CHECK DUPLICATES AND MISSING VALUES---\n')
print('Duplicate_values =', df.duplicated().sum())
print(df.isnull().sum())
print('-' * 50)

# # FIX DATA TYPES
print('--- FIX DATA TYPES ---\n')
df['Last_Login'] = pd.to_datetime(df['Last_Login'])
print(df.info())
print('-' * 50)

# # FIND NUMBER USERS PER COUNTRY
print('--- NUMBER OF USERS BY COUNTRY---\n')
print(df['Country'].value_counts())
print('-' * 50)

plt.figure(figsize=(12,6))
df['Country'].value_counts().plot(kind='bar',color='Green')
plt.title("Number Of Users Per Country")
plt.xlabel('Country')
plt.ylabel('Number Of Users')
plt.xticks(rotation=45)
plt.show()

print('--- COUNT OF SUBSCRIPTION TYPE AND FAVORITE GENRE\n')
print(df['Favorite_Genre'].value_counts())
print(df['Subscription_Type'].value_counts())
print('-' * 50)

# COUNT OF SUBSCRIPTION TYPE AND FAVORITE GENRE
columns_titles = {
    'Subscription_Type' : 'Subscription Types Counts',
    'Favorite_Genre'    : 'Favorite Genre Counts'
}

for column, title in columns_titles.items():
    plt.figure(figsize=(12,6))
    df[column].value_counts().plot(kind='bar',color='Orange')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# DISTRIBUTION OF USERS BY COUNTRY
print('--- DISTRIBUTION OF USERS BY COUNTRY ---\n')
user_counts_by_country = df['Country'].value_counts().reset_index()
user_counts_by_country.columns = ['Country','User_ID']
print('-' * 50)



fig = px.choropleth(user_counts_by_country, locations='Country',
                     locationmode='country names',color='User_ID',
                     hover_name='Country',title='User Distribution By Country',
                     color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(
    width=1000,
    height=700,
    title_font_size=24,
    geo=dict(
        showframe=False,
        showcoastlines=False
     )
)
fig.show()

# SUBSCRIPTION TYPE ACCORDING TO COUNTRY
print('--- SUBSCRIPTION TYPE BY COUNTRY ---\n')

plt.figure(figsize=(12,6))

sns.countplot(data=df,x='Country',hue='Subscription_Type',palette='Set2')
plt.title('Subscription Type By Country')
plt.xticks(rotation=45)
plt.show()

subs_by_country = df.pivot_table(index='Country',columns='Subscription_Type', values='User_ID',aggfunc='count',fill_value=0)


subs_by_country['Total'] = subs_by_country.sum(axis=1)
print(subs_by_country.sort_values(by='Total',ascending=False).reset_index())
print('-' * 50)

# USER ID BY AGE
print('--- AGE DISTRIBUTION ---\n')

Age_Distribution = df['Age'].value_counts().sort_index()
print(Age_Distribution)
print('-' * 50)

plt.figure(figsize=(12,6))
Age_Distribution.plot(kind='bar',color='purple',edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('age')
plt.ylabel('Count')
plt.show()


age_bins = pd.cut(
    df['Age'],
    bins=[0, 18, 30, 45, 60, 100],
    labels=['0-18', '19-30', '31-45', '46-60', '60+'],
    include_lowest=True
  )

Age_Distribution = age_bins.value_counts().sort_index()
print(Age_Distribution)
print('-' * 50)

plt.figure(figsize=(12,6))
sns.histplot(data=df,x='Age',bins=6,color='purple',edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# AVERAGE WATCH TIME HOURS BY COUNTRY
print('---WATCH TIME BY COUNTRY ---\n')

watch_time_country = df.groupby('Country')['Watch_Time_Hours'].mean().sort_values(ascending=False)
print(watch_time_country)
print('-' * 50)

plt.figure(figsize=(12,6))
watch_time_country.plot(kind='bar',color='purple')
plt.title('Average Watch Time Hours By Country')
plt.xlabel('Country')
plt.ylabel('Watch_Time_Hours')
plt.xticks(rotation=45)
plt.show()

# Count Unlog Time From Last Login To Current date
print('--- UNLOG DAYS ---\n')
df['Unlog_Time'] = pd.Timestamp.now() - df['Last_Login']
df['Unlog_Days'] = df['Unlog_Time'].dt.days
print(df.head(20))
print('-' * 50)