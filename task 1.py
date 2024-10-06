# Creating a list 
my_list = [10, 20, 30, 40]
# Adding an element to the list
my_list.append(50) 
print("List after adding:", my_list) 
# Removing an element from the list
my_list.remove(20) 
print("List after removing:", my_list) 
# Modifying an element in the list
my_list[0] = 100
print("List after modifying:", my_list) 
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Adding a new key-value pair
my_dict["occupation"] = "Software Engineer"
print("Dictionary after adding:", my_dict) 
# Removing a key-value pair
del my_dict["city"]
print("Dictionary after removing:", my_dict)
# Modifying a value
my_dict["age"] = 31
print("Dictionary after modifying:", my_dict)
# Creating a set
my_set = {1, 2, 3, 4, 1}  # Duplicates are automatically removed 
# Adding an element to a set
my_set.add(5) 
print("Set after adding:", my_set) 
# Removing an element from a set
my_set.remove(2) 
print("Set after removing:", my_set) 
