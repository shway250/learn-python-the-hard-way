the_count = [1,2,3,4,5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this first kind of for-loop goes through a list
for number in the_count:
  print(f"this is count {number}")

#same as above
for fruit in fruits:
  print(f"I like {fruit}")

#also we can go through mixed lists
#notice we have to use {} since we don't know what's in it

for i in change:
  print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
  print(f"adding {i} to the list.")
  #append is a function that lists understand
  elements.append(i)

#now we can prin our new list
for elem in elements:
  print(f"this is a recently added element to my array: {elem}")