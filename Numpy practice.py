#!/usr/bin/env python
# coding: utf-8

# # List to array using numpy

# In[1]:


my_list=[1,2 ,3,4]


# In[2]:


type(my_list)


# In[3]:


import numpy as np
arr= np.array(my_list)


# In[4]:


type(arr)


# # arrange feature

# In[5]:


twoD_list=[[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


np.arange(0,10)#starting and ending index 


# In[7]:


np.arange(0,10,2)#starting and ending index with a gap of 2


# In[8]:


np.arange(0,101,2)


# # zeros feature
# 

# In[9]:


np.zeros(5) #prints zeros 5 times. this are foating point numbers


# In[10]:


np.zeros((5,5)) 


# # ones and linspace 

# In[11]:


np.ones(5)


# In[12]:


np.linspace(0,10,3) #returns numbers linearly spaced by 5 between 5 n 10


# In[13]:


np.linspace(0,10,21)


# # random number

# In[14]:


np.random.rand(5) #5 random numbers in range[0,1)


# In[15]:


np.random.rand(5,3)


# In[16]:


np.random.randint(1,50,5) # lower limeit, upper limit, no of occurances


# In[17]:


np.random.randint(1,50,(4,5))


# In[18]:


np.random.seed(42) #for getiing the same random numbers. Else the random number keeps changing
np.random.rand(4)


# In[19]:


arr=np.random.randint(0,10,5) #max/min in array
arr


# In[20]:


print(arr.max())
print(arr.min())
print(arr.argmax()) #index of max
print(arr.argmin()) #index of min
print(arr.shape)
print(arr.reshape(5,1)) #change shape of array


# # numpy indexing and selections

# In[21]:


brr=np.arange(0,11)


# In[22]:


brr


# In[23]:


print(brr[9]) #value at index 9
print(brr[1:7]) #value within a range of index

      


# In[24]:


brr[0:5] =100 #setting values in idex 0 to 5 = 100
brr


# In[25]:


brr=np.arange(0,11) #resetting the values
brr


# ### slicing

# In[26]:


slice_of_brr=brr[0:5]
slice_of_brr


# In[27]:


slice_of_brr[0:4]=200 #to show that it affects the original array too
print(slice_of_brr)
print(brr)


# In[28]:


brr=np.arange(0,11)
brr


# In[29]:


#to prevent that from happening we use the copy method
brr_copy =brr.copy()
slice_of_brr_copy=brr_copy[0:5]
slice_of_brr_copy[0:3]=200
print(brr_copy)
print(brr)


# In[30]:


#creting 2d arrays normally
arr_2d=[[1,2,3],[4,5,6],[7,8,9]]
arr_2d 


# In[31]:


#creting 2d arrays using numpy
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d


# In[32]:


arr_2d.shape


# In[33]:


arr_2d[2]


# In[34]:


arr_2d[2,2]


# In[35]:


#slicing
arr_2d[:1,1:] =99
arr_2d


# In[36]:


arr_2d<8


# In[38]:


a=np.arange(0,11)
a


# In[39]:


#to show that we can pass  conditions in array as well
bool_a=a>4
bool_a


# In[40]:


a[a>4]


# #### array operations

# In[41]:


ar=np.arange(0,10)


# In[42]:


print(ar+ar)
print(ar*2)
print(ar*5)


# In[43]:


br=np.arange(0,10)
br


# In[44]:


np.sqrt(br)


# In[45]:


np.sin(br)


# In[46]:


np.log(br)


# In[47]:


print(br.sum())


# In[48]:


print(br.mean())


# In[53]:


cr=np.arange(0,25).reshape(5,5)
cr


# In[54]:


cr.sum()


# In[56]:


cr.sum(axis=0) #sum column wise


# In[57]:


cr.sum(axis =1) #row wise


# In[ ]:




