# 📊 Final Project Data Science: Prediksi GPA Mahasiswa

## 🧠 Introduction

Proyek ini merupakan bagian dari Final Project kelas **Data Science Beginner** di KSM Android UPN Veteran Jakarta.  
Kami membangun model machine learning untuk **memprediksi nilai GPA (Indeks Prestasi)** mahasiswa berdasarkan data kebiasaan, psikologi, dan performa akademik mereka.

Dataset yang digunakan diambil dari [**Kaggle**](https://www.kaggle.com/datasets/aryan208/student-habits-and-academic-performance-dataset), yang berisi informasi lengkap tentang faktor-faktor yang memengaruhi performa akademik mahasiswa.

---

## 🎯 Tujuan Proyek

✅ Melakukan **Exploratory Data Analysis (EDA)** terhadap data kebiasaan dan performa akademik mahasiswa  
✅ Membersihkan, memproses, dan menyiapkan data untuk regresi  
✅ Melatih dan mengevaluasi model machine learning menggunakan random forest  
✅ Membuat aplikasi interaktif dengan **Streamlit** untuk melakukan prediksi GPA secara real-time

---

## 📁 Deskripsi Dataset

- **Sumber**: [Student Habits and Academic Performance Dataset](https://www.kaggle.com/datasets/aryan208/student-habits-and-academic-performance-dataset)  
- **Jumlah Data**: 8000 baris × 31 kolom  
- **Jenis Tugas**: *Regresi*

Beberapa fitur yang dipilih setelah seleksi fitur :
- 'semester' Semester mahasiswa saat ini,
- "age": Umur mahasiswa,
- "exam_score": Nilai ujian,
- "attendance_percentage": Persentase kehadiran,
- "stress_level": Levels stress (semakin tinggi semakin berat stress),
- "mental_health_rating": Level kesehatan mental (semkain tinggi, kesehatan mental semakin baik),
- "parental_support_level": Level dukungan orangtua,
- "motivation_level": Level motivasi,
- "study_hours_per_day": Jam belajar per hari,
- "time_management_score": Skor manajemen waktu,
- "sleep_hours": Jam tidur per hari,
- "screen_time": Screen time per hari,
- "social_media_hours": Jam penggunaan sosial media per hari,
- "netflix_hours": Jam penggunaan netlif per hari,
- "exercise_frequency": Frekuensi olahraga,

> 🧩 **Target Prediksi**: `GPA` mahasiswa selanjutnya

---

## 🛠️ Metodologi

- 🔍 Exploratory Data Analysis (EDA) dengan `Seaborn` & `Matplotlib`
- 📊 Preprocessing: imputasi, encoding, scaling
- 🌲 Model: `RandomForestRegressor` untuk seleksi fitur terbaik
- 📉 Evaluasi: `RMSE`, `R² Score`, dan visualisasi residual
- 📦 Deployment: menggunakan `Streamlit` dan `joblib`

---

## 🔮 Output yang Diharapkan

Dengan aplikasi ini, pengguna dapat:
- Mengisi data input berdasarkan kebiasaan dan performa mahasiswa
- Mendapatkan **prediksi GPA secara instan**
- Menggunakan model sebagai alat bantu prediktif bagi mahasiswa, dosen, atau akademisi

---

## 🚀 Teknologi yang Digunakan

- `Python` (pandas, numpy, sklearn, seaborn, matplotlib)
- `Streamlit` untuk pembuatan aplikasi web interaktif
- `Joblib` untuk serialisasi model
- `GitHub` & `Streamlit Cloud` untuk deployment

---

## Hasil testing

- RMSE : 0.1630
- R squared : 0.8763

---

## 👨‍💻 Link Aplikasi

➡️ **[Coba Aplikasinya di Streamlit](https://gpa-prediction-2025.streamlit.app/)**  
➡️ **[Lihat Repository GitHub](https://github.com/evasbr/gpa-prediction)**

---

## 🧑‍🤝‍🧑 Penyusun

Anggota kelompok:

1. Eva Sabrina
2. Alya Nurmala Dewi
3. Dea Radita Indayani

---

