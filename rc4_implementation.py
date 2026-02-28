# ==========================================
# TUGAS KEAMANAN DATA DAN INFORMASI
# Implementasi Algoritma RC4 (Stream Cipher)
# Nama : Rahman Abror Zati
# NIM  : 24051204019
# ==========================================

def KSA(key):
    """
    Langkah 1: Key-Scheduling Algorithm (KSA)
    Fungsi ini menginisialisasi array S-box dan mengacaknya secara matematis 
    berdasarkan kunci rahasia yang diberikan.
    
    Parameter:
        key (list): Kunci rahasia yang sudah dikonversi menjadi list nilai ASCII.
    Return:
        list: Array S (S-box) berukuran 256 byte yang sudah teracak.
    """
    print("\n--- Langkah 1: Key-Scheduling Algorithm (KSA) ---")
    key_length = len(key)
    
    # Inisialisasi array S berurutan dari 0 hingga 255
    S = list(range(256))
    j = 0
    
    print("Proses mengacak S-box (menampilkan 5 iterasi awal):")
    for i in range(256):
        # Rumus Matematis: j = (j + S[i] + key[i mod key_length]) mod 256
        j = (j + S[i] + key[i % key_length]) % 256
        
        # Demonstrasi visual pergerakan index i dan j
        if i < 5:
            print(f" Putaran ke-{i}: (i)={i}, (j)={j} --> Menukar isi S[{i}] dan S[{j}]")
            
        # Proses penukaran nilai (Swap)
        S[i], S[j] = S[j], S[i] 
        
    print(" ... (proses pengacakan berlanjut hingga putaran ke-255) ...")
    print("[+] S-box berhasil diinisialisasi dan diacak penuh.")
    return S

def PRGA(S, text_length):
    """
    Langkah 2: Pseudo-Random Generation Algorithm (PRGA)
    Fungsi ini membangkitkan aliran kunci acak (Keystream) yang panjangnya 
    disesuaikan dengan panjang teks yang akan diproses.
    
    Parameter:
        S (list): S-box yang sudah diacak dari tahap KSA.
        text_length (int): Panjang karakter/byte dari teks pesan.
    Return:
        list: Kumpulan angka acak (Keystream) untuk di-XOR dengan teks.
    """
    print("\n--- Langkah 2: Pseudo-Random Generation Algorithm (PRGA) ---")
    i = 0
    j = 0
    keystream = []
    
    print("Proses mengambil angka acak untuk dijadikan Keystream:")
    for step in range(text_length):
        # Rumus Matematis pergerakan pointer:
        # i = (i + 1) mod 256
        # j = (j + S[i]) mod 256
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        # Penukaran nilai lanjutan (Swap)
        S[i], S[j] = S[j], S[i] 
        
        # Rumus Matematis ekstraksi Keystream (K):
        # K = S[(S[i] + S[j]) mod 256]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
        
        # Demonstrasi visual pengambilan Keystream
        print(f" Ambil ke-{step+1}: i={i:3}, j={j:3} -> Menghasilkan Keystream (K) = {K}")
        
    print(f"\n[+] Keseluruhan Keystream yang didapat: {keystream}")
    return keystream

def proses_rc4(text, key, is_encrypt=True):
    """
    Fungsi Utama RC4 yang menggabungkan KSA, PRGA, dan operasi XOR.
    Sifat Stream Cipher: Fungsi Enkripsi dan Dekripsi adalah identik (simetris).
    """
    mode = "ENKRIPSI" if is_encrypt else "DEKRIPSI"
    print(f"\n========== MEMULAI PROSES {mode} ==========")
    
    # 1. Konversi kunci string menjadi list of integer (ASCII)
    key_bytes = [ord(c) for c in key]
    
    # Penyesuaian input berdasarkan mode (Enkripsi butuh konversi ASCII, Dekripsi tidak)
    if is_encrypt:
        text_bytes = [ord(c) for c in text]
        print(f"Input Plaintext       : '{text}'")
        print(f"Plaintext (Byte)      : {text_bytes}")
    else:
        text_bytes = text
        print(f"Input Ciphertext (Byte): {text_bytes}")

    print(f"Kunci Rahasia         : '{key}'")

    # 2. Eksekusi KSA untuk mendapatkan S-box
    S = KSA(key_bytes)
    
    # 3. Eksekusi PRGA untuk mendapatkan Keystream
    keystream = PRGA(S, len(text_bytes))
    
    # 4. Langkah 3: Operasi Logika XOR
    print(f"\n--- Langkah 3: Proses XOR ({mode}) ---")
    result_bytes = []
    
    for i in range(len(text_bytes)):
        # Operasi bitwise XOR dilambangkan dengan operator (^) di Python
        # Rumus: Ciphertext = Plaintext XOR Keystream (dan sebaliknya)
        xor_val = text_bytes[i] ^ keystream[i]
        result_bytes.append(xor_val)
        
        # Cetak pembuktian matematis ke terminal
        if is_encrypt:
            print(f"Byte-{i+1}: Plaintext({text_bytes[i]:3}) XOR Keystream({keystream[i]:3}) = Ciphertext({xor_val:3})")
        else:
            print(f"Byte-{i+1}: Ciphertext({text_bytes[i]:3}) XOR Keystream({keystream[i]:3}) = Plaintext({xor_val:3}) -> '{chr(xor_val)}'")

    # 5. Pengembalian Hasil Akhir
    if is_encrypt:
        # Format Hexadecimal agar hasil enkripsi rapi saat dicetak
        hex_result = ''.join([f"{b:02X}" for b in result_bytes])
        print(f"\n[HASIL] Ciphertext (Hex) : {hex_result}")
        return result_bytes 
    else:
        # Konversi kembali array byte menjadi karakter string (Plaintext asli)
        original_text = ''.join([chr(b) for b in result_bytes])
        print(f"\n[HASIL] Plaintext Asli   : {original_text}")
        return original_text

# ==========================================
# Blok Eksekusi Utama
# ==========================================
if __name__ == "__main__":
    print("=== DEMONSTRASI ALGORITMA RC4 ===")
    
    # Data Uji Coba (Bisa diganti sesuai kebutuhan)
    pesan_rahasia = "KriptoUNESA"
    kunci = "KunciAman123"
    
    # Skenario 1: Proses Enkripsi
    ciphertext_bytes = proses_rc4(pesan_rahasia, kunci, is_encrypt=True)
    
    print("\n" + "="*60)
    
    # Skenario 2: Proses Dekripsi (Membuktikan pesan kembali utuh)
    plaintext_hasil = proses_rc4(ciphertext_bytes, kunci, is_encrypt=False)