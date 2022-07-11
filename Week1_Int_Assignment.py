#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q. Declare an int value and store it in a variable.
# Check the type and print the id of the same.

a =10
print(a,type(a),id(a))


# In[3]:


# Q. Take one int value between 0 - 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come the same. Check why?

a =10
b =10

print(a,b,id(a),id(b))

id of both a and b same, because of the object reusability of integer caching -5 to 256.


# In[4]:


# Q. Take one int value either less than -5 or greater than 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come different.Check why?

a = -10
b = 300

print(a,b,id(a),id(b))

id of both a and b same, because of the object reusability of integer caching -5 to 256.


# In[8]:


# Q. Arithmetic Operations on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
# Find sum of both numbers
# Find difference between them
# Find the product of both numbers.
# Find value after dividing first num with second number
# Find the remainder after dividing first number with second number
# Find the quotient after dividing first number with second number
# Find the result of the first num to the power of the second number.

a = 30
b = 15

# Find sum of both numbers
print(a+b)
# Find the product of both numbers.
print(a*b)
# Find value after dividing first num with second number
print(a/b)
# Find the remainder after dividing first number with second number
print(a%b)
# Find the quotient after dividing first number with second number
print(a//b)
# Find the result of the first num to the power of the second number.
print(a**b)


# In[9]:


# Q. Comparison Operators on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
# Compare se two numbers with below operator:-
# Greater than, '>'
print(a>b)

# Smaller than, '<'
print(a<b)
# Greater than or equal to, '>='
print(a>=b)
# Less than or equal to, '<='
print(a<=b)
# Observe their output(return type should be boolean)


# In[12]:


# Q. Equality Operator
# Take two different integer values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
a = 30
b = 15
print(a==b)
print(a!=b)
# Observe the output(return type should be boolean)


# In[13]:


# Q. Logical operators
# Observe the output of below code

# Cross check the output manually
print(10 and 20)
#----------------------------------------->Output is 20
print(0 and 20)
#----------------------------------------->Output is 0
print(20 and 0)
#----------------------------------------->Output is 0
print(0 and 0)
#----------------------------------------->Output is 0
print(10 or 20)
#----------------------------------------->Output is 10
print(0 or 20)
#----------------------------------------->Output is 20
print(20 or 0)
#----------------------------------------->Output is 20
print(0 or 0)
#----------------------------------------->Output is 0
print(not 10)
#----------------------------------------->Output is False
print(not 0)
#----------------------------------------->Output is True


# In[21]:


# Q. Bitwise Operators
# Do below operations on the values provided below:-
# Bitwise and(&) -----------------------------------------> 10, 20
print(bin(10))
print(bin(20))

# 0b01010
# 0b10100
# ---------
print(0b00000)
# -------> Output is 0


# Bitwise or(|) -----------------------------------------> 10, 20
# 0b01010
# 0b10100
# ---------
print(0b11110)
# -------> Output is 30
# Bitwise(^) -----------------------------------------> 10, 20
# 0b01010
# 0b10100
# -----------
print(0b11110)
# -------> Output is 30


# Bitwise negation(~) ------------------------------------> 10
# -(n+1)
print(~10)
# -------> Output is -11



# Bitwise left shift ------------------------------------> 10,2
# num*2**no. of shifts
print(10*2**2)
# -------> Output is 40


# Bitwise right shift ------------------------------------> 10,2
# num//2**2
print(10//2**2)

# -------> Output is 2
# Cross check the output manually


# In[22]:


# Q. What is the output of expression inside print statement. Cross check
# before running the program.

a = 10
b = 10
print(a is b) #True or False?
# True

print(a is not b) #True or False?
# False
a = 1000
b = 1000
print(a is b) #True or False?
# False
print(a is not b) #True or False?
# True


# In[36]:


# # Q. What is the output of expression inside print statement. Cross check
# # before running the program.
# print(10+(10*32)//2**5&20+(~(-10))<<2)
# print(10+320//32  &  29 <<2)
# print(10+10 & 116)
print(20&116)


# In[37]:


# Q. Membership operation
# in, not in are two membership operators and it returns boolean value
print('2' in 'Python2.7.8')
# True
print(10 in [10,10.20,10+20j,'Python'])
# True
print(10 in (10,10.20,10+20j,'Python'))
# True
print(2 in {1,2,3})
# True
print(3 in {1:100, 2:200, 3:300})
# True
print(10 in range(20))
# True


# In[40]:


# Q. An integer can be represented in binary, octal or hexadecimal form.
# Declare one binary, one octal and one hexadecimal value and store them
# in three different variables.
# Convert 9876 to its binary, octal and hexadecimal equivalent and print
# their corresponding value.

# a =0b1010
# b =0c3465
# c =0xfc45

print(bin(9876))
print(oct(9876))
print(hex(9876))


# In[45]:


# Q. What will be the output of following:-
a = 0b1010000
print(a)
print(0b1010000)
b = 0o7436
print(b)
print(0o7436)
c = 0xfade
print(c)
print(0xfade)
print(bin(80))

print(oct(3870))
print(hex(64222))
print(bin(0b1010000))
print(bin(0xfade))
print(oct(0xfade))
print(oct(0o7436))
print(hex(0b1010000))
print(hex(0xfade))


# In[ ]:




