nums = [1, 3, 5, 7, 9, 11]
x = 3

list_2d = [nums[i:i+x] for i in range(0, len(nums), x)]
print(list_2d)
# [[1, 3, 5], [7, 9, 11]]



list_2d = []
for i in range(0, len(nums), x):
    rowlist = []
    for j in range(i,i+x):
        rowlist.append(nums[j])
    list_2d.append(rowlist)
print(list_2d)