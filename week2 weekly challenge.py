#task 1 Sum of Integers in a List
user_integer =input("Enter intergers speration with a space bar: ")
integer_list=[int(x) for x in user_integer.split()]
sum_integers = sum(integer_list)
print(sum_integers)

#task 2 Favorite Books
Books= ("Book 1: The Power", "Book 2: The people", "Book 3: The Kingdom", "Book 4: The Family", "Book 5: The Goose" )
print("List of favorite books:")
for items in Books:
    print(items)

#task 3 Dictionary Information
person_info ={}
person_info['name'] = input("Enter your name:" )
person_info['age'] = input("Enter your age:" )
person_info['phone number'] = input("Your phone number:")
person_info['location'] = input("Enter your location: ")
print(person_info)

#task 4 Common Elements in Sets
set1 = set(map(int, input("Enter elements for the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements for the second set separated by spaces: ").split()))
common_elements = set1.intersection(set2)
print(f"Common elements in the sets: {common_elements}\n")

#task 5 Words with Odd Number of Characters
word_list = ["savannah", "land", "foret", "desert", "windward", "mushroom"]
odd_number_words= [word for word in word_list if len(word)% 2 != 0]
print (f"Words with odd number characters: {odd_number_words}")