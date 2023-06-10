#!/usr/bin/env python
# coding: utf-8
import pandas as pd
# ### pandas series

# In[3]:


help(pd.Series)


# In[13]:


mydata=[1233,56456,39475] #python converts this series into a numpy array held inside as a pandas series
myindex=["SL1","SL2","SL3"]


# In[14]:


#myser=pd.Series(mydata) #trying to create an indexed list using pandas.ie myser[0]=1233 = myser[SL1]
#myser
myser=pd.Series(data=mydata,index=myindex)
myser


# In[16]:


myser['SL1']


# In[17]:


ages={'Bedanta':26,'Proteeti':26,'Pol':26} #using series in dictionary


# In[18]:


pd.Series(ages)


# In[20]:


ages['Pol']


# In[21]:


q1={'Japan':80,'China':70,'India':90}
q2={'Brazil':100,'China':40,'India':99}


# In[22]:


sales_q1 =pd.Series(q1)
sales_q2=pd.Series(q2)


# In[23]:


sales_q1


# In[24]:


sales_q2


# In[25]:


sales_q1.keys()


# In[26]:


sales_q1*2


# In[34]:


sales_q1 +sales_q2 #without using add


# In[36]:


sales_q1.add(sales_q2,fill_value=0) #doing this this will not give NAN values for those not present in both the list, instead will keep whatever value it has+0


# In[32]:


#combining numpy and Pandas
print([1,2]*2)#without numpy
import numpy as np
print(np.array([1,2])*2) #using numpy


# ## Dataframe

# In[39]:


np.random.seed(101)
mydata=np.random.randint(0,101,(4,3))
mydata


# In[41]:


myindex=['CA','NY','AZ','TX']
mycolumns=['Jan','Feb','March']


# In[43]:


df=pd.DataFrame(mydata)
df


# In[44]:


df=pd.DataFrame(data=mydata,index=myindex)
df


# In[46]:


df=pd.DataFrame(data=mydata,index=myindex,columns =mycolumns)
df


# ### Filepaths

# In[49]:


pwd #for file fath


# In[51]:


ls #for all files in the place where this file is located


# ### Dataframe basic features

# #### Column operations

# In[88]:


df=pd.read_csv('C:\\Users\\hp\\tips.csv')
df


# In[89]:


print(df.shape)
print("\n")
print(df.columns)
print(df.index) # to return number of columns


# In[90]:


df.head()


# In[91]:


df.tail(5)


# In[92]:


df.info()


# In[93]:


df.describe() #to return statistical values


# In[94]:


df.describe().transpose()


# In[95]:


df['total_bill'] #we are using total bill as an index previously as shown above


# In[96]:


mycols=['total_bill','tip'] #we are creating a subset of the main dataset
df[mycols]


# In[97]:


df[['total_bill','size']] # we can do it in one step as well


# In[98]:


#df['tip']/df['total_bill'] #peforming mathematical operations among columns
df['tip/total']=df['tip']/df['total_bill']
df['tip/total'] # we created a new column


# In[99]:


df['tip/total']=np.round(df['tip']/df['total_bill'],2) #we rounded the values using built-in Numpy functions upto 2 decimals
df['tip/total']


# In[100]:


df.head()


# In[101]:


#removing columns
# to remove rows: axis =0, for columns, axis =1
#try not using inplace
#if you dont want to use inpplace, try df= df.drop('tip/total',axis=1)
df.drop('tip/total',axis=1,inplace=True) 
df


# #### Row Operations

# In[102]:


df.index


# In[103]:


df['tip/total']=np.round(df['tip']/df['total_bill'],2) #we rounded the values using built-in Numpy functions upto 2 decimals
df['tip/total']


# In[106]:


df.set_index('tip/total')   # we can set index but this is not the most correct as tip/total migh have duplicate values, else we would have seen that index will be tip/toal(primary key)
df.head()


# In[107]:


df.reset_index() #removes the indexing(not accurate in this code). the index  will reset back to acolumn


# In[108]:


df.iloc[0] # first row(iloc = index location)


# In[110]:


#df.loc['#index name'] -> incase we have a primary key as index we can enter the primary key here instead of the row number


# In[112]:


df.iloc[0:6] #range


# In[131]:


#df.loc['primary key 1' , 'primary key 2',...] #range
#df.drop(,'row primary key name',axis=0) axis=0 means rows


# In[132]:


#adding rows    !!!NOT WORKING
df #244 rows


# In[133]:


#new_row = df.iloc[0]
#new_row


# In[134]:


#df=df.append(new_row,ignore_index = True)
#df


# ### Conditional filtering

# In[145]:


#we created a data frame to perfprm conditional formatting


# In[150]:


np.random.seed(101)
mydata=np.random.randint(0,101,(4,3))
mydata


# In[151]:


df=pd.DataFrame(mydata,index =mycountry,columns = myindex)


# In[152]:


df


# In[153]:


df['pop']>50 #return true for index that follows the condition


# In[154]:


df=pd.read_csv('C:\\Users\\hp\\tips.csv')
df


# In[155]:


df['total_bill']>40


# In[156]:


df.set_index('total_bill')


# In[159]:


df.reset_index()


# In[160]:


boolean=df['total_bill']>40


# In[163]:


df[boolean]  #returns only those rows the return true in above code 


# In[164]:


df[df['total_bill']>40] #same as above 2 piece of code


