import seaborn as sns
import matplotlib.pyplot as plt

# 1. Mengambil model data 'iris' yang sudah tersedia di library
data_iris = sns.load_dataset('iris')

# 2. Menampilkan 5 data teratas untuk memahami struktur kolomnya
print(data_iris.head())

# 3. Visualisasi Scatter Plot untuk mencari insight antar spesies
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data_iris)

# 4. Menambahkan judul dan label
plt.title('Hubungan Panjang vs Lebar Sepal Berdasarkan Spesies')
plt.xlabel('Panjang Sepal (cm)')
plt.ylabel('Lebar Sepal (cm)')

# 5. Menampilkan Plot
plt.show()