#!/usr/bin/env python
# coding: utf-8

# #study

# ##while loops
# -not the be all end all loop
# -goal with a while loop is to run as many times as needed
# -that manes while loops != the best tool for iterating finite lists of numbers
# 
# #(ex): while True:
#     #       print("loop going forever")
#     #^ will continue fOREVER until .... your computer dies
#     

# In[5]:


##looping through a list dictionaries
drinks = [
    { 
        "type" : "water",
        "calories": 0,
        "number_consumed" : 5
    
    },
    {
        "type" : "orange juice",
        "calories": 220,
        "number_consumed" : 3
    },
    {    
        "type" : "gatorage",
        "calories": 150,
        "number_consumed" : 5
    },
    ]


# In[6]:


drinks


# ##one weird trick to solving looping problems == blow off the loop, forgetaboutiiiiiit!
# - make a variable holding only the first item

# In[13]:


drink = drinks[1] #interchangeable index, will change rest of the formula
drink


# In[14]:


drinktype = drink["type"] #gives you the type (water, oj, gatorage)
calories = drink["calories"] 
number_consumed = drink["number_consumed"]
total_calories = number_consumed * calories
print(f"{total_calories} is the total calories from drinking {number_consumed} units of {drinktype}")


# In[15]:


for drink in drinks: #this is a for loop
    drinktype = drink["type"] 
    calories = drink["calories"] 
    number_consumed = drink["number_consumed"]
    total_calories = number_consumed * calories
    print(f"{total_calories} is the total calories from drinking {number_consumed} units of {drinktype}")


# ##NESTED DICTIONARIES

# In[17]:


x = [
    [1, 2, 3],
    [2, 3, 4]
]


# In[20]:


first_row = x[0] #gives first list in nested dictionary
first_row


# In[21]:


first_row[1] #gives you the second element of the first list in the nested dictionary


# In[ ]:


#regular dictionary


# In[36]:


beatles = [
    "john",
    "ringo",
    "george",
    "paul"
]
beatles


# In[37]:


second_on_list = beatles[1] #gives second item on list
second_on_list


# In[38]:


second_on_list[-1] #gives us the last character of the second item from list


# In[39]:


#SAME AS
beatles[1][-1]


# In[41]:


#ds_topics.keys() #returns ALL the values
#ds_topics.values() #returns ALL the keys


# In[ ]:


#MORE NESTED DICTIONARIES


# In[42]:


ds_topics = {
    "fundamentals" : {
        "beginning" : "data science pipeline",
        "middle" : "ds skills in demand",
        "end" : " git"
    },
    "sql" : {
        "beginning" : "what is sql?",
        "middle" : "joins and subqueries",
        "end" : " case"
    "python" : {
        "beginning" : "how to run python",
        "middle" : "loops and data structure",
        "end" : "python assessment"
    }
}


# In[ ]:


ds_topics["python"]["middle"] #will return all data from middle of python


# In[34]:


#GIT SYNTAX
ds_topics.get("python").get("middle")


# #to loop through a dictionary
# for key in ds_topics.keys()
#     if key.lower() == "python":
#         middle_section =ds_topics[key]["middle"]
#         print(f"In the middle of the {key} lessons, we focus on {middle_section}")
