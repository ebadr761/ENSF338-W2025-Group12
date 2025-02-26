def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2
#1. There exists a nested loop that runs if the element at index i is greater than 5, so the worst-case
#   time complexity is O(n^2) when all elements are greater than 5. The best-case time complexity is O(n)
#   when all elements are less than or equal to 5. The average time complexity is O(n^2) when half of the
#   elements are greater than 5 and half are less than or equal to 5 because the inner loop runs half the
#   time in the worst-case scenario. The space complexity is O(1) because the function modifies the input list
#   in-place without using additional data structures.

#2. Are average, best, and worst case complexity the same? If not, produce a modified version of the code above
#   for which average, best, and worst case complexity are equivalent.
#   The average, best, and worst case complexities are not the same. The average case complexity is O(n^2) while
#   the best and worst case complexities are O(n). The modified version of the code below ensures that the average,
#   best, and worst case complexities are equivalent by removing the inner loop and replacing the multiplication
#   with a conditional statement.
def processdata_modified(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
