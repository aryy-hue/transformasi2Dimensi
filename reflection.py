import matplotlib.pyplot as plt

# Data
x = [1, 1, 2, 3, 3]
y = [2, 4, 5, 4, 2]

tx = int(input("Masukkan nilai tx: "))
ty = int(input("Masukkan nilai ty: "))

# Melakukan refleksi terhadap sumbu x
refleksi_x = [xi for xi in x]
refleksi_y = [-yi for yi in y]

# Melakukan pertambahan pada setiap elemen matriks
hasil_tx = [xi + tx for xi in x]
hasil_ty = [yi + ty for yi in y]

# Membuat plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data')
plt.plot(refleksi_x, refleksi_y, marker='o', linestyle='-', color='r', label='Refleksi terhadap titik')

# Menambahkan label sumbu
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menambahkan judul plot
plt.title('Contoh Plot Matplotlib dengan Refleksi ')

# Menambahkan legenda
plt.legend()

# Menambahkan grid
plt.grid(True)

# Menampilkan plot
plt.show()
