import panda as pd

##df = pd.read_csv('pokemon_data.csv') #.csv file
#print(df.head(5))

#df_xlsx = pd.read_excel('pokemon_data.xlsx') #.xlsx file
#print(df_xlsx.head(3))

#df = pd.read_csv('pokemon_data.txt', delimiter='\t')
##df = pd.read_csv('pokemon_data.txt') #.txt file
#print(df.head(3))

#print(df.columns) #Show Columns
#print(df[['Name', 'Type 1', HP]]) #Show the columns selected
#print(df.iloc[0:4]) #Get multiple
#print(df.iloc[4]) #Get one row
#for index, row in df.iterrows(): #Show data in a index format, one by one
    #print(index, row)
#df.loc[df['Type 1'] == "Water"]   #Show all type 1 are fire

#df.describe() #Describes in numeric

#df.sort_values('Name', ascending=False) #Sort by name
#df.sort_values(['Type 1', 'HP']) #Show more than one value
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] #Short elements in a variable
#df.head(5)

#df = df.drop(columns=['Total']) #Removes column
#df['Total'] = df.iloc[:,4:10].sum(axis=1) #Iloc all columns and rows
#cols = list (df.columns)
#df = df[cols[0:4]+[cols[-1]]+cols[4:12]] #plus
#df.head(5)

#df.to_csv('modified.csv', index=False) #Makes a copy with other name, removes the index
#df.to_csv('modified.csv', index=False, sep='\t') #Separates with spaces

#df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison' ) | (df['HP'] > 70)] #Show the columns in one and conditions
#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison' ) & (df['HP'] > 70)] #Filters and creates a new file
#new_df.to_csv('filtered.csv') #Filters and creates a new file
#new_df = new_df.reset_index() #Add the index
#new_df.reset_index(drop=True) #Shows the old index
#df = pd.read_csv('filtered.csv') #Reads file
#print (new_df)
#df.loc[df['Name'].str.contains('Mega')] #Filters by string
#df.loc[~df['Name'].str.contains('Mega')] #Filters by string and removes

#import re
#df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)] #Can filter two elements at one regex
#df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)] #Ignores caps
#df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)] #Show everthing starts with
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' #Renames a field
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True #If is fire or Legendary, sets true
#df
#df.loc[df['Total'] > 500, ['Generation','Legendary']] = 'TEST' #If the conditionals are true fills the fields
#df
#df.groupby(['Type 1']).mean() #Groups be field
#df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False) #Sort by field and ascending
#df['count'] = 1
#df.groupby(['Type 1']).count()

#new_df = pd.DataFrame(columns=df.columns) #Estrucutre of columns
#for df in pd.read.csv('pokemon_data.csv', chunksize=5):
       #print(df)