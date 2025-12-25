
# Laporan Praktikum Minggu III
Topik: linux fs permision
---

## Identitas
<<<<<<< HEAD
- **Nama**  : Faik Setyawan
- **NIM**   : 2502020936  
=======
- **Nama**  : Evelin Natalie
- **NIM**   : 250202916 
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190
- **Kelas** : 1IKRA

---

## Tujuan
<<<<<<< HEAD

Setelah menyelesaikan tugas ini, mahasiswa mampu:

Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
Menggunakan chmod dan chown untuk manajemen hak akses file.
Menjelaskan hasil output dari perintah Linux dasar.
Menyusun laporan praktikum dengan struktur yang benar.
Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
=======
Setelah menyelesaikan tugas ini, mahasiswa mampu:
- Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
- Menggunakan chmod dan chown untuk manajemen hak akses file.
- Menjelaskan hasil output dari perintah Linux dasar.
- Menyusun laporan praktikum dengan struktur yang benar.
- Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190


---

## Dasar Teori
<<<<<<< HEAD

1. Tipe pengguna Setiap file atau direktori memiliki tiga jenis pengguna: owner (pemilik), group (grup), dan others (lainnya). Hak akses dapat berbeda untuk tiap kategori.

2. Tiga hak akses dasar:
   
- r (read) → baca isi file / list isi direktori
- w (write) → ubah isi file / tambah hapus file di direktori

3. Representasi permission:
   
- Secara simbolik: rwxr-xr-- (owner, group, others)
- Secara numerik (octal): 7=rwx, 6=rw-, 5=r-x, 4=r--, dst.

4. Perintah utama:
   
- chmod → ubah permission file/direktori
- chown → ubah pemilik dan/atau grup file
=======
- Model Kepemilikan (Ownership Model)
  
Setiap file dan direktori di Linux dimiliki oleh user (pemilik) dan group (kelompok), serta dapat diakses oleh others (pengguna lain) di sistem.

- Tiga Jenis Hak Akses (Permissions Types)
  
Linux menggunakan tiga jenis izin utama:
r (read): membaca isi file atau daftar direktori.
w (write): mengubah atau menghapus isi file/direktori.


- Representasi Simbolik dan Numerik
  
Hak akses dapat ditampilkan dalam bentuk simbolik (rwxr-xr--) atau numerik (contoh: 755), di mana setiap angka mewakili kombinasi izin (r=4, w=2, x=1).

- Perintah Pengaturan Akses (chmod, chown, chgrp)
  
chmod untuk mengubah izin file dan chown untuk mengubah pemilik file.
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
<<<<<<< HEAD
   ```
=======
   ```vv
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<<<<<<< HEAD
<img width="1366" height="768" alt="Capture 7" src="https://github.com/user-attachments/assets/47eaac5e-37c1-47d2-af30-903bf4057d01" />

=======
<img width="1366" height="766" alt="week3 sistem operasi" src="https://github.com/user-attachments/assets/1ff18f32-4a09-4b2d-959e-086fc04bece2" />
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Analisis
2. Jelaskan hasil tiap perintah.
- Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

<<<<<<< HEAD
**JAWAB:** 
- perintah pwd: Menampilkan direktori aktif (current working directory).
- perintah ls -l :Menampilkan daftar isi folder dengan format panjang (long listing), termasuk permission, pemilik, ukuran, dan tanggal modifikasi.
- perintah cd /tmp: indah direktori ke /tmp, folder sementara di Linux./tmp biasanya digunakan untuk file sementara yang bisa diakses oleh semua user.Setelah ini, direktori aktif (pwd) berubah menjadi /tmp.
- perintah ls -a : Menampilkan semua file di direktori, termasuk file tersembunyi (dimulai dengan titik .)

3. Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

**JAWAB**
- cat /etc/passwd menampilkan isi file /etc/passwd, yang berisi informasi semua user di sistem Linux.head -n 5 → menampilkan 5 baris pertama dari hasil cat.

struktur baris:
1. username	Nama user
2. password	Biasanya hanya x, berarti password disimpan di /etc/shadow
3. UID	User ID (angka unik untuk setiap user)
4. GID	Group ID utama user
5. GECOS	Informasi tambahan (nama lengkap, kontak, dsb)
6. home_directory	Lokasi folder home user
7. shell	Program shell default user (misal /bin/bash)
=======
**Jawab:** 
- perintah pwd: Menampilkan direktori aktif saat ini (tempat kamu sedang berada di sistem file).
- perintah ls -l: Menampilkan daftar isi folder saat ini dengan format lengkap, yaitu, izin file (permissions),jumlah link,pemilik (owner),grup,ukuran file (bytes),waktu modifikasi,nama file.
- perintah cd /tmp: Berpindah ke direktori /tmp, yaitu folder sementara (temporary directory) yang digunakan sistem dan aplikasi untuk menyimpan file sementara.
- perintah ls -a: Menampilkan semua file dan folder di direktori saat ini, termasuk file tersembunyi.

3. Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

**Jawab**
- cat /etc/passwd enampilkan isi file. | head -n 5 → menampilkan 5 baris pertama saja dari hasil tersebut (biar tidak terlalu panjang).File /etc/passwd menyimpan informasi dasar setiap user di sistem Linux.

sruktur baris:
1. username	root	Nama akun pengguna
2. password	x	Menandakan password disimpan terenkripsi di /etc/shadow
3. UID (User ID)	0	ID pengguna unik; 0 = superuser (root)
4. GID (Group ID)	0	ID grup utama pengguna
5. comment / GECOS	root	Deskripsi atau nama lengkap pengguna
6. home directory	/root	Folder pribadi pengguna
7. shell	/bin/bash	Shell login default (program yang dijalankan saat login)


4.Analisis perbedaan sebelum dan sesudah chmod.

Sebelum chmod (rw-r--r--)
- User (pemilik / evelin) → rw- → boleh baca & tulis
- Group (grup evelin) → r-- → hanya boleh baca
- Others (pengguna lain) → r-- → hanya boleh baca

Artinya: semua orang di sistem bisa melihat isi file, tapi hanya evelin yang bisa mengubahnya.

Sesudah chmod (rw-------)
- User (evelin) → rw- → boleh baca & tulis
- Group → --- → tidak boleh apa pun
- Others → --- → tidak boleh apa pun
- Artinya: hanya evelin sendiri yang bisa membuka dan mengedit file.
Pengguna lain tidak bisa membaca, menyalin, atau menghapus file ini (akan muncul pesan Permission denied).
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Kesimpulan
<<<<<<< HEAD

Permission di Linux berfungsi sebagai mekanisme kontrol akses yang membatasi tindakan pengguna terhadap file dan direktori. Dengan pengaturan owner, group, dan others serta hak akses read, write, sistem dapat menjaga keamanan, mencegah perubahan tidak sah, dan memastikan integritas data. Perintah seperti chmod dan chown memudahkan administrator untuk mengelola hak akses secara fleksibel.

---

## Tugas 
=======
1. inux FS Permission merupakan mekanisme dasar keamanan yang mengatur siapa yang boleh membaca, menulis, dan mengeksekusi file atau direktori, sehingga menjaga kerahasiaan dan integritas sistem.

2. Sistem izin berbasis user, group, dan others memastikan setiap file memiliki kontrol akses yang jelas dan terstruktur.

3. Pengelolaan izin melalui perintah seperti chmod dan chown memberi administrator fleksibilitas untuk menyesuaikan hak akses sesuai kebutuhan keamanan dan fungsi sistem.

---

## Tugas
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md.
2. Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).
3. Analisis peran chmod dan chown dalam keamanan sistem Linux.
4. Upload hasil dan laporan ke repositori Git sebelum deadline.

**JAWAB**
<<<<<<< HEAD

1. 


