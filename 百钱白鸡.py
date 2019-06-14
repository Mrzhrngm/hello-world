for a in range(20,-1,-1):
    for b in range (34,-1,-1):
        for c in range(100,-1,-1):
            if 5*a+3*b+c/3==100 and a+b+c==100:
                print('%d 只公鸡，%d 只母鸡， %d 只小鸡' %( a, b, c))