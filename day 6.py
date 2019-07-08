#!/usr/bin/env python
# coding: utf-8

# In[2]:


# to check the greatest number
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if (a>b) and (a>c):
    print (a,"is greatest")
elif (b>a) and (b>c):
    print (b,"is greatest")
if (c>b) and (c>a):
    print (c,"is greatest")


# In[6]:


# to check if given year is leap year or not
y = int(input("enter the year"))
if (y%4==0) and (y%100!=0):
    print ("it is a leap year")
else:
    print ("it is not a leap year")


# ## while loop

# In[12]:


# print gitam 5 times 
print("gitam")
print("gitam")
print("gitam")
print("gitam")
print("gitam")
print("\nor using while loop ")
a=0
n = int(input("enter how many time u want to print ==\t"))
while a < n :
    print("gitam")
    a=a+1


# In[17]:


# print N natural numbers using while loop
a=1
n = int(input("enter the end number==\t"))
while a < n :
    print(a,end = " ")
    a=a+1


# In[24]:


# adding of even number from 1
a = 0
s = 0 
n = int(input("enter the end number==\t"))
while a <=n:
    print(a,end=" ")
    s = s + a
    a=a+2
print("\nsum of even numbers is =",s)    


# In[32]:


# given number is -- 123
# print the given number like -- 321
a = int(input("enter a number ==\t"))
b = a
s = 0
c=0
while a != 0:
    c= a % 10
    s= c + (s*10)
    a= a // 10
print(b,"\n",s)    


# ## functional programming
# * simple
# * easy read
# * Lengthy program divides into sub programs
def name of the function(<parameters>):
    statements
    return
# In[34]:


# sum of even numbers
def sumofeven(n):
    i=0
    sum=0
    while i<n:
        i=i+1
        if (i%2==0):
            sum=sum + i
    return(sum)
k=int(input("enter end number"))
l= sumofeven(k)
print(l)


# In[3]:


# read a number --1234
#Output --6 (2+4)
def addEvenDigits(n):
    sum=0
    while n!= 0:
        r=n%10
        if r%10 ==0:
            sum=sum+r
        n=n//10
    print(sum)    
    return
addEvenDigits(1234)


# In[9]:


# read a number --1234
#Output --6 (2+4)
def addEvenDigits(n):
    s=0
    while n!= 0:
        r=n%10
        if r%10 ==0:
            s=s+r
        n=n//10  
    return s
addEvenDigits(1234)


# In[7]:


# read a number -- 19528
# print the large digit print the number
def printlarge(n):
    large = 0
    while n != 0:
        r = n%10
        if large < r:
            large =r
        n = n// 10
    return large
printlarge(19528)
            


# In[6]:


# read the number input
# Output reverse of the given number
# 123 - 321
def reverseNumber(n):
    a = int(input("enter a number ==\t"))
    b = a
    s = 0
    c=0
    while a != 0:
        c= a % 10
        s= c + (s*10)
        a= a // 10
    return s
reverseNumber(123)         


# In[10]:


# given number is palendrome or not
# input
# 123 -- 321 No
# 121 -- 121 Yes
def palindrome(n):
   rev = 0
   buffer = n
   while n != 0:
       r =n%10
       rev = rev * 10 +r
       n = n // 10
   if buffer == rev:
       return "Yes"
   else:
       return "No"
   
print(palindrome(123))
print(palindrome(121))


# In[11]:


# function to print N natural Numbers
def NNaturalNumbers(n):
    for x in range(1,n+1):
        print(x,end=" ")
    return    
NNaturalNumbers(10)


# In[13]:


# function to print two numbers bitween two limits
# input: 11,25
# Output: 11,12,13...25
def printseries(lb,ub):
    for x in range(lb,ub+1):
        print(x,end=" ")
    return    
printseries(11,25)


# In[15]:


# function to print alternate number
# [500,520] -- 500 502 504 506..... 520
# [100,150] -- 100 102 104 106 ..150
def alternateNumbers(lb,ub):
    for x in range(lb,ub+1,4):
        print(x,end=" ")
    return    
alternateNumbers(500,520)
print("\n")
alternateNumbers(100,150)        


# In[18]:


# function to print the serice in reverse
# input 1,10
# Output: 10,9,8,7....1
def reverserange(start,end):
    for x in range(end,start-1,-1):
        print(x,end=" ")
    return
reverserange(1,10)

