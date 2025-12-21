
# Laporan Praktikum Minggu XI
Topik: simulasi Scheduling 
---

## Identitas
- **Nama**  : Evelin Natalie
- **NIM**   : 250202916  
- **Kelas** : 1IKRA    

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


---

## Dasar Teori
Konsep Dasar Penjadwalan CPU
Penjadwalan CPU merupakan fungsi utama sistem operasi yang bertugas mengatur pembagian waktu pemrosesan CPU kepada berbagai proses yang berada dalam keadaan siap (ready state). Karena jumlah proses yang meminta layanan CPU sering kali lebih banyak daripada jumlah CPU yang tersedia, diperlukan mekanisme penjadwalan agar setiap proses memperoleh giliran eksekusi secara adil dan efisien. Dalam simulasi, konsep ini dimodelkan dengan mengatur urutan eksekusi proses berdasarkan aturan tertentu yang ditentukan oleh algoritma penjadwalan yang digunakan.

Karakteristik dan Status Proses
Setiap proses dalam sistem memiliki karakteristik tertentu seperti arrival time (waktu kedatangan proses), burst time (lama waktu eksekusi CPU), dan priority (tingkat prioritas). Selain itu, proses juga dapat berada dalam beberapa status seperti new, ready, running, waiting, dan terminated. Simulasi algoritma penjadwalan CPU memanfaatkan karakteristik dan perubahan status ini untuk merepresentasikan kondisi nyata sistem operasi secara lebih akurat.

Jenis dan Mekanisme Algoritma Penjadwalan
Algoritma penjadwalan CPU dibedakan menjadi dua kategori utama, yaitu non-preemptive dan preemptive. Pada algoritma non-preemptive, proses yang sedang berjalan tidak dapat dihentikan hingga selesai atau menunggu I/O, sedangkan pada algoritma preemptive, proses dapat dihentikan sementara untuk memberi kesempatan kepada proses lain yang lebih prioritas. Simulasi memungkinkan pengamatan bagaimana perbedaan mekanisme ini memengaruhi urutan eksekusi dan respons sistem terhadap proses baru.

Kriteria Evaluasi Kinerja Penjadwalan
Untuk menilai efektivitas suatu algoritma penjadwalan, digunakan beberapa metrik kinerja seperti waiting time, turnaround time, response time, throughput, dan CPU utilization. Simulasi berperan penting dalam menghitung dan membandingkan nilai-nilai metrik tersebut secara sistematis, sehingga dapat diketahui algoritma mana yang memberikan kinerja terbaik untuk kondisi beban kerja tertentu.

Peran dan Manfaat Simulasi dalam Analisis Penjadwalan
Simulasi digunakan sebagai pendekatan eksperimental untuk mempelajari perilaku algoritma penjadwalan tanpa harus menerapkannya langsung pada sistem operasi nyata. Melalui simulasi, berbagai skenario beban kerja dapat diuji dengan aman dan fleksibel, seperti perubahan jumlah proses, variasi waktu eksekusi, dan perbedaan prioritas. Hal ini membantu dalam memahami kelebihan, keterbatasan, serta dampak penerapan suatu algoritma penjadwalan CPU secara mendalam.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Hasil Eksekusi

<img width="1360" height="768" alt="dataset FCFS" src="https://github.com/user-attachments/assets/d6a95524-0ddb-421c-9745-6fa8584b18b1" />


<img width="1366" height="768" alt="dataset SJF" src="https://github.com/user-attachments/assets/7c21805f-caec-44a8-8ea2-14bdaf4f030f" />



---

## Analisis
   - Jelaskan alur program.  

. Alur Program
a. Inisialisasi Data
```bash
processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]
```

Menentukan daftar proses, arrival time, dan burst time.

Urutan proses sudah sesuai dengan kedatangan (FCFS).
```
n = len(processes)
```

Menyimpan jumlah proses.
```
start_time = [0] * n
finish_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
```

Menyediakan array untuk menyimpan hasil perhitungan setiap proses.

b. Proses Penjadwalan FCFS
for i in range(n):


Perulangan untuk memproses setiap proses satu per satu sesuai urutan kedatangan.

Proses pertama
   ```
if i == 0:
    start_time[i] = arrival_time[i]
````

Proses pertama langsung dieksekusi saat tiba.

Proses berikutnya
```
else:
    start_time[i] = max(finish_time[i - 1], arrival_time[i])
