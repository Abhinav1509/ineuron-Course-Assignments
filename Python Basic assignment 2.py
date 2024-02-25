#!/usr/bin/env python
# coding: utf-8

# In[1]:


""""
1.What are the two values of the Boolean data type? How do you write them?
Answer:  The Boolean data type has two values: true and false. You write them either by writing true and false or by writing 0 and 1.  


# In[ ]:


""""
2.What are the three different types of Boolean operators?
Answer: The three different types of boolean operators are OR,AND and NOT.


# In[ ]:


""""
3.Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
Answer:
---> AND operator
 A        B     A && B
false   false   false
false   true    false
true    false   false
true    true    true

---> OR operator
  A      B     A || B
false   false   false
false   true    true
true    false   true
true    true    true

---> NOT operator
  A     !A
false   true
true    false


# In[ ]:


""""
4.What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Answer: 
-->(5 > 4) and (3 == 5)
(5 > 4) is True and (3 == 5) is False, so
True and False evaluates to FALSE.

-->not (5 > 4)
This is TRUE.

-->(5 > 4) or (3 == 5)
(5 > 4) is True and (3 == 5) is false
True or False evaluates to TRUE.

-->not ((5 > 4) or (3 == 5))
(5 > 4) is True and (3 == 5) is False, so
(True or False) is True and
not True evaluates to FALSE. 

-->(True and True) and (True == False)
True and True is True
True == False is False
True and False evaluates to FALSE.

-->(not False) or (not True)
not False is True
not True is False
True or False evaluates to TRUE.


# In[ ]:


""""
5.What are the six comparison operators?
Answer: 
Equal to (==)
Not equal to (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)


# In[ ]:


""""
6.How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
Answer: The equal to operator is used by writing "==" and the assignment operator is used by writing "=".
""""
#Example for equal to operator
x = 5
y = 10
if x == y:
    print("x is equal to y")
    
#Example for assignment operator
x = 5  # Assigns the value 5 to the variable x
y = x  # Assigns the value of x (which is 5) to the variable y


# In[ ]:


""""
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Answer: 
--> The first block comes in the third line; "print('eggs')"
--> The secon line comes in the fifth line; "print('bacon')"
--> The third block comes in the seventh line' "print('ham')"


# In[10]:


"""
8.Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
"""
#Answer: 
spam=(input())
if spam=="1":
    print("Hello")
elif spam=="2":
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


""""
9.If your programme is stuck in an endless loop, what keys you’ll press?
Answer: Ctrl+c


# In[ ]:


""""
10.How can you tell the difference between break and continue?
Answer: 
-->break statement:
When encountered within a loop, break immediately terminates the loop and transfers the program control
to the statement immediately following the loop.

-->continue statement:
When encountered within a loop, continue skips the rest of the code inside the loop for the current 
iteration and jumps to the next iteration of the loop.


# In[ ]:


""""
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Answer: range(10):

This form of range() generates a sequence of numbers starting from 0 (inclusive) up to, but not 
including, the specified number (10 in this case).

range(0, 10):
This form of range() generates a sequence of numbers starting from the first argument (0 in this case) 
up to, but not including, the second argument (10 in this case).

range(0, 10, 1):
This form of range() generates a sequence of numbers starting from the first argument (0 in this case)
up to, but not including, the second argument (10 in this case), with the specified step value 
(1 in this case).


# In[16]:


""""
12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.
"""
#Answer:
for i in range(1,11):
    print(i)

print("------------------")    

n=1
while n<=10:
    print(n)
    n+=1


# In[ ]:


""""
13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
Answer: spam.bacon()