# In[171]:


#multiple conditions
#AND &
#OR |
#df[df['total_bill'>40 & 'sex'=='Male']] to combine these 2

df[(df['total_bill']>40) & (df['sex']=='Male')]


# In[174]:


options=['Sat','Sun']
df[df['day'].isin(options)]


# In[178]:


df[df['day'].isin(options)]


# ### Single column operations

# In[4]:


import pandas as pd
df=pd.read_csv('C:\\Users\\hp\\tips.csv')
df.info()


# In[5]:


#suppose we want to extract last  digit of size(which is an integer, we cant do it )
1234[-4]


# In[8]:


str(1234)[-2:] #therefore we convert the integer to string in order to extract parts of the integer


# Pandas Apply function

# In[9]:


#in cases like above, pandas dont have a builtin function.In this case We need to use "apply" feature to use custom functions


# In[27]:


def last_1(num):
    return str(num)[-1:]


# In[28]:


last_1(123456)


# In[29]:


df['last_num']=df['size'].apply(last_1) #we applied "Apply" in the dataframe
last_num


# In[31]:


df   #new column (last_num has been added that return the last digit of size column)


# ### Multiple column operations 

# In[32]:


def simplenumber(num):
    return(num*2)


# In[33]:


simplenumber(4)


# In[35]:


df['size_operation'] = df['size'].apply(simplenumber)
df


# In[38]:


df['size_operation2'] = df['size'].apply(lambda num :num-2) #using lambda function
df


# In[43]:


# section actually starts here
def quality(total_bill,tip):
    if tip/total_bill>0.25 :
        return 'Generous'
    else:
        return 'Not Generous'


# In[44]:


quality(1.01,16.99) #tried for first row


# In[46]:


#using lambda functio
# after = :   columns we are using                  our lambda function using our custom function 'quality' and its paramenters        
df['Quality']=df[['total_bill','tip']].apply(lambda df:quality(df['total_bill'],df['tip']),axis =1) #just to confirm that we are working on columns and not rows
#instead df


# In[50]:


#instead of lambda function, we can also use "vectorize"
#vectorize is advantageous as it allows to action on a function that we expect that a numpy array will be worked on
# the quality function dint specify that we will be working on a numpy array. So we used the lambda function to pass the df

import numpy as np
df['Quality_vector']=np.vectorize(quality)(df['total_bill'],df['tip'])
df


# ### Pandas -useful methods(statistical)

# In[98]:


df=pd.read_csv('C:\\Users\\hp\\tips.csv')


# In[99]:


print(df.info())
print("\n")
print(df.describe())
print("\n")
print(df.head())


# In[100]:


df.describe().transpose()


# In[101]:


df.sort_values('tip') #default way of sorting is ascending but 


# In[102]:


df.sort_values('tip',ascending=False)


# In[103]:


df
print(df.sort_values('tip'))
print(df.sort_values(['tip','size'])) #first it will sort by tip then by size


# In[104]:


df['total_bill'].max() #max value of total bill


# In[105]:


df['total_bill'].idxmax()#index of the row containing total bill


# In[106]:


df.iloc[170] #to figure out which row is this


# In[107]:


print(df['total_bill'].min())
print(df['total_bill'].idxmin())


# In[108]:


df.iloc[67]


# In[109]:


df.drop(['smoker','day','time','sex'],axis=1,inplace=True)
df


# In[113]:


#df.corr() is used to find the correlation betwwen various fields.Like if its 0.44, that is value of a variable will be affected by +0.44 if another value on which this is dependent changes

df.corr()
#here the matrix values(1,1),(2,2),(3,3) is perfectly depndent on themself 
#also values will be same for (a,b),(b,a)


# Counts

# In[136]:


df=pd.read_csv('C:\\Users\\hp\\tips.csv')
print(df['sex'].count())
print("\n")
print(df['sex'].value_counts())


# In[137]:


print(df['day']) #to print the day column
print('\n')
print(df['day'].nunique()) #no of unique values in day column  = print(len(df['day'].unique()))
print('\n')
print(df['day'].unique()) #the unique values in day column 
print("\n")
print(df['day'].value_counts()) #counts per unique values


# REPLACE

# In[138]:


df['sex'].replace('Female','Women',inplace=True)
df


# In[140]:


#for multiple rows

df['sex'].replace(['Women','Male'],['F','M'],inplace=True)
df


# MAP

# In[143]:


#shortcut of replace method

MYMAP={'F':'female','M':'male'}


# In[144]:


df['sex'].map(MYMAP)   


# DUPLICATES

# In[149]:


mydata =pd.DataFrame(['Proteeti','Parthiv','Proteeti','Reedom'],[1,2,3,4])
mydata


# In[152]:


mydata.duplicated() #return true if there is a duplicate value


# In[153]:


mydata.drop_duplicates(inplace=True)


# In[154]:


mydata


# BETWEEN

# In[160]:


#original dataframe
df['ooo']=df['total_bill'].between(10,20)
df


# In[162]:


df[df['total_bill'].between(10,20)] #returns dataframe only between the given range


# In[166]:


df.nlargest(10,'tip') #returns 10 rows that have the largest tips in desc order # try nsmallest


# SAMPLING

# In[168]:


df.sample(5) #samples 5 random rows from the dataframe


# In[171]:


df.sample(frac=0.1) #returns 10 percent of the sample


# In[ ]:




