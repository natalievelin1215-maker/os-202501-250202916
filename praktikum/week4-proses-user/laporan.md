
# Laporan Praktikum Minggu IV
<<<<<<< HEAD
Topik: Proses user
---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936  
=======
Topik: Proses User
---

## Identitas
- **Nama**  : Evelin Natalie
- **NIM**   : 250202916
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.
3. Menggunakan perintah untuk membuat dan mengelola user.
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.
<<<<<<< HEAD
=======

>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Dasar Teori
<<<<<<< HEAD
- Konsep User (Pengguna):
User adalah individu atau entitas yang berinteraksi dengan sistem komputer untuk menjalankan perintah, mengakses data, dan menggunakan sumber daya sistem.

- Identitas dan Autentikasi:
Setiap user memiliki identitas unik (username) dan kredensial (password atau token) untuk memastikan keamanan serta mencegah akses tidak sah ke sistem.

- Hak Akses dan Otorisasi:
Sistem memberikan hak akses tertentu (read, write, execute) kepada user sesuai perannya. Ini diatur melalui permission atau access control list.

- Manajemen Proses User:
Saat user menjalankan program, sistem membuat process atas nama user tersebut. Proses ini membawa identitas dan hak akses user untuk mengontrol apa yang dapat dilakukan di sistem.

- Isolasi dan Keamanan:
Setiap user dan prosesnya diisolasi untuk mencegah gangguan atau penyalahgunaan antar pengguna, mendukung stabilitas dan keamanan sist
=======
1. Definisi Proses User
- Proses user adalah program yang dijalankan dalam mode pengguna (user mode), yaitu lingkungan terbatas yang tidak memiliki akses langsung ke sumber daya kernel untuk menjaga keamanan sistem.

2. Pemrosesan oleh Sistem Operasi
- Sistem operasi bertanggung jawab untuk membuat, mengatur, dan menghapus proses user menggunakan Process Control Block (PCB) yang menyimpan informasi penting seperti status, prioritas, dan konteks eksekusi.

3. Transisi User–Kernel Mode
- Saat proses user membutuhkan layanan sistem (misalnya akses file, memori, atau perangkat keras), terjadi transisi ke mode kernel melalui system call. Setelah selesai, kontrol dikembalikan ke mode user.

4. Isolasi dan Keamanan
- Proses user diisolasi satu sama lain agar tidak saling mengganggu. OS menggunakan proteksi memori dan kontrol hak akses untuk mencegah pelanggaran keamanan antar proses.

5. Manajemen Multitasking
- Beberapa proses user dapat dijalankan secara bersamaan melalui penjadwalan CPU (scheduling), memungkinkan sistem mendukung multitasking secara efisien tanpa konflik sumber daya.
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---
## Hasil Eksekusi

<<<<<<< HEAD
<img width="1365" height="768" alt="proses user 1" src="https://github.com/user-attachments/assets/460e6dd1-607a-44c4-8344-6fdb75cbea4b" />

<img width="1365" height="767" alt="proses user 2" src="https://github.com/user-attachments/assets/98cf7dea-128d-4943-843f-702b1e5d32ae" />

<img width="1366" height="768" alt="proses user 3" src="https://github.com/user-attachments/assets/a7241b3e-de3e-4033-ac02-a97fb1ad11d3" />
=======
<img width="1366" height="768" alt="Proses user 1" src="https://github.com/user-attachments/assets/9bcf977b-34ac-484c-8c6d-86d8df17bad6" />

<img width="1366" height="758" alt="proses user 2" src="https://github.com/user-attachments/assets/b29e66fe-7a8c-41ce-bf70-550e660186bd" />

<img width="1366" height="767" alt="proses user 3" src="https://github.com/user-attachments/assets/cd191ad3-5ec4-4f53-b121-ff22f3bde0a3" />

>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190


---

## Analisis
<<<<<<< HEAD
2. eksperimen 2: Jelaskan setiap output dan fungsinya (whoami, id, groups)
3. eksperimen 3: Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND
4. eksperimen 4: Catat PID proses sleep
5. eksperimen 5: Amati hierarki proses dan identifikasi proses induk (init/systemd)

**jawaban**

2. `whoami`
- Fungsi:
Menampilkan nama user yang sedang aktif (login) di sistem saat ini.
Perintah ini sering digunakan untuk memastikan identitas user yang sedang menjalankan shell atau perintah.
- Contoh output:faik
- Penjelasan output:
Menunjukkan bahwa user yang sedang aktif atau menjalankan terminal adalah faik.

`id`

Fungsi:Menampilkan informasi identitas lengkap dari user, termasuk:
- UID (User ID)
- GID (Group ID)
- Kelompok tambahan (groups)

- Contoh output:uid=1000(faik) gid=1000(faik) groups=1000(faik),27(sudo)

- Penjelasan output:
   - uid=1000(faik) : ID unik user bernama faik adalah 1000.
   - gid=1000(faik) : ID grup utama user faik adalah 1000.
   - groups=1000(faik),27(sudo) : User faik termasuk dalam dua grup: faik dan sudo (berarti punya hak administratif).

`groups`
- Fungsi:Menampilkan daftar grup yang diikuti oleh user saat ini.
- Contoh output:faik sudo
- Penjelasan output:User faik adalah anggota dari dua grup: faik (grup utama) dan sudo (grup dengan hak akses administratif).

3. faik         432  0.0  0.0   3212  1792 pts/0    S    18:01   0:00 sleep 1000
faik         434  0.0  0.1   4028  2176 pts/0    S+   18:01   0:00 grep --color=auto sleep


4. - PID (Process ID)
Artinya: Nomor unik yang diberikan oleh sistem untuk setiap proses yang sedang berjalan. Fungsinya Digunakan untuk mengidentifikasi dan mengontrol proses, misalnya ketika ingin menghentikan proses menggunakan kill PID.

- USER
Artinya: Nama pengguna (user) yang menjalankan proses tersebut.Fungsi nya Menunjukkan siapa pemilik proses, berguna untuk manajemen keamanan dan hak akses.

- %CPU
Artinya: Persentase penggunaan CPU oleh proses tersebut. Fungsi nya Menunjukkan seberapa besar beban prosesor yang digunakan proses itu, nilai tinggi berarti proses tersebut menggunakan banyak daya komputasi.

- %MEM
Artinya: Persentase penggunaan memori (RAM) oleh proses tersebut. Fungsi nya Memantau seberapa besar memori yang dikonsumsi, berguna untuk mengidentifikasi proses yang boros memori.

- COMMAND

Artinya: Nama atau perintah yang menjalankan proses. Fungsi nya menunjukkan program atau skrip apa yang sedang berjalan biasanya mencantumkan path atau argumen lengkap dari perintah tersebut.


4. - Analisis Hierarki:
Ini adalah proses pertama yang dijalankan oleh kernel saat sistem booting.
Fungsi systemd: Menginisialisasi seluruh sistem (mengganti peran lama init pada sistem modern).Menjalankan semua proses anak (child processes) seperti NetworkManager, sshd, cron, dan Mengatur lifecycle (start, stop, restart) layanan sistem.
=======
2. eksperimen 1 : Jelaskan setiap output dan fungsinya.(whoami,id,groups)
3. eksperimen 2 : Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
4. eksperimen 3 : Catat PID proses sleep
5. eksperimen 4 : Amati hierarki proses dan identifikasi proses induk (init/systemd).

**JAWAB** 
1. - Whoami Menampilkan nama user yang sedang login atau menjalankan terminal saat ini.Output evelin berarti user aktif saat ini bernama evelin.Perintah ini berguna untuk mengecek identitas user yang sedang digunakan, terutama setelah berpindah ke user lain menggunakan sudo.
   -id Menampilkan informasi lengkap tentang identitas user, termasuk UID (User ID),GID (Group ID),dan daftar grup yang diikuti oleh user.id memberikan informasi identitas lengkap user dalam bentuk angka (ID) dan nama (label).
   - groups Menampilkan semua grup yang diikuti oleh user yang sedang aktif. groups menampilkan daftar keanggotaan grup user, yang menentukan hak akses dan izin terhadap file atau perangkat.

