def count():
    jml = 0
    name = "arkademy"
    for h in name:
        if h == 'a':
            jml += 1
    return jml

print("Huruf a muncul", count(), "kali")