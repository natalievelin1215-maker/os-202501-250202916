
# Laporan Praktikum Minggu [3]
Topik: linux fs permision
---

## Identitas
- **Nama**  : Evelin Natalie
- **NIM**   : 250202916 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
   ```vv
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1366" height="766" alt="week3 sistem operasi" src="https://github.com/user-attachments/assets/1ff18f32-4a09-4b2d-959e-086fc04bece2" />

---

## Analisis
2. Jelaskan hasil tiap perintah.
- Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

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

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Tugas
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md.
2. Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).
3.cc
4. Upload hasil dan laporan ke repositori Git sebelum deadline.



## Quiz
1.Apa fungsi dari perintah chmod?
   **Jawaban:** chmod (change mode) mengatur siapa yang boleh membaca (read), menulis (write), atau menjalankan (execute) sebuah file atau folder. 
   
2.Apa arti dari kode permission rwxr-xr--?
   **Jawaban:**  Kode rwxr-xr-- adalah kode permission (izin akses) pada file atau direktori di Linux, termasuk di WSL.
   
3.Jelaskan perbedaan antara chown dan chmod? 
   **Jawaban:** 
   
- chmod = Mengatur apa yang boleh dilakukan orang terhadap rumah (boleh masuk, boleh ubah isi, dsb).
- chown = Mengatur siapa pemilik rumahnya.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
