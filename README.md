# Pertemuan 11 - Dictionary/Map

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Fikri Yustiawan |
| **NIM** | 2225250075 |
| **Kelas** | 3-E |
| **Jurusan** | Pendidikan Matematika |

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Folder

```
pertemuan-11-dictionary-2225250075/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_dasar_dictionary.py
|   |-- 02_akses_get.py
|   |-- 03_manipulasi_dictionary.py
|   |-- 04_iterasi_dictionary.py
|   |-- 05_dictionary_bersarang.py
|   `-- 06_fungsi_dictionary.py
|-- praktik/
|   `-- data_mahasiswa.py
`-- kuis/
    `-- Kuis_Formatif_Pertemuan_11_2225250075.pdf
```

## Struktur Data

- **Key utama:** NIM mahasiswa (string, contoh `"A001"`). NIM dipilih karena unik, sehingga setiap mahasiswa dapat ditemukan langsung tanpa tertukar posisi.
- **Value:** dictionary berisi `nama` (string), `kelas` (string), dan `nilai` (angka).

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    ...
}
```

Fungsi yang dibuat: `cari_mahasiswa`, `tampilkan_mahasiswa`, `tambah_mahasiswa`, `ubah_nilai`, `rata_rata_nilai`, `tampilkan_rekap`.

## Cara Menjalankan

```bash
# Latihan 1-6
python3 latihan/01_dasar_dictionary.py
python3 latihan/02_akses_get.py
python3 latihan/03_manipulasi_dictionary.py
python3 latihan/04_iterasi_dictionary.py
python3 latihan/05_dictionary_bersarang.py
python3 latihan/06_fungsi_dictionary.py

# Latihan 2 (praktik)
python3 praktik/data_mahasiswa.py
```

Kuis formatif berupa file PDF di folder `kuis/` (tinggal dibuka).

## Test Case

| Kasus | Input/aksi | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan | `A003: {'nama': 'Citra', 'kelas': 'B', 'nilai': 92}` | Lulus |
| Pencarian tidak tersedia | A999 | Pesan "Data tidak ditemukan" | `Data tidak ditemukan untuk NIM A999` | Lulus |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 menjadi 82 | `Nilai A002 sekarang: 82` | Lulus |
| Penambahan data | A006 | Key A006 tersedia | `A006 tersedia: True` | Lulus |
| Rekap | items() | Semua NIM dan data tampil | Enam baris (A001-A006) tampil | Lulus |
| Rata-rata | 6 mahasiswa setelah perubahan | (85+82+92+74+88+80)/6 = 83.50 | `Rata-rata = 83.50` | Lulus |

## Refleksi

Kesalahan akses key yang saya temukan adalah mengakses `data["kelas"]` pada dictionary yang belum memiliki key `"kelas"`, yang menghasilkan `KeyError`. Perbaikannya adalah memeriksa dulu dengan operator `in` atau memakai `data.get("kelas", "Belum ada")`. Pada program praktik, pencarian memakai `data.get(nim)` lalu hasilnya dicek dengan `is not None`, sehingga NIM yang tidak ada (misalnya A999) menampilkan pesan yang jelas tanpa error.

## Exit Ticket

- **Keuntungan utama dictionary dibanding list untuk kasus tertentu adalah** data dapat langsung dicari berdasarkan key yang bermakna, seperti NIM, tanpa perlu mengingat posisi indeks. Hal ini mengurangi risiko salah posisi dan membuat kode lebih mudah dibaca.
- **Kesalahan akses key yang perlu saya hindari adalah** mengakses key yang belum tentu ada menggunakan kurung siku, karena bisa menyebabkan `KeyError`. Saya perlu menggunakan `in` atau `get()` ketika key mungkin tidak tersedia.
- **Hubungan string dan dictionary yang saya pahami adalah** string dapat menjadi key atau value pada dictionary. Hasil normalisasi string (misalnya `strip()` dan `upper()`) menjaga konsistensi key agar data tidak gagal ditemukan.
- **Konsep Pertemuan 11 yang akan membantu materi file I/O adalah** dictionary sebagai struktur penampung data terstruktur di memori, sebelum data ditulis ke file atau setelah dibaca dari file.

## Kuis Formatif

File `kuis/Kuis_Formatif_Pertemuan_11_2225250075.pdf` memuat 10 pertanyaan kuis formatif beserta jawaban dan contoh kode, dengan identitas Fikri Yustiawan, NIM 2225250075, kelas 3-E.

## Catatan Sumber dan Bantuan

Sumber: bahan ajar Pertemuan 11 (Dr. Aan Hendrayana, S.Si., M.Pd.) dan dokumentasi Python 3 tentang dictionary. Bantuan AI (Claude) digunakan untuk menyusun kerangka file, kuis, dan draf README; seluruh kode telah dijalankan dan diuji, dan saya dapat menjelaskan alasan pemilihan key-value serta cara kerjanya.
