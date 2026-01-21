
# Laporan Praktikum Minggu [X]
Topik: DOCKER RESOUCE LIMIT

---

## Identitas
- **Nama**  : Evelin natali 
- **NIM**   : 250202916  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
Docker Container
Docker adalah platform containerisasi yang memungkinkan aplikasi dijalankan secara terisolasi bersama dependensinya. Container bersifat ringan karena berbagi kernel dengan sistem operasi host.

Resource Limitation (CPU & Memory)
Docker menyediakan fitur pembatasan resource seperti CPU dan memori untuk mencegah satu container menghabiskan seluruh sumber daya sistem yang dapat mengganggu container lain atau host.

CPU Limit pada Docker
Pembatasan CPU (--cpus) mengatur seberapa besar waktu prosesor yang boleh digunakan container. Jika dibatasi, proses di dalam container akan berjalan lebih lambat.

Memory Limit pada Docker
Pembatasan memori (--memory) menentukan jumlah maksimum RAM yang boleh digunakan container. Jika melebihi batas, container akan dihentikan paksa oleh Docker (OOM Killer).

Monitoring Resource
Perintah docker stats digunakan untuk memantau penggunaan CPU, memori, dan resource lain secara real-time pada container yang sedang berjalan.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
app.py
```
import time

data = []

print("=== UJI RESOURCE LIMIT DOCKER ===")

try:
    i = 0
    while True:
        i += 1

        # Bebani CPU
        x = i * i * i

        # Alokasi memori bertahap (1 MB)
        data.append("X" * 1024 * 1024)

        print(f"Iterasi: {i} | Memori terpakai: {len(data)} MB")
        time.sleep(0.1)

except MemoryError:
    print("ERROR: Memori tidak mencukupi!")

except Exception as e:
    print("Program dihentikan:", e)
```
dockerfile
```
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```
membuat dockerfile build 
```
docker build -t week13-resource-limit .
```
menjalankan container tanpa limir
``` 
docker run --rm week13-resource-limit .
```
menjalankan container dengan limit
```
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```


---

## Hasil Eksekusi
build
![hasil](<screenshots/build container.PNG>)
container limit
![hasil](<screenshots/container limit.PNG>)
container tanpa limit
![hasil](<screenshots/container tanpa limit.PNG>)
monitoring sederhana
![hasil](<screenshots/monitoring sederhana.PNG>)
---

## Catatan output tanpa limit dan limit
tanpa limit
```
=== UJI RESOURCE LIMIT DOCKER ===
Iterasi: 1 | Memori terpakai: 1 MB
Iterasi: 2 | Memori terpakai: 2 MB
Iterasi: 3 | Memori terpakai: 3 MB
Iterasi: 4 | Memori terpakai: 4 MB
Iterasi: 5 | Memori terpakai: 5 MB
Iterasi: 6 | Memori terpakai: 6 MB
Iterasi: 7 | Memori terpakai: 7 MB
Iterasi: 8 | Memori terpakai: 8 MB
Iterasi: 120 | Memori terpakai: 120 MB
Iterasi: 121 | Memori terpakai: 121 MB
```
(Setiap iterasi menambah ±1 MB memori dan membebani CPU)

dengan limit



```
=== UJI RESOURCE LIMIT DOCKER ===
Iterasi: 1 | Memori terpakai: 1 MB
Iterasi: 2 | Memori terpakai: 2 MB
Iterasi: 3 | Memori terpakai: 3 MB
Iterasi: 4 | Memori terpakai: 4 MB
Iterasi: 5 | Memori terpakai: 5 MB
...
Iterasi: 120 | Memori terpakai: 120 MB
Iterasi: 256 | Memori terpakai: 256 MB
```

Setiap iterasi menambah ±1 MB memori.

Saat mendekati 256 MB, container dihentikan secara paksa oleh Docker.

Program tidak sempat menangkap MemoryError Python.


---

## Kesimpulan
Docker memungkinkan pembatasan CPU dan memori pada container sehingga penggunaan resource dapat dikontrol dengan baik.

Container tanpa limit resource dapat menggunakan memori dan CPU secara bebas, sedangkan container dengan limit akan melambat atau dihentikan jika melebihi batas.

Pembatasan resource sangat penting untuk menjaga stabilitas sistem, terutama saat menjalankan banyak container secara bersamaan.

---

## Tugas Dan Quiz
### Tugas
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa container perlu dibatasi CPU dan memori?

Container perlu dibatasi CPU dan memori agar tidak menghabiskan seluruh resource sistem. Pembatasan ini mencegah aplikasi yang boros resource mengganggu aplikasi lain serta menjaga kestabilan dan performa sistem host.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?

Virtual Machine (VM) memiliki sistem operasi sendiri dan menggunakan hypervisor sehingga lebih berat namun isolasinya lebih kuat. Container hanya mengisolasi aplikasi dan dependensinya serta berbagi kernel dengan host, sehingga lebih ringan dan efisien dalam penggunaan resource.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?

Aplikasi yang boros memori akan dihentikan secara paksa oleh Docker ketika penggunaan memori melebihi batas yang ditentukan. Biasanya aplikasi tidak sempat menangani error karena container langsung dimatikan oleh sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
