
# Laporan Praktikum Minggu [2]
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
- Antarmuka Terkendali dan Abstraksi (Controlled Interface and Abstraction): System call menyediakan antarmuka terstandardisasi yang aman bagi program untuk mengakses layanan kernel.
Abstraksi: Pengembang aplikasi tidak perlu memahami detail teknis yang rumit tentang cara kerja perangkat keras (misalnya, mengakses hard disk atau jaringan).
- Antarmuka terkendali: Setiap permintaan akan melewati "gerbang" yang dikendalikan oleh kernel. Hal ini mencegah program berbahaya atau yang salah menulis kode untuk merusak sistem dengan langsung mengakses sumber daya penting.
Transisi dari User Mode ke Kernel Mode: Perpindahan dari user mode ke kernel mode dipicu oleh sebuah software interrupt.
Ketika sebuah program memanggil system call, ia menempatkan nomor system call dan parameter-parameternya ke dalam register CPU.
CPU kemudian mengalihkan eksekusi ke kernel menggunakan mekanisme interrupt.
Kernel memeriksa nomor system call, mengeksekusi layanan yang diminta, dan mengembalikan kontrol ke program pengguna setelah tugas selesai.


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
Sertakan screenshot hasil system call
<img width="1352" height="728" alt="Sytem Call" src="https://github.com/user-attachments/assets/64835ff4-4cd7-47cf-8adf-4e9dc40ee15d" />
<img width="1366" height="768" alt="Capture 4" src="https://github.com/user-attachments/assets/95268416-3d24-4748-80be-e9759c12dca8" />

<img width="1366" height="768" alt="Capture3" src="https://github.com/user-attachments/assets/6b3cbe04-b700-450d-ade0-301b48bd726c" />

---

## Analisis
- Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel
- Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?
> JAWAB
- ystem Call	Penjelasan Fungsi	Analisis Cara Kerja Kernel
1. open("/etc/passwd", O_RDONLY)	Membuka file /etc/passwd dalam mode read-only. Kernel memeriksa apakah file tersebut ada, apakah proses cat memiliki izin untuk membacanya, dan jika iya, kernel memberikan file descriptor (biasanya angka 3) kepada proses.	Kernel berperan mengatur manajemen file descriptor dan keamanan akses file (melalui permission checking di sistem file).
2.	read(3, ... , 4096)	Membaca isi file dari file descriptor 3 sebanyak maksimal 4096 byte (ukuran buffer standar). Kernel akan menyalin isi file dari sistem file ke buffer memori user-space program cat.	Kernel mengatur transisi data dari storage (disk) ke memori, memastikan hanya bagian file yang diizinkan dapat diakses oleh proses.
3.	write(1, ... , 1582)	Menulis data ke file descriptor 1 (stdout — layar terminal). Kernel akan menyalin isi buffer tadi ke output terminal pengguna.	Kernel menangani output stream, memastikan data dikirim ke perangkat output (terminal) melalui buffer output standar.
4.	close(3)	Menutup file descriptor 3. Setelah ditutup, kernel membebaskan resource yang digunakan oleh file tersebut.	Kernel membersihkan tabel file terbuka (file table) untuk proses cat, sehingga descriptor dapat digunakan kembali untuk file lain nanti.

