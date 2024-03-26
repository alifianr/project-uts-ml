#import library yang digunakan
import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

#Load save model
model_fraud = pickle.load(open('model_fraud.sav', 'rb'))

#kita panggil perintah tfidf lagi 
tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))


# Judul halaman web
st.title ('Prediksi SMS Penipuan')

# Masukan text input
clean_teks = st.text_input('Masukan Teks SMS')

fraud_detection = ''

# Masukan kondisinya
if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))

    if (predict_fraud == 0):
        fraud_detection = 'SMS Normal'
    elif (predict_fraud == 1):
        fraud_detection = 'SMS Fraud'
    else :
        fraud_detection = 'SMS Promo'
st.success(fraud_detection)