```

Proses dimulai setelah proses sebelumnya selesai atau setelah ia datang.

Perhitungan waktu
```
finish_time[i] = start_time[i] + burst_time[i]
waiting_time[i] = start_time[i] - arrival_time[i]
turnaround_time[i] = finish_time[i] - arrival_time[i]
```

Finish Time = Start + Burst

Waiting Time = Start − Arrival

Turnaround Time = Finish − Arrival

c. Menghitung Rata-rata
```
avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n
```

Menghitung rata-rata waiting time dan turnaround time.
   - Bandingkan hasil simulasi dengan perhitungan manual.

    Perbandingan Hasil Simulasi dan Perhitungan Manual
a. Perhitungan Manual FCFS

| Proses | Arrival |	Burst | Start | Finish | Waiting	| Turnaround |
| ------ | ------- | ----- | ----- | ------ | ------- | ---------  |
| P1 | 0	| 6 |	0 | 6 | 0 | 6 |
| P2 | 1 | 8 |	6 | 14| 5 | 13|
| P3 | 2 | 7 |	14| 21| 12| 19|
| P4 | 3 | 3 |	21| 24| 18|	21|

Rata-rata Waiting Time
(0+5+12+18)/4=8.75

Rata-rata Turnaround Time
(6+13+19+21)/4=14.75

b. Hasil Simulasi Program

Waiting Time rata-rata = 8.75

Turnaround Time rata-rata = 14.75

Hasil simulasi sama persis dengan perhitungan manual, sehingga program berjalan dengan benar.

- Jelaskan kelebihan dan keterbatasan simulasi.

a. Kelebihan Simulasi

1. Cepat dan akurat
Menghindari kesalahan perhitungan manual.

2. Mudah diuji ulang
Dataset dapat diubah tanpa menghitung ulang secara manual.

3. Cocok untuk banyak proses
Efisien untuk jumlah proses besar.

4. Membantu visualisasi konsep
Mempermudah pemahaman algoritma scheduling.

b. Keterbatasan Simulasi

1. Tidak merepresentasikan kondisi nyata sepenuhnya
Tidak memperhitungkan context switching dan I/O.

2. Hanya sesuai algoritma tertentu
Kode ini khusus FCFS, tidak bisa langsung dipakai untuk SJF atau Round Robin.

3. Urutan proses statis
Tidak menangani proses yang datang secara dinamis saat CPU idle.

4. Tidak menunjukkan performa sistem secara real-time
Hanya menghasilkan hasil numerik.

---

## Kesimpulan
Simulasi algoritma penjadwalan CPU menggunakan metode First Come First Served (FCFS) berhasil diimplementasikan dan dijalankan dengan baik menggunakan dataset yang diberikan. Hasil simulasi menunjukkan perhitungan waiting time dan turnaround time yang sesuai dengan teori penjadwalan CPU.

Perbandingan antara hasil simulasi dan perhitungan manual menunjukkan nilai yang sama, sehingga dapat disimpulkan bahwa program simulasi yang dibuat benar secara logika dan matematis serta mampu merepresentasikan konsep dasar penjadwalan CPU dengan akurat.

Simulasi terbukti efektif sebagai alat bantu pembelajaran karena mempermudah analisis kinerja algoritma penjadwalan, meskipun masih memiliki keterbatasan dalam merepresentasikan kondisi sistem operasi nyata secara penuh.

---

## Quiz & Tugas
### Tugas
1. Buat program simulasi FCFS atau SJF.  
2. Jalankan program dengan dataset uji.  
3. Sajikan output dalam tabel atau grafik.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  

Simulasi diperlukan untuk menguji algoritma scheduling karena beberapa alasan penting berikut:
   
   1. Sulit diuji langsung pada sistem nyata
Menguji algoritma scheduling langsung pada sistem operasi yang sedang berjalan berisiko mengganggu kinerja sistem, menyebabkan crash, atau kehilangan data. Simulasi memungkinkan pengujian tanpa risiko tersebut.

   2. Lingkungan pengujian dapat dikontrol
Dengan simulasi, kondisi seperti jumlah proses, waktu kedatangan (arrival time), waktu eksekusi (burst time), dan prioritas dapat diatur secara bebas sehingga hasil pengujian lebih terukur dan adil.

   3. Memudahkan perbandingan antar algoritma
Simulasi memungkinkan beberapa algoritma (misalnya FCFS, SJF, Priority, Round Robin) diuji dengan data yang sama, sehingga perbedaan performa dapat dibandingkan secara objektif.

   4. Menghemat waktu dan biaya
Simulasi lebih efisien dibandingkan implementasi langsung pada sistem nyata, terutama untuk skenario kompleks atau skala besar.

   5. Dapat mengukur metrik kinerja dengan jelas
Melalui simulasi, metrik seperti waiting time, turnaround time, response time, dan CPU utilization dapat dihitung dan dianalisis secara akurat.

   6. Mendukung analisis berbagai skenario ekstrem
Kondisi ekstrem (beban sangat tinggi, banyak proses bersamaan) sulit direalisasikan pada sistem nyata, tetapi mudah diuji melalui simulasi.
.

2.Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar? 

Pada dataset yang berukuran besar, perbedaan antara hasil simulasi dan perhitungan manual menjadi semakin jelas, terutama dari segi ketelitian, efisiensi, dan keandalan hasil. Perhitungan manual pada jumlah data yang banyak sangat rentan terhadap kesalahan manusia, seperti salah menjumlahkan waktu, keliru menentukan urutan proses, atau tidak konsisten dalam menerapkan aturan algoritma scheduling. Kesalahan kecil ini dapat berdampak besar pada hasil akhir, sehingga akurasi perhitungan manual sulit dipertahankan ketika kompleksitas data meningkat.

Sebaliknya, simulasi dilakukan menggunakan program komputer yang mampu memproses dataset besar secara sistematis dan konsisten sesuai dengan algoritma yang diterapkan. Simulasi dapat menghitung berbagai metrik kinerja, seperti waiting time, turnaround time, dan response time untuk seluruh proses dengan cepat dan tepat. Selain itu, simulasi juga memungkinkan pengujian berbagai skenario yang kompleks—misalnya perubahan jumlah proses, variasi waktu kedatangan, atau perbedaan prioritas—yang hampir tidak mungkin dilakukan secara manual dalam waktu yang wajar.

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

Algoritma scheduling yang paling mudah diimplementasikan adalah First Come First Served (FCFS). Hal ini karena FCFS bekerja dengan prinsip yang sangat sederhana, yaitu proses yang pertama kali datang akan dilayani terlebih dahulu tanpa mempertimbangkan waktu eksekusi, prioritas, atau faktor lainnya. Implementasinya cukup menggunakan satu antrian (queue) dan mengeksekusi proses secara berurutan sesuai urutan kedatangan, sehingga logika programnya mudah dipahami dan tidak memerlukan struktur data atau perhitungan yang kompleks.

Dibandingkan dengan algoritma lain seperti Shortest Job First (SJF), Priority Scheduling, atau Round Robin, FCFS tidak memerlukan proses pemilihan ulang (selection) atau pengurutan proses berdasarkan kriteria tertentu. SJF dan Priority membutuhkan perbandingan antar proses, sedangkan Round Robin memerlukan pengaturan time quantum dan mekanisme context switching yang lebih rumit. Oleh karena itu, dari segi konsep, logika, dan implementasi teknis, FCFS merupakan algoritma scheduling yang paling mudah untuk diterapkan, terutama bagi pemula atau untuk tujuan pembelajaran dasar sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Bagian yang paling menantang pada praktikum ini adalah memahami alur kerja algoritma penjadwalan CPU serta menghubungkan konsep teoritis seperti arrival time, burst time, waiting time, dan turnaround time ke dalam bentuk program simulasi. Selain itu, memastikan hasil simulasi sesuai dengan perhitungan manual juga memerlukan ketelitian.

- Bagaimana cara Anda mengatasinya?  
Cara mengatasinya adalah dengan mempelajari kembali materi penjadwalan CPU, mengerjakan perhitungan manual terlebih dahulu, lalu membandingkannya secara bertahap dengan hasil program. Dengan melakukan pengujian berulang dan mengecek setiap tahapan perhitungan, kesalahan dapat diminimalkan dan pemahaman terhadap algoritma FCFS menjadi lebih baik.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
