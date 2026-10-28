"""Latihan 2 - Sistem Data Mahasiswa (Dictionary dengan NIM sebagai key).

Nama  : Fikri Yustiawan
NIM   : 2225250075
Kelas : 3-E
"""


def cari_mahasiswa(data, nim):
    """Mengembalikan dictionary mahasiswa untuk NIM tertentu, atau None."""
    return data.get(nim)


def tampilkan_mahasiswa(data, nim):
    """Menampilkan data satu mahasiswa; pesan jelas jika NIM tidak ada."""
    hasil = cari_mahasiswa(data, nim)
    if hasil is not None:
        print(f"{nim}: {hasil}")
    else:
        print(f"Data tidak ditemukan untuk NIM {nim}")


def tambah_mahasiswa(data, nim, nama, kelas, nilai):
    """Menambah mahasiswa baru. Mengembalikan False jika NIM sudah ada."""
    if nim in data:
        return False
    data[nim] = {"nama": nama, "kelas": kelas, "nilai": nilai}
    return True


def ubah_nilai(data, nim, nilai_baru):
    """Mengubah nilai mahasiswa. Mengembalikan False jika NIM tidak ada."""
    if nim in data:
        data[nim]["nilai"] = nilai_baru
        return True
    return False


def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)


def tampilkan_rekap(data):
    """Menampilkan seluruh data menggunakan items()."""
    for nim, info in data.items():
        print(nim, info)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


def main():
    print("=== Test 1: Pencarian tersedia (A003) ===")
    tampilkan_mahasiswa(data_mahasiswa, "A003")

    print("\n=== Test 2: Pencarian tidak tersedia (A999) ===")
    tampilkan_mahasiswa(data_mahasiswa, "A999")

    print("\n=== Test 3: Pembaruan nilai A002 menjadi 82 ===")
    ubah_nilai(data_mahasiswa, "A002", 82)
    print("Nilai A002 sekarang:", data_mahasiswa["A002"]["nilai"])

    print("\n=== Test 4: Penambahan data A006 ===")
    tambah_mahasiswa(data_mahasiswa, "A006", "Fajar", "B", 80)
    print("A006 tersedia:", "A006" in data_mahasiswa)

    print("\n=== Test 5: Rekap seluruh data (items) ===")
    tampilkan_rekap(data_mahasiswa)

    print()
    print(f"Rata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")


if __name__ == "__main__":
    main()
