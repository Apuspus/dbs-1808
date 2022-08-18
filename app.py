#!/usr/bin/env python
# coding: utf-8

# In[21]:


from flask import Flask,request,render_template


# In[22]:


#__ are used for reserved/magic words

app = Flask(__name__)


# In[23]:


import joblib


# In[24]:


# @ is a decorator --> Any function that needs to be run must go through the decorator

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html",result1=r1,result2=r2))

    else: #before you click enter on the "website"
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[25]:


#Development Environment 

if __name__ == "__main__":
    app.run()


# In[ ]:




