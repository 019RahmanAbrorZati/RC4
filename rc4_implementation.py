# ==========================================
# Implementasi Algoritma RC4 (Stream Cipher)
# ==========================================

def KSA(key):
    """
    Langkah 1: Key-Scheduling Algorithm (KSA)
    """
    print("\n--- Langkah 1: Key-Scheduling Algorithm (KSA) ---")
    key_length = len(key)
    S = list(range(256))
    j = 0
    
    print("Proses mengacak S-box:")
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        
        # Tambahan: Print nilai i dan j SEBELUM ditukar (dibatasi 5 putaran awal)
        if i < 5:
            print(f" Putaran ke-{i}: (i)={i}, (j)={j} --> Menukar isi S[{i}] dan S[{j}]")
            
        S[i], S[j] = S[j], S[i] # Swap nilai
        
    print(" ... (proses pengacakan berlanjut berulang-ulang sampai putaran ke-255) ...")
    print("[+] S-box berhasil diinisialisasi dan diacak penuh.")
    return S

def PRGA(S, text_length):
    """
    Langkah 2: Pseudo-Random Generation Algorithm (PRGA)
    """
    print("\n--- Langkah 2: Pseudo-Random Generation Algorithm (PRGA) ---")
    i = 0
    j = 0
    keystream = []
    
    print("Proses mengambil angka acak untuk dijadikan Keystream:")
    for step in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] # Swap nilai
        
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
        
        # Tambahan: Print pergerakan i, j, dan hasil Keystream yang didapat
        print(f" Ambil ke-{step+1}: i={i:3}, j={j:3} -> Menghasilkan Keystream (K) = {K}")
        
    print(f"\n[+] Keseluruhan Keystream yang didapat: {keystream}")
    return keystream

def proses_rc4(text, key, is_encrypt=True):
    """
    Fungsi utama untuk menggabungkan KSA, PRGA, dan proses XOR.
    Karena RC4 adalah symmetric stream cipher, proses enkripsi dan dekripsi menggunakan logika yang SAMA PERSIS.
    """
    mode = "ENKRIPSI" if is_encrypt else "DEKRIPSI"
    print(f"\n========== MEMULAI PROSES {mode} ==========")
    
    # Konversi kunci ke bentuk list of integer (berdasarkan nilai ASCII)
    key_bytes = [ord(c) for c in key]
    
    # Penyesuaian input teks berdasarkan mode
    if is_encrypt:
        # Jika enkripsi, ubah string plaintext menjadi list of integer (ASCII)
        text_bytes = [ord(c) for c in text]
        print(f"Input Plaintext       : '{text}'")
        print(f"Plaintext (Byte)      : {text_bytes}")
    else:
        # Jika dekripsi, input sudah berbentuk list of integer (ciphertext)
        text_bytes = text
        print(f"Input Ciphertext (Byte): {text_bytes}")

    print(f"Kunci Rahasia         : '{key}'")

    # Jalankan KSA untuk mendapatkan S-box yang teracak
    S = KSA(key_bytes)
    
    # Jalankan PRGA untuk mendapatkan Keystream
    keystream = PRGA(S, len(text_bytes))
    
    # Langkah 3: Operasi XOR antara Teks dan Keystream
    print(f"\n--- Langkah 3: Proses XOR ({mode}) ---")
    result_bytes = []
    
    for i in range(len(text_bytes)):
        # Operasi bitwise XOR (^)
        xor_val = text_bytes[i] ^ keystream[i]
        result_bytes.append(xor_val)
        
        if is_encrypt:
            print(f"Byte-{i+1}: Plaintext({text_bytes[i]:3}) XOR Keystream({keystream[i]:3}) = Ciphertext({xor_val:3})")
        else:
            print(f"Byte-{i+1}: Ciphertext({text_bytes[i]:3}) XOR Keystream({keystream[i]:3}) = Plaintext({xor_val:3}) -> '{chr(xor_val)}'")

    # Menampilkan hasil akhir
    if is_encrypt:
        # Hasil enkripsi ditampilkan dalam format Hexadecimal agar rapi
        hex_result = ''.join([f"{b:02X}" for b in result_bytes])
        print(f"\n[HASIL] Ciphertext (Hex) : {hex_result}")
        return result_bytes # Dikembalikan dalam bentuk byte array untuk dites dekripsi
    else:
        # Hasil dekripsi dikembalikan ke bentuk teks asli (string)
        original_text = ''.join([chr(b) for b in result_bytes])
        print(f"\n[HASIL] Plaintext Asli   : {original_text}")
        return original_text

# ==========================================
# Blok Eksekusi Utama
# ==========================================
if __name__ == "__main__":
    print("=== DEMONSTRASI ALGORITMA RC4 ===")
    
    # Data Uji Coba
    pesan_rahasia = "KriptoUNESA"
    kunci = "KunciAman123"
    
    # 1. Proses Enkripsi
    ciphertext_bytes = proses_rc4(pesan_rahasia, kunci, is_encrypt=True)
    
    print("\n" + "="*50)
    
    # 2. Proses Dekripsi
    # Memasukkan hasil enkripsi (ciphertext_bytes) dan kunci yang sama
    plaintext_hasil = proses_rc4(ciphertext_bytes, kunci, is_encrypt=False)