def minimun(*n):
    print(type(n))
    #print(n)
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimun(1, 3, -7, 9)
minimun()