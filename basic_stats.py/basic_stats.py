from random import random
import numpy as np
# Import plotting library
import matplotlib.pyplot as plt 
from os import *


# In[103]:


# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
#Randomely generated numbers on Excel to help check my work

def basicstats(N=25):
    
    #create list
    list1 = []
    
    #Randomly generated numbers between 1 and 10 appended into list
    for i in range(N):
        value = random()*10
        i += 1
        list1.append(value)
    
    #Sums the list
    summation = 0
    for value in list1:
        summation = summation + value
    
    #Calculate mean by dividing sum by N
    mean = summation/N
    mean2 = "The mean is:", mean
    
    #Creates a new list that updates each list element to equal (X-mu)^2
    list2 = [(element - mean)**2 for element in list1]

    #Sums the new list
    summation2 = 0
    for value in list2:
        summation2 = summation2 + value
    
    #Standard deviation equation
    std = "The standard deviation is:", (summation2/(N-1))**0.5
    
    #Create Histogram
    plt.hist(list1, rwidth=0.9)
    plt.title("Histogram of List")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    histogram = plt.figure()
    #Return statement
    return mean2, std, histogram

