def find(s, n):
# write your implementation here
    # ansList = []
    for i in range(len(s)):
        first = s[i]
        for j in range(i+1,len(s)):
            sum = s[i]+s[j]
            if sum == n:
                return [i,j]
    return None
        # print("first number:")
        # print(first)
        # listWithoutFirst = s[:]
        # print("copy of list:")
        # print(listWithoutFirst)
        # listWithoutFirst.remove(first)
        # print("list without first number:")
        # print(listWithoutFirst)
        # for j in range(len(listWithoutFirst)):
        #     second = listWithoutFirst[j]
        #     print("second number:")
        #     print(second)
        #     sum = first + second
        #     print("Sum:")
        #     print(sum)
        #     if sum == n:
        #         ansList.append(i)
        #         ansList.append(j)
        #         print(ansList)
    # print("ans list:")
    # print(ansList)

nums = [2,7,11,15]
target = 9
print(find(nums,9))

        
