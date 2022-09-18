# Defining strings
var1 = "Hello "
var2 = "World"
 
# + Operator is used to combine strings
var3 = var1 + var2
print(var3)
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string
  
s = "GoodMorningSunshine"
  
print("The original string is : ", end="")
print(s)
  
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))
# String slicing
String = 'MOUNTAIN'
 
# Using indexing sequence
print(String[:3])