2. - PID adalah nomor identitas unik untuk setiap proses yang sedang berjalan di sistem.
   - USER yaitu nama pengguna (user) yang menjalankan proses tersebut.
   - %CPU adalah Persentase penggunaan CPU oleh proses tersebut.
   - %MEM adalah Persentase penggunaan memori fisik (RAM) oleh proses
   - COMMAND adalah Perintah atau nama program yang dijalankan oleh proses.
3. - evelin       710  0.0  0.0   3124  1664 pts/0    S    16:44   0:00 sleep 1000
- evelin       712  0.0  0.0   4088  1920 pts/0    S+   16:45   0:00 grep --color=auto sleep

4. - Analisis hierarki proses
Proses paling atas (induk utama) adalah systemd(1), dengan PID 1.Semua proses lain seperti cron, dbus-daemon, rsyslogd, dan login merupakan proses turunan (child process) dari systemd.Proses seperti bash, head, dan pstree merupakan proses anak dari sesi login user (login atau bash).

- Proses induk utama sistem adalah:systemd (PID 1)
- Fungsinya:
1. Menginisialisasi sistem saat booting.
2. Menjalankan dan memonitor seluruh proses sistem.
3. Mengatur layanan (services) dan sesi pengguna.

>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190


## Kesimpulan
<<<<<<< HEAD
- Proses user merupakan proses yang dijalankan oleh pengguna di ruang pengguna (user space) dan berinteraksi dengan kernel melalui system call untuk menggunakan sumber daya sistem.
- Proses ini memastikan sistem dapat menjalankan banyak program secara terpisah, sehingga meningkatkan keamanan, stabilitas, dan efisiensi sistem operasi.

=======
1. Setiap proses di Linux dijalankan oleh user tertentu dan memiliki identitas unik berupa PID (Process ID) yang digunakan sistem untuk mengelola, memantau, atau menghentikan proses tersebut.

2. User dan hak aksesnya menentukan kendali terhadap proses. Hanya user pemilik proses atau root yang dapat memodifikasi atau menghentikan proses tersebut.

3. Perintah seperti whoami, id, dan ps aux membantu mengenali identitas user dan proses yang sedang berjalan, sehingga memudahkan administrasi dan pengawasan sistem.
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---
## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.

Perintah `whoami` digunakan untuk mengetahui user yang sedang aktif pada sistem, sedangkan `id` dan `groups` memberikan informasi lebih detail mengenai identitas pengguna, termasuk UID, GID, serta keanggotaan grup yang menentukan hak aksesnya. Perintah `sudo adduser praktikan` berfungsi untuk menambahkan user baru bernama praktikan, dan `sudo passwd praktikan` digunakan untuk mengatur kata sandinya agar akun tersebut dapat digunakan untuk login. Selanjutnya, `ps aux | head -10` menampilkan daftar proses yang sedang berjalan di sistem secara ringkas, dan `top -n 1` memberikan gambaran penggunaan sumber daya seperti CPU dan memori secara real-time. Perintah `sleep 1000` & digunakan untuk menjalankan proses sleep di latar belakang, sementara `ps aux | grep sleep` berguna untuk mencari dan memastikan proses tersebut sedang aktif dengan menampilkan PID-nya. Jika proses tersebut ingin dihentikan, maka digunakan perintah `kill <PID>`, yang mengakhiri proses berdasarkan nomor PID yang ditentukan. Terakhir, `pstree -p | head -20` menampilkan struktur hierarki proses, sehingga dapat diketahui proses induk seperti systemd beserta proses turunannya. Secara keseluruhan, rangkaian perintah ini menunjukkan bagaimana administrator sistem dapat mengelola user dan memantau proses yang berjalan dalam sistem Linux secara efisien.
   
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.

<img width="2082" height="882" alt="Untitled diagram-2025-10-28-115837" src="https://github.com/user-attachments/assets/1bd79a88-85c1-4416-a7b6-d96fce5ba810" />

 
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
  - User management berfungsi sebagai lapisan pengendali akses dan perlindungan data, yang secara langsung berkontribusi pada keamanan sistem Linux dengan memastikan bahwa hanya pengguna yang berwenang dapat melakukan tindakan tertentu di dalam sistem.
4. Upload laporan ke repositori Git tepat waktu.

