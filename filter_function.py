def m1(a):
    if a %2 == 0:
        return True
    else:
        return False

l = [10,20,11,30,23]
l1 = list(filter(m1,l))

print(l1)
