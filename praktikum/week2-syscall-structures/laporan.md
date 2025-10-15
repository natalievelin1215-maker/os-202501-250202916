
# Laporan Praktikum Minggu [X]
Topik: system call

---

## Identitas
- **Nama**  :Evelin Natalie
- **NIM**   :250202916  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Setelah menyelesaikan tugas ini, mahasiswa mampu:
1.Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2.Mengidentifikasi jenis-jenis system call dan fungsinya.
3.Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4.Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
JAWAB:
1.Konsep system call adalah jembatan antara program pengguna (user mode) dan kernel (kernel mode) dalam sistem operasi, yang memungkinkan aplikasi untuk meminta layanan dari sistem operasi.Permintaan ini, seperti membuka atau membaca file, diperlukan karena aplikasi tidak memiliki akses langsung ke perangkat keras dan sumber daya sistem, yang hanya dapat dikelola oleh kernel. Dengan demikian, system call bertindak sebagai antarmuka yang aman bagi program untuk berinteraksi dengan kernel dan menjalankan instruksi istimewa.
Fungsi system call yaitu:
-Manajemen Proses
-Manajemen File
-Manajemen Perangkatlainnya dengan cara yang aman dan terstruktur. 
-Komunikasi
-Pemeliharaan Informasi
2.Jenis-jenis system call yaitu
 kontrol proses:Mengelola eksekusi proses, termasuk pembuatan, terminasi, dan koordinasi antar-proses.
 manajemen berkas:Melakukan operasi pada berkas seperti membuat, menghapus, membuka, membaca, dan menulis. 
 manajemen perangkat:Mengelola perangkat keras seperti printer, scanner, atau jaringan. 
 pemeliharaan informasi:Mengambil dan mengatur informasi tentang sistem atau proses. 
 komunikasi:Memungkinkan pertukaran informasi antara proses yang berbeda
3.Alur perpindahan dari mode pengguna ke mode kernel saat system call terjadi karena serangkaian langkah yang dipicu oleh instruksi khusus. Pustaka C atau kode aplikasi akan memuat nomor system call dan parameternya ke dalam register, lalu memicu perpindahan mode melalui trap atau interupsi perangkat lunak
4.Penrintah Linux untuk menampilkan adalah strce .perintah ini juga berfungsi untuk menganalisis system call
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1352" height="728" alt="Sytem Call" src="https://github.com/user-attachments/assets/64835ff4-4cd7-47cf-8adf-4e9dc40ee15d" />

---

## Analisis
- Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel
- Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**  
2. Sebutkan 4 kategori system call yang umum digunakan? 
   **Jawaban:**  
3.Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
