import streamlit as st
import pandas as pd
import joblib
import gdown
import os
import joblib

# Judul aplikasi
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🎓 Prediksi Nilai IP Mahasiswa</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Final Project Data Science Beginner KSM Android UPNVJ 2025</h4>", unsafe_allow_html=True)
st.markdown("🔗 Cek kode sumber di [GitHub](https://github.com/username/repo)")
st.write("Nama anggota : ")
st.markdown('''
<ul>
    <li>Eva Sabrina</li> 
    <li>Alya Nurmala Dewi</li> 
    <li>Dea Radita Indayani</li> 
</ul>
''', unsafe_allow_html=True)

st.divider()

model_path = "model_rf.pkl"

if not os.path.exists(model_path):
    # Download dari Google Drive
    file_id = "1_OEP51gp1RiQTcfBTAcXVFiDcIXHFMA1" 
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, model_path, quiet=False)

# Load model
model = joblib.load(model_path)

# Load fitur
selected_features = joblib.load("selected_features.pkl")

# Penjelasan singkat
st.markdown("Masukkan data berikut untuk memprediksi IP Anda di semester berikutnya.👇")

# Input Form
with st.form("prediction_form"):
    st.subheader("📝 Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        semester = st.number_input("📚 Semester", min_value=1, max_value=16)
        age = st.number_input("🎂 Umur", min_value=15, max_value=100)
        exam_score = st.number_input("🧪 Nilai Ujian", min_value=0, max_value=100)
        attendance_percentage = st.number_input("🏫 Persentase Kehadiran", min_value=0.0, max_value=100.0, step=0.1)
        stress_level = st.number_input("😫 Level Stress (1-10)", min_value=1.0, max_value=10.0, step=0.1)
        mental_health_rating = st.number_input("🧠 Rating Kesehatan Mental", min_value=1.0, max_value=10.0, step=0.1)
        parental_support_level = st.number_input("👨‍👩‍👧‍👦 Dukungan Orang Tua", min_value=1, max_value=10)
        motivation_level = st.number_input("🚀 Level Motivasi", min_value=1, max_value=10)

    with col2:
        study_hours_per_day = st.number_input("📖 Jam Belajar per Hari", min_value=0.0, max_value=24.0, step=0.1)
        time_management_score = st.number_input("📅 Skor Time Management", min_value=1.0, max_value=10.0, step=0.1)
        sleep_hours = st.number_input("🛌 Jumlah Jam Tidur", min_value=0.0, max_value=24.0, step=0.1)
        screen_time = st.number_input("📱 Screen Time (jam/hari)", min_value=0, max_value=24)
        social_media_hours = st.number_input("📵 Waktu di Media Sosial", min_value=0.0, max_value=24.0, step=0.1)
        netflix_hours = st.number_input("📺 Waktu di Netflix", min_value=0.0, max_value=24.0, step=0.1)
        exercise_frequency = st.number_input("🏃‍♂️ Frekuensi Olahraga / minggu", min_value=1, max_value=10)

    # Submit button
    submitted = st.form_submit_button("🔮 Prediksi Nilai IP")

    if submitted:
        user_inputs = {
            "semester": semester,
            "age": age,
            "exam_score": exam_score,
            "attendance_percentage": attendance_percentage,
            "stress_level": stress_level,
            "mental_health_rating": mental_health_rating,
            "parental_support_level": parental_support_level,
            "motivation_level": motivation_level,
            "study_hours_per_day": study_hours_per_day,
            "time_management_score": time_management_score,
            "sleep_hours": sleep_hours,
            "screen_time": screen_time,
            "social_media_hours": social_media_hours,
            "netflix_hours": netflix_hours,
            "exercise_frequency": exercise_frequency,
        }

        input_df = pd.DataFrame([[user_inputs[feature] for feature in selected_features]], columns=selected_features)

        prediction = model.predict(input_df)
        st.success(f"📊 Prediksi IP Anda di semester berikutnya adalah: **{prediction[0]:.2f}**")
