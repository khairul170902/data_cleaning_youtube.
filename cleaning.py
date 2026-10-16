import pandas as pd

# 1. Load dataset (sesuaikan letak foldernya di dalam folder 'archive')
df = pd.read_csv('archive/data_youtube.csv')

print('--- 5 Data Pertama ---')
print(df.head())

print('\n--- Informasi Dataset (Cek Tipe Data & Missing Value) ---')
print(df.info())

# 2. Cek jumlah data yang kosong (Missing Values)
print('\n--- Jumlah Data Kosong per Kolom ---')
print(df.isnull().sum())

# 3. Data Cleaning: Menghapus baris yang duplikat (jika ada)
initial_rows = len(df)
df = df.drop_duplicates()
print(f'\nJumlah baris duplikat yang dihapus: {initial_rows - len(df)}')

# 4. Simpan hasil cleaning ke file CSV baru di luar folder archive (biar gampang di-upload)
df.to_csv('cleaned_data_youtube.csv', index=False)
print(
    "\nSukses! Data bersih disimpan dengan nama 'cleaned_data_youtube.csv'."
)