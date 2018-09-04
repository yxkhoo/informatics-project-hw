#import pandas library
import pandas as pd

#read the original data
df = pd.read_csv('data.csv')

#stack the 'State' columns
stacked_df = df.set_index(['State']).stack(dropna=False)

#reset the index to reshape the data
newdf = stacked_df.reset_index()

#seperate year and rate type of the unstacked columns
yrlist = newdf.level_1.str.split(' ')

#create 'Year' column, put the first element (year) from the list
newdf['Year'] = [i[0] for i in yrlist]

#create 'Rate Type' column, put the second element (divorce/marriage) rom the list
newdf['Rate Type'] = [i[1] for i in yrlist]

#create '% value' column, put the values into the column
newdf[' % value'] = newdf[0]

#drop the 'level_1' column
outputdf = newdf.drop(['level_1',0], axis = 1)

#output the data to a csv file
outputdf.to_csv('outputdata.csv')
