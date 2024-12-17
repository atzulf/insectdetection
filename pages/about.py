import streamlit as st
import os


def show_about():
    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../src/style/style.css")
    mini = os.path.join(parent_dir, "../src/image/mini.png")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)
    
    st.markdown("""
                <div class="section">
                    <div class="title">
                        Tentang Aplikasi Ini
                    </div>
                </div>
                """, unsafe_allow_html=True)
    st.write("")

    st.image(mini, use_column_width=True)
    
    st.markdown("""
                <div class="subsection">
                    <div class="subheader">Insect Animal Classification 🦟🦋🦗</div>
                    <br>
                    <p>Aplikasi Identifikasi Serangga yang cepat dan mudah digunakan</p>
                </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
                <div class="subsection">
                    <div class="subheader">Harapan dibuatnya Aplikasi ini✨</div>
                    <br>
                    <ul>
                        <li>Meningkatkan kesadaran masyarakat tentang pentingnya peran serangga dalam keseimbangan ekosistem.</li>
                        <li>Menyediakan media pembelajaran interaktif untuk siswa, guru, dan pecinta lingkungan.</li>
                        <li>Mendorong generasi muda untuk aktif dalam pelestarian lingkungan.</li>
                        <li>Berperan dalam mendukung konservasi keanekaragaman hayati.</li>
                        <li>Memberikan pengalaman belajar yang menyenangkan melalui konten visual dan interaktif.</li>
                    </ul>
                </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
                <div class="criteria">
                    <div class="subheader">
                        <div class="content_position">
                            👤Informasi Pembuat
                        </div>
                    </div>
                    <br>
                    <div class="content_position">
                        <img src="https://media.licdn.com/dms/image/v2/D5603AQFeb91M8UDq8g/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1732253181932?e=1737590400&v=beta&t=e98Z0lUTQEzTHOWMDE0bq5BulycgdKvOJ_8RDA9DCLw" class="circle">
                        <br>
                        <b>Nama:</b> Ataka Dzulfikar<br>
                        <b>NIM:</b> 22537141002<br>
                        <b>Prodi:</b> Teknologi Informasi I / 2022
                    </div>
                </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
                <div class="criteria">
                    <div class="subheader">
                        <div class="content_position">
                            📬 Kontak
                        </div>
                    </div>
                    <br>
                    <div class="content_position">
                        <b>Email:</b> <a href="mailto:atakadzulfikar.2022@student.uny.ac.id">atakadzulfikar.2022@student.uny.ac.id</a><br>
                        <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/ataka-dzulfikar" target="_blank">Ataka Dzulfikar</a><br>
                        <b>Instagram:</b> <a href="https://www.instagram.com/atakazulfikar" target="_blank">@ataka_zulfikar</a><br>
                        <b>GitHub:</b> <a href="https://github.com/atzulf/insectdetection" target="_blank">GitHub</a><br>
                    </div>
                </div>
        """, unsafe_allow_html=True)


