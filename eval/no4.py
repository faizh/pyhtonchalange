def count3():
    jml = 0
    allNumber = generate()
    for h in allNumber:
        if h == '3':
            jml += 1
    return jml

def generate():
    result = ""
    for i in range(0, 100):
        result += str(i) + " "
    return result
print("Angka 3 muncul", count3(), "kali")