def print_statistics(arr):
    arr.sort()
    sum_chisel = 0
    if len(arr) == 0:
        print("0")
    else:
        for i in arr:
            sum_chisel += int(i)
        print(len(arr))
        sred_znach = sum_chisel / len(arr)
        print(sred_znach)
        print(arr[0])
        print(arr[-1])
        if len(arr) % 2 == 0:
            n1 = len(arr) // 2
            n2 = n1 - 1
            print((int(arr[n1]) + int(arr[n2])) / 2)
        else:
            print(arr[(len(arr) // 2)])


arr = list(input().split())
print_statistics(arr)