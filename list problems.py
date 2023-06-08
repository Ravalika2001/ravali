#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1. Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.# 
list1=[x for x in range(1200,2000,130)]
print(list1)


# In[5]:


#2. Use list comprehension to construct a new list but add 6 to each item.

my_list1=[1,2,3,4,5]
my_list2=[x+6 for x in my_list1]
print(my_list2)


# In[6]:


#3. Using list comprehension, construct a list from the squares of each element in the list.

my_list1=[1,2,3,4,5]
print([x**2 for x in my_list1])


# In[7]:


#Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
my_list1=[1,2,3,4,5,6,7,8,9,10]
print([x**2 for x in my_list1 if x>7])
   


# In[8]:


#Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. 
   #In the same list comprehension make the key names all upper case.
#dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict1={x.upper() for x in dict}
print(dict1)


# In[ ]:




