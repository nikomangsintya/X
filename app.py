import streamlit as st
from datetime import datetime


# ==============================
# KONFIGURASI
# ==============================

st.set_page_config(
    page_title="Kalkulator FPB & KPK",
    page_icon="🧮",
    layout="centered"
)


# ==============================
# RIWAYAT
# ==============================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []


# ==============================
# DESAIN CSS
# ==============================

st.markdown("""
<style>

.stApp{
    background:#eaf6ff;
}


h1{
    color:#1565c0;
    text-align:center;
}


h2,h3{
    color:#1976d2;
}


.stButton button{
    width:100%;
    background:#42a5f5;
    color:white;
    border-radius:10px;
    height:45px;
    font-size:18px;
}


.card{

    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 12px #b0bec5;

}


.history{

    background:white;
    padding:12px;
    border-radius:10px;
    margin:8px 0;

}


</style>
""", unsafe_allow_html=True)



# ==============================
# BACKGROUND SIMBOL MATEMATIKA
# ==============================

st.markdown("""
<div style="
position:fixed;
z-index:-1;
opacity:0.08;
font-size:80px;
color:#1565c0;
">

π ∑ √ ∞ λ θ ∆ ∫
<br>
∞ √ π ∑ λ θ ∫
<br>
∆ π √ ∞ ∑ λ

</div>
""", unsafe_allow_html=True)



# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.title("🧮 Menu")

    st.write(
    """
    **Kalkulator FPB dan KPK**

    Metode:

    ✔ Algoritma Euclid

    ✔ Rumus KPK

    ✔ Riwayat Perhitungan
    """
    )


# ==============================
# JUDUL
# ==============================

st.title("🧮 Kalkulator FPB dan KPK")

st.write(
"""
Aplikasi Teori Bilangan untuk menghitung
**Faktor Persekutuan Terbesar (FPB)** dan
**Kelipatan Persekutuan Terkecil (KPK)**.
"""
)



# ==============================
# FUNGSI EUCLID
# ==============================

def euclid(a,b):

    langkah=[]

    while b != 0:

        q=a//b
        r=a%b

        langkah.append(
            {
                "a":a,
                "b":b,
                "q":q,
                "r":r
            }
        )

        a,b=b,r

    return a, langkah



# ==============================
# INPUT
# ==============================

col1,col2 = st.columns(2)


with col1:

    angka1 = st.number_input(
        "Bilangan pertama",
        min_value=1,
        value=10
    )


with col2:

    angka2 = st.number_input(
        "Bilangan kedua",
        min_value=1,
        value=5
    )



# ==============================
# HITUNG
# ==============================

if st.button("🔍 Hitung"):


    fpb, langkah = euclid(
        int(angka1),
        int(angka2)
    )


    kpk = (int(angka1)*int(angka2))//fpb



    # simpan riwayat

    waktu=datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )


    st.session_state.riwayat.insert(
        0,
        f"{angka1} dan {angka2} → FPB {fpb}, KPK {kpk} ({waktu})"
    )



    # ======================
    # HASIL
    # ======================

    a,b=st.columns(2)


    with a:

        st.markdown(
        f"""
        <div class="card">

        <h2>FPB</h2>

        <h1>{fpb}</h1>

        </div>
        """,
        unsafe_allow_html=True
        )


    with b:

        st.markdown(
        f"""
        <div class="card">

        <h2>KPK</h2>

        <h1>{kpk}</h1>

        </div>
        """,
        unsafe_allow_html=True
        )



    st.divider()



    # ======================
    # LANGKAH EUCLID
    # ======================

    st.subheader("📖 Langkah Algoritma Euclid")


    for i,data in enumerate(langkah,1):

        st.write(
            f"### Langkah {i}"
        )


        st.write(
            f"{data['a']} ÷ {data['b']} = "
            f"{data['q']} sisa {data['r']}"
        )


        st.latex(
            f"{data['a']}={data['q']}\\times{data['b']}+{data['r']}"
        )


        if data["r"]!=0:

            st.info(
            "Sisa tidak nol, maka proses dilanjutkan."
            )

        else:

            st.success(
            "Sisa sama dengan nol, proses berhenti."
            )



    # ======================
    # RUMUS KPK
    # ======================


    st.divider()

    st.subheader("🎯 Perhitungan KPK")


    st.write(
        "Menggunakan rumus:"
    )


    st.latex(
        r"KPK(a,b)=\frac{a \times b}{FPB(a,b)}"
    )


    st.latex(
        rf"KPK({angka1},{angka2})="
        rf"\frac{{{angka1}\times{angka2}}}{{{fpb}}}"
    )


    st.latex(
        rf"={kpk}"
    )



# ==============================
# RIWAYAT
# ==============================

st.divider()

st.subheader("🕘 Riwayat Perhitungan")


if st.session_state.riwayat:


    for r in st.session_state.riwayat:

        st.markdown(
        f"""
        <div class="history">
        {r}
        </div>
        """,
        unsafe_allow_html=True
        )

else:

    st.info(
        "Belum ada riwayat."
    )



# ==============================
# FOOTER
# ==============================

st.divider()

st.caption(
    "🧮 Kalkulator Teori Bilangan | Algoritma Euclid"
)
