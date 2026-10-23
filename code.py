nilai_mahasiswa = []

while True:
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
        if n >= 1:
            break
        print("Jumlah mahasiswa harus >= 1.")
    except ValueError:
        print("Masukkan angka bulat yang valid.")
# Input nilai
for i in range(n):
    while True:
        try:
            nilai = int(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
            if 0 <= nilai <= 100:
                nilai_mahasiswa.append(nilai)
                break
            print("Nilai harus antara 0-100.")
        except ValueError:
            print("Masukkan angka bulat yang valid.")
# Menampilkan data
print("\nDaftar Nilai Mahasiswa:")
for i, nilai in enumerate(nilai_mahasiswa):
    print(f"Mahasiswa {i+1}: {nilai}")

# Menghitung rata-rata
rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
print(f"\nRata-rata awal: {rata:.2f}")

# Menghapus nilai terendah
nilai_terendah = min(nilai_mahasiswa)
nilai_mahasiswa.remove(nilai_terendah)
print(f"\nNilai terendah ({nilai_terendah}) dihapus.")

# Menampilkan data akhir
print("\nData nilai setelah dihapus:")
for i, nilai in enumerate(nilai_mahasiswa):
    print(f"Mahasiswa {i+1}: {nilai}")

# Menghitung rata-rata akhir
rata_akhir = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
print(f"Rata-rata akhir: {rata_akhir:.2f}")
