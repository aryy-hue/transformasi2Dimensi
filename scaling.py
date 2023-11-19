import matplotlib.pyplot as plt

# Data
x = [1, 1, 2, 3, 3]
y = [2, 4, 5, 4, 2]

sx = int(input("Masukkan nilai sx: "))
sy = int(input("Masukkan nilai sy: "))

# Melakukan pertambahan pada setiap elemen matriks
hasil_sx = [xi * sx for xi in x]
hasil_sy = [yi * sy for yi in y]

# Membuat plot
plt.plot(x,y, marker='o', linestyle='-', color='b', label='Data Sebelum Scalling')
plt.plot(hasil_sx, hasil_sy, marker='o', linestyle='-', color='r', label='Data Sesudah di Scalling')

# Menambahkan label sumbu
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menambahkan judul plot
plt.title('Contoh Plot Matplotlib dengan Scalling')

# Menambahkan legenda
plt.legend()

# Menambahkan grid
plt.grid(True)

# Menampilkan plot
plt.show()
