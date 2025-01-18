#  program to print the pairs and the count of number of pairs that their sum is equal to the target and both of the numbers should not be equal

def findPairs(nums, tar):
    list = []
    c = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == tar:
                c += 1
                list.append(str(nums[i])+"+"+str(nums[j]))
    print(list)
    return c

n = int(input())
a = int(input())
st = []
for i in range(n):
    b = int(input())
    st.append(b)

print(findPairs(st, a))