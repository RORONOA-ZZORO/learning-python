How_Many_NO = (input("enter numbers you want to store separated by spaces : "))
num_list = [int(x) for x in How_Many_NO.split(",")]

def Odd_Even_Counter(items):
    even = 0
    odd = 0

    for item in items:
        if (item%2 == 0):
            even += 1
        else :
            odd +=1
        print(item)
    return odd,even
odd,even = Odd_Even_Counter(num_list)
print(even, odd)
