#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Initializing a queue 
q = Queue(maxsize = 3) 
#queue = [] 
  
# Adding elements to the queue 
queue.append('Chicken Nuggets') 
queue.append('Fries') 
queue.append('Sprite')
queue.append('Ketchup')
queue.append('Mustard')
queue.append('Extra Napkins')

print("Drive-Thru Order") 
print(queue) 
print('Size of Order:',q.qsize()) 
 
# Removing elements from the queue 
print("\nElements dequeued from queue") 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements") 
print(queue) 


# In[ ]:




