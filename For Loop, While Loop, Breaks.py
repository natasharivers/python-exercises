#!/usr/bin/env python
# coding: utf-8

# In[1]:


geek_status = True


# In[2]:


if geek_status:
    print('haha nerd')
else:
    print('normie')


# In[3]:


beverage_of_choice = 'coffee'


# In[5]:


if beverage_of_choice == 'tea':
    print('not big on coffeine?')
elif beverage_of_choice == 'monster energy':
    print('whoa slow down')
elif beverage_of_choice == 'coffee':
    print('ayyy')
else: 
    print('i dont know anything about that')


# In[6]:


##for loop


# In[8]:


for n in range(10):
    print(n)


# In[9]:


for n in range(1, 10, 2):
    print(n)


# In[18]:


fruits = ['apple', 'banana', 'cherry', 'grapefruit', 'orange']
    


# In[19]:


for i, el in enumerate(fruits):
    print(fruits[i])


# In[20]:


# while loop


# In[21]:


patience = ''


# In[27]:


while patience != 'please stop':
    patience = input('Hi buddy how\'s it going')


# In[26]:


# requires you to respond to hi buddy hows it going UNTIL you respond with "please stop" to end the while loop


# In[24]:


citrus = ['grapefuit', 'orange', 'lemon']
for fruit in fruits:
    if fruit in citrus:
        print('tangy')
        break
    else:
        print('boring')


# In[ ]:




