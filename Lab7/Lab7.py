print("Lab 6. Performed by Vlad Kolosov.")
print()

a_list = [1, 1.2, True, "str&ASDASD&asdas", [1, 2, 3], int(1), int(1)]


print("Start list")
print(a_list)
print()

i = 0
j = 1
x = "asd"
rasdel = "&"

print("range setting (a_list[0:1] = x) add \"asd\"")
a_list[i:j] = x
print(a_list)

print("range setting (a_list.extend([1]))")
a_list.extend([1])
print(a_list)

print("range setting (a_list.insert(2, 55))")
a_list.insert(2, 55)
print(a_list)

#///////////////////
#////string work////
#///////////////////
b_list = str(a_list[6]).split(rasdel)

print()
print("b_list View:")
print(b_list)

print()
#min function for b_list
print("min for b_list")
print(min(b_list, key=len))
#max function for b_list
print("max for b_list")
print(max(b_list, key = len))
