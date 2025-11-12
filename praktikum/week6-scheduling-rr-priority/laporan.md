
# Laporan Praktikum Minggu VI
Topik: "Penjadwalan CPU - Round Robin (RR) dan Priority Scheduling"

---

## Identitas
- **Nama**  : Evelin Natalie
- **NIM**   : 250202916
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
- Menyusun tabel hasil perhitungan dengan benar dan sistematis.
- Membandingkan performa algoritma RR dan Priority.
- Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
- Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
- Round Robin (RR) adalah algoritma penjadwalan CPU yang membagi waktu eksekusi menjadi beberapa time quantum sehingga setiap proses mendapat giliran secara bergantian dan adil.

- RR termasuk jenis preemptive scheduling, artinya CPU dapat berpindah dari satu proses ke proses lain setelah quantum habis, untuk menjaga responsivitas sistem.

- Pemilihan nilai time quantum sangat berpengaruh: quantum terlalu kecil menimbulkan context switching berlebih, sedangkan quantum terlalu besar menurunkan keadilan antarproses.

- Priority Scheduling mengeksekusi proses berdasarkan tingkat prioritas; proses dengan prioritas lebih tinggi akan dijalankan terlebih dahulu.

- Kelemahan utama algoritma prioritas adalah potensi terjadinya starvation, yaitu proses prioritas rendah tidak mendapat giliran eksekusi jika proses prioritas tinggi terus datang.

---

## Langkah Praktikum

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  

   | Proses |   CT   | Arivaal| TAT(ct-at) |	WT(TAT-bt) |
   | :----: | :----: | :----: | :--------: | :--------: |
   |   P1   |	 14   |    0   |	14-0=14   |	14-5=9     |
   |   P2   |   6 	|    1	|  6-1=5	    | 5-3=2      |
   |   P3	|   22   |	  2   |	22-2=20   |	20-8=12    |
   |   P4	|   20   |    3	|  20-3=17   |	17-6=11    |
Rata rata TAT:14
Rata rata WT :8,5

   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
     ```
   - Catat sisa *burst time* tiap putaran.
   
   | waktu | Brust | sisa waktu|
   |:-----:|:-----:|:---------:|
   | 0-3   | 5-3=0 | P1 sisa 2 |
   | 3-6   | 3-3=0 | 2 selesai |
   | 6-9   | 8-3=5 | P3 sisa 5 |
   | 9-12  | 6-3=3 | P4 sisa 3 |
   | 12-14 | 2 < 3 | P1 selesai|
   | 14-17 | 5-3=0 | P3 sisa 2 |
   | 17-20 | 3-3=0 | P4 selesai|
   | 20-22 | 2 < 3 | P3 selesai|
   

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]o
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

|Proses|	BT | AT |PRIO|	ST |	WT(ST-AT)	|TAT(WT+BT)|
|:----:|:--:|:--:|:--:|:--:|:------------:|:--------:|
|  P1  |	 5 | 0  |  2 |	0  |	   0        | 	  5     |
|  P2  |	 3 | 1  |  1 |	5  | 	   4        |	  7     |
|  P4  |	 6 | 3  |  3 |	8  |	   5        |	  11    |
|  P3  |	 8 | 2  |  4 |	14 |     12       |    20    |

Rata rata WT  :5,25
Rata rata TAT :10,75

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  

Quantum 2
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	18 |  0 | 5 |	18 |  13|
|  P2  |	13 |	1 | 3 |	12 |	9 |
|  P3  |	24 |	2 | 8 |	22 |	14|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |   ||17.75|12.25|

Quantum 5
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	5  |  0 | 5 |	5  |  0 |
|  P2  |	8  |	1 | 3 |	7  |	4 |
|  P3  |	21 |	2 | 8 |	19 |	11|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |  || 12.5|  7 |




   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```
---

## Hasil Eksekusi


---

## Analisis

---

## Kesimpulan
1. Algoritma Round Robin (RR) memberikan keadilan dalam eksekusi proses karena setiap proses mendapat jatah waktu (time quantum) yang sama, namun efisiensinya sangat bergantung pada ukuran quantum—terlalu kecil menyebabkan context switching berlebihan, sedangkan terlalu besar membuatnya mirip dengan FCFS.

2. Algoritma Priority Scheduling lebih efisien untuk proses dengan prioritas tinggi karena mengeksekusi proses penting lebih dahulu, tetapi dapat menimbulkan masalah starvation bagi proses dengan prioritas rendah.

3. Berdasarkan hasil perhitungan, Priority Scheduling menghasilkan rata-rata waktu tunggu (WT) dan turnaround time (TAT) yang lebih kecil dibandingkan Round Robin, sehingga lebih efisien, sedangkan RR lebih unggul dari sisi keadilan terhadap semua proses.

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.  
2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.  
3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.  
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`.  

WT dan TAT RR dan Priority

Round Robin
   | Proses |   CT   | Arivaal| TAT(ct-at) |	WT(TAT-bt) |
   | :----: | :----: | :----: | :--------: | :--------: |
   |   P1   |	 14   |    0   |	14-0=14   |	14-5=9     |
   |   P2   |   6 	|    1	|  6-1=5	    | 5-3=2      |
   |   P3	|   22   |	  2   |	22-2=20   |	20-8=12    |
   |   P4	|   20   |    3	|  20-3=17   |	17-6=11    |
Rata rata TAT:14
Rata rata WT :8,5

Priority
|Proses|	BT | AT |PRIO|	ST |	WT(ST-AT)	|TAT(WT+BT)|
|:----:|:--:|:--:|:--:|:--:|:------------:|:--------:|
|  P1  |	 5 | 0  |  2 |	0  |	   0        | 	  5     |
|  P2  |	 3 | 1  |  1 |	5  | 	   4        |	  7     |
|  P4  |	 6 | 3  |  3 |	8  |	   5        |	  11    |
|  P3  |	 8 | 2  |  4 |	14 |     12       |    20    |

Rata rata WT  :5,25
Rata rata TAT :10,75

perbandingan performa quantum dan prioritas
Performa Algoritma Round Robin (RR)

RR menekankan keadilan karena semua proses mendapat giliran eksekusi secara bergantian.
Namun, efisiensinya sangat tergantung pada nilai time quantum.
Jika quantum terlalu kecil, maka terjadi banyak context switching yang menurunkan kinerja sistem.
Jika quantum terlalu besar, maka proses menjadi seperti FCFS, sehingga waktu tunggu proses pendek meningkat.
Dari hasil praktikum, perubahan quantum (2, 3, 5) menunjukkan perbedaan signifikan pada rata-rata waiting time dan turnaround time, di mana quantum sedang (3–5) memberikan hasil paling seimbang.

- Performa Algoritma Priority Scheduling

Algoritma ini menekankan efisiensi eksekusi dengan memberi prioritas pada proses penting.
Semakin tinggi prioritas (angka lebih kecil), semakin cepat proses tersebut dieksekusi.
Namun, terdapat risiko starvation untuk proses dengan prioritas rendah karena bisa terus tertunda jika selalu ada proses prioritas tinggi yang baru datang.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
