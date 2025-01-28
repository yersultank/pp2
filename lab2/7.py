#Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# *Set items are unchangeable, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Set items are unordered, unchangeable, and do not allow duplicate values.
#The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Add Set Items
#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #If the item to remove does not exist, discard() will NOT raise an error.

'''
You can also use the pop() method to remove an item,
but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.
'''
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset 
#print(thisset) will give error because the set is deleted


#Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#Join Sets

#The union() and update() methods joins all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4) #or myset = set1 | set2 | set3 |set4
print(myset)

#The intersection() method keeps ONLY the duplicates.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #or set3 = set1 & set2
print(set3)

#The difference() method keeps the items from the first set that are not in the other set(s).
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # or set3 = set1 - set2
print(set3)

'''
The difference_update() method will also keep the items from the first set that are not in the other set,
but it will change the original set instead of returning a new set.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#The symmetric_difference() method keeps all items EXCEPT the duplicates.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) # or set3 = set1 ^ set2 only with sets
print(set3)

'''
The symmetric_difference_update() method will also keep all but the duplicates,
but it will change the original set instead of returning a new set.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)