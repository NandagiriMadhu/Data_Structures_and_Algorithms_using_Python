prev_list = [1,2,3,4]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)

lan = "Python"
list = [letter for letter in lan]
print(lan)
print(list)

list1 = [number for number in range(1,10)]
print(list1)

tup = (1,2,3,4,5)
tup2 = tuple(i for i in tup)
print(tup2)