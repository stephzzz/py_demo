G=[x for x in range(100,1000)if (x//100)**3+((x%100)//10)**3+(x%10)**3==x]
print(G)

L=[x for x in range(100,1000) if int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3==x]
print(L)
