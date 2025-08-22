<div align="center">
  
# IMG-BYPASS

<div align="center">

![Build](https://img.shields.io/badge/build-stable-28a745?style=for-the-badge&logo=github)
![Platform](https://img.shields.io/badge/platform-Linux-0078D6?style=for-the-badge&logo=linux&logoColor=white)
![Last Commit](https://img.shields.io/github/last-commit/denoyey/Img-Bypass?style=for-the-badge&logo=git)
![Language](https://img.shields.io/github/languages/top/denoyey/Img-Bypass?style=for-the-badge&color=informational)
![Technologies](https://img.shields.io/badge/technologies-%20Python-yellow?style=for-the-badge&logo=terminal)
![Stars](https://img.shields.io/github/stars/denoyey/Img-Bypass?style=for-the-badge&color=ffac33&logo=github)
![Forks](https://img.shields.io/github/forks/denoyey/Img-Bypass?style=for-the-badge&color=blueviolet&logo=github)
![Issues](https://img.shields.io/github/issues/denoyey/Img-Bypass?style=for-the-badge&logo=github)
![Contributors](https://img.shields.io/github/contributors/denoyey/Img-Bypass?style=for-the-badge&color=9c27b0)

<br />

<img src="https://api.visitorbadge.io/api/VisitorHit?user=denoyey&repo=Img-Bypass&countColor=%237B1E7A&style=flat-square" alt="visitors"/>

</div>

</div>

## 📌 About

**Img-Bypass** adalah tool berbasis Python yang memungkinkan kamu untuk:

- 📥 Menyisipkan (embed) script PHP ke dalam metadata gambar JPG/JPEG
- 📤 Mengekstrak kembali script PHP dari file gambar
- 📁 Menyimpan hasil ke dalam direktori `output_img_bypass` secara otomatis

Tool ini cocok untuk keperluan _security testing_, _proof of concept_, atau _educational purposes only_.

## 🚀 Installation

### 🔧 Requirements

- Python 3.6+
- pip

### 🧪 Install modules (otomatis saat dijalankan)

```bash
pip install Pillow piexif --break-system-packages
```

💻 Clone this repo
```bash
git clone https://github.com/denoyey/Img-Bypass.git
cd Img-Bypass
python img_bypass.py
```

## 🕹️ Usage

### 📥 Embed PHP ke dalam Gambar
```bash
[1] Embed PHP
> Masukkan path ke file .jpg
> Masukkan path ke file .php
```
> Output akan disimpan ke dalam folder: `output_img_bypass/embedded_nama_gambar.jpg`

### 📤 Extract PHP dari Gambar
```bash
[2] Extract PHP
> Masukkan path ke file .jpg
```
> Output akan disimpan ke dalam folder: `output_img_bypass/extracted_nama_file.php`

## 📂 Output Folder
Semua hasil embedding & extraction otomatis disimpan di folder:
```bash
output_img_bypass/
├── embedded_image.jpg
└── extracted_code.php
```

## 🛑 Disclaimer
> Tool ini dibuat hanya untuk tujuan edukasi dan pengujian keamanan. <br>
> Segala bentuk penyalahgunaan bukan tanggung jawab saya.

## 🧑‍💻 Author
- **denoyey** - <a href="https://github.com/denoyey">Github</a>

## 📄 License
Licensed under the <a href="https://github.com/denoyey/Img-Bypass/blob/main/LICENSE">MIT License</a>
