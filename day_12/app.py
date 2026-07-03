# std1 = "Abdul Wahhab Rana"
# std2 = "Ali"
# std3 = "Affan"
std4 = "Abdullah"
# list in py


# list --rules
# made by using []
# comma , separated
#  all datatype can be store in list
# order    1    2     3    4 (length)
# order acces..         0          1       2         3 (index) starts from zero
studentslist = [ "Abdul Wahhab Rana", 30,True ,76.76]

# print(len(studentslist))
print(studentslist[0])
print(studentslist[1])
# print(studentslist[4]) - out of range error
print(studentslist[-1]) # last index
print(studentslist[-2]) # second last index
print(studentslist[1:]) # from 1st index to last
#  # index order cant be changed
#   # list can be changed

mydata= ["Affan",20,"affanrana612@gmail.com"]
mydata.append(30) # add new data at the end of list
mydata.insert(0,30) # 0 is index, 30 is element
mydata.remove("affanrana612@gmail.com")
mydata.remove("rana") # doesnt exist in list
mydata.pop() #empty () remove last element from list, pop(2) remove index 2
mydata.clear() # remove all data from list
del mydata [2]  # remove index 2,del keyword
print(mydata)

#  # str,int,list,remove (reserved keywords in python ) not use in variable name
list1 = ["a", "b", "c" ]
list2 = ["d", "e", "f" ]
# list1.extend(list2) # ()method (formula)

print(list1)

list1 = ["a","b","c"]
# list1[0] = "Rana"
list1[0:2] = ["Rana","Affan"] # replace index 0 and 1 with new values
print(list1)
