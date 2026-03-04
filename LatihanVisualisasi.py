import pandas as pd
import matplotlib.pyplot as plt

# Pastikan file ini satu folder dengan script .py Anda
data = pd.read_csv("tips.csv")

# Fungsi value_counts() akan menghitung frekuensi setiap kategori
gender_counts = data['sex'].value_counts()

plt.figure(figsize=(8, 6))

# autopct='%1.1f%%' digunakan untuk menampilkan persentase secara otomatis
# startangle=140 memutar diagram agar tampilan lebih proporsional
plt.pie(gender_counts, 
        labels=gender_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['skyblue', 'lightpink'])

plt.title("Persentase Pemberi Tips Berdasarkan Jenis Kelamin")

plt.show()