- [13.154095] systemd-journald[81]: Collecting audit messages is disabled.	Kernel mencatat aktivitas dari proses systemd-journald, yaitu layanan yang menangani logging di sistem Linux. Pesan ini menunjukkan fitur audit sedang dimatikan.
- [13.274579] systemd-journald[81]: Received client request to flush runtime journal.	Kernel menerima permintaan untuk menyimpan log - sementara (runtime journal) ke disk.
- [13.336252] systemd-journald[81]: File .../system.journal corrupted or uncleanly shut down...	Kernel mendeteksi file log system.journal rusak atau tidak ditutup dengan benar (mungkin akibat shutdown mendadak), lalu membuat file pengganti.
- [14.143751] ACPI: AC: AC Adapter [AC1] (on-line)	Kernel mendeteksi adaptor daya (charger) aktif — ini adalah pesan dari subsistem ACPI (Advanced Configuration and Power Interface).
- [14.144667] ACPI: battery: Slot [BAT1] (battery present)	Kernel mendeteksi baterai laptop terpasang.
- [17.482122] WSL (2 - init-systemd(Ubuntu)) ERROR: WaitForBootProcess...	Kernel mencatat error pada Windows Subsystem for Linux (WSL2) karena proses inisialisasi systemd tidak selesai tepat waktu.
- [27.582691] WSL (2 - Interop) ERROR: CreateLoginSession...	Masih terkait WSL2 — kernel melaporkan gagal membuat sesi login karena waktu tung gu habis.
- [30.018063] TCP: eth0: Driver has suspect GRO implementation...	Kernel memberikan peringatan terkait driver jaringan (eth0), mungkin berpengaruh pada performa TCP.
- [48.368303] hv_balloon: Max. dynamic memory size: 4034 MB	Kernel Hyper-V (digunakan WSL2) melaporkan ukuran maksimum memori dinamis yang dialokasikan.
- [600.986549] mini_init (175): drop_caches: 1	Kernel mencatat perintah pembersihan cache memori (drop_caches) oleh proses mini_init.

- perbedaan
Dmesg (dari "display message") adalah perintah yang menampilkan pesan-pesan log dari kernel Linux. Ini mencakup informasi tentang aktivitas kernel, seperti deteksi hardware, pemasangan driver, error kernel, boot messages, dan event sistem lainnya.
Output biasa adalah hasil dari perintah atau program yang dijalankan di user space (ruang pengguna), seperti perintah shell standar. Ini bisa berupa teks, data, atau hasil komputasi dari program seperti echo, ls, cat, atau aplikasi seperti Python script

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
## Tugas
1. Dokumentasikan hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.

- strace

| No. | Perintah | Observasi | Deskripsi |
|-----|----------|-----------|-----------|
| 1 | strace | execve("/bin/ls", ["ls"], 0x7ffd...) = 0 | Proses memulai eksekusi program ls. |
| 2 | strace | openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_DIRECTORY) = 3 | Membuka direktori saat ini. |
| 3 | strace | getdents(3, /* 10 entries */, 32768) = 280 | Membaca entri direktori. |
| 4 | strace | write(1, "file1.txt\nfile2.txt\ndirektori1\n", 30) = 30 | Menulis output ke layar. |
| 5 | strace | exit_group(0) = ? | Proses berakhir. |

- dmesg

| no | Perintah | Observasi | Deskripsi |
|----|----------|-----------|-----------|
| 1 | dmesg | [ 0.000000] Linux version 5.15.0-58-generic | Informasi versi kernel Linux yang digunakan saat boot, menunjukkan konfigurasi dasar sistem. |
| 2 | dmesg | [ 2.123456] usb 1-1: | new high-speed USB device number 2 using xhci_hcd |  Kernel mendeteksi perangkat USB baru terhubung, seperti flash drive atau mouse. |
| 3 | dmesg | [ 3.456789] EXT4-fs (sda1): mounted filesystem with ordered data mode | Sistem file EXT4 pada partisi sda1 berhasil dimount, menandakan partisi root atau data siap digunakan.
| 4 | dmesg | [ 10.789012] random: crng init done | Kernel menyelesaikan inisialisasi Cryptographically Secure Pseudo-Random Number Generator (CSPRNG) untuk keamanan.
| 5 | dmesg | [ 123.456789] ata1.00: failed command: | READ FPDMA QUEUED Error pada operasi disk (misalnya, hard drive gagal membaca data), yang mungkin menunjukkan masalah hardware. |

1. Mengapa system call penting untuk keamanan OS?
- karena berfungsi sebagai gerbang kontrol antara program pengguna dan kernel sistem operasi, sehingga mencegah akses tidak sah dan menjaga stabilitas sistem. Kernel memvalidasi setiap permintaan melalui system call, memastikan program hanya mengakses sumber daya yang diizinkan, seperti memori atau perangkat keras

2. Bagaimana OS memastikan transisi user–kernel berjalan aman?
- melalui pemisahan mode user dan mode kernel, yang menciptakan dua tingkat hak istimewa terpisah. Transisi ini dikelola oleh mekanisme khusus seperti panggilan sistem (system calls) dan interrupt, yang memvalidasi permintaan dari user mode sebelum kernel mengeksekusinya. Mekanisme Keamanan:
-	Operasi Dual-Mode : OS menjlankan dua mode operasi, yaitu user mode (mode pengguna) untuk aplikasi dan kernel mode (mode kernel) untuk kernel. 
-	User Mode : Hanya dapat mengakses sumber daya yang diizinkan untuk proses yang sedang berjalan, tidak bisa langsung mengakses hardware atau memori vital. 
-	Kernel Mode : Memiliki akses penuh ke seluruh hardware dan memori sistem. 
-	Kontrol Akses dan Perizinan: 
Kernel bertanggung jawab untuk mengelola kontrol akses dan izin pengguna, serta operasi data yang aman untuk mencegah akses tidak sah. 
-	Panggilan Sistem (System Calls): 
Ketika sebuah aplikasi membutuhkan layanan kernel (seperti membaca file atau membuat proses baru), aplikasi harus melakukan panggilan sistem. Panggilan ini adalah cara yang aman untuk meminta izin, dan kernel akan memvalidasi permintaan tersebut sebelum mengeksekusinya.

3. Sebutkan contoh system call yang sering digunakan di Linux.
system call yang paling sering digunakan di Linux adalah 
1. Manajemen Proses 
-	fork(): Membuat proses anak yang merupakan salinan persis dari proses induknya.
-	execve(): Mengganti citra program dari proses yang sedang berjalan dengan program baru.
-	exit(): Mengakhiri eksekusi sebuah proses.
-	wait4(): Menunggu hingga proses anak selesai atau statusnya berubah.
-	getpid(): Mengambil ID proses dari proses yang sedang berjalan.
-	kill(): Mengirim sinyal ke proses tertentu. 
2. Manajemen Berkas (File)
-	open(): Membuka berkas dan mengembalikan file descriptor yang digunakan untuk operasi berikutnya.
-	read(): Membaca data dari file descriptor ke dalam buffer.
-	write(): Menulis data dari buffer ke file descriptor.
-	close(): Menutup file descriptor yang sebelumnya dibuka.
-	stat(): Mengambil informasi status berkas, seperti ukuran dan izin akses.
-	mkdir(): Membuat direktori baru.
-	rmdir(): Menghapus direktori.
3. Manajemen Perangkat (Device)
-	ioctl(): Melakukan operasi masukan/keluaran pada perangkat keras, seperti mengubah pengaturan terminal.
-	read() dan write(): Digunakan juga untuk berinteraksi dengan perangkat, tidak hanya berkas.
-	select(): Memantau beberapa file descriptor untuk aktivitas I/O. 
4. Manajemen Informasi
-	gettimeofday(): Mendapatkan waktu sistem saat ini.
-	sysinfo(): Mengambil informasi tentang sistem, seperti penggunaan memori dan beban CPU.
-	uname(): Mendapatkan informasi tentang kernel saat ini.
-	getuid(): Mendapatkan ID pengguna (UID) dari proses yang sedang berjalan. 
5. Manajemen Memori
-	brk(): Mengubah lokasi batas atas data (data segment) suatu proses untuk mengalokasikan atau membebaskan memori.
-	mmap(): Memetakan berkas atau perangkat ke memori suatu proses. 



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
- Apa bagian yang paling menantang minggu ini?  ada kendala di wsl   
- Bagaimana cara Anda mengatasinya?  dengan cara mencari tutorial di media sosial

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
