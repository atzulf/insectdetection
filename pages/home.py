import streamlit as st
import os


def show_home():
    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../src/style/style.css")
    banner = os.path.join(parent_dir, "../src/image/banner.png")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)
    st.markdown("""
                <div class="section">
                    <div class="title">
                        Insect Animal Classification
                    </div>
                </div>
                """, unsafe_allow_html=True)
    st.write("")

    # Menampilkan gambar banner
    st.image(banner,caption='klasifikasi serangga', use_column_width=True)
    
    st.markdown("""
                <div class="subsection">
                    <div class="header">
                        Selamat Datang di Aplikasi Klasifikasi Serangga!
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""
                <div class="subsection">
                    <div class="subheader">🔍Serangga yang Dapat Diklasifikasikan:</div>
                    <br>
                    <ul>
                        <li>🦋 <b>Butterfly</b>: Si anggun penyerbuk bunga.</li>
                        <li>𓆤 <b>Dragonfly</b>: Sang pemangsa alami serangga kecil.</li>
                        <li>🦗 <b>Grasshopper</b>: Si pelompat tangguh di ladang dan padang rumput.</li>
                        <li>🐞 <b>Ladybird</b>: Pahlawan kecil pengendali hama tanaman.</li>
                        <li>🦟 <b>Mosquito</b>: Serangga kecil yang memengaruhi kesehatan manusia.</li>
                    </ul>
                </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
                <div class="subsection">
                    <div class="subheader">✨ Fitur Unggulan Aplikasi Ini:</div>
                    <br>
                    <ul>
                        <li>Kemudahan Penggunaan: Antarmuka sederhana yang cocok untuk semua kalangan.</li>
                        <li>Hasil Cepat dan Akurat: Didukung oleh model deep learning terkini.</li>
                        <li>Edukasi Serangga: Pelajari fakta menarik setelah klasifikasi selesai.</li>
                    </ul>
                </div>
        """, unsafe_allow_html=True)

    st.markdown("""
                <div class="subsection">
                    <div class="subheader">🎯Tujuan Kami**</div>
                    <br>
                    <ul>
                        <li>📖 <b>Pengenalan tentang tiap jenis Serangga</b>:Memahami nama latin serangga dan bagaimana siklus hidup serangga</li>
                        <li>🧠 <b>Edukasi dan Kesadaran Keanekaragaman Hayati</b>: Memahami peran serangga dalam menjaga keseimbangan ekosistem.</li>
                        <li>🔬 <b>Dukungan Penuh terhadap pelestari alam</b>: Dengan mengetahui peran serangga maka diharapkan dapat melestarikan alam.</li>
                    </ul>
                </div>
        """, unsafe_allow_html=True)
    
