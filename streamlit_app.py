import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Informasi Titrimetri",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 0.5rem;
    }
    .formula-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1E88E5;
        margin: 1rem 0;
    }
    .reaction-box {
        background-color: #FFF3E0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FF9800;
        margin: 1rem 0;
    }
    .result-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🧪 Sistem Informasi Titrimetri</h1>', unsafe_allow_html=True)

# Sidebar - Pilihan Jenis Titrasi
st.sidebar.title("📋 Menu Navigasi")
jenis_titrasi = st.sidebar.selectbox(
    "Pilih Jenis Titrasi:",
    ["Beranda", "Asidimetri-Alkalimetri", "Argentometri", "Kompleksometri", "Permanganometri", "Iodometri"]
)

# ============== BERANDA ==============
if jenis_titrasi == "Beranda":
    st.markdown("## Selamat Datang!")
    st.write("""
    Aplikasi ini menyediakan informasi lengkap tentang berbagai jenis titrasi dalam analisis titrimetri, 
    meliputi:
    - **Prinsip dasar** titrasi
    - **Alat dan bahan** yang digunakan
    - **Rumus perhitungan**
    - **Reaksi kimia**
    - **Bagan alur kerja**
    - **Kalkulator analisis hasil**
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 🔬 Asidimetri\nTitrasi asam-basa")
    with col2:
        st.info("### 🧂 Argentometri\nTitrasi pengendapan")
    with col3:
        st.info("### 🔗 Kompleksometri\nTitrasi pembentukan kompleks")
    
    col4, col5 = st.columns(2)
    with col4:
        st.info("### ⚡ Permanganometri\nTitrasi redoks dengan KMnO₄")
    with col5:
        st.info("### 🟤 Iodometri\nTitrasi redoks dengan Iodium")

    # Rumus Dasar Titrimetri
    st.markdown("---")
    st.markdown("## 📐 Rumus Dasar Titrimetri")
    
    st.latex(r"M_1 \times V_1 = M_2 \times V_2")
    st.caption("Untuk reaksi dengan perbandingan mol 1:1")
    
    st.latex(r"\frac{M_1 \times V_1}{n_1} = \frac{M_2 \times V_2}{n_2}")
    st.caption("Untuk reaksi dengan perbandingan mol berbeda")
    
    st.latex(r"\text{Kadar (\%)} = \frac{V \times M \times BE \times FP}{W \times 1000} \times 100\%")
    st.caption("Rumus perhitungan kadar")

# ============== ASIDIMETRI-ALKALIMETRI ==============
elif jenis_titrasi == "Asidimetri-Alkalimetri":
    st.markdown('<h2 class="sub-header">⚗️ Titrasi Asidimetri-Alkalimetri</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Prinsip", "🔧 Alat & Bahan", "📐 Rumus", "⚛️ Reaksi", "📊 Kalkulator"])
    
    with tab1:
        st.markdown("### Prinsip Dasar")
        st.write("""
        **Asidimetri** adalah titrasi untuk menentukan kadar basa dengan menggunakan larutan asam standar.
        
        **Alkalimetri** adalah titrasi untuk menentukan kadar asam dengan menggunakan larutan basa standar.
        
        **Titik ekuivalen** tercapai ketika mol asam = mol basa (atau sesuai stoikiometri reaksi).
        """)
        
        # Bagan Alur Kerja
        st.markdown("### 📋 Bagan Alur Kerja")
        st.markdown("""
        ```
        ┌─────────────────────────────────────────┐
        │     PERSIAPAN LARUTAN STANDAR           │
        │  (NaOH/HCl dengan konsentrasi pasti)    │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │     PIPET SAMPEL KE ERLENMEYER          │
        │         (Volume terukur)                │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │       TAMBAHKAN INDIKATOR               │
        │   (PP, MO, atau indikator lainnya)      │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │      TITRASI DENGAN BURET               │
        │  (Tetes demi tetes hingga TAT)          │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │     CATAT VOLUME TITRAN                 │
        │      HITUNG KADAR ANALIT                │
        └─────────────────────────────────────────┘
        ```
        """)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔬 Alat")
            st.write("""
            - Buret 50 mL
            - Erlenmeyer 250 mL
            - Pipet volume 10/25 mL
            - Gelas ukur
            - Statif dan klem buret
            - Corong
            - Botol semprot
            - Labu ukur
            """)
        with col2:
            st.markdown("### 🧪 Bahan")
            st.write("""
            - **Larutan Standar:**
              - NaOH 0,1 N (untuk asidimetri)
              - HCl 0,1 N (untuk alkalimetri)
            - **Indikator:**
              - Phenolphthalein (PP): pH 8,3-10
              - Methyl Orange (MO): pH 3,1-4,4
              - Methyl Red: pH 4,2-6,3
            - Aquadest
            """)
    
    with tab3:
        st.markdown("### 📐 Rumus Perhitungan")
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Rumus Dasar (Mol ekuivalen):**")
        st.latex(r"N_{asam} \times V_{asam} = N_{basa} \times V_{basa}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Rumus Kadar:**")
        st.latex(r"\text{Kadar (\%)} = \frac{V_{titran} \times N_{titran} \times BE_{analit} \times FP}{W_{sampel} \times 1000} \times 100\%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("**Keterangan:**")
        st.write("""
        - V = Volume (mL)
        - N = Normalitas (N)
        - BE = Berat Ekuivalen (g/ekuivalen)
        - FP = Faktor Pengenceran
        - W = Berat sampel (gram)
        """)
        
        st.markdown("**Berat Ekuivalen Umum:**")
        data_be = {
            "Senyawa": ["NaOH", "HCl", "H₂SO₄", "CH₃COOH", "Na₂CO₃", "NaHCO₃"],
            "BM (g/mol)": [40, 36.5, 98, 60, 106, 84],
            "Valensi": [1, 1, 2, 1, 2, 1],
            "BE (g/ekuiv)": [40, 36.5, 49, 60, 53, 84]
        }
        st.table(data_be)
    
    with tab4:
        st.markdown("### ⚛️ Reaksi Titrasi")
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Asam Kuat + Basa Kuat:**")
        st.latex(r"HCl + NaOH \rightarrow NaCl + H_2O")
        st.latex(r"H_2SO_4 + 2NaOH \rightarrow Na_2SO_4 + 2H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Asam Lemah + Basa Kuat:**")
        st.latex(r"CH_3COOH + NaOH \rightarrow CH_3COONa + H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Karbonat:**")
        st.latex(r"Na_2CO_3 + 2HCl \rightarrow 2NaCl + H_2O + CO_2")
        st.latex(r"NaHCO_3 + HCl \rightarrow NaCl + H_2O + CO_2")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 📊 Kalkulator Titrasi Asam-Basa")
        
        calc_type = st.radio("Pilih jenis perhitungan:", 
                            ["Hitung Normalitas", "Hitung Kadar (%)"])
        
        if calc_type == "Hitung Normalitas":
            col1, col2 = st.columns(2)
            with col1:
                v_titran = st.number_input("Volume Titran (mL):", min_value=0.0, value=10.0, step=0.1)
                n_titran = st.number_input("Normalitas Titran (N):", min_value=0.0, value=0.1, step=0.01)
            with col2:
                v_sampel = st.number_input("Volume Sampel (mL):", min_value=0.1, value=25.0, step=0.1)
            
            if st.button("Hitung Normalitas Sampel"):
                n_sampel = (v_titran * n_titran) / v_sampel
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.success(f"**Normalitas Sampel = {n_sampel:.4f} N**")
                st.markdown('</div>', unsafe_allow_html=True)
        
        else:
            col1, col2 = st.columns(2)
            with col1:
                v_titran = st.number_input("Volume Titran (mL):", min_value=0.0, value=10.0, step=0.1)
                n_titran = st.number_input("Normalitas Titran (N):", min_value=0.0, value=0.1, step=0.01)
                be_analit = st.number_input("BE Analit (g/ekuiv):", min_value=0.0, value=40.0, step=0.1)
            with col2:
                w_sampel = st.number_input("Berat Sampel (gram):", min_value=0.001, value=1.0, step=0.001)
                fp = st.number_input("Faktor Pengenceran:", min_value=1, value=1, step=1)
            
            if st.button("Hitung Kadar"):
                kadar = (v_titran * n_titran * be_analit * fp) / (w_sampel * 1000) * 100
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.success(f"**Kadar = {kadar:.4f} %**")
                st.latex(rf"\text{{Kadar}} = \frac{{{v_titran} \times {n_titran} \times {be_analit} \times {fp}}}{{{w_sampel} \times 1000}} \times 100\% = {kadar:.4f}\%")
                st.markdown('</div>', unsafe_allow_html=True)

# ============== ARGENTOMETRI ==============
elif jenis_titrasi == "Argentometri":
    st.markdown('<h2 class="sub-header">🧂 Titrasi Argentometri</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Prinsip", "🔧 Alat & Bahan", "📐 Rumus", "⚛️ Reaksi", "📊 Kalkulator"])
    
    with tab1:
        st.markdown("### Prinsip Dasar")
        st.write("""
        **Argentometri** adalah titrasi pengendapan menggunakan larutan standar AgNO₃ untuk menentukan kadar halida (Cl⁻, Br⁻, I⁻) atau senyawa lain yang membentuk endapan dengan Ag⁺.
        
        **Metode Argentometri:**
        1. **Metode Mohr** - Indikator K₂CrO₄
        2. **Metode Volhard** - Indikator Fe³⁺ (titrasi balik)
        3. **Metode Fajans** - Indikator adsorpsi
        """)
        
        st.markdown("### 📋 Bagan Alur Kerja (Metode Mohr)")
        st.markdown("""
        ```
        ┌─────────────────────────────────────────┐
        │   PIPET SAMPEL (larutan halida)         │
        │        ke Erlenmeyer                    │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │    TAMBAH INDIKATOR K₂CrO₄ 5%           │
        │         (2-3 tetes)                     │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │    TITRASI DENGAN AgNO₃ STANDAR         │
        │   (kocok terus sampai TAT)              │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │   TAT: Endapan merah bata Ag₂CrO₄       │
        │        (permanen)                       │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │     CATAT VOLUME & HITUNG KADAR         │
        └─────────────────────────────────────────┘
        ```
        """)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔬 Alat")
            st.write("""
            - Buret 50 mL (hindari buret kaca untuk AgNO₃)
            - Erlenmeyer 250 mL
            - Pipet volume
            - Gelas ukur
            - Statif dan klem
            - Botol coklat (untuk AgNO₃)
            """)
        with col2:
            st.markdown("### 🧪 Bahan")
            st.write("""
            - **Larutan Standar:** AgNO₃ 0,1 N
            - **Indikator:**
              - K₂CrO₄ 5% (Mohr)
              - Fe-amonium sulfat (Volhard)
              - Fluorescein/Eosin (Fajans)
            - KSCN 0,1 N (untuk Volhard)
            - Aquadest
            """)
    
    with tab3:
        st.markdown("### 📐 Rumus Perhitungan")
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Metode Mohr (Langsung):**")
        st.latex(r"\text{Kadar Cl}^- (\%) = \frac{V_{AgNO_3} \times N_{AgNO_3} \times BE_{Cl} \times FP}{W_{sampel} \times 1000} \times 100\%")
        st.markdown("BE Cl⁻ = 35,5 g/ekuiv")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Metode Volhard (Titrasi Balik):**")
        st.latex(r"\text{Kadar Cl}^- = \frac{(V_{AgNO_3} \times N_{AgNO_3}) - (V_{KSCN} \times N_{KSCN})}{W} \times BE_{Cl} \times 100\%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("**Data Berat Ekuivalen:**")
        data_be = {
            "Ion": ["Cl⁻", "Br⁻", "I⁻", "NaCl", "KCl", "KBr"],
            "BE (g/ekuiv)": [35.5, 80, 127, 58.5, 74.5, 119]
        }
        st.table(data_be)
    
    with tab4:
        st.markdown("### ⚛️ Reaksi Titrasi")
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Utama:**")
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl \downarrow \text{ (putih)}")
        st.latex(r"Ag^+ + Br^- \rightarrow AgBr \downarrow \text{ (kuning pucat)}")
        st.latex(r"Ag^+ + I^- \rightarrow AgI \downarrow \text{ (kuning)}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Indikator (Mohr):**")
        st.latex(r"2Ag^+ + CrO_4^{2-} \rightarrow Ag_2CrO_4 \downarrow \text{ (merah bata)}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Volhard:**")
        st.latex(r"Ag^+ + SCN^- \rightarrow AgSCN \downarrow \text{ (putih)}")
        st.latex(r"Fe^{3+} + SCN^- \rightarrow FeSCN^{2+} \text{ (merah)}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 📊 Kalkulator Argentometri")
        
        metode = st.radio("Pilih Metode:", ["Mohr (Langsung)", "Volhard (Titrasi Balik)"])
        
        if metode == "Mohr (Langsung)":
            col1, col2 = st.columns(2)
            with col1:
                v_ag = st.number_input("Volume AgNO₃ (mL):", min_value=0.0, value=10.0, step=0.1)
                n_ag = st.number_input("Normalitas AgNO₃ (N):", min_value=0.0, value=0.1, step=0.01)
            with col2:
                be = st.number_input("BE Analit (g/ekuiv):", min_value=0.0, value=35.5, step=0.1)
                w = st.number_input("Berat Sampel (gram):", min_value=0.001, value=1.0, step=0.001)
                fp = st.number_input("Faktor Pengenceran:", min_value=1, value=1)
            
            if st.button("Hitung Kadar"):
                kadar = (v_ag * n_ag * be * fp) / (w * 1000) * 100
                st.success(f"**Kadar = {kadar:.4f} %**")
        
        else:  # Volhard
            col1, col2 = st.columns(2)
            with col1:
                v_ag = st.number_input("Volume AgNO₃ ditambahkan (mL):", min_value=0.0, value=25.0)
                n_ag = st.number_input("Normalitas AgNO₃ (N):", min_value=0.0, value=0.1)
                v_kscn = st.number_input("Volume KSCN titrasi (mL):", min_value=0.0, value=5.0)
            with col2:
                n_kscn = st.number_input("Normalitas KSCN (N):", min_value=0.0, value=0.1)
                be = st.number_input("BE Analit (g/ekuiv):", min_value=0.0, value=35.5)
                w = st.number_input("Berat Sampel (gram):", min_value=0.001, value=1.0)
            
            if st.button("Hitung Kadar"):
                meq_ag = v_ag * n_ag
                meq_kscn = v_kscn * n_kscn
                meq_cl = meq_ag - meq_kscn
                kadar = (meq_cl * be) / (w * 1000) * 100
                st.success(f"**Kadar = {kadar:.4f} %**")
                st.write(f"mEq AgNO₃ = {meq_ag:.4f}")
                st.write(f"mEq KSCN = {meq_kscn:.4f}")
                st.write(f"mEq Cl⁻ = {meq_cl:.4f}")

# ============== KOMPLEKSOMETRI ==============
elif jenis_titrasi == "Kompleksometri":
    st.markdown('<h2 class="sub-header">🔗 Titrasi Kompleksometri</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Prinsip", "🔧 Alat & Bahan", "📐 Rumus", "⚛️ Reaksi", "📊 Kalkulator"])
    
    with tab1:
        st.markdown("### Prinsip Dasar")
        st.write("""
        **Kompleksometri** adalah titrasi berdasarkan pembentukan senyawa kompleks antara ion logam dengan ligan (umumnya EDTA).
        
        **EDTA** (Ethylenediaminetetraacetic acid) adalah ligan heksadentat yang membentuk kompleks 1:1 dengan ion logam.
        
        **Aplikasi:** Penentuan kesadahan air (Ca²⁺, Mg²⁺), analisis logam berat.
        """)
        
        st.markdown("### 📋 Bagan Alur Kerja")
        st.markdown("""
        ```
        ┌─────────────────────────────────────────┐
        │    PIPET SAMPEL (larutan logam)         │
        │         ke Erlenmeyer                   │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │    TAMBAH BUFFER pH 10 (untuk Ca/Mg)    │
        │         (5-10 mL)                       │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │     TAMBAH INDIKATOR EBT/Murexide       │
        │         (sedikit, warna merah)          │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │       TITRASI DENGAN Na₂EDTA            │
        │   (sampai perubahan warna)              │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │   TAT: Merah → Biru (EBT)               │
        │        Merah → Ungu (Murexide)          │
        └─────────────────────────────────────────┘
        ```
        """)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔬 Alat")
            st.write("""
            - Buret 50 mL
            - Erlenmeyer 250 mL
            - Pipet volume
            - Gelas ukur
            - Statif dan klem
            - pH meter/kertas pH
            """)
        with col2:
            st.markdown("### 🧪 Bahan")
            st.write("""
            - **Larutan Standar:** Na₂EDTA 0,01 M
            - **Buffer:**
              - Buffer pH 10 (NH₄Cl + NH₄OH) untuk Ca+Mg
              - NaOH 2N untuk Ca saja
            - **Indikator:**
              - EBT (Eriochrome Black T)
              - Murexide (untuk Ca)
              - PAN, Xylenol Orange
            """)
    
    with tab3:
        st.markdown("### 📐 Rumus Perhitungan")
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Rumus Kesadahan Total (sebagai CaCO₃):**")
        st.latex(r"\text{Kesadahan (mg/L CaCO}_3) = \frac{V_{EDTA} \times M_{EDTA} \times 1000 \times 100}{V_{sampel}}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Rumus Kadar Logam:**")
        st.latex(r"\text{Kadar (mg/L)} = \frac{V_{EDTA} \times M_{EDTA} \times BA_{logam} \times 1000}{V_{sampel}}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("**Data Berat Atom Logam:**")
        data_ba = {
            "Logam": ["Ca²⁺", "Mg²⁺", "Zn²⁺", "Cu²⁺", "Fe³⁺", "Pb²⁺"],
            "BA (g/mol)": [40.08, 24.31, 65.38, 63.55, 55.85, 207.2]
        }
        st.table(data_ba)
    
    with tab4:
        st.markdown("### ⚛️ Reaksi Titrasi")
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Utama dengan EDTA:**")
        st.latex(r"Ca^{2+} + EDTA^{4-} \rightarrow [Ca-EDTA]^{2-}")
        st.latex(r"Mg^{2+} + EDTA^{4-} \rightarrow [Mg-EDTA]^{2-}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi dengan Indikator EBT:**")
        st.write("Sebelum TAT:")
        st.latex(r"M^{2+} + EBT \rightarrow M-EBT \text{ (merah anggur)}")
        st.write("Saat TAT:")
        st.latex(r"M-EBT + EDTA \rightarrow M-EDTA + EBT \text{ (biru)}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 📊 Kalkulator Kompleksometri")
        
        calc_type = st.radio("Pilih Perhitungan:", 
                            ["Kesadahan Total (CaCO₃)", "Kadar Logam Spesifik"])
        
        if calc_type == "Kesadahan Total (CaCO₃)":
            col1, col2 = st.columns(2)
            with col1:
                v_edta = st.number_input("Volume Na₂EDTA (mL):", min_value=0.0, value=10.0)
                m_edta = st.number_input("Molaritas Na₂EDTA (M):", min_value=0.0, value=0.01, format="%.4f")
            with col2:
                v_sampel = st.number_input("Volume Sampel (mL):", min_value=0.1, value=50.0)
            
            if st.button("Hitung Kesadahan"):
                kesadahan = (v_edta * m_edta * 1000 * 100) / v_sampel
                st.success(f"**Kesadahan Total = {kesadahan:.2f} mg/L sebagai CaCO₃**")
                
                # Klasifikasi kesadahan
                if kesadahan < 75:
                    st.info("Klasifikasi: Air Lunak (Soft)")
                elif kesadahan < 150:
                    st.info("Klasifikasi: Air Sedang (Moderately Hard)")
                elif kesadahan < 300:
                    st.warning("Klasifikasi: Air Sadah (Hard)")
                else:
                    st.error("Klasifikasi: Air Sangat Sadah (Very Hard)")
        
        else:
            col1, col2 = st.columns(2)
            with col1:
                v_edta = st.number_input("Volume Na₂EDTA (mL):", min_value=0.0, value=10.0)
                m_edta = st.number_input("Molaritas Na₂EDTA (M):", min_value=0.0, value=0.01, format="%.4f")
            with col2:
                v_sampel = st.number_input("Volume Sampel (mL):", min_value=0.1, value=50.0)
                ba_logam = st.number_input("BA Logam (g/mol):", min_value=0.0, value=40.08)
            
            if st.button("Hitung Kadar"):
                kadar = (v_edta * m_edta * ba_logam * 1000) / v_sampel
                st.success(f"**Kadar Logam = {kadar:.4f} mg/L**")

# ============== PERMANGANOMETRI ==============
elif jenis_titrasi == "Permanganometri":
    st.markdown('<h2 class="sub-header">⚡ Titrasi Permanganometri</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Prinsip", "🔧 Alat & Bahan", "📐 Rumus", "⚛️ Reaksi", "📊 Kalkulator"])
    
    with tab1:
        st.markdown("### Prinsip Dasar")
        st.write("""
        **Permanganometri** adalah titrasi redoks menggunakan larutan standar KMnO₄ (kalium permanganat).
        
        KMnO₄ bersifat sebagai **oksidator kuat** dan berubah warna dari ungu menjadi tidak berwarna (Mn²⁺) dalam suasana asam.
        
        **Keunggulan:** Tidak memerlukan indikator tambahan (autoindikator).
        
        **Aplikasi:** Penentuan Fe²⁺, H₂O₂, asam oksalat, COD air.
        """)
        
        st.markdown("### 📋 Bagan Alur Kerja")
        st.markdown("""
        ```
        ┌─────────────────────────────────────────┐
        │    PIPET SAMPEL ke Erlenmeyer           │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │    TAMBAH H₂SO₄ (suasana asam)          │
        │         atau H₃PO₄                      │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │   PANASKAN (untuk asam oksalat)         │
        │        70-80°C                          │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │      TITRASI DENGAN KMnO₄               │
        │   (tetes demi tetes, kocok)             │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │   TAT: Warna ungu muda permanen         │
        │        (30 detik tidak hilang)          │
        └─────────────────────────────────────────┘
        ```
        """)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔬 Alat")
            st.write("""
            - Buret 50 mL (coklat/amber)
            - Erlenmeyer 250 mL
            - Pipet volume
            - Pemanas/hot plate
            - Statif dan klem
            - Gelas ukur
            """)
        with col2:
            st.markdown("### 🧪 Bahan")
            st.write("""
            - **Larutan Standar:** KMnO₄ 0,1 N
            - **Pengasam:** H₂SO₄ 2N atau 4N
            - **Standar Primer:** Na₂C₂O₄ (natrium oksalat)
            - Aquadest (bebas organik)
            - H₃PO₄ (untuk titrasi Fe)
            """)
    
    with tab3:
        st.markdown("### 📐 Rumus Perhitungan")
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Rumus Kadar:**")
        st.latex(r"\text{Kadar (\%)} = \frac{V_{KMnO_4} \times N_{KMnO_4} \times BE_{analit}}{W_{sampel} \times 1000} \times FP \times 100\%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("**Berat Ekuivalen dalam Permanganometri:**")
        st.write("KMnO₄ dalam suasana asam: Mn⁷⁺ → Mn²⁺ (menerima 5e⁻)")
        st.latex(r"BE_{KMnO_4} = \frac{BM}{5} = \frac{158}{5} = 31.6 \text{ g/ekuiv}")
        
        data_be = {
            "Senyawa": ["KMnO₄", "Fe²⁺", "H₂C₂O₄", "Na₂C₂O₄", "H₂O₂", "FeSO₄·7H₂O"],
            "BM": [158, 56, 90, 134, 34, 278],
            "Elektron Transfer": [5, 1, 2, 2, 2, 1],
            "BE": [31.6, 56, 45, 67, 17, 278]
        }
        st.table(data_be)
    
    with tab4:
        st.markdown("### ⚛️ Reaksi Titrasi")
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Setengah Sel KMnO₄ (Asam):**")
        st.latex(r"MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Titrasi Asam Oksalat:**")
        st.latex(r"2KMnO_4 + 5H_2C_2O_4 + 3H_2SO_4 \rightarrow")
        st.latex(r"2MnSO_4 + K_2SO_4 + 10CO_2 + 8H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Titrasi Fe²⁺:**")
        st.latex(r"MnO_4^- + 5Fe^{2+} + 8H^+ \rightarrow Mn^{2+} + 5Fe^{3+} + 4H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Titrasi H₂O₂:**")
        st.latex(r"2KMnO_4 + 5H_2O_2 + 3H_2SO_4 \rightarrow")
        st.latex(r"2MnSO_4 + K_2SO_4 + 5O_2 + 8H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 📊 Kalkulator Permanganometri")
        
        analit = st.selectbox("Pilih Analit:", 
                             ["Fe²⁺ (BE=56)", "Asam Oksalat (BE=45)", "H₂O₂ (BE=17)", "Custom"])
        
        col1, col2 = st.columns(2)
        with col1:
            v_kmno4 = st.number_input("Volume KMnO₄ (mL):", min_value=0.0, value=10.0)
            n_kmno4 = st.number_input("Normalitas KMnO₄ (N):", min_value=0.0, value=0.1)
        with col2:
            w_sampel = st.number_input("Berat Sampel (gram):", min_value=0.001, value=1.0)
            fp = st.number_input("Faktor Pengenceran:", min_value=1, value=1)
            
            if analit == "Custom":
                be = st.number_input("BE Analit (g/ekuiv):", min_value=0.0, value=50.0)
            elif analit == "Fe²⁺ (BE=56)":
                be = 56
            elif analit == "Asam Oksalat (BE=45)":
                be = 45
            else:
                be = 17
        
        if st.button("Hitung Kadar"):
            kadar = (v_kmno4 * n_kmno4 * be * fp) / (w_sampel * 1000) * 100
            st.success(f"**Kadar {analit.split('(')[0].strip()} = {kadar:.4f} %**")

# ============== IODOMETRI ==============
elif jenis_titrasi == "Iodometri":
    st.markdown('<h2 class="sub-header">🟤 Titrasi Iodometri/Iodimetri</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Prinsip", "🔧 Alat & Bahan", "📐 Rumus", "⚛️ Reaksi", "📊 Kalkulator"])
    
    with tab1:
        st.markdown("### Prinsip Dasar")
        st.write("""
        **Iodimetri** adalah titrasi langsung menggunakan larutan I₂ standar untuk menentukan reduktor.
        
        **Iodometri** adalah titrasi tidak langsung, di mana oksidator bereaksi dengan KI berlebih menghasilkan I₂, 
        kemudian I₂ dititrasi dengan Na₂S₂O₃ (natrium tiosulfat).
        
        **Aplikasi:** Penentuan Cu²⁺, vitamin C, ClO⁻, SO₂, bilangan iod/peroksida.
        """)
        
        st.markdown("### 📋 Bagan Alur Kerja (Iodometri)")
        st.markdown("""
        ```
        ┌─────────────────────────────────────────┐
        │   PIPET SAMPEL (oksidator)              │
        │        ke Erlenmeyer                    │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │   TAMBAH KI BERLEBIH + ASAM             │
        │   (diamkan di tempat gelap)             │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │      I₂ TERBENTUK (warna coklat)        │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │    TITRASI DENGAN Na₂S₂O₃               │
        │   (sampai kuning muda)                  │
        └─────────────────────┬───────────────────┘
                              ▼
        ┌─────────────────────────────────────────┐
        │      TAMBAH AMILUM (biru)               │
        │   Lanjutkan titrasi → TAT tidak berwarna│
        └─────────────────────────────────────────┘
        ```
        """)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔬 Alat")
            st.write("""
            - Buret 50 mL (coklat/tutup)
            - Erlenmeyer 250 mL (tutup)
            - Pipet volume
            - Gelas ukur
            - Statif dan klem
            - Tempat gelap
            """)
        with col2:
            st.markdown("### 🧪 Bahan")
            st.write("""
            - **Larutan Standar:**
              - Na₂S₂O₃ 0,1 N
              - I₂ 0,1 N
            - **Reagen:**
              - KI 10%
              - HCl/H₂SO₄ encer
            - **Indikator:** Amilum (kanji) 1%
            - Aquadest bebas oksigen
            """)
    
    with tab3:
        st.markdown("### 📐 Rumus Perhitungan")
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Rumus Iodometri:**")
        st.latex(r"\text{Kadar (\%)} = \frac{V_{Na_2S_2O_3} \times N_{Na_2S_2O_3} \times BE_{analit}}{W_{sampel} \times 1000} \times FP \times 100\%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.markdown("**Bilangan Iod (minyak/lemak):**")
        st.latex(r"\text{Bilangan Iod} = \frac{(V_{blanko} - V_{sampel}) \times N_{Na_2S_2O_3} \times 12.69}{W_{sampel}}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("**Berat Ekuivalen:**")
        data_be = {
            "Senyawa": ["I₂", "Na₂S₂O₃", "Cu²⁺", "Vitamin C", "ClO⁻"],
            "BM": [254, 158, 64, 176, 51.5],
            "Elektron Transfer": [2, 1, 1, 2, 2],
            "BE": [127, 158, 64, 88, 25.75]
        }
        st.table(data_be)
    
    with tab4:
        st.markdown("### ⚛️ Reaksi Titrasi")
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Tiosulfat dengan Iod:**")
        st.latex(r"2Na_2S_2O_3 + I_2 \rightarrow Na_2S_4O_6 + 2NaI")
        st.latex(r"2S_2O_3^{2-} + I_2 \rightarrow S_4O_6^{2-} + 2I^-")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Pembebasan I₂ dari Oksidator:**")
        st.latex(r"2Cu^{2+} + 4I^- \rightarrow 2CuI + I_2")
        st.latex(r"ClO^- + 2H^+ + 2I^- \rightarrow Cl^- + I_2 + H_2O")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="reaction-box">', unsafe_allow_html=True)
        st.markdown("**Reaksi Amilum-Iod:**")
        st.write("I₂ + Amilum → Kompleks biru (deteksi TAT)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 📊 Kalkulator Iodometri")
        
        calc_type = st.radio("Pilih Perhitungan:", 
                            ["Kadar Analit", "Bilangan Iod"])
        
        if calc_type == "Kadar Analit":
            col1, col2 = st.columns(2)
            with col1:
                v_tio = st.number_input("Volume Na₂S₂O₃ (mL):", min_value=0.0, value=10.0)
                n_tio = st.number_input("Normalitas Na₂S₂O₃ (N):", min_value=0.0, value=0.1)
            with col2:
                be = st.number_input("BE Analit (g/ekuiv):", min_value=0.0, value=64.0)
                w = st.number_input("Berat Sampel (gram):", min_value=0.001, value=1.0)
                fp = st.number_input("Faktor Pengenceran:", min_value=1, value=1)
            
            if st.button("Hitung Kadar"):
                kadar = (v_tio * n_tio * be * fp) / (w * 1000) * 100
                st.success(f"**Kadar = {kadar:.4f} %**")
        
        else:  # Bilangan Iod
            col1, col2 = st.columns(2)
            with col1:
                v_blanko = st.number_input("Volume Blanko (mL):", min_value=0.0, value=25.0)
                v_sampel = st.number_input("Volume Sampel (mL):", min_value=0.0, value=15.0)
            with col2:
                n_tio = st.number_input("Normalitas Na₂S₂O₃ (N):", min_value=0.0, value=0.1)
                w = st.number_input("Berat Sampel (gram):", min_value=0.001, value=0.5)
            
            if st.button("Hitung Bilangan Iod"):
                bil_iod = ((v_blanko - v_sampel) * n_tio * 12.69) / w
                st.success(f"**Bilangan Iod = {bil_iod:.2f} g I₂/100g**")
                
                # Interpretasi
                if bil_iod < 100:
                    st.info("Klasifikasi: Minyak/Lemak Non-Drying")
                elif bil_iod < 130:
                    st.info("Klasifikasi: Minyak/Lemak Semi-Drying")
                else:
                    st.info("Klasifikasi: Minyak/Lemak Drying")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🧪 Sistem Informasi Titrimetri | Dibuat dengan Streamlit</p>
</div>
""", unsafe_allow_html=True)
