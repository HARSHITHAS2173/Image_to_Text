#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import PIL
import pytesseract
import re
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().system('pip install pytesseract')


# In[38]:


img1 = PIL.Image.open(r"C:\Users\ADMIN\Desktop\Important_stuffs\Projects\Image_to_Text\test1.JPG")
img2 = PIL.Image.open(r"C:\Users\ADMIN\Desktop\Important_stuffs\Projects\Image_to_Text\test2.PNG")


# In[39]:


img1


# In[40]:


img2


# ## 

# In[25]:


get_ipython().system('pip install pytesseract')


# In[41]:


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'


# In[42]:


text_data1 = pytesseract.image_to_string(img1.convert('RGB'), lang='eng')


# In[43]:


text_data2 = pytesseract.image_to_string(img2.convert('RGB'), lang='eng')


# In[44]:


print(text_data1)


# In[45]:


print(text_data2)


# In[46]:


import re
m = re.search("Name: (\w+)", text_data1)
name = m[1]
name


# In[47]:


m = re.search("Start Date: (\S+)", text_data1)
start_date = m[1]
start_date


# In[ ]:




