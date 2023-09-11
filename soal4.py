n = int(input("Masukkan banyaknya data: "))
total = 0
for i in range(n):
    nilai = int(input("Masukkan angka: "))
    total += nilai
    rata = total / n

print("Rata-rata = ", rata)