class Pasien:
    nama_klinik = "Healthy Smile Dental Clinic"
    total_pasien = 0

    def __init__(self, id_pasien, nama, umur):
        self.id_pasien = id_pasien
        self.nama = nama
        self.umur = umur
        Pasien.total_pasien += 1

    def tampil(self):
        print(f"{self.id_pasien} | {self.nama}, {self.umur} tahun")

    @classmethod
    def ganti_nama_klinik(cls, nama_baru):
        cls.nama_klinik = nama_baru

    @staticmethod
    def cek_umur(umur):
        return isinstance(umur, int) and umur > 0


class DokterGigi:
    total_dokter = 0

    def __init__(self, id_dokter, nama, spesialisasi):
        self.id_dokter = id_dokter
        self.nama = nama
        self.spesialisasi = spesialisasi
        DokterGigi.total_dokter += 1

    def tampil(self):
        print(f"{self.id_dokter} | drg. {self.nama}, {self.spesialisasi}")


class RekamMedis:
    total_rekam_medis = 0

    def __init__(self, id_rekam, pasien, dokter, tanggal, keluhan, tindakan, biaya):
        self.id_rekam = id_rekam
        self.pasien = pasien
        self.dokter = dokter
        self.tanggal = tanggal
        self.keluhan = keluhan
        self.tindakan = tindakan
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
        print(f"Keluhan: {self.keluhan}")
        print(f"Tindakan: {self.tindakan}")
        print(f"Biaya: Rp{self.biaya:,.0f}")


if __name__ == "__main__":
    pasien1 = Pasien("P01", "Andi", 20)
    pasien2 = Pasien("P02", "Siti", 22)

    dokter1 = DokterGigi("D01", "Rina", "Gigi Umum")
    dokter2 = DokterGigi("D02", "Budi", "Ortodonti")

    rekam1 = RekamMedis(
        "RM01", pasien1, dokter1, "20-09-2026",
        "Gigi berlubang", "Tambal gigi", 500000
    )
    rekam2 = RekamMedis(
        "RM02", pasien2, dokter2, "21-09-2026",
        "Gigi tidak rapi", "Cek kawat gigi", 300000
    )

    print("DATA PASIEN")
    pasien1.tampil()
    pasien2.tampil()

    print("\nDATA DOKTER")
    dokter1.tampil()
    dokter2.tampil()

    print("\nREKAM MEDIS")
    rekam1.tampil()
    rekam2.tampil()

    print("\nUJI METODE KELAS")
    print(f"Sebelum: {Pasien.nama_klinik}")
    Pasien.ganti_nama_klinik("Healthy Smile Dental Care")
    print(f"Sesudah: {Pasien.nama_klinik}")

    print("\nUJI METODE STATIS")
    hasil1 = "valid" if Pasien.cek_umur(20) else "tidak valid"
    hasil2 = "valid" if Pasien.cek_umur(-5) else "tidak valid"
    print(f"Umur 20: {hasil1}")
    print(f"Umur -5: {hasil2}")

    print("\nUJI PENGUBAH BIAYA")
    rekam1.biaya = 600000
    print(f"Biaya baru: Rp{rekam1.biaya:,.0f}")

    try:
        rekam1.biaya = -100000
    except ValueError as kesalahan:
        print(f"Gagal diubah: {kesalahan}")

    print(
        f"\nTotal: {Pasien.total_pasien} pasien, "
        f"{DokterGigi.total_dokter} dokter, "
        f"{RekamMedis.total_rekam_medis} rekam medis"
    )
