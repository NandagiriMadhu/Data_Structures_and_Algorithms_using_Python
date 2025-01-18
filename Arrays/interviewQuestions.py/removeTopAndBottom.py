# removing first and last elements of an array 
def removeEle(list):
    return list[1:-1]

n = int(input())
st = []
for i in range(n):
    b = int(input())
    st.append(b)

print(removeEle(st))
 