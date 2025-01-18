# check whether any element is duplicate
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return "true"
    return "false"

n = int(input())
st = []
for i in range(n):
    b = int(input())
    st.append(b)

print(contains_duplicate(st))