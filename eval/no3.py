from datetime import *

start = input("Masukan tanggal awal ")
end = input("Masukkan tanggal akhir ")
startDate = datetime.strptime(start, '%Y-%m-%d').date()
endDate = datetime.strptime(end, '%Y-%m-%d').date()
delta = endDate - startDate

print(delta.days, "Hari")