# Program Rekapitulasi Nilai Mahasiswa

# Dictionary untuk menyimpan data
data_mahasiswa = {}

# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")

    # Validasi NIM hanya angka
    while True:
        nim = input("Masukkan NIM: ")
        if nim.isdigit():
            break
        else:
            print("  ❌ NIM harus berupa angka!")

    nama = input("Masukkan Nama: ")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

    mata_kuliah = [] 
    for j in range(jumlah_matkul):
        # Validasi nama mata kuliah hanya huruf/spasi
        while True:
            matkul = input(f"  Nama Mata Kuliah ke-{j+1}: ")
            if all(c.isalpha() or c.isspace() for c in matkul) and matkul.strip() != "":
                break
            else:
                print("  ❌ Nama mata kuliah harus berupa huruf dan tidak boleh mengandung angka!")

        # Validasi nilai mata kuliah harus float
        while True:
            try:
                nilai = float(input(f"  Nilai Mata Kuliah '{matkul}': "))
                break
            except ValueError:
                print("  ❌ Nilai harus berupa angka (misal: 80 atau 75.5)!")

        mata_kuliah.append((matkul, nilai))

    # Simpan ke dictionary sesuai struktur
    data_mahasiswa[nim] = (nama, mata_kuliah)

# Menampilkan semua data
print("\n=== Rekap Data Mahasiswa ===")

print(f"{data_mahasiswa[nim]} : nama : {nama}, matkul : {mata_kuliah}")
for nim, (nama, nilai_list) in data_mahasiswa.items():
    total_nilai = sum(nilai for _, nilai in nilai_list)
    rata_rata = total_nilai / len(nilai_list) if nilai_list else 0

    print(f"\nNIM   : {nim}")
    print(f"Nama  : {nama}")
    print("Nilai Mata Kuliah:")
    for matkul, nilai in nilai_list:
        print(f"  - {matkul}: {nilai}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")

