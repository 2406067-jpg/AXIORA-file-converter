# app.py - Main Entry Point AXIORA Universal File Converter
import io
import multiprocessing
import os
import subprocess
import streamlit as st
from docx import Document
from pdf2docx import Converter
from PIL import Image

# 1. Konfigurasi Halaman Streamlit (HARUS PERTAMA DARI SEMUA ST.* COMMANDS)
st.set_page_config(
    page_title="AXIORA - Universal File Converter Suite",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Handler verifikasi file HTML Google Search Console
query_params = st.query_params
if "google_verification" in query_params:
    st.write("google-site-verification: google062eae63eb97ec5f.html")
    st.stop()

# Import Module Tema & Views Navigasi
from themes import get_axiora_css
from views import render_bantuan, render_pengaturan, render_riwayat

# 2. Inject CSS Tampilan AXIORA
st.markdown(get_axiora_css(), unsafe_allow_html=True)

# 3. Inject Meta Tag Google Search Console
GOOGLE_VERIFICATION_CODE = "KDhmJIapBuzwa-TzJpDZZB92wIbKZVtAhpAvtEmR8cY"
st.markdown(
    f'<meta name="google-site-verification" content="{GOOGLE_VERIFICATION_CODE}" />',
    unsafe_allow_html=True,
)

# 4. Sidebar Navigation Interaktif
with st.sidebar:
    st.markdown(
        """
        <div class="brand-container">
            <div class="brand-logo">A</div>
            <div>
                <h1 class="brand-text">AXIORA</h1>
                <span class="brand-subtext">Fast • Simple • Reliable</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### 📌 Menu Navigasi")

    # Navigasi Utama
    menu_pilihan = st.radio(
        "Pilih Halaman:",
        ["🏠 Beranda", "📜 Riwayat Konversi", "⚙️ Pengaturan", "❓ Bantuan"],
        label_visibility="collapsed",
    )

    st.write("---")

    # Menu Tools / Fitur Tambahan (Akses Cepat)
    st.markdown("### 🛠️ Fitur & Tools")
    tools_pilihan = st.selectbox(
        "Akses Alat Cepat:",
        [
            "⚡ Konverter Utama",
            "🗜️ PDF Compressor",
            "✂️ PDF Splitter",
            "🖼️ Pasfoto Resizer",
            "💧 Watermark Generator",
        ],
        key="sb_tools_pilihan",
    )

    st.write("---")
    st.markdown(
        """
        <div style="background: rgba(37, 99, 235, 0.1); border: 1px solid rgba(37, 99, 235, 0.3); padding: 14px; border-radius: 12px;">
            <p style="font-size: 0.85rem; font-weight: 700; color: #60a5fa; margin: 0 0 6px 0;">⚡ Konversi File Lebih Mudah!</p>
            <p style="font-size: 0.75rem; color: #94a3b8; margin: 0;">Mendukung berbagai format dokumen, gambar, audio, & video secara instan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Engine Konversi Presisi Word ➔ PDF (LibreOffice)
def process_docx_to_pdf(docx_path, output_pdf_path):
    try:
        cmd = [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            docx_path,
            "--outdir",
            os.path.dirname(output_pdf_path) or ".",
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(output_pdf_path):
            return True
    except Exception:
        pass

    try:
        cmd = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            docx_path,
            "--outdir",
            os.path.dirname(output_pdf_path) or ".",
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(output_pdf_path):
            return True
    except Exception:
        pass

    return False


# Engine Konversi Presisi PDF ➔ Word (pdf2docx dengan Multiprocessing)
def process_pdf_to_docx(pdf_bytes, output_docx_path):
    temp_pdf = f"temp_input_{os.getpid()}.pdf"
    with open(temp_pdf, "wb") as f:
        f.write(pdf_bytes)

    try:
        cv = Converter(temp_pdf)
        cores = multiprocessing.cpu_count()
        cv.convert(
            output_docx_path,
            start=0,
            end=None,
            multi_processing=True,
            cpu_count=cores,
        )
        cv.close()

        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)
        return True
    except Exception:
        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)
        return False


# Helper aman untuk menjalankan perintah FFmpeg
def run_ffmpeg_command(cmd):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        return res.returncode == 0
    except FileNotFoundError:
        st.error(
            "⚠️ System Package 'FFmpeg' belum terinstall atau aktif di server. Silakan buka menu 'Manage app' lalu klik 'Reboot app'."
        )
        return False
    except Exception as e:
        st.error(f"⚠️ Terjadi kesalahan eksekusi FFmpeg: {str(e)}")
        return False


# ================= ROUTING HALAMAN BERDASARKAN MENU =================

if menu_pilihan == "📜 Riwayat Konversi":
    render_riwayat()

elif menu_pilihan == "⚙️ Pengaturan":
    render_pengaturan()

elif menu_pilihan == "❓ Bantuan":
    render_bantuan()

else:
    # 🏠 HALAMAN UTAMA (BERANDA CONVERTER)
    col_text, col_graphic = st.columns([1.6, 1])

    with col_text:
        st.markdown(
            '<div class="tag-badge">⚡ File Converter Suite</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="main-title">Ubah File Apapun<br><span class="main-title-highlight">Jadi Format yang Kamu Butuhkan</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="hero-description">AXIORA adalah solusi lengkap untuk mengonversi file dengan cepat, aman, dan mudah digunakan. Mendukung berbagai format file populer seperti PDF, DOCX, JPG, PNG, WEBP, MP3, WAV, MP4, MOV dan lainnya.</p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="feature-grid">
                <div class="feature-pill">⚡ <b>Cepat</b> & Akurat</div>
                <div class="feature-pill">👍 <b>Mudah</b> Digunakan</div>
                <div class="feature-pill">📁 <b>Berbagai</b> Format</div>
                <div class="feature-pill">🔒 <b>Aman</b> & Terpercaya</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        btn_col1, btn_col2 = st.columns([1.2, 1])
        with btn_col1:
            if st.button("📋 Lihat Semua Menu & Tools", use_container_width=True, key="btn_hero_menu"):
                st.info(
                    "👈 Buka **Sidebar (Menu Kiri)** atau cek area **Tools & Utility** di bawah untuk menggunakan fitur lengkap!"
                )

    with col_graphic:
        st.markdown(
            """
            <div style="background: radial-gradient(circle, rgba(37,99,235,0.25) 0%, rgba(0,0,0,0) 70%); border-radius: 20px; padding: 25px; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 10px;">🔄</div>
                <div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap;">
                    <span style="background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444; color: #fca5a5; padding: 4px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;">PDF</span>
                    <span style="background: rgba(59, 130, 246, 0.2); border: 1px solid #3b82f6; color: #93c5fd; padding: 4px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;">DOCX</span>
                    <span style="background: rgba(34, 197, 94, 0.2); border: 1px solid #22c55e; color: #86efac; padding: 4px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;">JPG</span>
                    <span style="background: rgba(168, 85, 247, 0.2); border: 1px solid #a855f7; color: #d8b4fe; padding: 4px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;">MP3</span>
                    <span style="background: rgba(236, 72, 153, 0.2); border: 1px solid #ec4899; color: #fbcfe8; padding: 4px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: bold;">MP4</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    if tools_pilihan != "⚡ Konverter Utama":
        st.info(
            f"💡 **Kamu memilih menu:** {tools_pilihan}. Fitur ini sedang disiapkan untuk pembaruan berikutnya!"
        )

    uploaded_files = st.file_uploader(
        "Upload File di Sini (PDF, DOCX, JPG, PNG, WEBP, MP3, WAV, MP4, MOV)",
        type=[
            "docx",
            "pdf",
            "jpg",
            "jpeg",
            "png",
            "webp",
            "wav",
            "mp3",
            "mp4",
            "mov",
        ],
        accept_multiple_files=True,
    )

    if uploaded_files:
        st.markdown(
            f"📌 **{len(uploaded_files)} File Terpilih** untuk dikonversi."
        )

        # Cek apakah pengguna mengunggah banyak foto
        image_files = [
            f
            for f in uploaded_files
            if f.name.split(".")[-1].lower() in ["jpg", "jpeg", "png", "webp"]
        ]

        if len(image_files) > 1:
            st.markdown(
                """
                <div style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); padding: 14px; border-radius: 12px; margin-bottom: 15px;">
                    <p style="font-size: 0.9rem; font-weight: 700; color: #4ade80; margin: 0 0 4px 0;">🖼️ Opsi Penggabungan Multi-Foto</p>
                    <p style="font-size: 0.8rem; color: #cbd5e1; margin: 0;">Kamu mengunggah beberapa gambar. Kamu bisa menggabungkan semuanya menjadi 1 file PDF sekaligus di bawah ini.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            with st.expander(
                f"📑 Gabungkan {len(image_files)} Foto Menjadi 1 Document PDF",
                expanded=True,
            ):
                merged_name = st.text_input(
                    "✏️ Nama File PDF Gabungan:",
                    value="Gabungan_Foto_AXIORA",
                    key="merged_pdf_name",
                )

                if st.button("🚀 GABUNGKAN SEMUA FOTO KE 1 PDF", key="btn_merge_photos"):
                    with st.spinner(
                        "⚡ Mengolah & menggabungkan foto menjadi 1 PDF..."
                    ):
                        processed_images = []
                        for img_file in image_files:
                            img = Image.open(img_file)
                            if img.mode in ("RGBA", "P"):
                                img = img.convert("RGB")
                            processed_images.append(img)

                        if processed_images:
                            pdf_bytes = io.BytesIO()
                            first_img = processed_images[0]
                            rest_imgs = (
                                processed_images[1:]
                                if len(processed_images) > 1
                                else []
                            )

                            first_img.save(
                                pdf_bytes,
                                format="PDF",
                                save_all=True,
                                append_images=rest_imgs,
                            )

                            st.balloons()
                            st.success(
                                f"🎉 Berhasil menggabungkan {len(processed_images)} foto ke 1 PDF!"
                            )
                            st.download_button(
                                label="📥 DOWNLOAD PDF GABUNGAN",
                                data=pdf_bytes.getvalue(),
                                file_name=f"{merged_name}.pdf",
                                mime="application/pdf",
                                key="dl_merged_pdf",
                            )

        for idx, uploaded_file in enumerate(uploaded_files):
            file_name = uploaded_file.name
            file_ext = file_name.split(".")[-1].lower()
            base_name = os.path.splitext(file_name)[0]

            with st.expander(
                f"📁 File #{idx+1}: {file_name} (.{file_ext.upper()})",
                expanded=True,
            ):
                st.markdown(
                    f"""
                    <div class="status-card">
                        📁 <b>File:</b> <code style="color: #60a5fa;">{file_name}</code><br>
                        ⚡ <b>Format Asal:</b> .{file_ext.upper()} | <b>Ukuran:</b> {round(uploaded_file.size / (1024 * 1024), 2)} MB
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.write("")

                # Custom Naming Output
                custom_name = st.text_input(
                    "✏️ Ubah Nama File Output (Opsional):",
                    value=base_name,
                    key=f"name_{idx}",
                )
                target_filename = custom_name if custom_name else base_name

                # 1. DOKUMEN
                if file_ext == "pdf":
                    pilihan_target = st.selectbox(
                        "🎯 Pilih Format Tujuan Konversi:",
                        ["Word Document (.docx)"],
                        key=f"target_{idx}",
                    )
                    if st.button(
                        "🚀 MULAI KONVERSI PDF ➔ WORD", key=f"btn_{idx}"
                    ):
                        with st.spinner(
                            "⚡ Mempertahankan layout & mengonversi PDF ke Word secara cepat..."
                        ):
                            output_docx_file = f"output_{idx}.docx"
                            success = process_pdf_to_docx(
                                uploaded_file.getvalue(), output_docx_file
                            )

                        if success and os.path.exists(output_docx_file):
                            st.balloons()
                            st.success(
                                "🎉 Berhasil diubah ke Word dengan format rapi!"
                            )
                            with open(output_docx_file, "rb") as f:
                                st.download_button(
                                    label="📥 DOWNLOAD FILE WORD (.DOCX)",
                                    data=f,
                                    file_name=f"{target_filename}.docx",
                                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                    key=f"dl_{idx}",
                                )
                            os.remove(output_docx_file)
                        else:
                            st.error("⚠️ Gagal memproses format PDF ke Word.")

                elif file_ext == "docx":
                    pilihan_target = st.selectbox(
                        "🎯 Pilih Format Tujuan Konversi:",
                        ["PDF Document (.pdf)"],
                        key=f"target_{idx}",
                    )
                    if st.button(
                        "🚀 MULAI KONVERSI WORD ➔ PDF", key=f"btn_{idx}"
                    ):
                        with st.spinner(
                            "⚡ Mengonversi Word ke PDF secara presisi..."
                        ):
                            input_docx = f"temp_input_{idx}.docx"
                            output_pdf = f"temp_output_{idx}.pdf"

                            with open(input_docx, "wb") as f:
                                f.write(uploaded_file.read())

                            success = process_docx_to_pdf(
                                input_docx, output_pdf
                            )

                        if success and os.path.exists(output_pdf):
                            st.balloons()
                            st.success("🎉 Berhasil diubah ke PDF!")
                            with open(output_pdf, "rb") as f:
                                st.download_button(
                                    label="📥 DOWNLOAD FILE PDF",
                                    data=f,
                                    file_name=f"{target_filename}.pdf",
                                    mime="application/pdf",
                                    key=f"dl_{idx}",
                                )
                            os.remove(input_docx)
                            os.remove(output_pdf)
                        else:
                            st.error(
                                "⚠️ Gagal merender PDF. Pastikan LibreOffice terinstall di server/sistem."
                            )

                # 2. GAMBAR
                elif file_ext in ["jpg", "jpeg", "png", "webp"]:
                    pilihan_target = st.selectbox(
                        "🎯 Pilih Format Tujuan Konversi:",
                        [
                            "PNG Image",
                            "JPG (JPEG)",
                            "WEBP Image",
                            "PDF Document",
                        ],
                        key=f"target_{idx}",
                    )

                    if st.button(f"🚀 MULAI KONVERSI GAMBAR", key=f"btn_{idx}"):
                        with st.spinner(
                            f"⚡ Mengonversi gambar ke {pilihan_target}..."
                        ):
                            img = Image.open(uploaded_file)

                            if (
                                "JPG" in pilihan_target
                                or "PDF" in pilihan_target
                            ):
                                if img.mode in ("RGBA", "P"):
                                    img = img.convert("RGB")

                            img_bytes = io.BytesIO()

                            if "JPG" in pilihan_target:
                                img.save(img_bytes, format="JPEG", quality=95)
                                mime_type, out_ext = "image/jpeg", "jpg"
                            elif "PNG" in pilihan_target:
                                img.save(img_bytes, format="PNG")
                                mime_type, out_ext = "image/png", "png"
                            elif "WEBP" in pilihan_target:
                                img.save(img_bytes, format="WEBP", quality=90)
                                mime_type, out_ext = "image/webp", "webp"
                            elif "PDF" in pilihan_target:
                                img.save(img_bytes, format="PDF")
                                mime_type, out_ext = "application/pdf", "pdf"

                        st.balloons()
                        st.success(
                            f"🎉 Gambar berhasil diubah ke {out_ext.upper()}!"
                        )
                        st.download_button(
                            label=f"📥 DOWNLOAD FILE .{out_ext.upper()}",
                            data=img_bytes.getvalue(),
                            file_name=f"{target_filename}.{out_ext}",
                            mime=mime_type,
                            key=f"dl_{idx}",
                        )

                # 3. AUDIO
                elif file_ext in ["mp3", "wav"]:
                    pilihan_target = st.selectbox(
                        "🎯 Pilih Format Tujuan Konversi:",
                        ["WAV Audio", "MP3 Audio"],
                        key=f"target_{idx}",
                    )

                    if st.button(f"🚀 MULAI KONVERSI AUDIO", key=f"btn_{idx}"):
                        target_ext = "wav" if "WAV" in pilihan_target else "mp3"
                        with st.spinner(
                            f"⚡ Memproses audio ke format {target_ext.upper()}..."
                        ):
                            input_audio = f"temp_input_{idx}.{file_ext}"
                            output_audio = (
                                f"output_converted_{idx}.{target_ext}"
                            )

                            with open(input_audio, "wb") as f:
                                f.write(uploaded_file.read())

                            cmd = [
                                "ffmpeg",
                                "-y",
                                "-i",
                                input_audio,
                                output_audio,
                            ]
                            success = run_ffmpeg_command(cmd)

                        if success and os.path.exists(output_audio):
                            st.balloons()
                            st.success(
                                f"🎉 Audio berhasil diubah ke format {target_ext.upper()}!"
                            )
                            with open(output_audio, "rb") as f:
                                st.download_button(
                                    label=f"📥 DOWNLOAD AUDIO .{target_ext.upper()}",
                                    data=f,
                                    file_name=f"{target_filename}.{target_ext}",
                                    mime=f"audio/{target_ext}",
                                    key=f"dl_{idx}",
                                )
                            os.remove(input_audio)
                            os.remove(output_audio)

                # 4. VIDEO
                elif file_ext in ["mp4", "mov", "m4v"]:
                    pilihan_target = st.selectbox(
                        "🎯 Pilih Format / Mode Tujuan:",
                        [
                            "MP3 (Ekstrak Suara Audio)",
                            "MP4 (Anti-Burik Sosmed 1080p 60FPS)",
                            "MOV Video Format",
                        ],
                        key=f"target_{idx}",
                    )

                    if st.button(f"🚀 MULAI KONVERSI VIDEO", key=f"btn_{idx}"):
                        with st.spinner(
                            "⚡ Sedang me-render video via FFmpeg..."
                        ):
                            input_video = f"temp_input_{idx}.{file_ext}"
                            with open(input_video, "wb") as f:
                                f.write(uploaded_file.read())

                            if "MP3" in pilihan_target:
                                output_file = f"output_audio_{idx}.mp3"
                                cmd = [
                                    "ffmpeg",
                                    "-y",
                                    "-i",
                                    input_video,
                                    "-vn",
                                    "-ab",
                                    "192k",
                                    "-ar",
                                    "44100",
                                    output_file,
                                ]
                                mime_out, out_name = (
                                    "audio/mp3",
                                    f"{target_filename}.mp3",
                                )

                            elif "Anti-Burik" in pilihan_target:
                                output_file = f"output_video_{idx}.mp4"
                                cmd = [
                                    "ffmpeg",
                                    "-y",
                                    "-i",
                                    input_video,
                                    "-vf",
                                    "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
                                    "-c:v",
                                    "libx264",
                                    "-preset",
                                    "slow",
                                    "-crf",
                                    "18",
                                    "-maxrate",
                                    "18M",
                                    "-bufsize",
                                    "36M",
                                    "-pix_fmt",
                                    "yuv420p",
                                    "-r",
                                    "60",
                                    "-movflags",
                                    "+faststart",
                                    "-c:a",
                                    "aac",
                                    "-b:a",
                                    "192k",
                                    output_file,
                                ]
                                mime_out, out_name = (
                                    "video/mp4",
                                    f"{target_filename}_anti_burik.mp4",
                                )

                            elif "MOV" in pilihan_target:
                                output_file = f"output_video_{idx}.mov"
                                cmd = [
                                    "ffmpeg",
                                    "-y",
                                    "-i",
                                    input_video,
                                    output_file,
                                ]
                                mime_out, out_name = (
                                    "video/quicktime",
                                    f"{target_filename}.mov",
                                )

                            success = run_ffmpeg_command(cmd)

                        if success and os.path.exists(output_file):
                            st.balloons()
                            st.success("🎉 Konversi video berhasil!")
                            with open(output_file, "rb") as f:
                                st.download_button(
                                    label="📥 DOWNLOAD HASIL KONVERSI",
                                    data=f,
                                    file_name=out_name,
                                    mime=mime_out,
                                    key=f"dl_{idx}",
                                )
                            os.remove(input_video)
                            os.remove(output_file)

    # Widget Tools / Fitur Ekstra Interaktif
    st.write("---")
    with st.expander("🛠️ **Tools & Utility Tambahan**", expanded=False):
        st.markdown(
            "Pilih alat bantu cepat di bawah ini untuk pemrosesan file cepat:"
        )
        t_col1, t_col2, t_col3, t_col4 = st.columns(4)
        with t_col1:
            if st.button("🗜️ PDF Compressor", use_container_width=True, key="tool_pdf_compressor"):
                st.toast("🗜️ Fitur PDF Compressor akan segera aktif!", icon="⚡")
        with t_col2:
            if st.button("✂️ Split / Merge PDF", use_container_width=True, key="tool_pdf_splitter"):
                st.toast("✂️ Fitur Split / Merge PDF akan segera aktif!", icon="⚡")
        with t_col3:
            if st.button("🖼️ Pasfoto 3x4 / 4x6", use_container_width=True, key="tool_pasfoto_resizer"):
                st.toast("🖼️ Fitur Pasfoto Resizer akan segera aktif!", icon="⚡")
        with t_col4:
            if st.button("💧 Watermark PDF", use_container_width=True, key="tool_watermark_gen"):
                st.toast("💧 Fitur Watermark Generator akan segera aktif!", icon="⚡")

    # Info Baris Bawah
    st.write("---")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            '<div class="info-card"><div class="info-card-title">📄 Berbagai Format</div><div class="info-card-desc">Dukung PDF, DOCX, JPG, PNG, MP3, MP4, dll.</div></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="info-card"><div class="info-card-title">⚡ Proses Cepat</div><div class="info-card-desc">Konversi cepat dalam hitungan detik.</div></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="info-card"><div class="info-card-title">🔒 Aman & Privasi</div><div class="info-card-desc">File aman diproses lokal di server.</div></div>',
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            '<div class="info-card"><div class="info-card-title">♾️ Tanpa Batas</div><div class="info-card-desc">Bebas konversi kapan saja tanpa batas.</div></div>',
            unsafe_allow_html=True,
        )