<<<<<<< HEAD
## Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?
- Menjalankan proses awal setelah kernel aktif
Setelah kernel Linux selesai di-load, ia memanggil proses pertama — dulu init, sekarang umumnya systemd.
- Mengatur urutan booting sistem
systemd menjalankan layanan (service) seperti network, ssh, cron, dan lainnya sesuai dependensi dan urutan yang benar.
-Mengelola proses dan service
Dapat memulai, menghentikan, me-restart, dan memantau status service.


2. Apa perbedaan antara `kill` dan `killall`?
  - kill menargetkan proses tertentu berdasarkan PID.
  - killall menargetkan semua proses berdasarkan nama program. 
  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
   User root memiliki hak istimewa karena berperan sebagai superuser yang memiliki kendali penuh terhadap sistem Linux.


=======
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.  
4. Upload laporan- whoami
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190


**JAWAB** 


1. - id
Menampilkan identitas user (uid, gid) dan grup-grup yang diikutinya.

- groups
Menunjukkan daftar grup tempat user evelin tergabung, seperti sudo, adm, dan lainnya.

- sudo adduser praktikan
Menambahkan akun baru bernama praktikan ke sistem beserta home directory-nya.

- sudo passwd praktikan
Mengatur atau mengganti password untuk user praktikan.

- ps aux | head -10
Melihat daftar proses yang sedang berjalan di sistem, ditampilkan 10 baris pertama.

- top -n 1
Menampilkan penggunaan CPU, memori, dan daftar proses aktif saat ini (snapshot sekali).

- sleep 1000 &
Menjalankan proses sleep selama 1000 detik di background.

- ps aux | grep sleep
Mengecek apakah proses sleep masih berjalan dengan mencari berdasarkan nama.

- kill 710
Menghentikan proses sleep dengan PID 710.

- pstree -p | head -20
Menampilkan struktur hierarki proses dalam bentuk pohon, dengan systemd(1) sebagai induk utama. ke repositori Git tepat waktu.

2.  <img width="3756" height="1072" alt="diagram pohon" src="https://github.com/user-attachments/assets/8ec3ec06-e5c6-4a6c-bde0-59e68cc1b436" />

3. Hubungan antara user management dan keamanan sistem Linux sangat erat, karena pengelolaan pengguna adalah salah satu cara utama untuk mengontrol akses dan melindungi sistem dari penyalahgunaan.User management adalah fondasi utama keamanan Linux.
Dengan mengatur akun, hak akses, dan izin secara tepat, sistem dapat mencegah pelanggaran keamanan, membatasi dampak kesalahan manusia, dan menjaga integritas serta stabilitas sistem


### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
2. Apa perbedaan antara `kill` dan `killall`?  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

**JAWAB**  
1. Fungsi dari proses init atau systemd dalam sistem Linux
- Menginisialisasi sistem setelah boot — menyiapkan lingkungan kerja, memeriksa file system, dan memulai service penting.
- Menjalankan dan mengatur proses background (daemon) seperti jaringan, logging, atau cron.
- Mengatur urutan start/stop service berdasarkan dependensi.
- Memantau dan menghidupkan ulang service jika terjadi kegagalan.

2.
- kill digunakan untuk menghentikan proses tertentu berdasarkan PID (Process ID).
Misalnya, jika kamu tahu proses dengan PID 1234 sedang berjalan
- killall digunakan untuk menghentikan semua proses yang memiliki nama tertentu.

3. Karena User root memiliki hak istimewa karena dibutuhkan untuk mengelola, mengamankan, dan memelihara sistem Linux secara penuh, sementara user biasa dibatasi agar sistem tetap stabil dan aman
   
---

## Refleksi Diri
Tuliskan secara singkat:
<<<<<<< HEAD
- Apa bagian yang paling menantang minggu ini?  laptop yang kurang mendukung dalam mengerjakan week 4
- Bagaimana cara Anda mengatasinya?  meminjam laptop teman 
=======
- Apa bagian yang paling menantang minggu ini?  pemahaman konsep dasar sistem Linux dan interpretasi hasil perintah secara logis
- Bagaimana cara Anda mengatasinya?  Belajar memahami konsep dasar dulu sebelum praktik,Diskusi dan latihan bersama teman
>>>>>>> 8fe25f9a935a979f0fb4648bd07d8efa09ba7190

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
