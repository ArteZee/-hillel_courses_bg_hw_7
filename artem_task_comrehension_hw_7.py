# list comprehension
first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 22, 33, 44, 55, 66]
market_list = ["bread", "tomato", "egg", 'water', "pencil", "cucumber"]

final_list =[ x for x in first_list if x % 2 == 0]
print(final_list)

second_final_list = [y for y in second_list if 22 <= y <= 55]
print(second_final_list)

edit_market_list = [x for x in market_list if "r" in x]
print(edit_market_list)

third_list =[x + x for x in first_list]
print(third_list)

fourth_list = [x.upper() for x in market_list]
print(fourth_list)

# dict comprehension
dict_product = {first_list[x]:market_list[x] for x in range(len(first_list))}
print(dict_product)

dict_math = {second_list[x] - (x+1): second_list[x] for x in range(len(first_list))}
print(dict_math)

dict_random = {x: x**2 for x in range(1,10)}
print(dict_random)

list_random= list(dict_random.values())
dict_from_list = {market_list[x]: list_random[x] for x in range(0,len(market_list))}
print(dict_from_list)

# set comprehension

beginner_set = {x for x in range(0, 20)}
print(beginner_set)

even_set = {x for x in beginner_set if x %2 == 0}
print(even_set)

list_of_number = [1,2,3,34,2,45,556,6,7,8,1,1,2,3,4,5,6,78,5,3,3,3,3,3,3,3,3,3,33,3,3,3,41]

unic_set_of_number = {x for x in list_of_number}
print(unic_set_of_number)

list_of_name = ["Artem", "Maria", "Katya", "Kirill", "Ruslan", "Artem", "Kirill "]

name_set = {x for x in list_of_name if "l" not in  x }
print(name_set)

new_set = {x for x in list_of_number if x not in beginner_set}
print(new_set)