# Dynamic array and creating list 

# Seeing that how much space a list take in our ram 
# Importing sys module 
import sys

# Creating a empty list 
L = []

# print("Occuping the size before appending: ", sys.getsizeof(L))

# # Appending a item in the empty list 
# L.append("Hello")
# print(L)
# print("Occuping the size after appending: ", sys.getsizeof(L))

# We will do it using a loop 
for i in range(100):
    print(i, sys.getsizeof(L))
    L.append(i)
