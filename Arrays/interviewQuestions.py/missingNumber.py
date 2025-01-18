# Program to find the missing number from 1 to N Natural Numbers

def missingNumber(list, a):
    total = a * (a + 1) // 2
    num = total - sum(list)
    return num

n = int(input())
st = []
for i in range(n - 1):
    b = int(input())
    st.append(b)

print(missingNumber(st, n))