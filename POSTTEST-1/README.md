# Dental Medical Record

Simple project buat manage data rekam medis di **Healthy Smile Dental Clinic**.

## What's Inside?

Ada tiga class utama di project ini:

- `Pasien` buat nyimpan ID, nama, dan umur pasien.
- `DokterGigi` buat nyimpan data dokter dan spesialisasinya.
- `RekamMedis` buat nyatet keluhan, tindakan, sampai biaya perawatan.

Class `RekamMedis` connect langsung ke objek `Pasien` dan `DokterGigi`, jadi semua datanya saling terhubung.

## OOP Stuff

Konsep yang dipakai di program ini:

- Class dan object
- Class attribute dan instance attribute
- Instance method, class method, dan static method
- Encapsulation dengan private attribute `__biaya`
- Getter dan setter pakai `@property`

Bagian biaya dibuat private biar nggak bisa diubah asal-asalan. Kalau input-nya bukan angka atau nilainya minus, setter langsung reject datanya.

## How to Run

Buka terminal di folder `POSTTEST-1`, terus run:

```bash
python 2509106045-Athasyahri-Syawal-Fahrezy-PT1.py
```

## Quick Test

Pas dijalankan, program bakal:

1. Bikin dua pasien, dua dokter, dan dua rekam medis.
2. Show data dari setiap objek.
3. Ganti nama klinik lewat class method.
4. Check umur lewat static method.
5. Update biaya pakai nilai valid.
6. Coba biaya minus buat buktiin validasinya jalan.

That's it. Simple & clean.
