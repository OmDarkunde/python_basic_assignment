#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment no 1


# In[ ]:


#1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
"""
* -- mathematical opearator
'hello' -->  string
-87.8 --> float
-  ---> mathematical oprator
/  ---> mathematical operator
+ ---> mathematical operator
6  --> integer
"""


# In[8]:


#2. What is the difference between string and variable? 
"""
variable is a box where we can store multiple data and string is the data which we can use to fill the variables 

"""
example = "hello world"
# example --> is the variable & 'hello world' --. is the string which is the data of the variable 


# In[9]:


# 3. Describe three different data types.
"""
 int --> integers is the data type in which we can hold the natural numbers  (1,2,3,4,..) numbers which comes without deciaml valus thoses all are integers
 float --> float is the data type in which we can hold the deciaml numbers (1.2 , 1.6 ,3.5 , 1.0) 1.0 is also a float number
 string --> string is the sequence of the charcter data , stringcan create through "" or  '' both are the ways to create the string 
"""


# In[ ]:


# 4. What is an expression made up of? What do all expressions do?
"""
What is an expression made of what do all expressions do?
An expression is a construct made up of variables, operators, and method invocations, which are constructed according to the syntax of the language, that evaluates to a single value.

Expressions are representations of value. They are different from statement in the fact that statements do something while expressions are representation of value
"""


# In[11]:


#5. This assignment statements, like spam = 10. What is the difference between an expression and a statement? 
"""
expressiion is the comabination of values  and function  that are combined and interpreted by the compiler to create a new value
and string are the  statement” which is just a stand alone unit of execution and doesn't return 
"""


# In[12]:


#6. After running the following code, what does the variable bacon contain?

bacon = 22
bacon + 1
"""out put is 23 because 1 is added to the bacon and bacon contains a value that is 22  so 1 is added to that 22"""


# In[13]:


#7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
"""output is spam spam spam beacuse spam*3  is evaluate because python obey the bottom-up approch of the same element"""


# In[ ]:


# 8 Why is eggs a valid variable name while 100 is invalid?
""" egg is valid because we can give the character name to the variable beacuse of the rule we have to start the variable by a character
100 is not valid beacause a variable is not started by a number we can use 100 after a charater in the variable name that is valid """


# In[ ]:


# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
""" for the interger  -- > int()
for the floating-number --> float()
for the string  -- > str()"""


# In[16]:


#10. Why does this expression cause an error? How can you fix it?

'I have eaten ' + str(99) + ' burritos.'
"""we will convert the 99 int data type to the string data type there are two types to do that 
1 -- '99'  place the 99  in the single / doubble inverted comma 
2 -- put the 99  into the str() data type """

