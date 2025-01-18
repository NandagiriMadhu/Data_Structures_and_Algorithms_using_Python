# printing the first and second largest numbers of the List
def first_second(my_list):
    list = sorted(my_list, reverse = True)
    first_num = list[0]
    second_num = 0
    for num in list:
        if num < first_num:
            second_num += num
            break
    return first_num, second_num

n = int(input())
st = []
for i in range(n):
    b = int(input())
    st.append(b)

print(first_second(st))