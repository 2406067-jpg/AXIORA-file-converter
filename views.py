# views.py - Penampung Konten Halaman Navigasi AXIORA Suite
import streamlit as st


def render_riwayat():
    st.markdown("## 📜 Riwayat Konversi")
    st.markdown("Berikut adalah daftar file yang baru saja kamu konversi:")

    # Simulasi Tabel Riwayat
    riwayat_data = [
        {
            "File": "pertemuan_3.docx",
            "Format": "DOCX ➔ PDF",
            "Waktu": "12:35 PM",
            "Status": "✅ Selesai",
        },
        {
            "File": "photo_profile.jpg",
            "Format": "JPG ➔ PNG",
            "Waktu": "11:20 AM",
            "Status": "✅ Selesai",
        },
        {
            "File": "podcast_audio.wav",
            "Format": "WAV ➔ MP3",
            "Waktu": "Kemarin",
            "Status": "✅ Selesai",
        },
    ]

    st.table(riwayat_data)


def render_pengaturan():
    st.markdown("## ⚙️ Pengaturan Aplikasi")
    st.write("")

    st.markdown("### 🎨 Tema & Tampilan")
    st.selectbox(
        "Model UI System:",
        [
            "Dark Glassmorphism (Default)",
            "Cyberpunk Neon",
            "Midnight Ocean",
        ],
    )

    st.markdown("### ⚡ Performa Konversi")
    st.slider("Kualitas Rendering Video (Bitrate Max M):", 10, 50, 18)
    st.checkbox("Otomatis bersihkan file sementara setelah download", value=True)

    st.write("")
    if st.button("💾 SIMPAN PENGATURAN"):
        st.success("Pengaturan berhasil disimpan!")


def render_bantuan():
    st.markdown("## ❓ Pusat Bantuan & Panduan")
    st.write("")

    with st.expander("❓ Bagaimana cara mengubah PDF ke Word?"):
        st.write(
            "Cukup upload file PDF lo di Beranda, pilih format tujuan **Word (.docx)**, lalu klik tombol **Mulai Konversi**."
        )

    with st.expander("❓ Apakah file yang saya upload aman?"):
        st.write(
            "Sangat aman! Semua proses konversi berjalan secara lokal di komputer lo tanpa di-upload ke server luar."
        )

    with st.expander("❓ Format apa saja yang didukung?"):
        st.write(
            "AXIORA mendukung Dokumen (PDF, DOCX), Gambar (JPG, PNG, WEBP), Audio (MP3, WAV), dan Video (MP4, MOV)."
        )