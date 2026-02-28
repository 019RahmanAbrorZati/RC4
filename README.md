# Implementasi Algoritma RC4 (Stream Cipher) 🔐

Repositori ini berisi implementasi algoritma kriptografi **RC4 (Rivest Cipher 4)** menggunakan bahasa pemrograman Python murni (*from scratch*), tanpa menggunakan *library* kriptografi eksternal. 

Proyek ini dibuat untuk memenuhi tugas mata kuliah **Keamanan Data dan Informasi**.

## 👨‍💻 Identitas Pembuat
* **Nama:** Rahman Abror Zati
* **NIM:** 24051204019

## ⚙️ Fitur Program
Program ini mendemonstrasikan proses enkripsi dan dekripsi *stream cipher* RC4 dengan mencetak langkah-langkah detail ke terminal, meliputi:
1. **KSA (Key-Scheduling Algorithm):** Inisialisasi dan pengacakan *S-box* berdasarkan kunci rahasia (ditampilkan 5 iterasi awal untuk demonstrasi visual).
2. **PRGA (Pseudo-Random Generation Algorithm):** Pembangkitan *Keystream* secara dinamis.
3. **Proses XOR:** Operasi logika XOR antara teks asli (*Plaintext*) dengan *Keystream* untuk menghasilkan *Ciphertext*, serta proses sebaliknya untuk dekripsi.

## 🚀 Cara Menjalankan Program (Instruksi)
Pastikan Anda telah menginstal **Python 3.x** di perangkat Anda.

1. Buka terminal (Command Prompt / PowerShell / Terminal bawaan VS Code).
2. Arahkan direktori terminal ke folder tempat file ini berada.
3. Jalankan perintah berikut:
   ```bash
   python rc4_implementation.py