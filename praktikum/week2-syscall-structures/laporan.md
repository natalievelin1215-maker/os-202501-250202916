
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
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
>JAWAB:
1. Konsep system call adalah jembatan antara program pengguna (user mode) dan kernel (kernel mode) dalam sistem operasi, yang memungkinkan aplikasi untuk meminta layanan dari sistem operasi.Permintaan ini, seperti membuka atau membaca file, diperlukan karena aplikasi tidak memiliki akses langsung ke perangkat keras dan sumber daya sistem, yang hanya dapat dikelola oleh kernel. Dengan demikian, system call bertindak sebagai antarmuka yang aman bagi program untuk berinteraksi dengan kernel dan menjalankan instruksi istimewa.
Fungsi system call yaitu:
- Manajemen Proses
- Manajemen File
- Manajemen Perangkatlainnya dengan cara yang aman dan terstruktur. 
- Komunikasi
- Pemeliharaan Informasi
2. Jenis-jenis system call yaitu
- kontrol proses:Mengelola eksekusi proses, termasuk pembuatan, terminasi, dan koordinasi antar-proses.
- manajemen berkas:Melakukan operasi pada berkas seperti membuat, menghapus, membuka, membaca, dan menulis. 
- manajemen perangkat:Mengelola perangkat keras seperti printer, scanner, atau jaringan. 
- pemeliharaan informasi:Mengambil dan mengatur informasi tentang sistem atau proses. 
- komunikasi:Memungkinkan pertukaran informasi antara proses yang berbeda
3. Alur perpindahan dari mode pengguna ke mode kernel saat system call terjadi karena serangkaian langkah yang dipicu oleh instruksi khusus. Pustaka C atau kode aplikasi akan memuat nomor system call dan parameternya ke dalam register, lalu memicu perpindahan mode melalui trap atau interupsi perangkat lunak
4. Penrintah Linux untuk menampilkan adalah strce .perintah ini juga berfungsi untuk menganalisis system call
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari system call.
- System Call sebagai Antarmuka antara Program dan Kernel.Teori ini menjelaskan bahwa system call adalah cara utama program di mode pengguna berinteraksi dengan kernel OS untuk meminta layanan, seperti akses hardware atau manajemen memori. Dasarnya adalah prinsip abstraksi, di mana OS menyembunyikan kompleksitas internal untuk memudahkan pengembangan perangkat lunak tanpa mengganggu keamanan keseluruhan sistem.

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
> JAWAB
- Analisis System Call untuk Operasi File
Proses Pembukaan File (Open Operations):
System call seperti openat digunakan untuk membuka file atau sumber daya, seperti /etc/ld.so.cache atau /lib/x86_64-linux-gnu/libselinux.so.1. Dalam output, kernel memeriksa akses (misalnya, dengan flag O_RDONLY|O_CLOEXEC) untuk memastikan file dapat dibaca tanpa modifikasi. Ini mencerminkan teori isolasi, di mana kernel memvalidasi izin pengguna sebelum memberikan akses, mencegah potensi serangan seperti akses tidak sah. Contohnya, openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3 mengembalikan file descriptor (3), yang menunjukkan file berhasil dibuka dan siap untuk operasi selanjutnya.

- Proses Pembacaan File (Read Operations):
System call read memungkinkan program untuk membaca isi file, seperti saat membaca dari /proc/mounts atau library dinamis. Dalam output, Anda melihat read(3, "...", 1024) = 1024, di mana kernel membaca data dari file descriptor 3 (dari openat sebelumnya). Ini mengilustrasikan validasi input, di mana kernel memastikan ukuran baca tidak melebihi batas dan data aman untuk diproses, sesuai dengan prinsip keamanan system call yang mencegah buffer overflow atau korupsi memori.

- Proses Penutupan File (Close Operations):
System call close digunakan untuk menutup file descriptor setelah operasi selesai, seperti close(3) = 0 setelah membaca file. Ini penting untuk membebaskan sumber daya sistem, mencegah kebocoran memori atau descriptor yang terbuka terlalu lama. Dalam konteks teori, ini menunjukkan efisiensi system call, di mana kernel mengelola transisi balik ke mode user dengan aman, memastikan sumber daya seperti file descriptor tidak tersisa dan berpotensi dieksploitasi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
- System Call adalah Pilar Keamanan dan Interaksi OS:
Dari praktikum, terlihat bahwa system call memainkan peran kunci dalam menjaga isolasi antara program pengguna dan kernel, sehingga mencegah serangan keamanan seperti akses tidak sah. Kesimpulannya, penggunaan system call dalam percobaan menunjukkan betapa pentingnya mekanisme ini untuk stabilitas OS, di mana setiap panggilan divalidasi untuk memastikan operasi yang aman dan terkendali.

- Efisiensi dan Penerapan Praktis dalam Pengembangan:
Praktikum mengilustrasikan bahwa system call seperti read(), write(), atau fork() di Linux memungkinkan interaksi efisien dengan hardware, tetapi juga menyoroti tantangan seperti overhead transisi mode. Kesimpulan ini menekankan bahwa memahami system call membantu dalam mengoptimalkan kinerja aplikasi, serta mendorong praktik pengkodean yang lebih aman dalam pengembangan perangkat lunak.

- Implikasi untuk Pembelajaran dan Inovasi:
Secara keseluruhan, praktikum system call menunjukkan bahwa konsep ini bukan hanya teori, tetapi juga alat praktis untuk eksperimen keamanan OS. Kesimpulannya, hal ini mendorong inovasi dalam desain sistem, di mana pemahaman tentang validasi input dan transisi aman dapat diterapkan untuk mengembangkan OS yang lebih tangguh terhadap ancaman masa depan.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**  fungsi utama system call adalah sebagai antarmuka atau jembatan bagi program aplikasi untuk meminta layanan dari sistem operasi (OS) 
2. Sebutkan 4 kategori system call yang umum digunakan? 
   **Jawaban:**  kategori system call yang umum digunakan adalah Manajemen Proses, Manajemen Berkas, Manajemen Perangkat, dan Komunikasi
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:**  karena program pengguna berjalan di "user mode", sementara system call hanya bisa dijalankan di "kernel mode" yang lebih aman dan memiliki hak akses istimewa untuk berinteraksi langsung dengan perangkat keras dan memori.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
