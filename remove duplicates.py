#!/usr/bin/env python
# coding: utf-8

# In[1]:


input = 'sttranger thinnggsss carrot'
output = ''

for ch in input:
    if ch not in output:
        output = output + ch
print(output)

