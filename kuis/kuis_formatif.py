"""Kuis Formatif Pertemuan 11 - Dictionary/Map (versi interaktif di terminal).

Jalankan: python3 kuis/kuis_formatif.py
Jawab dengan huruf pilihan (A/B/C/D).
"""

SOAL = [
    {
        "tanya": "Apa perbedaan utama list dan dictionary?",
        "opsi": {
            "A": "List diakses dengan indeks posisi, dictionary diakses dengan key",
            "B": "List hanya untuk angka, dictionary hanya untuk string",
            "C": "List tidak bisa diubah, dictionary bisa diubah",
            "D": "Tidak ada perbedaan",
        },
        "jawaban": "A",
        "penjelasan": "List diakses lewat posisi indeks (nilai[0]), dictionary lewat key (mahasiswa['A001']).",
    },
    {
        "tanya": "Apa fungsi key dalam dictionary?",
        "opsi": {
            "A": "Menghitung jumlah data",
            "B": "Sebagai pengenal untuk menemukan value",
            "C": "Mengurutkan data",
            "D": "Menghapus data otomatis",
        },
        "jawaban": "B",
        "penjelasan": "Key adalah pengenal yang dipakai untuk menemukan value pasangannya.",
    },
    {
        "tanya": "Apa yang terjadi jika data['kelas'] dipanggil saat key 'kelas' tidak ada?",
        "opsi": {
            "A": "Mengembalikan None",
            "B": "Mengembalikan string kosong",
            "C": "Terjadi KeyError",
            "D": "Key dibuat otomatis",
        },
        "jawaban": "C",
        "penjelasan": "Akses dengan kurung siku pada key yang tidak ada menghasilkan KeyError.",
    },
    {
        "tanya": "Apa perbedaan data['kelas'] dengan data.get('kelas')?",
        "opsi": {
            "A": "Keduanya selalu sama",
            "B": "get() menghasilkan KeyError, [] tidak",
            "C": "[] menghasilkan KeyError jika key tidak ada, get() mengembalikan None atau nilai default",
            "D": "get() hanya untuk dictionary bersarang",
        },
        "jawaban": "C",
        "penjelasan": "get() lebih aman: mengembalikan None, atau nilai default jika disediakan.",
    },
    {
        "tanya": "Bagaimana memeriksa apakah suatu key tersedia?",
        "opsi": {
            "A": "Dengan operator in, misalnya 'nilai' in data",
            "B": "Dengan fungsi len()",
            "C": "Dengan data.clear()",
            "D": "Dengan data.pop()",
        },
        "jawaban": "A",
        "penjelasan": "Operator in memeriksa keberadaan key dan menghasilkan True/False.",
    },
    {
        "tanya": "Apa fungsi items()?",
        "opsi": {
            "A": "Menghasilkan seluruh key saja",
            "B": "Menghasilkan seluruh value saja",
            "C": "Menghapus semua pasangan",
            "D": "Menghasilkan pasangan (key, value) untuk ditelusuri",
        },
        "jawaban": "D",
        "penjelasan": "items() menghasilkan tuple (key, value) pada setiap iterasi.",
    },
    {
        "tanya": "Bagaimana menambahkan pasangan key-value baru?",
        "opsi": {
            "A": "data.add('kelas', 'A')",
            "B": "data['kelas'] = 'A'",
            "C": "data.append('kelas')",
            "D": "data.insert('kelas', 'A')",
        },
        "jawaban": "B",
        "penjelasan": "Cukup assignment data[key] = value; tidak perlu method khusus.",
    },
    {
        "tanya": "Bagaimana mengubah value dari key yang sudah ada?",
        "opsi": {
            "A": "Assignment ke key yang sama, misalnya data['nilai'] = 90",
            "B": "Menghapus dictionary lalu membuat ulang",
            "C": "Menggunakan data.keys()",
            "D": "Tidak bisa diubah",
        },
        "jawaban": "A",
        "penjelasan": "Assignment ke key yang sama menimpa value lama (atau gunakan update()).",
    },
    {
        "tanya": "Dalam data pendidikan, mengapa NIM cocok digunakan sebagai key?",
        "opsi": {
            "A": "Karena NIM selalu angka kecil",
            "B": "Karena nama mahasiswa tidak boleh dipakai",
            "C": "Karena NIM bisa berubah-ubah",
            "D": "Karena NIM unik sehingga tiap mahasiswa dapat ditemukan tanpa tertukar",
        },
        "jawaban": "D",
        "penjelasan": "Key harus unik sebagai identitas; nama bisa kembar, NIM tidak.",
    },
    {
        "tanya": "Perintah apa yang digunakan untuk mengirim commit ke GitHub?",
        "opsi": {
            "A": "git add",
            "B": "git commit",
            "C": "git push",
            "D": "git status",
        },
        "jawaban": "C",
        "penjelasan": "git commit merekam perubahan lokal; git push mengirim commit ke GitHub.",
    },
]


def tanya_pengguna(nomor, soal):
    print(f"\nSoal {nomor}/{len(SOAL)}: {soal['tanya']}")
    for huruf, teks in soal["opsi"].items():
        print(f"  {huruf}. {teks}")
    while True:
        jawab = input("Jawaban Anda (A/B/C/D): ").strip().upper()
        if jawab in soal["opsi"]:
            return jawab
        print("Masukkan salah satu huruf: A, B, C, atau D.")


def main():
    print("=== Kuis Formatif Pertemuan 11: Dictionary/Map ===")
    nama = input("Nama Anda: ").strip() or "Mahasiswa"

    skor = 0
    rekap = {}  # nomor soal -> True/False

    for nomor, soal in enumerate(SOAL, start=1):
        jawab = tanya_pengguna(nomor, soal)
        benar = jawab == soal["jawaban"]
        rekap[nomor] = benar
        if benar:
            skor += 1
            print("Benar!")
        else:
            print(f"Kurang tepat. Jawaban yang benar: {soal['jawaban']}.")
        print("Penjelasan:", soal["penjelasan"])

    nilai = skor / len(SOAL) * 100
    print("\n=== Hasil ===")
    print(f"{nama}: {skor}/{len(SOAL)} benar (nilai {nilai:.0f})")

    salah = [n for n, ok in rekap.items() if not ok]
    if salah:
        print("Soal yang perlu dipelajari lagi:", ", ".join(map(str, salah)))
    else:
        print("Semua jawaban benar. Kerja bagus!")


if __name__ == "__main__":
    main()
