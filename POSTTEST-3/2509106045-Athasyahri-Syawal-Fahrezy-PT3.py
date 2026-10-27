from abc import ABC, abstractmethod


class Orang(ABC):
    total_orang = 0

    def __init__(self, nama, nomor_telepon, nik):
        self.nama = nama
        self._nomor_telepon = nomor_telepon
        self.__nik = nik
        Orang.total_orang += 1

    @property
    def nik_tersensor(self):
        return f"************{self.__nik[-4:]}"

    @abstractmethod
    def tampil(self):
        pass

    @abstractmethod
    def aktivitas(self):
        pass

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}.")


class Pasien(Orang):
    total_pasien = 0

    def __init__(self, id_pasien, nama, umur, nomor_telepon, nik):
        super().__init__(nama, nomor_telepon, nik)
        self.id_pasien = id_pasien
        self.umur = umur
        Pasien.total_pasien += 1

    def tampil(self):
        print(
            f"{self.id_pasien} | {self.nama}, {self.umur} tahun | "
            f"Telp: {self._nomor_telepon} | NIK: {self.nik_tersensor}"
        )

    def aktivitas(self):
        print(f"{self.nama} sedang menunggu giliran pemeriksaan.")

    @staticmethod
    def cek_umur(umur):
        return isinstance(umur, int) and umur > 0


class DokterGigi(Orang):
    total_dokter = 0

    def __init__(self, id_dokter, nama, spesialisasi, nomor_telepon, nik):
        super().__init__(nama, nomor_telepon, nik)
        self.id_dokter = id_dokter
        self.spesialisasi = spesialisasi
        DokterGigi.total_dokter += 1

    def tampil(self):
        print(
            f"{self.id_dokter} | drg. {self.nama}, {self.spesialisasi} | "
            f"Telp: {self._nomor_telepon} | NIK: {self.nik_tersensor}"
        )

    def aktivitas(self):
        print(f"drg. {self.nama} sedang menyiapkan alat pemeriksaan.")

    def periksa(self, pasien):
        print(f"drg. {self.nama} sedang memeriksa {pasien.nama}.")


class Klinik:
    nama_klinik = "Healthy Smile Dental Clinic"

    def __init__(self, alamat):
        self.alamat = alamat
        self._daftar_dokter = []

    def tambah_dokter(self, dokter):
        self._daftar_dokter.append(dokter)

    def tampilkan_dokter(self):
        print(f"Dokter di {Klinik.nama_klinik}:")
        for dokter in self._daftar_dokter:
            print(f"- drg. {dokter.nama} ({dokter.spesialisasi})")


class DetailPemeriksaan:
    def __init__(self, keluhan, tindakan):
        self.keluhan = keluhan
        self.tindakan = tindakan


class RekamMedis:
    total_rekam_medis = 0

    def __init__(self, id_rekam, pasien, dokter, tanggal, keluhan, tindakan, biaya):
        self.id_rekam = id_rekam
        self.pasien = pasien
        self.dokter = dokter
        self.tanggal = tanggal
        self.detail = DetailPemeriksaan(keluhan, tindakan)
        self.biaya = biaya
        RekamMedis.total_rekam_medis += 1

    @property
    def biaya(self):
        return self.__biaya

    @biaya.setter
    def biaya(self, biaya_baru):
        if not isinstance(biaya_baru, (int, float)):
            raise ValueError("Biaya harus berupa angka")
        if biaya_baru < 0:
            raise ValueError("Biaya tidak boleh negatif")
        self.__biaya = biaya_baru

    def __str__(self):
        return (
            f"{self.id_rekam} | {self.tanggal} | Pasien: {self.pasien.nama} | "
            f"Dokter: drg. {self.dokter.nama} | Keluhan: {self.detail.keluhan} | "
            f"Tindakan: {self.detail.tindakan} | Biaya: Rp{self.biaya:,.0f}"
        )


class PengingatWhatsApp:
    def kirim(self, nama_pasien):
        print(f"WhatsApp: Hai {nama_pasien}, jangan lupa jadwal kontrol kamu!")


class PengingatEmail:
    def kirim(self, nama_pasien):
        print(f"Email: Reminder kontrol gigi untuk {nama_pasien} sudah dikirim.")


def kirim_pengingat(layanan, nama_pasien):
    layanan.kirim(nama_pasien)


if __name__ == "__main__":
    pasien1 = Pasien("P01", "Andi", 20, "081234567890", "6472010101010001")
    pasien2 = Pasien("P02", "Siti", 22, "081298765432", "6472020202020002")
    dokter1 = DokterGigi(
        "D01", "Rina", "Gigi Umum", "081311112222", "6472030303030003"
    )
    dokter2 = DokterGigi(
        "D02", "Budi", "Ortodonti", "081333334444", "6472040404040004"
    )

    print("=== BUKTI ABSTRACT CLASS ===")
    try:
        Orang("Contoh", "081200000000", "6472000000000000")
    except TypeError as kesalahan:
        print(f"Objek Orang gagal dibuat: {kesalahan}")

    print("\n=== POLIMORFISME VIA PEWARISAN ===")
    daftar_orang = [pasien1, dokter1, pasien2, dokter2]
    for orang in daftar_orang:
        orang.perkenalan()
        orang.tampil()
        orang.aktivitas()

    print("\n=== ASOSIASI ===")
    dokter1.periksa(pasien1)
    dokter2.periksa(pasien2)

    print("\n=== AGREGASI ===")
    klinik = Klinik("Jl. Kesehatan No. 10")
    klinik.tambah_dokter(dokter1)
    klinik.tambah_dokter(dokter2)
    klinik.tampilkan_dokter()

    print("\n=== KOMPOSISI & OPERATOR OVERLOADING ===")
    rekam1 = RekamMedis(
        "RM01",
        pasien1,
        dokter1,
        "26-10-2026",
        "Gigi berlubang",
        "Tambal gigi",
        500000,
    )
    rekam2 = RekamMedis(
        "RM02",
        pasien2,
        dokter2,
        "26-10-2026",
        "Gigi tidak rapi",
        "Cek kawat gigi",
        300000,
    )
    print(rekam1)
    print(rekam2)

    print("\n=== DUCK TYPING ===")
    daftar_layanan = [PengingatWhatsApp(), PengingatEmail()]
    for layanan in daftar_layanan:
        kirim_pengingat(layanan, pasien1.nama)

    print("\n=== VALIDASI SETTER ===")
    try:
        rekam1.biaya = -100000
    except ValueError as kesalahan:
        print(f"Biaya gagal diubah: {kesalahan}")

    print(
        f"\nTotal: {Orang.total_orang} orang, "
        f"{Pasien.total_pasien} pasien, "
        f"{DokterGigi.total_dokter} dokter, dan "
        f"{RekamMedis.total_rekam_medis} rekam medis."
    )
