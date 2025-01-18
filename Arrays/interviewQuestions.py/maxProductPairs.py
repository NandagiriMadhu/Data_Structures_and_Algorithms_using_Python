# printing the max of the product of the two numbers in the list
def max_product(arr):
    first_max = second_max = 0
    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return first_max * second_max

n = int(input())
st = []
for i in range(n):
    b = int(input())
    st.append(b)

print(max_product(st))
