def l(a,b): #1,2
    if a > b:  # 1 > 3
        return a
    else:
        return b
print(l(1,3))

l = lambda a,b: a if a > b else b
print(l(1,2),'This is lambda function')
