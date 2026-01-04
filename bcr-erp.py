import streamlit as st
import google.generativeai as genai

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Aplikasi AI Saya", page_icon="🤖")

# 2. Masukkan API Key (Nanti kita atur agar aman saat online)
# Di komputer lokal, Anda bisa tempel langsung, tapi untuk online pakai 'Secrets'
api_key = st.secrets["GEMINI_API_KEY"] 
genai.configure(api_key=api_key)

# 3. Setting Model (Sesuai setelan Anda di AI Studio)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash", # Atau model yang Anda pakai
  generation_config=generation_config,
  # Masukkan System Instruction dari AI Studio di sini jika ada
  system_instruction="Anda adalah asisten ahli..." 
)

# 4. Tampilan Antarmuka (UI)
st.title("Program AI Super Canggih")
st.write("Masukkan data di bawah ini:")

user_input = st.text_area("Input Data:", height=150)

if st.button("Proses Data"):
    if user_input:
        with st.spinner('Sedang berpikir...'):
            # Kirim ke AI
            response = model.generate_content(user_input)
            
            # Tampilkan Hasil
            st.subheader("Hasil:")
            st.write(response.text)
    else:
        st.warning("Mohon isi data terlebih dahulu.")
      