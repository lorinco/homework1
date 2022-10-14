#1)Say "Hello, World!" With Python


print("Hello, World!")

#2)Python If-Else


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 0:
        if n>= 2 and n<=5:
            print('Not Weird')
        if n >= 6 and n <= 20:
            print('Weird')
        if n > 20:
            print('Not Weird') 
    else:
        print('Weird')



#3)Arithmetic Operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)


#4)Python: Division


if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)


#5)Loops


if __name__ == '__main__':
    n = int(input())
i=0
while i<n:
    print(i**2)
    i+=1


#6)Write a function


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 100 ==0 and  year % 400 != 0:
        return False
    if year % 4 == 0:
        return True
    
    return leap

year = int(input())
print(is_leap(year))


#7)Print Function
if __name__ == '__main__':
    n = int(input())
a=''
for i in range(1,n+1):
    a=a+str(i)
print(a)



#8)List Comprehensions


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
a=[]
b=[]
for i in range(x+1):
     for j in range(y+1):
         for k in range(z+1):
             if i+j+k !=n:
                a=[i,j,k]
                b.append(a)
print(b)



#9)Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
   
a=[]
for i in arr:
    if i != max(arr):
        a.append(i)
print(max(a))



#10)Nested Lists


if __name__ == '__main__':
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        b.append(score)
    i=0
    while i<len(a):
        if b[i]!=min(b):
            c.append(a[i])
            d.append(b[i])
        i+=1
    i=0
    while i<len(c):
        if d[i]==min(d):
            e.append(c[i])
        i+=1
    e.sort()

    print("\n".join(e))
        



#11)Finding the percentage


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
a=student_marks[query_name]
print(format((sum(a)/len(a)),'.2f'))



#12)sWAP cASE


def swap_case(s):
    a=[]
    for i in s:
        if i.isalpha()==True:
            if i == i.lower():
                a.append(i.upper())
            if i == i.upper():
                a.append(i.lower())
        else:
            a.append(i)
                
    a=''.join(a)
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



#13)String Split and Join


def split_and_join(line):
    a=line.split(" ")
    a="-".join(a)
    return a
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#14)What's Your Name?


    def print_full_name(first, last):
    print("Hello "+ first +" "+last+"! You just delved into python.")
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)



#15)Mutations


def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



#16)Find a string


def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



#17)String Validators


if __name__ == '__main__':
    s = input()
    n=False
    a=False
    b=False
    c=False
    d=False
    for i in range(len(s)):
        if s[i].isalnum()==True:
            n=True
        if s[i].isalpha()==True:
            a=True
        if s[i].isdigit()==True:
            b=True
        if s[i].islower()==True:
            c=True
        if s[i].isupper()==True:
            d=True
        
            
    print(n)
    print(a)
    print(b)
    print(c)
    print(d)
        


#18)Text Wrap


def wrap(string, max_width):
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



#19)Introduction to Sets


def average(array):
    x=sum(set(array))/len(set(array))
    return round(x,3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


#20)Symmetric Difference


M=input()
m=input().split()
N=input()
n=input().split()
a=m+n
b=set(a)
for i in m:
    for k in n:
        if i == k:
            b.remove(i)

s=list(b)
print(s)
h='\n'.join(s)

print(h)



#21)Set .add()


n=int(input())
m=[input() for i in range(0,n)]
m=set(m)
print(len(m))



#22)Set .discard(), .remove() & .pop()


n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(0,m):
    z=input().split()
    if z[0]=='pop':
        s.pop()
    elif z[0]=='remove':
        s.remove(int(z[1]))
    elif z[0]=='discard':
        s.discard(int(z[1]))
print(sum(s))



#23)Set .union() Operation


n=input()
m=set(input().split())
a=input()
b=set(input().split())
print(len(m.union(b)))



#24)Set .intersection() Operation
n=input()
m=set(input().split())
a=input()
b=set(input().split())
print(len(m.intersection(b)))



#25)Set .difference() Operation


n=input()
m=set(input().split())
a=input()
b=set(input().split())
print(len(m.difference(b)))


#26)Set .symmetric_difference() Operation


from collections import namedtuple
n=int(input())

x=namedtuple('x',input().split())



y= [int(x(*input().split()).MARKS) for i in range(n)]

print(sum(y)/n)

#Collections.namedtuple()
from collections import namedtuple
n=int(input())

x=namedtuple('x',input().split())



y= [int(x(*input().split()).MARKS) for i in range(n)]

print(sum(y)/n)



