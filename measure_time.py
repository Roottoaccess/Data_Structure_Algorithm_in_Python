# Importing time module 
import time

# Storing the current time in a variable
start = time.time()
# Technique to measure times 
# To print from 1 to 100 we will do 
for i in range(1,101):
    print(i)
# Now after completing the program we will find the current time and substract it from the begining time 

print("The time its taken to execute the program in seconds: ", time.time() - start)