| No | Perintah                                         | Hasil / Output                                                                                                                                                                                                     | Keterangan                                                                                     |
| -- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| 1  | `pwd`                                            | `/home/faik`                                                                                                                                                                                                       | Direktori aktif saat ini adalah `/home/faik`.                                                  |
| 2  | `ls -l`                                          | `total 0`                                                                                                                                                                                                          | Tidak ada file di direktori home saat ini.                                                     |
| 3  | `cd /tmp`                                        | -                                                                                                                                                                                                                  | Pindah ke direktori sementara `/tmp`.                                                          |
| 4  | `ls -a`                                          | `.  ..  .X11-unix  snap-private-tmp  systemd-private-9cc0e4d5f45a4aa0a66b501a35fb6b75-systemd-logind.service-MiTbZV ...`                                                                                           | Menampilkan semua file & folder termasuk **tersembunyi** (`.` dan `..`).                       |
| 5  | `cat /etc/passwd \| head -n 5`                   | `root:x:0:0:root:/root:/bin/bash`<br>`daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin`<br>`bin:x:2:2:bin:/bin:/usr/sbin/nologin`<br>`sys:x:3:3:sys:/dev:/usr/sbin/nologin`<br>`sync:x:4:65534:sync:/bin:/bin/sync` | Menampilkan **5 user pertama** di sistem; format: `username:password:UID:GID:GECOS:home:shell`. |
| 6  | `echo "Hello <Faik><250202936>" > percobaan.txt` | -                                                                                                                                                                                                                  | Membuat file `percobaan.txt` di `/tmp` berisi teks `Hello <Faik><250202936>`.                  |
| 7  | `ls -l percobaan.txt`                            | `-rw-r--r-- 1 faik faik 24 Oct 21 17:32 percobaan.txt`                                                                                                                                                             | **Sebelum chmod:** Pemilik bisa baca/tulis; group & others hanya baca.                         |
| 8  | `chmod 600 percobaan.txt`                        | -                                                                                                                                                                                                                  | Mengubah permission file agar **hanya pemilik bisa baca & tulis**.                             |
| 9  | `ls -l percobaan.txt`                            | `-rw------- 1 faik faik 24 Oct 21 17:32 percobaan.txt`                                                                                                                                                             | **Setelah chmod:** Group & others tidak punya akses.                                           |
| 10 | `sudo chown root percobaan.txt`                  | `[sudo] password for faik:`                                                                                                                                                                                        | Mengubah **pemilik file menjadi root**.                                                        |
| 11 | `ls -l percobaan.txt`                            | `-rw------- 1 root faik 24 Oct 21 17:32 percobaan.txt`                                                                                                                                                             | File sekarang **dimiliki root**, hanya root yang bisa baca/tulis karena permission `600`.      |

2.
- Owner	rwx	Bisa membaca, mengedit, dan menjalankan file
- Group	r-x	Bisa membaca & menjalankan, tapi tidak bisa mengedit
- Others	r--	Hanya bisa membaca file, tidak bisa mengubah atau menjalankan
- Jadi, rwxr-xr-- artinya Pemilik bisa baca, tulis, eksekusi, grup bisa baca & eksekusi, dan pengguna lain hanya bisa baca

3. chmod mengatur izin akses file atau direktori, menentukan siapa yang bisa membaca, menulis, atau mengeksekusi. Dengan chmod, file sensitif bisa dilindungi dari akses atau modifikasi oleh user yang tidak berwenang dan chown mengatur kepemilikan (user & group) file atau direktori. Dengan chown, hanya pemilik atau root yang bisa mengubah file, sehingga mencegah akses tidak sah dan menjaga tanggung jawab file.

   
## Quiz
1. Apa fungsi dari perintah chmod?
   **Jawaban:**  chmod digunakan untuk menentukan siapa yang bisa:membaca file (read / r),menulis atau mengubah file (write / w)dan menjalankan file (execute / x)
   
2. Apa arti dari kode permission rwxr-xr--?
   **Jawaban:**  Kode rwxr-xr-- adalah bentuk permission (izin akses) pada file atau direktori di sistem Linux (termasuk WSL).
   
3. Jelaskan perbedaan antara chown dan chmod?
   **Jawaban:**
- chmod (change mode) → mengubah izin akses file (baca, tulis, eksekusi).
- chown (change owner) → mengubah pemilik atau grup file.
=======
1. 



