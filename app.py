import io
import os
import subprocess
import streamlit as st
from docx import Document
from PIL import Image
from pypdf import PdfReader

# Import Module Tema & Views Navigasi
from themes import get_axiora_css
from views import render_bantuan, render_pengaturan, render_riwayat

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="AXIORA - Universal File Converter Suite",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Inject CSS Tampilan AXIORA
st.markdown(get_axiora_css(), unsafe_allow_html=True)

# 3. Sidebar Navigation Interaktif
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

    # Navigasi Aktif yang Bisa Diklik!
    menu_pilihan = st.radio(
        "Pilih Halaman:",
        ["🏠 Beranda", "📜 Riwayat Konversi", "⚙️ Pengaturan", "❓ Bantuan"],
        label_visibility="collapsed",
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


# Engine Konversi DOCX ➔ PDF
def process_docx_to_pdf(docx_path, output_pdf_path):
    try:
        cmd = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            docx_path,
            "--outdir",
            ".",
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(output_pdf_path):
            return True
    except Exception:
        pass

    try:
        from docx2pdf import convert

        convert(docx_path, output_pdf_path)
        if os.path.exists(output_pdf_path):
            return True
    except Exception:
        pass

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

    uploaded_file = st.file_uploader(
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
    )

    if uploaded_file is not None:
        file_name = uploaded_file.name
        file_ext = file_name.split(".")[-1].lower()
        base_name = os.path.splitext(file_name)[0]

        st.markdown(
            f"""
            <div class="status-card">
                📁 <b>File Terdeteksi:</b> <code style="color: #60a5fa;">{file_name}</code><br>
                ⚡ <b>Format Asal:</b> .{file_ext.upper()} | <b>Ukuran:</b> {round(uploaded_file.size / (1024 * 1024), 2)} MB
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")

        # 1. DOKUMEN
        if file_ext == "pdf":
            pilihan_target = st.selectbox(
                "🎯 Pilih Format Tujuan Konversi:", ["Word Document (.docx)"]
            )
            if st.button("🚀 MULAI KONVERSI PDF ➔ WORD"):
                with st.spinner("⚡ Sedang mengekstrak PDF ke Word..."):
                    reader = PdfReader(uploaded_file)
                    doc = Document()
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            doc.add_paragraph(text)

                    output_stream = io.BytesIO()
                    doc.save(output_stream)

                st.balloons()
                st.success("🎉 Berhasil diubah ke Word!")
                st.download_button(
                    label="📥 DOWNLOAD FILE WORD (.DOCX)",
                    data=output_stream.getvalue(),
                    file_name=f"{base_name}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

        elif file_ext == "docx":
            pilihan_target = st.selectbox(
                "🎯 Pilih Format Tujuan Konversi:", ["PDF Document (.pdf)"]
            )
            if st.button("🚀 MULAI KONVERSI WORD ➔ PDF"):
                with st.spinner("⚡ Sedang mengonversi Word ke PDF..."):
                    input_docx = "temp_input.docx"
                    output_pdf = "temp_input.pdf"

                    with open(input_docx, "wb") as f:
                        f.write(uploaded_file.read())

                    success = process_docx_to_pdf(input_docx, output_pdf)

                if success and os.path.exists(output_pdf):
                    st.balloons()
                    st.success("🎉 Berhasil diubah ke PDF!")
                    with open(output_pdf, "rb") as f:
                        st.download_button(
                            label="📥 DOWNLOAD FILE PDF",
                            data=f,
                            file_name=f"{base_name}.pdf",
                            mime="application/pdf",
                        )
                else:
                    st.error(
                        "⚠️ Tidak dapat merender PDF secara otomatis di Mac tanpa LibreOffice (`brew install libreoffice`)."
                    )

        # 2. GAMBAR
        elif file_ext in ["jpg", "jpeg", "png", "webp"]:
            pilihan_target = st.selectbox(
                "🎯 Pilih Format Tujuan Konversi:",
                ["PNG Image", "JPG (JPEG)", "WEBP Image", "PDF Document"],
            )

            if st.button(f"🚀 MULAI KONVERSI GAMBAR"):
                with st.spinner(
                    f"⚡ Mengonversi gambar ke {pilihan_target}..."
                ):
                    img = Image.open(uploaded_file)

                    if "JPG" in pilihan_target or "PDF" in pilihan_target:
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
                st.success(f"🎉 Gambar berhasil diubah ke {out_ext.upper()}!")
                st.download_button(
                    label=f"📥 DOWNLOAD FILE .{out_ext.upper()}",
                    data=img_bytes.getvalue(),
                    file_name=f"{base_name}.{out_ext}",
                    mime=mime_type,
                )

        # 3. AUDIO
        elif file_ext in ["mp3", "wav"]:
            pilihan_target = st.selectbox(
                "🎯 Pilih Format Tujuan Konversi:", ["WAV Audio", "MP3 Audio"]
            )

            if st.button("🚀 MULAI KONVERSI AUDIO"):
                target_ext = "wav" if "WAV" in pilihan_target else "mp3"
                with st.spinner(
                    f"⚡ Memproses audio ke format {target_ext.upper()}..."
                ):
                    input_audio = f"temp_input.{file_ext}"
                    output_audio = f"output_converted.{target_ext}"

                    with open(input_audio, "wb") as f:
                        f.write(uploaded_file.read())

                    cmd = ["ffmpeg", "-y", "-i", input_audio, output_audio]
                    subprocess.run(cmd)

                st.balloons()
                st.success(
                    f"🎉 Audio berhasil diubah ke format {target_ext.upper()}!"
                )
                with open(output_audio, "rb") as f:
                    st.download_button(
                        label=f"📥 DOWNLOAD AUDIO .{target_ext.upper()}",
                        data=f,
                        file_name=f"{base_name}.{target_ext}",
                        mime=f"audio/{target_ext}",
                    )

        # 4. VIDEO
        elif file_ext in ["mp4", "mov", "m4v"]:
            pilihan_target = st.selectbox(
                "🎯 Pilih Format / Mode Tujuan:",
                [
                    "MP3 (Ekstrak Suara Audio)",
                    "MP4 (Anti-Burik Sosmed 1080p 60FPS)",
                    "MOV Video Format",
                ],
            )

            input_video = f"temp_input.{file_ext}"
            with open(input_video, "wb") as f:
                f.write(uploaded_file.read())

            if st.button("🚀 MULAI KONVERSI VIDEO"):
                with st.spinner("⚡ Sedang me-render video via FFmpeg..."):
                    if "MP3" in pilihan_target:
                        output_file = "output_audio.mp3"
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
                        mime_out, out_name = "audio/mp3", f"{base_name}.mp3"

                    elif "Anti-Burik" in pilihan_target:
                        output_file = "output_video.mp4"
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
                            f"{base_name}_anti_burik.mp4",
                        )

                    elif "MOV" in pilihan_target:
                        output_file = "output_video.mov"
                        cmd = ["ffmpeg", "-y", "-i", input_video, output_file]
                        mime_out, out_name = (
                            "video/quicktime",
                            f"{base_name}.mov",
                        )

                    subprocess.run(cmd)

                st.balloons()
                st.success("🎉 Konversi video berhasil!")
                with open(output_file, "rb") as f:
                    st.download_button(
                        label="📥 DOWNLOAD HASIL KONVERSI",
                        data=f,
                        file_name=out_name,
                        mime=mime_out,
                    )

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
            '<div class="info-card"><div class="info-card-title">🔒 Aman & Privasi</div><div class="info-card-desc">File aman diproses lokal di Mac lo.</div></div>',
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            '<div class="info-card"><div class="info-card-title">♾️ Tanpa Batas</div><div class="info-card-desc">Bebas konversi kapan saja tanpa batas.</div></div>',
            unsafe_allow_html=True,
        )