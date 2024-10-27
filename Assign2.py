list = [1,2,3,2,1,9]
print(" List :: " , list)
list1 = list.copy()

list1.reverse()

print("List1 :: ", list1)

if (list1 == list) :
    print("Palindrome")
else :
    print("Not Palindrome")