| **No.** | **Perintah** | **Fungsi / Tujuan Perintah** | **Hasil / Output** | **Keterangan** |
| :-- | :-- | :-- | :-- | :-- |
| 1 | `pwd` | Menampilkan direktori kerja saat ini | `/home/evelin` | Menunjukkan posisi pengguna saat ini di sistem file, yaitu di direktori home milik user *evelin*. |
| 2 | `ls -l` | Menampilkan isi direktori dengan format panjang (detail) | `total 0` | Direktori `/home/evelin` kosong, tidak ada file maupun folder di dalamnya. |
| 3 | `cd /tmp` | Berpindah ke direktori sementara `/tmp` | *(tidak ada output)* | Mengganti lokasi kerja aktif menjadi `/tmp`, tempat file sementara sistem disimpan. |
| 4 | `ls -a` | Menampilkan semua isi folder termasuk file tersembunyi | `. .. .X11-unix snap-private-tmp systemd-private-...` | `.` adalah direktori saat ini, `..` direktori induk, dan lainnya adalah file/folder sistem (termasuk yang tersembunyi). |
| 5 | `cat /etc/passwd \| head -n 5` | Menampilkan 5 baris pertama dari file `/etc/passwd` | ```<br>root:x:0:0:root:/root:/bin/bash<br>daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin<br>bin:x:2:2:bin:/bin:/usr/sbin/nologin<br>sys:x:3:3:sys:/dev:/usr/sbin/nologin<br>sync:x:4:65534:sync:/bin:/bin/sync<br>``` | File `/etc/passwd` berisi daftar akun pengguna. Tiap baris memiliki format: `user:password_placeholder:UID:GID:info_home:shell`. Contoh: user `root` memiliki UID 0, GID 0, direktori home `/root`, dan shell `/bin/bash`. |
| 6 | `echo "Hello <Evelin><250202916>" > percobaan.txt` | Membuat file baru dan menulis teks ke dalamnya | *(tidak ada output)* | File baru bernama `percobaan.txt` dibuat di `/tmp` berisi teks `"Hello <Evelin><250202916>"`. |
| 7 | `ls -l percobaan.txt` | Melihat detail file dan izin aksesnya | `-rw-r--r-- 1 evelin evelin 26 Oct 21 03:25 percobaan.txt` | File dimiliki oleh user *evelin*, dengan izin `rw-r--r--`: pemilik bisa baca/tulis, grup & others hanya bisa baca. |
| 8 | `chmod 600 percobaan.txt` | Mengubah izin file menjadi hanya pemilik yang bisa baca/tulis | *(tidak ada output)* | Izin diubah menjadi `rw-------`, artinya file hanya bisa diakses oleh pemilik (*evelin*). Keamanan meningkat. |
| 9 | `ls -l percobaan.txt` | Mengecek hasil perubahan izin | `-rw------- 1 evelin evelin 26 Oct 21 03:25 percobaan.txt` | Terbukti izin file sudah berubah. Grup dan pengguna lain kini tidak memiliki akses sama sekali. |
| 10 | `sudo chown root percobaan.txt` | Mengubah kepemilikan file dari *evelin* menjadi *root* | *(meminta password, lalu tidak ada output)* | Kepemilikan file berpindah ke *root*. Sekarang hanya user *root* yang berhak mengakses file sepenuhnya. |
| 11 | `ls -l percobaan.txt` | Mengecek hasil perubahan kepemilikan | `-rw------- 1 root evelin 26 Oct 21 03:25 percobaan.txt` | Pemilik file kini adalah *root* (kolom pertama), sedangkan grup masih *evelin*. File menjadi milik sistem. |



2. -	Jenis file	- = file biasa, d = direktori, l = link.
- rwx	Hak untuk user (pemilik)	r = read, w = write, x = execute. Pemilik bisa membaca, menulis, dan menjalankan file.
- r-x	Hak untuk group	r = read, - = tidak bisa menulis, x = bisa menjalankan. Anggota grup bisa membaca & menjalankan tapi tidak mengedit.
- r--	Hak untuk others (pengguna lain)	r = read, -- = tidak bisa menulis atau menjalankan. Pengguna lain hanya bisa membaca file.




3. chmod memastikan siapa yang boleh mengakses dan bagaimana caranya (baca/tulis/jalankan).dan chown memastikan siapa yang bertanggung jawab atas file tersebut. keduanya menjadi fondasi utama sistem keamanan Linux, menjaga agar hanya pengguna berhak yang dapat mengakses, memodifikasi, atau menjalankan file tertentu.
## Quiz
1.Apa fungsi dari perintah chmod?
   **Jawaban:** chmod (change mode) mengatur siapa yang boleh membaca (read), menulis (write), atau menjalankan (execute) sebuah file atau folder. 
   
2.Apa arti dari kode permission rwxr-xr--?
   **Jawaban:**  Kode rwxr-xr-- adalah kode permission (izin akses) pada file atau direktori di Linux, termasuk di WSL.
   
3.Jelaskan perbedaan antara chown dan chmod? 
   **Jawaban:** 
   
- chmod = Mengatur apa yang boleh dilakukan orang terhadap rumah (boleh masuk, boleh ubah isi, dsb).
- chown = Mengatur siapa pemilik rumahnya.
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Refleksi Diri
Tuliskan secara singkat:
<<<<<<< HEAD
- Apa bagian yang paling menantang minggu ini?  laptop kurang mendukung dalam pengerjaan tugas week 3
- Bagaimana cara Anda mengatasinya? meminjam laptop teman 
    
=======
- Apa bagian yang paling menantang minggu ini?  yang menantang minggu ini ada pada sinyal yang kurang mendukung
- Bagaimana cara Anda mengatasinya?  dengan menggunakan hospot teman
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
