# 📱 INAKu Portal - Mobile Automation Testing

Automated testing untuk aplikasi **INAKu Portal Layanan Publik** menggunakan **Appium + Pytest** dengan **Page Object Model (POM)** pattern.

---

## 📋 Daftar Isi

- [Prasyarat](#-prasyarat)
- [Instalasi](#-instalasi)
- [Menjalankan Appium Server](#-menjalankan-appium-server)
- [Menjalankan Test](#-menjalankan-test)
- [Generate Allure Report](#-generate-allure-report)
- [Membuka Allure Report](#-membuka-allure-report)
- [Struktur Project](#-struktur-project)
- [Test Cases](#-test-cases)

---

## 🔧 Prasyarat

Pastikan tools berikut sudah terinstal:

| No | Tools                | Versi Minimum  | Cek Versi                    |
|----|----------------------|----------------|------------------------------|
| 1  | Python               | 3.10+          | `python --version`         |
| 2  | Node.js              | 18+            | `node --version`           |
| 3  | Java JDK             | 11+            | `java -version`            |
| 4  | Android SDK          | -              | `adb --version`            |
| 5  | Appium               | 2.x            | `appium --version`         |
| 6  | Appium UiAutomator2  | -              | `appium driver list`       |
| 7  | Allure Commandline   | 2.x            | `allure --version`         |

### Instalasi Appium & Driver

```bash
npm install -g appium
appium driver install uiautomator2
```

### Instalasi Allure (Windows)

```bash
# Menggunakan Scoop
scoop install allure

# Atau menggunakan Chocolatey
choco install allure-commandline
```

---

## 📦 Instalasi

1. **Clone repository**

```bash
git clone https://github.com/WibbyRamdhani/inakuportal.git
cd inakuportal
```

2. **Buat virtual environment**

```bash
python -m venv venv
```

3. **Aktifkan virtual environment**

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Appium Server

Pastikan **device Android** (emulator/real device) sudah terhubung:

```bash
# Cek device yang terhubung
adb devices
```

Jalankan Appium Server:

```bash
appium
```

> Appium akan berjalan di `http://127.0.0.1:4723` secara default.

---

## 🧪 Menjalankan Test

### Jalankan semua test

```bash
pytest --alluredir=allure-results
```

### Jalankan test tertentu (per file)

```bash
pytest tests/test_login.py --alluredir=allure-results
pytest tests/test_beranda_login.py --alluredir=allure-results
pytest tests/test_bpjs.py --alluredir=allure-results
```

### Jalankan test tertentu (per function)

```bash
pytest tests/test_login.py::TestLogin::test_login_valid --alluredir=allure-results
```

### Jalankan dengan output verbose

```bash
pytest -v --alluredir=allure-results
```

> **Catatan:** Flag `--alluredir=allure-results` wajib ditambahkan agar hasil test tersimpan untuk Allure Report.

---

## 📊 Generate Allure Report

Setelah menjalankan test, generate report HTML dari hasil test:

```bash
allure generate allure-results --clean -o allure-report
```

**Penjelasan flag:**
- `allure-results` → Folder sumber data hasil test
- `--clean` → Hapus report lama sebelum generate yang baru
- `-o allure-report` → Output folder untuk report HTML

---

## 🌐 Membuka Allure Report

### Cara 1: `allure open` (Rekomendasi)

Buka report yang sudah di-generate:

```bash
allure open allure-report
```

Report akan otomatis terbuka di browser default.

### Cara 2: `allure serve` (Langsung dari Results)

Generate + buka report sekaligus tanpa perlu `allure generate` terlebih dahulu:

```bash
allure serve allure-results
```

> Cara ini paling praktis karena langsung generate dan membuka report di browser dalam satu perintah.

### Cara 3: Python HTTP Server (Alternatif)

Jika `allure` CLI tidak tersedia:

```bash
cd allure-report
python -m http.server 8080
```

Lalu buka `http://localhost:8080` di browser.

> ⚠️ **Jangan buka** `allure-report/index.html` langsung dengan double-click karena akan error (butuh web server).

---

## 📁 Struktur Project

```
inakuportal/
├── config/
│   └── capabilities.py          # Konfigurasi Appium capabilities
├── page/                        # Page Object Model
│   ├── base_page.py             # Base class untuk semua page
│   ├── beranda_page.py          # Halaman Beranda
│   ├── bpjs_page.py             # Halaman Cek BPJS
│   ├── bpom_page.py             # Halaman Cari BPOM
│   ├── cari_dokter_page.py      # Halaman Cari Dokter
│   ├── cek_bansos_page.py       # Halaman Cek Bansos
│   ├── detail_layanan_page.py   # Halaman Detail Layanan
│   ├── faskes_page.py           # Halaman Cari Faskes
│   ├── footer_component.py      # Komponen Footer
│   ├── layanan_bantuan_page.py  # Halaman Layanan Bantuan
│   ├── layanan_page.py          # Halaman Layanan
│   ├── login_pages.py           # Halaman Login
│   ├── profil_page.py           # Halaman Profil
│   ├── registrasi_page.py       # Halaman Registrasi
│   ├── search_page.py           # Halaman Search
│   ├── sidebar_component.py     # Komponen Sidebar
│   └── skm_page.py              # Halaman SKM
├── tests/                       # Test Cases
│   ├── test_beranda_login.py    # Test beranda (logged in)
│   ├── test_beranda_nonlogin.py # Test beranda (non-login)
│   ├── test_bpjs.py             # Test cek BPJS
│   ├── test_cari_bpom.py        # Test cari BPOM
│   ├── test_cari_dokter.py      # Test cari dokter
│   ├── test_cari_faskes.py      # Test cari faskes
│   ├── test_cek_bansos.py       # Test cek bansos
│   ├── test_footer.py           # Test footer navigation
│   ├── test_layanan.py          # Test layanan
│   ├── test_layanan_bantuan.py  # Test layanan bantuan
│   ├── test_login.py            # Test login
│   ├── test_profil.py           # Test profil user
│   ├── test_registrasi.py       # Test registrasi
│   ├── test_search.py           # Test search
│   ├── test_sidebar.py          # Test sidebar
│   └── test_skm.py              # Test SKM
├── conftest.py                  # Pytest fixtures & Appium setup
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Python dependencies
└── .gitignore                   # Git ignore rules
```

---

## 📝 Test Cases

| Module             | File Test                    | Deskripsi                          |
|--------------------|------------------------------|------------------------------------|
| Login              | `test_login.py`            | Login valid & invalid              |
| Registrasi         | `test_registrasi.py`       | Registrasi akun baru               |
| Beranda (Login)    | `test_beranda_login.py`    | Fitur beranda saat sudah login     |
| Beranda (Non-Login)| `test_beranda_nonlogin.py` | Fitur beranda tanpa login          |
| Profil             | `test_profil.py`           | Manajemen profil user              |
| Layanan            | `test_layanan.py`          | Navigasi layanan                   |
| Layanan Bantuan    | `test_layanan_bantuan.py`  | Fitur layanan bantuan              |
| Search             | `test_search.py`           | Fitur pencarian                    |
| Sidebar            | `test_sidebar.py`          | Navigasi sidebar                   |
| Footer             | `test_footer.py`           | Navigasi footer                    |
| BPJS               | `test_bpjs.py`             | Cek kepesertaan BPJS               |
| BPOM               | `test_cari_bpom.py`        | Pencarian data BPOM                |
| Cari Dokter        | `test_cari_dokter.py`      | Pencarian dokter                   |
| Cari Faskes        | `test_cari_faskes.py`      | Pencarian fasilitas kesehatan      |
| Cek Bansos         | `test_cek_bansos.py`       | Cek bantuan sosial                 |
| SKM                | `test_skm.py`              | Survei Kepuasan Masyarakat         |

---

## ⚙️ Tech Stack

- **Python** 3.10+
- **Appium** 2.x + UiAutomator2
- **Pytest** 8.x
- **Allure Report** 2.x
- **Selenium** 4.x (Appium dependency)
