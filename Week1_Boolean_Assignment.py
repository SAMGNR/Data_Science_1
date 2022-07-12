#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q. Declare a boolean value and store it in a variable.
# Check the type and print the id of the same.

a =True
print(type(a),id(a))


# In[2]:


# Q. Take one boolean value between 0 - 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come the same. Check why?

a =10
b =10
print(bool(a),id(a))
print(bool(b),id(b))


# In[5]:


# Q. Arithmetic Operations on boolean data
# Take two different boolean values.
# Store them in two different variables.
a =10
b =20
# Do below operations on them:-
# Find sum of both values
print(bool(a)+bool(b))
# Find difference between them
print(bool(a)-bool(b))
# Find the product of both.
print(bool(a)*bool(b))
# Find value after dividing first value with second value
print(bool(a)/bool(b))
# Find the remainder after dividing first value with second value
print(bool(a)%bool(b))
# Find the quotient after dividing first value with second value
print(bool(a)//bool(b))
# Find the result of first value to the power of second value.
print(bool(a)**bool(b))


# In[6]:


# Q. Comparison Operators on boolean values
# Take two different boolean values.
# Store them in two different variables.
# Do below operations on them:-
# Compare these two values with below operator:-
# Greater than, '>'
print(bool(a)>bool(b))
# less than, '<'
print(bool(a)<bool(b))
# Greater than or equal to, '>='
print(bool(a)>=bool(b))
# Less than or equal to, '<='
print(bool(a)<=bool(b))
# Observe their output(return type should be boolean)


# In[7]:


# Q. Equality Operator
# Take two different boolean values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
print(bool(a)==bool(b))
print(bool(a)!=bool(b))
# Observe the output(return type should be boolean)


# In[9]:


# Q. Logical operators
# Observe the output of below code
# Cross check the output manually
print(True and True)
#----------------------------------------->Output is True

print(False and True)
#----------------------------------------->Output is False
print(True and False)
#----------------------------------------->Output is False
print(False and False)
#----------------------------------------->Output is False
print(True or True)
#----------------------------------------->Output is True
print(False or True)
#----------------------------------------->Output is True
print(True or False)
#----------------------------------------->Output is True
print(False or False)
#----------------------------------------->Output is False
print(not True)
#----------------------------------------->Output is False
print(not False)
#----------------------------------------->Output is True


# In[14]:


# Q. Bitwise Operators
# Do below operations on the values provided below:-
# Bitwise and(&) --------------> True, True -------> Output is True
# Bitwise or(|) --------------> True, False -------> Output is True
# Bitwise(^) --------------> True, False -------> Output is True
# Bitwise negation(~) ---------> True -------> Output is -2
# Bitwise left shift ---------> True,2 -------> Output is 4
print(True <<2)
print(bool(1) <<2)
# Bitwise right shift ---------> True,2 -------> Output is 0
print(True >>2)
print(bool(1) >>2)
# Cross check the output manually


# In[16]:


# Q. What is the output of expression inside the print statement. Cross
# check before running the program.
a = True
b = True
print(a is b) #True or False? #
print(a is not b) #True or False?

a = False
b = False
print(a is b) #True or False?
print(a is not b) #True or False?


# In[17]:


# Q. Membership operation
# in, not in are two membership operators and it returns boolean value
print(True in [10,10.20,10+20j,'Python', True])
# True
print(False in (10,10.20,10+20j,'Python', False))
# True
print(True in {1,2,3, True})
# True
print(True in {True:100, False:200, True:300})
# True
print(False in {True:100, False:200, True:300})
# True


# In[ ]:




