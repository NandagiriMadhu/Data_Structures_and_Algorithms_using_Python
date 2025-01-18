# Question 1: Calculate Sum and Product of Array Elements
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i  # Adding each element to sum
    for i in array:
        product *= i  # Multiplying each element to product
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)  # Calling the function with the array [1, 2, 3, 4]

# Question 2: Print All Pairs of Elements from the Array
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))  # Print each pair of elements

printPairs([1,2,3,4,5])  # Calling the function with the array [1, 2, 3, 4, 5]

# Question 3: Print Unordered Pairs from Array (without duplicates)
def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):  # j starts from i+1 to avoid duplicate pairs
            print(str(array[i]) + "," + str(array[j]))  # Print unique pairs

printUnorderedPairs(ar1)  # Calling the function with the array [1, 2, 3, 4]

# Question 4: Print Unordered Pairs where Element in ArrayA < Element in ArrayB
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:  # Check if element from arrayA is smaller than arrayB
                print(str(arrayA[i]) + "," + str(arrayB[j]))  # Print the pair

arrayA = [1, 2, 3, 4, 5]
arrayB = [2, 6, 7, 8]
printUnorderedPairs(arrayA, arrayB)  # Calling the function with arrays arrayA and arrayB

# Question 5: (Commented Out) Print Unordered Pairs with a Long Loop (inefficient)
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):  # Extremely large loop that causes unnecessary delay
                print(str(arrayA[i]) + "," + str(arrayB[j]))  # Print each pair

# The following function call is commented out due to performance issues:
# printUnorderedPairss(arrayA, arrayB)

# Question 6: Reverse the Array
def reverse(array):
    for i in range(0, int(len(array) / 2)):  # Iterate from 0 to the middle of the array
        other = len(array) - i - 1  # Find the corresponding element from the other end
        temp = array[i]  # Temporary variable to store the element
        array[i] = array[other]  # Swap the elements
        array[other] = temp  # Swap the elements
    print(array)  # Print the reversed array

reverse(arrayA)  # Calling the function to reverse arrayA

