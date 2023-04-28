#!/usr/bin/env python
# coding: utf-8

# In[1]:



#Q1
'''re.compile() function is to create regex object'''


# In[2]:


#Q2
'''regex strings often use \ blackslashes ,so they are often raw strings r'/d' '''


# In[3]:


#Q3
'''search() method returns a match object 
if match fails it returns none'''


# In[4]:


#Q4
'''call match group match() method to get the matched string'''


# In[5]:


#Q5
'''the group(0) returns full matching string
the first set of parentheses is group 1 
the second is group 2'''


# In[6]:


#Q6
'''we can use \ to match the literal parentheses in the regex string'''


# In[7]:


#Q7
'''if the regex has 0 or group 1 findall() returns a list of string 
if the regex has 2 or more groups findall() returns a list of tuples of strings'''


# In[8]:


#Q8
'''the | pipe can match one of many possible groups'''


# In[9]:


#Q9
'''Regular expressions are special strings representing a pattern to be matched in a search operation
"a" means match lowercase a
"^a" means do not match lowercase a'''


# In[10]:


#10
'''the + matches one or more times 
the * matches zero or more times'''


# In[11]:


#Q11
'''Specifies that exactly  copies of the previous re should be matched 
fewer matches cause the entire RE not to match. For example, a{4} will match exactly six 'a' characters, but not five

the resulting RE to match from 4 to 5 repetitions of the preceding RE
attempting to match as many repetitions as possible. For example, a{4,5} will match from 4 to 5 'a' characters'''


# In[12]:


#Q12
'''\d is a shorthand character class that matches digits
\w matches word characters
\s matches whitespace characters'''


# In[13]:


#Q13
'''The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace'''


# In[14]:


#Q14
'''(.*?) matches any character (.) any number of times (*), as few times as possible to make the regex match (?)
You will get a match on any string, but you will only capture a blank string because of the question mark.'''


# In[15]:


#Q15
'''_ ^ means the string must start with pattern
$ means the string must end with the pattern
Both means the entire string must match the entire pattern'''


# In[16]:


#Q16
'''Pass re.I as the second argument to re.compile() to make the matching case-insensitive.'''


# In[17]:


#Q17
'''The . dot is a wildcard it matches any character except newlines
we should Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.'''


# In[18]:


#Q19
'''Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile()''


# In[19]:


#Q19
'''Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile()'''


# In[ ]:




