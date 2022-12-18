#!/usr/bin/env python
# coding: utf-8

# #Python – mini Course project (IITM P11)
# 

# #1.Write a program to find out the prime numbers 
# 

# In[ ]:


num = int(input("Enter the number: "))
flag=0
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag=1
            break
    if flag==1:
        print(num, " is not a prime number")
    else:
        print(num, " is a prime number")
else:
    print(num, " is not a prime number")


# #2.write a program to create the equation (a+b+c) *  (a-b-c) * ab + a^2 + b ^2 + (abc)^3
# 

# In[ ]:


a = int(input('Enter value of a'))
b = int(input('Enter value of b'))
c = int(input('Enter value of c'))

eq = (a+b+c)*(a-b-c)*(a*b)+(a**2)+(b**2)+(a*b*c)**3

print('Equationv is:(',a,'+',b,'+',c,') * (',a,'-',b,'-',c,') * ',a,'*',b,' +', a,'^2 +', b,' ^2 + (',a,'*',b,'*',c,')^3 =',eq)


# #3. urlist = ['wood','knife','axe'] , mylist = ['tree', 'apple', 'mango', 'melon'] – combine two lists
# 

# In[10]:


urlist = ['wood','knife','axe']
mylist = ['tree', 'apple', 'mango', 'melon'] 
list3 =urlist+mylist
print(list3)


# #4.write a program for natural number based on user input

# In[8]:


num = int(input("Enter a number: "))  
  
if num <= 0:  
   print("NOT A NATURAL NAUMBER")  
else:  
   if num > 0:
      print("It is a natural number")  


# #5.write class and function for the equation sqrt(x1-x2) ^ 2 + sqrt( y1 – y2 ) ^2 using try except handling

# In[7]:


class point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_distance(self):
        try:
            return (sqrt(self.x1 - self.x2) ** 2 + sqrt(self.y1 - self.y2) ** 2)
        except ValueError:
            print("Not all arguments are numbers")


# #6. Name  = “Guvi python”  - write a program to get “python” word from the string

# In[12]:


test_str = input()
print(" The original string is: " + test_str)
x = test_str.split()
res=" ".join(x[1:])
print("The string after omitting first word is : " + str(res))


# #7.Using class and function - Write a program for palindrome Ex. Madam
# 

# In[6]:


class Palindrome:
    def __init__(self):
        pass

    def is_palindrome(self, string):
        return string == string[::-1]

# main
p = Palindrome()

word = input("Enter a word: ")

if(p.is_palindrome(word)):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")


# #8.using file handling – write a text file in ur system with “hello world

# In[5]:



file = open("textfile.txt","w") 
file.write("hello world") 
file.close()


# #9.create option button using tkinter GUI in python

# In[ ]:


from tkinter import *

root = Tk()

v = IntVar()

Radiobutton(root, text="Option 1", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Option 2", variable=v, value=2).pack(anchor=W)

mainloop()


# #10.Keep only numbers from the following string x = “ 89e9jcd^o38829@3%3,/mkl$w1”
# 

# In[ ]:


x = "89e9jcd^o38829@3%3,/mkl$w1"
for i in x:
    if i.isnumeric():
        print(i, end='')

