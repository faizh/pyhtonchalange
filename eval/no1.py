awal=1
while(awal<10):
    akhir = 10
    for i in range(awal,akhir,1):
        print(i, end=' ')
        if i==9:
            print("")
            break
    awal+=1