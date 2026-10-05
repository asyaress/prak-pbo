class Orang:
    total_orang = 0

    def __init__(self, nama, nomor_telepon, nik):
        self.nama = nama
        self._nomor_telepon = nomor_telepon
        self.__nik = nik
        Orang.total_orang += 1

    @property
    def nik_tersensor(self):
        return f"************{self.__nik[-4:]}"

    def tampil(self):
        print(f"{self.nama} | {self._nomor_telepon}")


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

    def periksa(self, pasien):
        print(f"drg. {self.nama} sedang memeriksa {pasien.nama}")


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

    @classmethod
    def ganti_nama_klinik(cls, nama_baru):
        cls.nama_klinik = nama_baru


class DetailPemeriksaan:
    def __init__(self, keluhan, tindakan):
        self.keluhan = keluhan
        self.tindakan = tindakan

    def tampil(self):
        print(f"Keluhan: {self.keluhan}")
        print(f"Tindakan: {self.tindakan}")


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

    def tampil(self):
        print(f"\n{self.id_rekam} | {self.tanggal}")
        print(f"Pasien: {self.pasien.nama}")
        print(f"Dokter: drg. {self.dokter.nama}")
        self.detail.tampil()
        print(f"Biaya: Rp{self.biaya:,.0f}")


if __name__ == "__main__":
    pasien1 = Pasien("P01", "Andi", 20, "081234567890", "6472010101010001")
    pasien2 = Pasien("P02", "Siti", 22, "081298765432", "6472020202020002")

    dokter1 = DokterGigi(
        "D01", "Rina", "Gigi Umum", "081311112222", "6472030303030003"
    )
    dokter2 = DokterGigi(
        "D02", "Budi", "Ortodonti", "081333334444", "6472040404040004"
    )

    print("INHERITANCE DAN OVERRIDING")
    pasien1.tampil()
    pasien2.tampil()
    dokter1.tampil()
    dokter2.tampil()
    print(f"Pasien adalah Orang: {isinstance(pasien1, Orang)}")
    print(f"Dokter adalah Orang: {isinstance(dokter1, Orang)}")

    print("\nASOSIASI")
    dokter1.periksa(pasien1)
    dokter2.periksa(pasien2)

    print("\nAGREGASI")
    klinik = Klinik("Jl. Kesehatan No. 10")
    klinik.tambah_dokter(dokter1)
    klinik.tambah_dokter(dokter2)
    klinik.tampilkan_dokter()

    print("\nKOMPOSISI")
    rekam1 = RekamMedis(
        "RM01", pasien1, dokter1, "05-10-2026",
        "Gigi berlubang", "Tambal gigi", 500000
    )
    rekam2 = RekamMedis(
        "RM02", pasien2, dokter2, "05-10-2026",
        "Gigi tidak rapi", "Cek kawat gigi", 300000
    )
    rekam1.tampil()
    rekam2.tampil()

    print("\nUJI METODE KELAS")
    print(f"Sebelum: {Klinik.nama_klinik}")
    Klinik.ganti_nama_klinik("Healthy Smile Dental Care")
    print(f"Sesudah: {Klinik.nama_klinik}")

    print("\nUJI METODE STATIS")
    hasil1 = "valid" if Pasien.cek_umur(20) else "tidak valid"
    hasil2 = "valid" if Pasien.cek_umur(-5) else "tidak valid"
    print(f"Umur 20: {hasil1}")
    print(f"Umur -5: {hasil2}")

    print("\nUJI SETTER")
    rekam1.biaya = 600000
    print(f"Biaya baru: Rp{rekam1.biaya:,.0f}")

    try:
        rekam1.biaya = -100000
    except ValueError as kesalahan:
        print(f"Gagal diubah: {kesalahan}")

    print(
        f"\nTotal: {Orang.total_orang} orang, "
        f"{Pasien.total_pasien} pasien, "
        f"{DokterGigi.total_dokter} dokter, "
        f"{RekamMedis.total_rekam_medis} rekam medis"
    )
