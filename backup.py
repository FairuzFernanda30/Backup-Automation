# project backup automation + pc health check
# import library (library yang digunakan)
import os
import shutil
import datetime
import subprocess
from pathlib import Path

# Konfigurasi (configuration)
SOURCE_DIR = "source"
DEST_DIR = "backup_destination"
LOG_DIR = "logs"

def safe_print(message):
    """Mencetak pesan dengan aman tanpa menyebabkan UnicodeEncodeError di Windows."""
    try:
        print(message)
    except UnicodeEncodeError:
        clean_msg = (
            message.replace("✅", "[OK]")
            .replace("❌", "[ERROR]")
            .replace("🔄", "[START]")
            .replace("📝", "[LOG]")
            .replace("📊", "[INFO]")
            .replace("⚠️", "[WARN]")
        )
        try:
            print(clean_msg)
        except Exception:
            print(message.encode('ascii', errors='replace').decode('ascii'))

def setup_directories():
    """Pastikan folder yang diperlukan ada."""
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    safe_print("✅ Direktori siap.")

def generate_pc_health_report():
    """Mengambil output dari script PC Health Check sebelumnya dan menyimpannya di folder source."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pc_health_dir = os.path.abspath(os.path.join(base_dir, "..", "05_ PC Health Check using Python"))
    pc_health_script = os.path.join(pc_health_dir, "pc_health.py")
    
    if os.path.exists(pc_health_script):
        safe_print("📊 Menghubungkan ke proyek PC Health Check untuk mengambil laporan...")
        try:
            # Jalankan pc_health.py dan ambil output cetaknya (stdout)
            result = subprocess.run(
                ["python", "pc_health.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
                cwd=pc_health_dir
            )
            
            # Tentukan path file target di dalam folder source
            report_file = os.path.join(SOURCE_DIR, "pc_health_report.txt")
            
            # Tulis output laporan ke file (menghapus baris terakhir penyimpanan log lokal pc_health agar rapi)
            report_lines = result.stdout.splitlines()
            clean_lines = [line for line in report_lines if not line.startswith("[SAVED]")]
            
            with open(report_file, "w", encoding="utf-8") as f:
                f.write("\n".join(clean_lines) + "\n")
                
            safe_print(f"✅ Laporan kesehatan PC berhasil dibuat di: {report_file}")
            return True
        except Exception as e:
            safe_print(f"⚠️ Gagal menjalankan PC Health Check: {e}")
            return False
    else:
        safe_print("⚠️ Script PC Health Check tidak ditemukan di folder proyek sebelah.")
        return False

def copy_files(src, dst):
    """Copy file/folder dari src ke dst."""
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)
        return True
    except Exception as e:
        safe_print(f"❌ Gagal copy {src}: {e}")
        return False

def write_log(message):
    """Tulis pesan ke file log."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file = os.path.join(LOG_DIR, f"backup_log_{datetime.datetime.now().strftime('%Y%m%d')}.txt")
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
    
    safe_print(f"📝 {message}")

def backup():
    """Fungsi utama backup."""
    safe_print("="*50)
    safe_print("🔄 MULAI BACKUP")
    safe_print(f"Waktu: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    safe_print(f"Source: {SOURCE_DIR}")
    safe_print(f"Destination: {DEST_DIR}")
    safe_print("-"*50)
    
    # Buat folder backup dengan timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(DEST_DIR, f"backup_{timestamp}")
    
    # Copy file/folder
    success = copy_files(SOURCE_DIR, backup_folder)
    
    if success:
        message = f"✅ Backup berhasil! Disimpan di: {backup_folder}"
        safe_print(message)
        write_log(message)
    else:
        message = f"❌ Backup gagal!"
        safe_print(message)
        write_log(message)
    
    safe_print("="*50)

def main():
    setup_directories()
    generate_pc_health_report()
    backup()

if __name__ == "__main__":
    main()