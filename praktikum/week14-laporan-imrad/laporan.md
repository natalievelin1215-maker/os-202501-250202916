
# Laporan Praktikum Minggu [X]


---

## Identitas
- **Nama**  : Evelin Natalie
- **NIM**   : 250202916 
- **Kelas** : 1IKRA

---

## 1. Pendahuluan (Introduction):

### 1.1 Latar Belakang
Dalam sistem operasi, banyak proses berjalan secara bersamaan dan saling berbagi sumber daya seperti CPU, memori, file, maupun perangkat input/output. Ketika beberapa proses saling menunggu sumber daya yang sedang digunakan oleh proses lain, dapat terjadi kondisi deadlock, yaitu keadaan di mana proses-proses tersebut tidak dapat melanjutkan eksekusinya karena saling menunggu tanpa batas waktu.

Deadlock merupakan masalah serius karena dapat menyebabkan sistem menjadi tidak responsif, menurunkan kinerja, bahkan menghentikan sebagian fungsi sistem. Oleh karena itu, diperlukan mekanisme untuk mendeteksi kondisi deadlock agar sistem dapat mengetahui proses mana yang terlibat dan mengambil tindakan pemulihan yang tepat.

Deadlock Detection adalah metode dalam sistem operasi yang digunakan untuk mengidentifikasi apakah deadlock sedang terjadi dengan menganalisis hubungan antar proses dan sumber daya. Dengan adanya mekanisme deteksi deadlock, sistem dapat meminimalkan dampak negatif deadlock dan menjaga kestabilan serta efisiensi kinerja sistem.

### 1.2 Rumusan Masalah
1. Bagaimana cara kerja deteksi deadlock berbasis timeout pada sistem operasi?

2. Apa kelebihan dan kelemahan metode timeout dalam mendeteksi deadlock?

3. Bagaimana hasil pengujian deteksi deadlock menggunakan batas waktu tertentu?


### 1.3 Tujuan
1. Memahami konsep deteksi deadlock berbasis timeout.

2. Mengimplementasikan atau mensimulasikan mekanisme timeout pada proses yang saling menunggu.

3. Menganalisis hasil deteksi deadlock berdasarkan waktu tunggu proses.

---

## 2.Metode (Methods):

### 2.1 Lingkungan Uji
- Sistem Operasi: Windows
- Bahasa Pemrograman: Python
- Tools pendukung: Terminal atau Visual Studio Code

### 2.2 Langkah Eksperimen
1. Menyiapkan dua atau lebih proses yang saling membutuhkan sumber daya yang sama.

2. Mengatur agar setiap proses meminta sumber daya secara berurutan sehingga berpotensi deadlock.

3. Menentukan batas waktu tunggu (timeout) untuk setiap proses.

4. Mengamati waktu tunggu proses terhadap sumber daya.

5. Menandai proses sebagai deadlock jika waktu tunggunya melebihi batas timeout.

### Program uji
```
import time
import threading

TIMEOUT = 5

resource_A = threading.Lock()
resource_B = threading.Lock()

def process_1():
    start_time = time.time()
    print("P1: Meminta Resource A")
    resource_A.acquire()
    print("P1: Mendapatkan Resource A")

    time.sleep(1)

    print("P1: Meminta Resource B")
    while not resource_B.acquire(blocking=False):
        if time.time() - start_time > TIMEOUT:
            print("P1: Deadlock terdeteksi (timeout)")
            resource_A.release()
            return
        time.sleep(0.5)

    print("P1: Mendapatkan Resource B")
    resource_B.release()
    resource_A.release()
    print("P1: Selesai")

def process_2():
    start_time = time.time()
    print("P2: Meminta Resource B")
    resource_B.acquire()
    print("P2: Mendapatkan Resource B")

    time.sleep(1)

    print("P2: Meminta Resource A")
    while not resource_A.acquire(blocking=False):
        if time.time() - start_time > TIMEOUT:
            print("P2: Deadlock terdeteksi (timeout)")
            resource_B.release()
            return
        time.sleep(0.5)

    print("P2: Mendapatkan Resource A")
    resource_A.release()
    resource_B.release()
    print("P2: Selesai")

t1 = threading.Thread(target=process_1)
t2 = threading.Thread(target=process_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Simulasi selesai")
```

---
## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Pembahasan (Discussion):
Berdasarkan hasil pengujian, metode timeout mampu mendeteksi proses yang mengalami waktu tunggu berlebihan dan mengindikasikannya sebagai deadlock. Proses P2 terdeteksi deadlock karena waktu tunggunya melebihi batas timeout yang ditentukan.

Kelebihan metode timeout adalah implementasinya yang sederhana dan tidak memerlukan struktur data kompleks seperti resource allocation graph. Namun, metode ini memiliki kelemahan, yaitu kemungkinan terjadinya false positive, di mana proses yang hanya lambat dapat dianggap deadlock. Selain itu, penentuan nilai timeout yang tidak tepat dapat mempengaruhi akurasi deteksi.

Hasil eksperimen ini sesuai dengan teori yang menyatakan bahwa deteksi deadlock berbasis timeout lebih cocok digunakan pada sistem sederhana atau sebagai solusi sementara (Tanenbaum, 2015).

---

## Kesimpulan
1. Deteksi deadlock berbasis timeout bekerja dengan mengamati waktu tunggu proses terhadap sumber daya.

2. Proses yang melebihi batas waktu tunggu ditandai sebagai deadlock.

3. Metode timeout mudah diimplementasikan tetapi kurang akurat untuk sistem berskala besar.

4. Pemilihan nilai timeout sangat berpengaruh terhadap hasil deteksi deadlock.
---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
