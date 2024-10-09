#!/usr/bin/env python
# coding: utf-8

# In[33]:


adult=int(input("give me a number"))
def check_age(age1,age2):
    if age1==adult or age2==adult:
        return age1 or age2
    else:
        print("you are not old enough to vote")
user1=int(input("enter the first age"))
user2=int(input("enter the second age"))
check_result=check_age(user1,user2)
print("you are old enough to vote")


# In[ ]:





# In[ ]:




