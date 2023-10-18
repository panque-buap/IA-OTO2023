#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        area = (self.base*self.altura)/2
        return area


# In[5]:


triangulo1 = Triangulo(5,6)
triangulo1.calcularArea()


# In[ ]:




