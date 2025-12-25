
<<<<<<< HEAD
# Laporan Praktikum Minggu [X]
Topik: Arsitektur Sistem Operasi dan Kernel
=======
# Laporan Praktikum Minggu [I]
Topik:Arsitektur Sistem Operasi dan Kernel
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Identitas
<<<<<<< HEAD
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936
- **Kelas** : 1IKRA
=======
- **Nama**  :  Evelin Natalie
- **NIM**   :  250202916
- **Kelas** : 1IKRA 
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
<<<<<<< HEAD
Fungsi Utama Sistem Operasi
Sistem operasi (Operating System / OS) adalah perangkat lunak yang menjadi penghubung antara pengguna dan perangkat keras komputer.
Fungsi utamanya antara lain:
Manajemen Proses (Process Management)
Mengatur jalannya proses (program yang sedang berjalan).
Menangani pembuatan, penjadwalan, dan penghentian proses.
Manajemen Memori (Memory Management)
Mengalokasikan dan mengatur penggunaan memori utama (RAM).
Memastikan tiap proses mendapat memori tanpa saling mengganggu.
Manajemen Penyimpanan (File Management)
Mengatur penyimpanan data dalam bentuk file dan direktori.
Menyediakan sistem file untuk membaca, menulis, atau menghapus data
Manajemen Perangkat Input/Output Management
Mengontrol interaksi antara sistem dan perangkat keras 
Menggunakan driver agar OS bisa berkomunikasi dengan perangkat
Manajemen Keamanan dan Proteksi (Security & Protection)
Melindungi data dan sumber daya sistem dari akses tidak sah
Mengatur hak akses pengguna.
User Interface (Antarmuka Pengguna)
Menyediakan cara bagi pengguna untuk berinteraksi (CLI seperti terminal, atau GUI seperti Windows).

Peran Kernel
Kernel adalah inti dari sistem operasi — bagian terpenting yang selalu aktif di memori.
Fungsinya:
Mengatur komunikasi antara software dan hardware.
Mengelola sumber daya sistem (CPU, memori, perangkat I/O).
Melaksanakan system call dari aplikasi pengguna.
Menangani interupsi perangkat keras.

Jenis kernel:
Monolithic Kernel → seluruh layanan sistem dijalankan dalam satu ruang kernel (misal: Linux).
Microkernel → hanya fungsi dasar di kernel, layanan lain dijalankan di ruang pengguna (misal: Minix, QNX).

Peran System Call
System call adalah jembatan antara program pengguna (user space) dan kernel (kernel space).
Ketika aplikasi ingin menggunakan sumber daya sistem, ia tidak bisa langsung mengakses hardware, jadi harus meminta layanan ke kernel melalui system call.

Contoh system call:
read() → membaca data dari file atau perangkat.
write() → menulis data ke file atau perangkat.
fork() → membuat proses baru.
exec() → menjalankan program baru.
exit() → mengakhiri proses.
---

## Dasar Teori
Teori ini didasarkan pada konsep dasar ilmu komputer, khususnya manajemen sumber daya dan abstraksi hardware, untuk memahami bagaimana OS bekerja secara praktis (misalnya, melalui simulasi proses atau pemanggilan system call di lingkungan lab seperti Linux).

Abstraksi dan Manajemen Sumber Daya: Sistem operasi berfungsi sebagai lapisan abstraksi antara perangkat lunak pengguna dan hardware, mengelola sumber daya seperti CPU, memori, dan I/O untuk efisiensi dan keamanan. Teori ini (dari model von Neumann) memungkinkan multiprogramming, di mana percobaan dapat mendemonstrasikan penjadwalan proses untuk menghindari konflik sumber daya.

Peran Kernel sebagai Pengontrol Inti: Kernel adalah modul privileged yang menangani operasi rendah-level seperti interrupt dan context switching, berdasarkan teori mode eksekusi (user mode vs. kernel mode). Dalam percobaan, ini mendasari pengamatan bagaimana kernel mencegah akses langsung hardware oleh aplikasi, memastikan stabilitas sistem (contoh: kernel panic jika ada kesalahan).

System Call sebagai Interface Komunikasi: System call merupakan mekanisme trap-based untuk transisi dari user space ke kernel space, didasarkan pada teori isolasi proses (process isolation) untuk keamanan. Percobaan dapat menguji ini melalui pemanggilan fungsi seperti fork() atau read(), menunjukkan bagaimana library (e.g., POSIX API) membungkus permintaan kernel tanpa membahayakan sistem.

Prinsip Keamanan dan Portabilitas: Teori hak akses (access control) dan virtualisasi memastikan OS portabel antar hardware, dengan kernel menyediakan layanan standar. Ini mendasari percobaan evaluasi performa, seperti mengukur overhead system call, untuk memverifikasi bagaimana OS melindungi dari kegagalan (fault tolerance) dan mendukung skalabilitas.
=======
**Fungsi Utama Sistem**
Sistem operasi atau operating system adalah perangkat lunak sistem yang menjadi penghubung perangkat keras dan perangkat lunak. Fungsinya yaitu: 1. Manajemen Proses; yaitu mengatur process yang ada di sistem, contoh: penjadwalan, pembuatan dan peghentian process.
2.Manajemen Memori (Memory Management):
Mengatur penggunaan memori utama (RAM), menentukan alokasi memori untuk proses yang berjalan.
3.Manajemen Penyimpanan (File System Management):
Mengatur penyimpanan data dalam file dan folder serta akses terhadapnya di media penyimpanan (HDD/SSD).
4.Manajemen Perangkat I/O (Device Management):
Mengelola komunikasi antara sistem dan perangkat input/output seperti keyboard, mouse, printer, dll.
5.Manajemen Keamanan dan Proteksi:
Menjaga sistem dari akses yang tidak sah dan melindungi data serta sumber daya.
6.User Interface:
Memberikan antarmuka bagi pengguna,baik berbasis teks maupun grafis.

**Peran Kernel:**
Kernel adalah inti dari sistem operasi yang langsung berinteraksi dengan perangkat keras. Tugas utama kernel meliputi:
Mengelola sumber daya sistem (CPU, memori, perangkat I/O).
Menjalankan dan menjadwalkan proses.
Menangani interrupt dan sistem call.
Memberikan abstraksi perangkat keras agar program aplikasi bisa berjalan tanpa harus memahami cara kerja perangkat keras.

**Jenis Kernel**
Monolithic Kernel: Semua fungsi berada dalam satu program besar (contoh: Linux).
Microkernel: Hanya fungsi dasar, sisanya berjalan di user space (contoh: Minix, QNX).
Hybrid Kernel: Kombinasi keduanya (contoh: Windows, macOS).

**Peran System Call**

System Call merupakan jembatan yang menghubungkan aplikasi dan kernel. Demi keamanan dan stabilitas, aplikasi tidak bisa langsung mengakses hardware. Melalui System Call, aplikasi dapat: Mengakses file (membaca, menulis, membuka, dan menutup). Mem-proses dan mengelola pembuatan proses. Mengalokasikan dan menghapus memori. Berkomunikasi dengan perangkat input/output. System Call adalah API (Application Programming Interface) tingkat dasar yang disiapkan oleh OS dan bisa diakses aplikasi.


Contoh Ilustrasi:
aplikasi ingin mencetak dokumen
Aplikasi tidak langsung mengakses printer.
Aplikasi melakukan system call ke kernel.
Kernel mengatur komunikasi dengan perangkat printer
-

## Dasar Teori
**Teori yang Mendasari Percobaan Sistem Operasi**
**1.Sistem operasi adalah perangkat lunak inti yang mengelola sumber daya komputer**
Sistem operasi bertugas mengatur penggunaan memori,proses,perangkat keras,dan perangkat lunak agar dapat berjalan secara efisien dan terkoordinasi 
**2.Kernel sebagai komponen utama sistem operasi**
Kernel mengontrol akses ke perangkat keras dan menjalankan proses, menjadi penghubung antara aplikasi dan hardware.
**3.System call sebagai mekanisme interaksi antara aplikasi dan kernel**
System call memungkinkan program pengguna untuk meminta layanan dari kernel, seperti akses file, manajemen proses, dan komunikasi antar proses.
**4.manajemen proses dan sinkronisasi**
Sistem operasi mengelola eksekusi beberapa proses secara bersamaan dan menangani kondisi seperti race condition untuk menghindari konflik akses sumber daya.
**5.Pengendalian input/output dan penyimpanan**
Sistem operasi mengatur perangkat input/output dan penyimpanan data agar aplikasi dapat menggunakan perangkat tersebut tanpa harus berinteraksi langsung dengan hardware.
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

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
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
<<<<<<< HEAD
 hasil screenshot percobaan atau diagram:
=======
Sertakan screenshot hasil percobaan atau diagram:

<img width="1366" height="762" alt="Capture" src="https://github.com/user-attachments/assets/292acb1d-fdb0-4c05-8bd5-328b794050e3" />
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190


--<img width="1364" height="767" alt="screenshot wsl" src="https://github.com/user-attachments/assets/60200375-2d88-4ca6-9ecb-c4a5d8db1c4e" />
-

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
<<<<<<< HEAD
1. Makna Hasil Percobaan

Pada gambar terlihat beberapa perintah Linux dijalankan di terminal WSL2 (Windows Subsystem for Linux):
-whoami
Output: faik
→ Menampilkan nama pengguna aktif yang sedang menjalankan shell.
Ini menunjukkan kamu masuk sebagai user biasa, bukan root.

-lsmod
Menampilkan daftar modul kernel (kernel modules) yang sedang dimuat oleh sistem Linux.
Modul adalah komponen tambahan kernel yang bisa dimuat atau dilepaskan sesuai kebutuhan.

Contoh modul yang muncul:
intel_rapl_msr, crc32c_intel → modul yang mengelola fitur prosesor Intel.
bridge, br_netfilter → modul jaringan (bridge/virtual network).
autofs4 → modul untuk sistem file otomatis.
Makna: kernel sedang memuat berbagai modul untuk mengelola hardware dan fitur sistem tertentu tanpa harus memodifikasi kernel utama.

lsmod | head
Menampilkan beberapa baris awal dari daftar modul kernel.Gunanya untuk melihat ringkasan saja (misal 10 modul teratas).

dmesg | head
Menampilkan log pesan kernel saat proses booting (awal sistem hidup).
Baris awal menunjukkan:
Versi kernel: Linux version 6.6.87.2-microsoft-standard-WSL2
Compiler: gcc (GCC) 11.2.0
Arsitektur CPU: Intel/AMD
Peta memori fisik (RAM map)
Makna: ini adalah hasil output dari kernel log buffer, yaitu pesan yang dihasilkan kernel ketika mendeteksi perangkat keras dan menginisialisasi sistem.

2. Hubungan dengan Teori
Fungsi Kernel
Kernel adalah inti sistem operasi yang mengatur:
Manajemen perangkat keras (CPU, memori, I/O)
Pengaturan modul (seperti yang ditampilkan lsmod)
Penanganan interupsi, manajemen proses, dan file system
Perintah lsmod dan dmesg langsung berinteraksi dengan kernel space — keduanya memanfaatkan system call untuk meminta data dari kernel.

Peran System Call
System call digunakan untuk berkomunikasi antara user space (program aplikasi) dengan kernel space.
Contohnya:
Saat lsmod dijalankan, program melakukan system call seperti open(), read(), dan ioctl() untuk membaca data dari /proc/modules (yang dikelola oleh kernel).
=======
jawab:
a. Perintah uname -a
Linux DESKTOP-C9IVJP5 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun 5 18:30:46 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
Makna:
Linux → Kernel yang digunakan.
DESKTOP-C9IVJP5 → Hostname sistem.
6.6.87.2-microsoft-standard-WSL2 → Versi kernel yang dimodifikasi oleh Microsoft untuk WSL2.
x86_64 → Arsitektur 64-bit.
GNU/Linux → Sistem berbasis kernel Linux dan tool GNU.
Kesimpulan:
Lingkungan ini bukan Linux asli, melainkan WSL2 (Windows Subsystem for Linux versi 2), yaitu lapisan virtualisasi ringan di Windows yang menjalankan kernel Linux.

b. Perintah whoami
evelin
Menunjukkan nama user Linux aktif di shell WSL2.
c. Perintah lsmod | head
Module                  Size  Used by
tls                    98304  0
intel_rapl_msr          16384  0
intel_rapl_common       32768  1 intel_rapl_msr
...
Makna:
Menampilkan modul kernel (kernel modules) yang sedang dimuat di memori.
Modul kernel = kode tambahan yang dapat dimuat/dilepas dinamis untuk memperluas kemampuan kernel (contoh: driver, filesystem, protokol jaringan).

d. Perintah dmesg | head
[    0.000000] Linux version 6.6.87.2-microsoft-standard-WSL2 ...
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
...
Makna:
dmesg menampilkan pesan kernel ring buffer, yaitu log awal boot yang berisi informasi inisialisasi kernel.
Baris awal memperlihatkan:
Versi kernel.
CPU yang didukung.
Pemetaan RAM fisik.
Komponen BIOS.
Ini menandakan kernel sedang melakukan inisialisasi perangkat keras virtual, termasuk memori dan CPU virtual di bawah WSL2.

2.Hubungkan Hasil dengan Teori (Kernel, System Call, Arsitektur OS)
Fungsi Kernel
Kernel bertanggung jawab langsung atas pengelolaan sumber daya sistem, seperti CPU, memori, file system, dan perangkat I/O.
Dalam percobaan, saat proses dijalankan dan melakukan operasi (misalnya menulis ke file), kernel yang mengatur dan menjadwalkan operasi tersebut.

System Call
System call adalah interface antara aplikasi dan kernel.
Hasil percobaan menunjukkan bahwa tanpa system call, aplikasi tidak dapat berinteraksi dengan hardware secara langsung.
Misalnya, pemanggilan write() di Linux adalah system call untuk mencetak ke layar. Proses ini terlihat dalam tool seperti strace, yang menunjukkan system call mana yang digunakan.

Arsitektur OS
Dalam Monolithic OS (seperti Linux), semua fungsi (I/O, file system, dll) dijalankan dalam ruang kernel. System call berlangsung lebih cepat, tapi potensi crash lebih tinggi jika ada bug.

3.1. Lingkungan Linux Asli
Linux menjalankan kernel Linux murni, sehingga perintah seperti:
uname -a → Menampilkan versi kernel Linux distro (misal Ubuntu/Fedora).
lsmod → Menunjukkan semua modul kernel (driver hardware, filesystem, protokol jaringan).
dmesg → Menampilkan pesan kernel lengkap tentang proses booting, deteksi perangkat keras (CPU, RAM, USB, disk, jaringan).

2.Lingkungan Windows
Windows tidak menggunakan kernel Linux,melainkan Windows NT kernel.Maka,perintah seperti uname,lsmod,dan dmesg tidak dikenali di Command Prompt atau PowerShell.Sebagai gantinya,Windows menggunakan alat lain seperti:
systeminfo → Menampilkan versi OS dan spesifikasi sistem.
driverquery → Menampilkan driver perangkat keras.
Event Viewer → Menampilkan log sistem (mirip fungsi dmesg).
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190


---

## Kesimpulan
<<<<<<< HEAD
Sekali lagi, kernel adalah jantung sistem operasi; sistem operasi elementer memberi izin komunikasi antara komponen ssistem operasi dan perangkat keras. Ini juga diperlihatkan oleh kenyataan bahwa perintah lsmod dan dmesg memberikan daftar modul utama dan logger boot-up sistem, masing-masing. Sistem-sistem panggilan adalah petugas penghubung antara user space dan kernel space, sehingga yang membalas hingga aktivitas termina l. Sistemplet user-space ikut meminta jasa dari kernel tanpa harus meributkan ke perangkat kerasnya sehabis itu. WSL2 Linux Environment salah satunya kernel asli linux, karena itu ia menunjukkan informasiwayar modul dan logger sistemnya tanpa melaluicara cara lain – sesuatu yang benar-benar tidak bisa dijumpai di Windows, asalkarena mereka gunakan katajalur kernel dan API sistem yang berbeda.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:** Manajemen Sumber Daya, Manajemen Proses dan File, serta Penyediaan Antarmuka Pengguna  
2. [Pertanyaan 2]  
   **Jawaban:**  mode kernel memiliki akses penuh ke perangkat keras dan memori sistem, sementara mode pengguna memiliki akses yang dibatasi dan harus melalui system calls untuk meminta layanan dari kernel.
3. [Pertanyaan 3]  
   **Jawaban:**  Linux dan Windows
=======
Kernel Linux adalah bagian terpenting dari sistem operasi yang mengkoordinasikan kerja antara perangkat keras dan perangkat lunak. Ada beberapa cara untuk memeriksa informasi kernel menggunakan perintah spesifik seperti uname,lsmod,dmesg,dan untuk memastikan bahwa modul tidak dinonaktifkan oleh sistem.Dalam lingkungan WSL2,kernel Linux asli dieksekusi di atas sistem operasi Windows,yang tercapai melalui virtualisasi.Ini memungkinkan Anda untuk menjalankan perangkat dan fungsi Linux tanpa meninggalkan sistem operasi Windows.Perbedaan utama adalah bahwa dalam versi ini,Linux tidak diizinkan mengakses perangkat keras,menetapkan tugas-tugas ini ke virtualisasi layer yang disediakan oleh Windows.

## Quiz
1. [Sebutkan tiga fungsi utama sistem operasi.]  
   **Jawaban:Manajemen Sumber Daya, Manajemen Proses dan File, serta Penyediaan Antarmuka Pengguna.**  
2. [Jelaskan perbedaan antara kernel mode dan user mode.]  
   **Jawaban:Perbedaan utama antara mode kernel dan mode pengguna adalah tingkat akses sumber daya. Mode kernel memberikan akses penuh ke perangkat keras dan memori sistem, di mana inti sistem operasi beroperasi, sedangkan mode pengguna menjalankan aplikasi dengan akses terbatas, hanya dapat meminta sumber daya melalui API sistem untuk menjaga keamanan dan stabilitas.**  
3. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.]  
   **Jawaban:Monolithic Kernel:Linux, MS-DOS, Unix tradisional
   MicrokernelMinix, QNX, macOS (XNU hybrid), Mach kernel**  
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
<<<<<<< HEAD
- Bagaimana cara Anda mengatasinya?  
1.terkendala di laptop karena laptop nya ngelag
2.dengan meminjam laptop teman
=======
- BagaimUana cara Anda mengatasinya?
1.Terkendala saat login akun git dan bingung pada tugas sistem opersai
2.dengan cara menanyakan kakak tingkat yang saya kenal di universitas putra bangsa  
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
