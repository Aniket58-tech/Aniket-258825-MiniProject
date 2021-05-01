#Reading Output using file handling operations
import os,sys
f1 = open('Output.txt','r')
print("Reading output file :")
print()
print(f1.read())
f1.close()