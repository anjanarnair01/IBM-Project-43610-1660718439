mylist = [1,14,9,2,3,4,5]
flag = True
print(mylist)
print("Enter the operation to perform on list\n")
print("options: \n 1.remove \n 2.append \n 3.sort \n 4.pop \n 5.reverse\n 6.Exit \n")


while (flag):
    option = int(input("Enter the option : \n"))
    if(option == 1) :
        inp = int(input("Enter the value to remove from the list : "))    
        mylist.remove(inp)
        print(mylist)
    
    elif (option == 2) :
        inp = int(input("Enter the value to append to the list : "))    
        mylist.append(inp)
        print(mylist)

    elif (option == 3):
        print("The sorted list is: ")
        mylist.sort()
        print(mylist)

    elif (option == 4):
        print("Removing last element...")
        mylist.pop()
        print(mylist)
    
    elif (option == 5):
        print("Reversing the list")
        mylist.sort(reverse = True)
        print(mylist)
    
    elif (option == 6):
        flag = False
