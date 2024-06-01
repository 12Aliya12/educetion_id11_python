def same_by(func, val):
    arr = []
    for el in val:
        if bool(func(el)):
            arr.append(bool(func(el)))
        else:
            arr.append(False)
    return all(arr)