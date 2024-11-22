import streamlit as st
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image


def show_classification():
    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../src/style/style.css")
    

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)
    
    st.markdown("""
                <div class="section">
                    <div class="title">
                        Klasifikasi Gambar menggunakan Camera dan Galeri
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""
                <div class="subsection">
                    <div class="subheader">
                        Unggah gambar atau gunakan kamera untuk mengidentifikasi jenis serangga.
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # Memuat model TensorFlow
    model_path = os.path.join("model/insect_model.h5")
    model = load_model(model_path)

    # Daftar kelas sesuai model
    class_names = ['butterfly', 'dragonfly', 'grasshopper', 'ladybird', 'mosquito']

    # Pilihan input gambar
    option = st.radio("Pilih metode input gambar:", ["Unggah Foto", "Gunakan Kamera"])

    if option == "Unggah Foto":
        uploaded_file = st.file_uploader("Unggah gambar serangga", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Gambar yang diunggah", use_column_width=True)

            # Proses prediksi
            processed_image = preprocess_image(image)
            predictions = model.predict(processed_image)
            pred_class = class_names[np.argmax(predictions[0])]
            confidence = np.max(predictions[0]) * 100

            # Tampilkan hasil
            display_prediction(pred_class, confidence)

    elif option == "Gunakan Kamera":
        camera_image = st.camera_input("Ambil gambar menggunakan kamera")
        if camera_image is not None:
            image = Image.open(camera_image)
            st.image(image, caption="Gambar dari kamera", use_column_width=True)

            # Proses prediksi
            processed_image = preprocess_image(image)
            predictions = model.predict(processed_image)
            pred_class = class_names[np.argmax(predictions[0])]
            confidence = np.max(predictions[0]) * 100

            # Tampilkan hasil
            display_prediction(pred_class, confidence)

# Fungsi untuk memproses gambar
def preprocess_image(image):
    """
    Praproses gambar untuk input model.
    - Resize gambar menjadi (150, 150)
    - Normalisasi nilai piksel antara 0 dan 1
    - Tambahkan dimensi batch
    """
    image = image.resize((150, 150))
    image_array = np.array(image) / 255.0
    return np.expand_dims(image_array, axis=0)

# Fungsi untuk menampilkan hasil prediksi dengan deskripsi
def display_prediction(pred_class, confidence):
    confidence_threshold = 80

    # Check if confidence is above the threshold
    if confidence >= confidence_threshold:
        st.success(f"Prediction: **{pred_class.capitalize()}**")
        st.write(f"Confidence: **{confidence:.2f}%**")
        
    # Tambahkan deskripsi untuk setiap kelas
        if pred_class == "butterfly":
            st.markdown("""
            <div class="criteria">
                <!-- Subheader untuk Kupu-Kupu -->
                <div class="subheader">🦋 Kupu-kupu / Butterfly</div>
                <p class="paragraf"><b>Kupu-kupu</b> 
                    merupakan serangga yang tergolong ke dalam ordo Lepidoptera, atau 'serangga bersayap sisik' (lepis, sisik dan pteron, sayap). Kupu-kupu memiliki tubuh ramping, sayap lebar berwarna-warni, dan antena berbentuk tongkat (Parker, Sybil, P (1984) ).
                </p>
                <br>
                <!-- Subheader untuk Siklus Hidup -->
                <div class="subheader">Siklus Hidup Kupu-Kupu</div>
                <!-- Penjelasan Siklus Hidup -->
                <ol class="desc">
                    <li class="paragraf"><b>Telur</b>: 
                        Tahap awal kehidupan kupu-kupu dimulai sebagai telur kecil yang diletakkan di daun atau batang tumbuhan. Betina biasanya memilih tumbuhan inang yang cocok untuk ulatnya, tergantung pada kondisi lingkungan, seperti suhu dan kelembaban.
                    </li>
                    <li class="paragraf"><b>Ulat (Larva)</b>: 
                        Setelah menetas, telur menghasilkan ulat atau larva. Ulat ini adalah tahap pertumbuhan di mana kupu-kupu makan dengan sangat banyak untuk mendapatkan energi. Ulat memakan daun tumbuhan inangnya dengan lahap untuk meningkatkan ukurannya beberapa kali lipat. Meski terlihat sederhana, ulat juga sudah memiliki mekanisme perlindungan, seperti warna tubuh yang menyerupai lingkungan atau duri untuk menakut-nakuti predator.
                    </li>
                    <li class="paragraf"><b>Kepompong (Pupa)</b>: 
                        Setelah mencapai ukuran maksimal, ulat membentuk kepompong atau pupa. Ini adalah tahap transisi di mana tubuh ulat akan berubah menjadi tubuh kupu-kupu. Di dalam kepompong, ulat mengalami proses metamorfosis besar, mengubah jaringan tubuhnya menjadi struktur baru seperti sayap, kaki, dan antena kupu-kupu.
                    </li>
                    <li class="paragraf"><b>Kupu-Kupu Dewasa</b>: 
                        Setelah proses dalam kepompong selesai, kupu-kupu dewasa keluar dengan sayap yang masih basah dan terlipat. Dalam beberapa jam, sayap akan mengering dan mengembang. Kupu-kupu dewasa ini siap untuk mencari makanan berupa nektar bunga dan memulai proses reproduksi, sehingga siklus hidupnya berulang kembali.
                    </li>
                </ol>
                <br>
                <!-- Subheader untuk Peran Ekosistem -->
                <div class="subheader">Peran dalam Ekosistem</div>
                <!-- Penjelasan Peran Ekosistem -->
                <ul class="desc">
                    <li class="paragraf"><b>Penyerbuk Tanaman</b>: 
                        Kupu-kupu membantu penyerbukan bunga ketika mereka menghisap nektar. Saat mereka hinggap di bunga, serbuk sari melekat pada tubuhnya dan terbawa ke bunga lain, memungkinkan proses reproduksi tumbuhan. Penyerbukan ini membantu berbagai tanaman berbunga, termasuk tanaman pangan seperti buah-buahan dan sayuran.
                    </li>
                    <li class="paragraf"><b>Bioindikator Kesehatan Lingkungan</b>: 
                        Kupu-kupu adalah indikator alami yang baik untuk menilai kesehatan ekosistem. Karena mereka sangat sensitif terhadap perubahan lingkungan seperti polusi, penggunaan pestisida, atau perubahan iklim, kehadiran atau ketiadaan kupu-kupu dapat menunjukkan kualitas suatu habitat. Habitat dengan keanekaragaman kupu-kupu yang tinggi menunjukkan ekosistem yang sehat.
                    </li>
                    <li class="paragraf"><b>Sebagai Mata Rantai Makanan</b>: 
                        Kupu-kupu, dalam berbagai tahap hidupnya, adalah sumber makanan bagi banyak spesies lain. Ulat menjadi makanan utama bagi burung, reptil, dan mamalia kecil. Kupu-kupu dewasa juga dimakan oleh burung, laba-laba, dan serangga predator lainnya.
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.video("https://youtu.be/6TYlVuREwvA?si=i6W3R-8M9jUFfzUM")
            st.caption("Source Video: Halo-Edukasi - Bagaimana proses metamorfosis Kupu-Kupu")

        elif pred_class == "dragonfly":
            st.markdown("""
            <div class="criteria">
                <!-- Subheader untuk Capung -->
                <div class="subheader">🪰 Capung / Dragonfly</div>
                <p class="paragraf"><b>Capung</b> Capung (Ordo Odonata) adalah serangga predatory yang sangat efisien dan dapat ditemukan di seluruh dunia, terutama di sekitar badan air seperti kolam, sungai, dan rawa. Capung dikenal dengan kemampuan terbangnya yang luar biasa cepat dan lincah, serta mata besar yang memberi mereka pandangan 360 derajat. </p>
                <br>
                <!-- Subheader untuk Proses Daur Hidup Capung -->
                <div class="subheader">Proses Daur Hidup Capung (Metamorfosis Tidak Sempurna)</div>
                <!-- Penjelasan Daur Hidup Capung -->
                <ol class="desc">
                    <li class="paragraf"><b>Fase Telur</b>: 
                        Capung betina bertelur di air, terutama di kolam, danau, atau area basah lainnya. Telur berbentuk kecil dan transparan. Satu capung betina dapat menghasilkan hingga 100 butir telur yang akan menetas dalam waktu 1–3 minggu.
                    </li>
                    <li class="paragraf"><b>Fase Nimfa</b>: 
                        Setelah menetas, telur berubah menjadi nimfa yang hidup di air. Nimfa adalah predator aktif yang memakan jentik nyamuk, larva, dan serangga air kecil lainnya. Nimfa mengalami pergantian kulit sebanyak 8–17 kali hingga siap menjadi capung dewasa.
                    </li>
                    <li class="paragraf"><b>Fase Dewasa</b>: 
                        Nimfa keluar dari air, menempel pada batang tanaman atau batu, dan tubuhnya berubah menjadi capung dewasa dengan sayap yang sempurna. Tahap dewasa berlangsung beberapa minggu hingga beberapa bulan, berfungsi untuk berkembang biak.
                    </li>
                </ol>
                <br>
                <!-- Subheader untuk Manfaat Capung dalam Ekosistem -->
                <div class="subheader">Manfaat Capung bagi Ekosistem</div>
                <ul class="desc">
                    <li class="paragraf"><b>Indikator Kualitas Air</b>: 
                        Nimfa capung hanya dapat hidup di air bersih dan minim polusi, sehingga keberadaannya menjadi tanda ekosistem air yang sehat.
                    </li>
                    <li class="paragraf"><b>Predator Hama</b>: 
                        Capung membantu mengendalikan populasi hama dengan memangsa serangga kecil seperti nyamuk, lalat, dan serangga lainnya yang dapat mengganggu manusia atau merusak tanaman.
                    </li>
                    <li class="paragraf"><b>Pengurai Organik</b>: 
                        Nimfa capung berkontribusi dalam penguraian bahan organik di air dengan memangsa serangga mati atau sisa-sisa organisme.
                    </li>
                    <li class="paragraf"><b>Penyerbuk Tanaman</b>: 
                        Beberapa spesies capung dapat membantu penyerbukan tanaman hutan dan tumbuhan air tertentu.
                    </li>
                    <li class="paragraf"><b>Menjaga Keseimbangan Rantai Makanan</b>: 
                        Capung sebagai predator serangga memainkan peran penting dalam menjaga keseimbangan ekosistem dan mengontrol populasi serangga lainnya.
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.video("https://youtu.be/fSXNGHznwGw?si=GOS_BiiHryqZ9aue")
            st.caption("Source Video: Halo-Edukasi - Bagaimana proses metamorfosis Capung")

            
        elif pred_class == "grasshopper":
            st.markdown("""
            <div class="criteria">
                <!-- Subheader untuk Belalang -->
                <div class="subheader">🦗 Belalang / Grasshopper</div>
                <p class="paragraf"><b>Belalang</b> adalah serangga herbivora dari subordo Caelifera dalam ordo Orthoptera. 
                Serangga ini dikenal karena kemampuan melompat yang tinggi berkat kaki belakangnya yang panjang dan kuat.</p>
                <br>
                <!-- Subheader untuk Proses Daur Hidup Belalang -->
                <div class="subheader">Proses Daur Hidup Belalang (Metamorfosis Tidak Sempurna)</div>
                <!-- Penjelasan Daur Hidup Belalang -->
                <ol class="desc">
                    <li class="paragraf"><b>Fase Telur</b>: 
                        Belalang betina bertelur di bawah pasir atau daun, disertai zat lengket untuk melindungi telur dari air. Setiap kali bertelur, belalang betina dapat menghasilkan 10–200 butir telur.
                    </li>
                    <li class="paragraf"><b>Fase Nimfa</b>: 
                        Setelah 10 bulan, telur menetas menjadi nimfa tanpa sayap dan organ reproduksi. Nimfa berganti kulit (moulting) hingga 6 kali dalam 30–40 hari, sebelum sayap mulai tumbuh. Warna nimfa berubah dari putih menjadi hijau atau cokelat saat terkena sinar matahari.
                    </li>
                    <li class="paragraf"><b>Fase Dewasa</b>: 
                        Nimfa berubah menjadi belalang dewasa dengan sayap sempurna. Belalang dewasa memiliki organ pendengar bernama <b>tympana</b> dan mata majemuk yang membantu penglihatan ke segala arah.
                    </li>
                </ol>
                <br>
                <!-- Subheader untuk Manfaat Belalang dalam Ekosistem -->
                <div class="subheader">Manfaat Belalang bagi Ekosistem</div>
                <ul class="desc">
                    <li class="paragraf"><b>Menyeimbangkan Rantai Makanan</b>: 
                        Sebagai konsumen tingkat satu, belalang memakan daun dan menjadi makanan bagi burung dan hewan lain.
                    </li>
                    <li class="paragraf"><b>Memberikan Nutrisi bagi Tanah</b>: 
                        Feses belalang kaya akan unsur kimia yang menyuburkan tanah.
                    </li>
                    <li class="paragraf"><b>Mengendalikan Populasi Serangga Pengganggu</b>: 
                        Membantu mengurangi jumlah serangga seperti kutu daun dan lalat.
                    </li>
                    <li class="paragraf"><b>Menjaga Keseimbangan Ekosistem Air</b>: 
                        Belalang bermigrasi ke area lembab, membantu menjaga keseimbangan lingkungan.
                    </li>
                    <li class="paragraf"><b>Menjaga Tanah Tetap Subur</b>: 
                        Lubang tempat bertelur belalang membantu mempertahankan kelembapan tanah.
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.video("https://youtu.be/0LZ0-zq9ycA?si=3vpGOz_is474gyeE")
            st.caption("Source Video: Halo-Edukasi - Bagaimana proses metamorfosis Belalang")
            

            
        elif pred_class == "ladybird":
            st.markdown("""
                <div class="criteria">
                    <!-- Subheader untuk Kumbang Kepik -->
                    <div class="subheader">🐞 Kumbang Kepik / Ladybird</div>
                    <p class="paragraf"><b>Kumbang Kepik</b> (Ladybird) adalah serangga kecil dari famili <b>Coccinellidae</b> yang dikenal karena bentuknya yang bulat dan warna cerah pada punggungnya. Kumbang ini sering dianggap sahabat petani karena berperan penting sebagai pengendali hama tanaman.</p>
                    <br>
                    <!-- Subheader untuk Proses Daur Hidup Kumbang Kepik -->
                    <div class="subheader">Proses Daur Hidup Kumbang Kepik (Metamorfosis Sempurna)</div>
                    <!-- Penjelasan Daur Hidup Kumbang Kepik -->
                    <ol class="desc">
                        <li class="paragraf"><b>Fase Telur</b>: 
                            Telur diletakkan berkelompok di bawah daun atau batang tanaman dekat koloni kutu daun. Kepik betina menghasilkan 10–50 kelompok telur sekaligus. Telur berbentuk oval dengan warna oranye atau kuning.
                        </li>
                        <li class="paragraf"><b>Fase Larva</b>: 
                            Larva berbentuk memanjang dengan kaki yang jelas terlihat. Mereka adalah predator aktif yang memakan kutu daun dan serangga parasit lainnya. Larva makan dalam jumlah besar untuk mempersiapkan diri ke fase berikutnya.
                        </li>
                        <li class="paragraf"><b>Fase Pupa</b>: 
                            Larva berubah menjadi pupa yang berbentuk bola dan ditutupi kulit pelindung. Proses metamorfosis berlangsung selama sekitar satu minggu.
                        </li>
                        <li class="paragraf"><b>Fase Dewasa</b>: 
                            Kepik dewasa memiliki tubuh bulat seperti kubah, dengan warna cerah seperti merah, oranye, hitam, kuning, atau merah muda. Corak bintik pada sayap berfungsi sebagai peringatan bagi pemangsa.
                        </li>
                    </ol>
                    <br>
                    <!-- Subheader untuk Manfaat Kumbang Kepik bagi Ekosistem -->
                    <div class="subheader">Manfaat Kumbang Kepik bagi Ekosistem</div>
                    <ul class="desc">
                        <li class="paragraf"><b>Mengontrol hama</b>: Predator alami kutu daun dan serangga hama lainnya.</li>
                        <li class="paragraf"><b>Membantu polinasi</b>: Beberapa spesies membantu penyerbukan dengan mentransfer serbuk sari antar bunga.</li>
                        <li class="paragraf"><b>Dekomposisi</b>: Membantu menguraikan bahan organik mati dan mengembalikan nutrisi ke tanah.</li>
                        <li class="paragraf"><b>Penelitian ilmiah</b>: Menjadi subjek studi yang mendukung pengembangan pertanian berkelanjutan.</li>
                    </ul>
                    <br>
                    <p class="paragraf">Dengan peranannya sebagai pengendali hama dan pendukung ekosistem, kumbang kepik merupakan serangga yang sangat bermanfaat bagi pertanian dan lingkungan.</p>
                </div>
        """, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.video("https://youtu.be/CLNneHdzd-A?si=cVEXH8cbZHiPiCEa")
            st.caption("Source Video: Halo-Edukasi - Bagaimana proses metamorfosis Kepik")   

            
        elif pred_class == "mosquito":
            st.markdown("""
                <div class="criteria">
                    <!-- Subheader untuk Nyamuk -->
                    <div class="subheader">🦟 Nyamuk / Mosquito</div>
                    <p class="paragraf"><b>Nyamuk</b> adalah serangga kecil dari famili <b>Culicidae</b> yang memiliki tubuh ramping, dua sayap bersisik, dan enam kaki panjang. Meski dikenal sebagai pengganggu dan penyebar penyakit, nyamuk juga memiliki peran dalam ekosistem sebagai bagian dari rantai makanan.</p>
                    <br>
                    <!-- Subheader untuk Siklus Hidup Nyamuk -->
                    <div class="subheader">Siklus Hidup Nyamuk (Metamorfosis Sempurna)</div>
                    <!-- Penjelasan Siklus Hidup Nyamuk -->
                    <ol class="desc">
                        <li class="paragraf"><b>Fase Telur</b>: 
                            Nyamuk betina bertelur di genangan air seperti mangkuk, cangkir, kolam, ban bekas, atau vas. Setiap kali bertelur, nyamuk betina dapat menghasilkan hingga 100 butir telur.
                        </li>
                        <li class="paragraf"><b>Fase Larva</b>: 
                            Telur menetas menjadi larva jika permukaan air naik dan menutupi telur. Larva hidup di air dan memakan mikroorganisme di dalamnya.
                        </li>
                        <li class="paragraf"><b>Fase Pupa</b>: 
                            Setelah mengalami tiga kali pergantian kulit, larva berubah menjadi pupa atau kepompong.
                        </li>
                        <li class="paragraf"><b>Fase Dewasa</b>: 
                            Nyamuk dewasa keluar dari kepompong di permukaan air. Nyamuk jantan memakan nektar bunga, sedangkan nyamuk betina mengisap darah manusia atau hewan untuk menghasilkan telur.
                        </li>
                    </ol>
                    <br>
                    <!-- Subheader untuk Manfaat Nyamuk bagi Ekosistem -->
                    <div class="subheader">Manfaat Nyamuk bagi Ekosistem</div>
                    <ul class="desc">
                        <li class="paragraf"><b>Makanan bagi hewan lain</b>: Nyamuk merupakan sumber makanan bagi ikan, burung, kadal, katak, kelelawar, dan beberapa spesies lainnya.</li>
                        <li class="paragraf"><b>Mendukung rantai makanan</b>: Kehilangan nyamuk dapat memengaruhi pasokan makanan bagi predator tertentu, yang berdampak pada ekosistem secara keseluruhan.</li>
                    </ul>
                    <br>
                    <p class="paragraf">Walaupun sering dianggap sebagai hama, nyamuk memiliki peran penting dalam menjaga keseimbangan ekosistem.</p>
                </div>
        """, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.video("https://youtu.be/UXWm1Ztq3ek?si=PHuDWqn65N2wLfqg")
            st.caption("Source Video: Halo-Edukasi - Bagaimana proses metamorfosis Nyamuk")

    else:
        # If confidence is below threshold, hide prediction and show a warning message
        st.warning(f"Confidence is too low ({confidence:.2f}%) to make a reliable prediction.")
        st.info("Kemungkinan ini bukan foto serangga. Silakan unggah gambar yang lebih jelas atau sesuai.")

