def loop(begin, end):
    last = 0
    current = begin
    temp = 0
    result = str(begin) + ", "
    for i in range(begin, end + 1):
        temp = last + current
        if(temp > end):
            break
        last = current
        current = temp
        result += str(temp) + ", "
    return result

x = input("Masukkan bilangan awal ")
y = input("Masukan bilangan akhir ")
print(loop(int(x), int(y)))