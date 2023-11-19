import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 1, 2, 3, 3]
y = [2, 4, 5, 4, 2]

# Memasukkan nilai sudut rotasi dari pengguna
sudut_rotasi = int(input("Masukkan nilai sudut rotasi (dalam derajat): "))
sudut_rotasi_rad = np.radians(sudut_rotasi)  # Mengonversi sudut ke radian

# Matriks rotasi
matriks_rotasi = np.array([[np.cos(sudut_rotasi_rad), -np.sin(sudut_rotasi_rad)],
                           [np.sin(sudut_rotasi_rad), np.cos(sudut_rotasi_rad)]])

# Melakukan rotasi pada setiap titik
rotasi_titik = np.column_stack((x, y)).dot(matriks_rotasi)

# Membuat plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data')
plt.plot(rotasi_titik[:, 0], rotasi_titik[:, 1], marker='o', linestyle='-', color='r', label=f'Rotasi {sudut_rotasi}°')

# Menambahkan label sumbu
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menambahkan judul plot
plt.title('Contoh Plot Matplotlib dengan Rotasi')

# Menambahkan legenda
plt.legend()

# Menambahkan grid
plt.grid(True)

# Menampilkan plot
plt.show()
