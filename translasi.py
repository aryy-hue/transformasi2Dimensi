import matplotlib.pyplot as plt

# Data
x = [1, 1, 2, 3, 3]
y = [2, 4, 5, 4, 2]

sx = int(input("Masukkan nilai tx: "))
sy = int(input("Masukkan nilai ty: "))

# Melakukan pertambahan pada setiap elemen matriks
hasil_tx = [xi + sx for xi in x]
hasil_ty = [yi + sy for yi in y]

# Membuat plot
plt.plot(x,y, marker='o', linestyle='-', color='b', label='Sebelum Translasi')
plt.plot(hasil_tx, hasil_ty, marker='o', linestyle='-', color='r', label='Sesudah Translasi')

# Menambahkan label sumbu
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menambahkan judul plot
plt.title('Contoh Plot Matplotlib dengan Translasi')

# Menambahkan legenda
plt.legend()

# Menambahkan grid
plt.grid(True)

# Menampilkan plot
plt.show()
