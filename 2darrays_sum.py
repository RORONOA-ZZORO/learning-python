import numpy

print("hello friends")

FirstArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arry_len = len(FirstArray)
print(arry_len)
total_sum = 0
row1, row2, row3 = 0,0,0
for i in range(arry_len):
    for j in range(arry_len):  
        total_sum += FirstArray[i][j]
        if i ==0:
            row1 += FirstArray[i][j]
        elif i==1:
            row2 += FirstArray[i][j]
        elif i==2:
            row3 += FirstArray[i][j]
        # print(FirstArray[i][j])
    # print(end="\n")

print(f"Total sum {total_sum} First row sum {row1} second row sum {row2} third row sum {row3}")