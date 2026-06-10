# Backup Automation with PC Health Check Integration

A Python-based local backup automation project designed to secure files periodically, featuring automatic system health check integration (PC Health Check) before starting the backup process.

## 🌟 Key Features

1. **Folder Backup Automation**: Copies data systematically from the source directory (`source/`) to the destination directory (`backup_destination/`).
2. **Timestamp-based Backup**: Saves each backup run in a new directory with a unique date-and-time suffix (e.g., `backup_YYYYMMDD_HHMMSS`) to prevent overwriting past backups.
3. **PC Health Check Integration**: Before copying files, the script automatically executes the `pc_health.py` diagnostic script from the sibling directory, captures system specifications/metrics (CPU, RAM, GPU, Storage, Uptime, Battery), and saves it as `pc_health_report.txt` inside the backup folder.
4. **Logging System**: Logs backup execution history and status in daily log files under the `logs/` directory for ease of auditing.
5. **Windows Safe Printing (Unicode Error Prevention)**: Features a custom `safe_print` printer utility to handle system console encoding constraints, preventing potential emoji encoding crashes on Windows CMD or PowerShell.

---

## 📁 Project Directory Structure

```text
📁 backup-automation/
   ├── backup.py              # Main script (clean production code)
   ├── backuphint.py          # Instructional script with line-by-line comments
   ├── requirements.txt       # Dependency configuration (runs on standard libraries only)
   ├── .gitignore             # Git ignore configuration
   ├── 📁 source/             # Source directory to back up (example)
   │   └── pc_health_report.txt
   ├── 📁 backup_destination/ # Destination directory for backups
   ├── 📁 logs/               # Folder storing daily execution logs
   └── README.md              # Project documentation
```

---

## 🚀 How to Run

### Prerequisites
- **Python**: Version 3.8 or above.
- **Third-Party Libraries** (if running the PC diagnostic feature):
  The `psutil` library must be installed on your system to collect computer hardware statistics.
  ```bash
  pip install psutil
  ```

### Running the Program
Execute the main script from your terminal/PowerShell in the project folder:
```bash
python backup.py
```

### Outputs Generated
1. The system report `pc_health_report.txt` is created under `source/`.
2. A new timestamped backup directory is created under `backup_destination/`.
3. Execution activities are recorded in the `logs/` folder.

---

## 🔧 Customization
You can easily customize the source, destination, and log directory names directly in the **Configuration** block at the beginning of `backup.py`:
```python
# Configuration (Konfigurasi)
SOURCE_DIR = "source"
DEST_DIR = "backup_destination"
LOG_DIR = "logs"
```

---

## 📷 Output & Screenshot Demos

### 1. Terminal Run & Log Output (Example)
```text
[OK] Setup directories completed.
[INFO] Connecting to PC Health Check project to gather reports...
[OK] PC Health report successfully created at: source\pc_health_report.txt
==================================================
[START] RUNNING BACKUP
Time: 2026-06-10 19:00:20
Source: source
Destination: backup_destination
--------------------------------------------------
[OK] Backup completed! Saved at: backup_destination\backup_20260610_190020
[LOG] [OK] Backup completed! Saved at: backup_destination\backup_20260610_190020
==================================================
```

### 2. Generated PC Health Report (Example)
```text
==================================================
PC HEALTH CHECK REPORT
==================================================
Waktu: 2026-06-10 19:00:18
Komputer: LAPTOP-xxxxxxxx
Sistem: Windows 11
--------------------------------------------------
CPU usage: 7.0%
RAM usage: 73.4% (11 GB / 15 GB)
Storage usage: 97.3%
Disk usage: 97.3% (Free: 4 GB / Total 181 GB)
Uptime: 3 days, 2 hours, 10 minutes
--------------------------------------------------
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
GPU Temp: 47 C
--------------------------------------------------
Battery Status: 80% (Charging (AC))
Battery Time Left: Connected to AC Power
==================================================
Health check completed!
```

<br>
<hr>
<br>

# Otomatisasi Backup dengan Integrasi PC Health Check (Bahasa Indonesia)

Proyek otomatisasi backup lokal berbasis Python yang dirancang untuk mengamankan data secara berkala, dilengkapi dengan integrasi laporan kesehatan sistem (PC Health Check) secara otomatis sebelum proses backup dimulai.

## 🌟 Fitur Utama

