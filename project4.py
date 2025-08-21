my_list = ["Asus", "Lenovo","Acer", "Macbook"]
print(f"Initial list: {my_list}")

my_list.append("Dell")
print(f"After adding 'Dell': {my_list}")

my_list.insert(1,"HP")
print(f"After inserting 'HP': {my_list}")

my_list.remove("Acer")
print(f"After removing 'Acer': {my_list}")

del my_list[2]
print(f"After removing item by index: {my_list}")

removed_item = my_list.pop()
print(f"Item removed by pop(): {removed_item}")
print(f"Final list: {my_list}")





number_list = [4, 7, 8, 3, , 0, 9, 5]
print(f"Original list: {number_list}")

number_list.sort() 

print(f"List sorted in place (using .sort()): {number_list}")

another_list = [2, 4, 3, 12, 87, 7, 6, 9]
print(f"Another original list: {another_list}")

sorted_list = sorted(another_list)

print(f"New sorted list (using sorted()): {sorted_list}")
print(f"The original list remains unchanged: {another_list}")




student_grades = {
    'Anna': 92,
    'Alex': 74,
    'Hayk': 89,
    'Elen': 98
}

print("Initial dictionary:")

print(student_grades)

print(f"\nAnna's grade: {student_grades["Anna"]}")

student_grades["Gevorg"] = 95
print(f"\nDictionary after adding a new student:")
print(student_grades)

student_grades["Alex"] = 100
print(f"\nDictionary after updating David's grade:")
print(student_grades)




set_1 = {1, 4, 8, 3, 5}
set_2 = {2, 7, 8, 4, 9}

print(f"Set 1: {set_1}")
print(f"Set 1: {set_1}")

common_elements_ampersand = set_1 & set_2
print(f"\nCommon elements using '&': {common_elements_ampersand}")

common_elements_method = set_1.intersection(set_2)
print(f"Common elements using .intersection(): {commmon_elements_method}")
