# 🚨 BUG REPORT & UPDATE INSTRUKSI BRIDGE 0.1 BRN 🚨

## ⚠️ Bug Ditemukan: Hex Berubah-ubah
Harap diperhatikan, terdapat bug di mana hex berubah-ubah secara acak. Selain itu, untuk menerima hadiah BRN, Anda **harus melakukan bridge minimal 0.1**. Jika di bawah 0.1, **tidak akan mendapatkan hadiah BRN**.

### 📝 Instruksi Langkah Demi Langkah:
Ikuti langkah-langkah berikut ini untuk mengatasi masalah tersebut.

---

### 1. Lakukan Bridge Manual (Contoh: Arbitrum ke Optimism)

Pastikan Anda melakukan bridge sebesar **0.1** dari jaringan **Arbitrum** ke **Optimism**.

![Bridge Example](https://github.com/user-attachments/assets/229a4247-5c49-41e3-8413-9587f84f207e)

---

### 2. Tunggu Hingga Transaksi Selesai

Pastikan transaksi berhasil diproses dan selesai.

![Transaction Complete](https://github.com/user-attachments/assets/7fa60b48-633d-4961-8b17-0e99b831df06)

---

### 3. Buka Detail Transaksi

Klik pada **Transaction Detail** untuk melihat lebih detail transaksi yang Anda lakukan.

![Transaction Detail](https://github.com/user-attachments/assets/f44fd8d2-242a-4d3e-b60f-45e2927c3cbb)

---

### 4. Temukan Transaction HASH

Di bagian bawah dari detail transaksi, Anda akan melihat **Transaction HASH**. Klik pada **Transaction HASH** untuk membuka di explorer.

**More Details:**
Click to show more

---

### 5. Cek Input Data di Explorer

Pada halaman explorer, cari bagian **Input Data**. Ubah tampilan **View Input AS** ke **ORIGINAL**. Salin seluruh data tersebut dengan cara klik dua kali pada datanya.

![Input Data Example](https://github.com/user-attachments/assets/c4210314-6720-48af-beb5-266ac814532b)

---

### 6. Edit File arbit-op.py

- Buka file **arbit-op.py** di editor teks.
- Temukan bagian **data** (Data transaksi untuk bridge).
- Hapus data default dan gantikan dengan data baru yang sudah Anda copy dari hasil **Transaction HASH** tadi.
- Simpan perubahan.

---

### 7. Jalankan Script

Setelah data diperbarui, jalankan script dengan perintah berikut:

```bash
python arbit-op.py
```

---

✅ **Selesai!** Anda telah berhasil memperbarui data dan menyelesaikan proses bridge. Pastikan untuk mengikuti instruksi ini dengan benar agar bisa mendapatkan hadiah BRN.

---

Semoga berhasil! Jika ada pertanyaan atau masalah, jangan ragu untuk menghubungi tim support.

---