1. **Otomatisasi Backup Folder**: Menyalin data secara terstruktur dari folder sumber (`source/`) ke folder tujuan (`backup_destination/`).
2. **Backup Berbasis Timestamp**: Setiap hasil backup disimpan di folder baru dengan label tanggal dan waktu yang unik (misal: `backup_YYYYMMDD_HHMMSS`) sehingga tidak menimpa data backup sebelumnya.
3. **Integrasi PC Health Check**: Sebelum menyalin file, script ini secara otomatis memanggil program diagnostic `pc_health.py` dari proyek sebelah, menangkap output data spesifikasi/utilitas komputer (CPU, RAM, GPU, Storage, Uptime, Baterai), dan menyimpannya sebagai berkas `pc_health_report.txt` di dalam folder backup.
4. **Sistem Logging**: Mencatat riwayat dan status eksekusi backup ke dalam berkas log harian di folder `logs/` untuk kemudahan pelacakan (*audit trail*).
5. **Aman dari Unicode Error (Windows)**: Dilengkapi dengan mekanisme cetak `safe_print` guna mengantisipasi *crash* akibat kesalahan encoding emoji pada konsol terminal Windows (CMD/PowerShell).

---

## 📁 Struktur Direktori Proyek

```text
📁 backup-automation/
   ├── backup.py              # Script utama (kode bersih untuk produksi/running)
   ├── backuphint.py          # Script dengan panduan penjelasan kode detail baris-per-baris
   ├── requirements.txt       # Daftar library dependensi (hanya menggunakan modul bawaan standard library)
   ├── .gitignore             # Konfigurasi file yang diabaikan oleh Git
   ├── 📁 source/             # Folder sumber yang akan di-backup (contoh)
   │   └── pc_health_report.txt
   ├── 📁 backup_destination/ # Folder tujuan penyimpanan hasil backup
   ├── 📁 logs/               # Folder penyimpanan log aktivitas harian
   └── README.md              # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan

### Prasyarat
- **Python**: Versi 3.8 ke atas.
- **Pustaka Pihak Ketiga** (jika menjalankan fitur diagnostic PC):
  Pustaka `psutil` harus terinstall di sistem agar script PC Health Check dapat mengambil metrik sistem secara akurat.
  ```bash
  pip install psutil
  ```

### Menjalankan Program
Jalankan script utama melalui terminal/PowerShell di direktori proyek:
```bash
python backup.py
```

### Output yang Dihasilkan
1. Berkas laporan sistem `pc_health_report.txt` akan dibuat di dalam folder `source/`.
2. Folder backup baru dengan stempel waktu dibuat di `backup_destination/`.
3. Aktivitas backup dicatat di dalam folder `logs/`.

---

## 🔧 Kustomisasi
Anda dapat menyesuaikan nama folder sumber, tujuan, dan log secara langsung pada blok **Konfigurasi** di bagian awal berkas `backup.py`:
```python
# Konfigurasi (configuration)
SOURCE_DIR = "source"
DEST_DIR = "backup_destination"
LOG_DIR = "logs"
```

---

## 📷 Demo Output & Tangkapan Layar

### 1. Eksekusi Terminal & Output Log (Contoh)
```text
[OK] Setup directories completed.
[INFO] Connecting to PC Health Check project to gather reports...
[OK] PC Health report successfully created at: source\pc_health_report.txt
==================================================
[START] RUNNING BACKUP
Time: 2026-06-10 19:00:20
Source: source
Destination: backup_destination
--------------------------------------------------
[OK] Backup completed! Saved at: backup_destination\backup_20260610_190020
[LOG] [OK] Backup completed! Saved at: backup_destination\backup_20260610_190020
==================================================
```

### 2. Berkas Laporan PC Health yang Dihasilkan (Contoh)
```text
==================================================
PC HEALTH CHECK REPORT
==================================================
Waktu: 2026-06-10 19:00:18
Komputer: LAPTOP-xxxxxxxx
Sistem: Windows 11
--------------------------------------------------
CPU usage: 7.0%
RAM usage: 73.4% (11 GB / 15 GB)
Storage usage: 97.3%
Disk usage: 97.3% (Free: 4 GB / Total 181 GB)
Uptime: 3 hari, 2 jam, 10 menit
--------------------------------------------------
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Suhu GPU: 47 C
--------------------------------------------------
Status Baterai: 80% (Di-charge (AC))
Sisa Waktu Baterai: Tersambung ke daya AC
==================================================
Health check selesai!
```

---

## 👤 Author
**Fairuz Fernanda**
* GitHub: [@FairuzFernanda30](https://github.com/FairuzFernanda30)

### 🔗 Other Projects
- **[PC Health Check Utility](https://github.com/FairuzFernanda30/PC-Health-Check-using-Python)**
- **[Web Scraper - Books to Scrape](https://github.com/FairuzFernanda30/Web-Scraper)**
- **[Excel Auto Cleaner Formatter](https://github.com/FairuzFernanda30/excel-cleaner)**
- **[PDF to Excel Extractor](https://github.com/FairuzFernanda30/pdf-to-excel-extractor)**
- **[Customer Churn Prediction](https://github.com/FairuzFernanda30/churn-app)**