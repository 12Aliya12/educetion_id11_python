def average(values):
    sum_chisel = 0
    if len(values) == 0:
        return 0
    else:
        for i in values:
            sum_chisel += int(i)
    sred_zanch = sum_chisel / len(values)
    return sred_zanch




values = list(input().split())
average(values)