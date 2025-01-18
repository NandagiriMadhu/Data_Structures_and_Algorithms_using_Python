# Removing duplicates in a list
def remove_duplicates(arr):
    list = []
    for i in range(len(arr)):
        if arr[i] not in list:
            list.append(arr[i])
    return list
n = int(input())
st = []
for i in range(n):
    b = int(input())
    st.append(b)

print(remove_duplicates(st))