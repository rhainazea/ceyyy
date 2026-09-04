import streamlit as st

# ==============================
# KONFIGURASI HALAMAN
# ==============================
st.set_page_config(
    page_title="halawwww ceyyyy 👋🏻👋🏻👋🏻",
    page_icon="⁉️",
    layout="centered"
)

# ==============================
# CSS
# ==============================
st.markdown("""
<style>

    /* Background utama */
    .stApp {
        background-color: #3B2418;
        color: #E8C39E;
    }

    /* Hilangkan header Streamlit */
    header {
        visibility: hidden;
    }

    /* Container */
    .block-container {
        padding-top: 5rem;
        padding-bottom: 4rem;
        max-width: 850px;
    }

    /* Judul utama */
    .judul {
        text-align: center;
        color: #D9A679;
        font-size: 65px;
        font-weight: 800;
        margin-top: 80px;
        margin-bottom: 20px;
        letter-spacing: 2px;
    }

    /* Subtitle */
    .subjudul {
        text-align: center;
        color: #E8C39E;
        font-size: 20px;
        line-height: 1.7;
        margin-bottom: 45px;
    }

    /* Judul halaman kedua */
    .judul-cerita {
        color: #D9A679;
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 35px;
    }

    /* Kotak cerita */
    .cerita {
        background-color: #4A2D20;
        border: 2px solid #9C6B48;
        border-radius: 25px;
        padding: 35px;
        color: #F0D1B2;
        font-size: 18px;
        line-height: 1.9;
        text-align: justify;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.25);
    }

    /* Tombol */
    div.stButton > button {
        width: 100%;
        background-color: #C28B62;
        color: #3B2418;
        border: none;
        border-radius: 20px;
        padding: 15px 25px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #D9A679;
        color: #3B2418;
        transform: scale(1.02);
    }

    /* Emoji */
    .emoji {
        text-align: center;
        font-size: 35px;
        margin-bottom: 10px;
    }

    /* Foto halaman 2 */
    .foto {
        border-radius: 25px;
        overflow: hidden;
        margin-bottom: 35px;
    }

</style>
""", unsafe_allow_html=True)


# ==============================
# SESSION STATE
# ==============================
if "halaman" not in st.session_state:
    st.session_state.halaman = 1


# ==============================
# HALAMAN 1 - MENU UTAMA
# ==============================
if st.session_state.halaman == 1:

    st.markdown(
        "<div class='emoji'>😾😾😾😾</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='judul'>halawwww ceyyyy</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='subjudul'>
        kaget yaa dan pasti bingung yaa ini apa wkwk <br>
        biar ga bingung kamu klik icon di kiri bawah yaa
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("➡️"):
        st.session_state.halaman = 2
        st.rerun()


# ==============================
# HALAMAN 2 - CERITA
# ==============================
elif st.session_state.halaman == 2:

    st.markdown(
        "<div class='judul-cerita'>halawww ceyyyyy</div>",
        unsafe_allow_html=True
    )

    # ==============================
    # FOTO
    # ==============================

    st.image(
        "https://cdn.phototourl.com/free/2026-09-04-299e4086-352e-4282-9782-80f5f9a18b6a.jpg",
        use_container_width=True
    )

    st.write("")
    st.write("")

    # ==============================
    # CERITA
    # ==============================

    st.markdown(
        """
        <div class='cerita'>

        halawww inii nama nya c yg poni nya patah patah kaya jagunggg 🤪🤪
        pasti orang- orang asing denger nama nya aneh karna cuma satu huruf wkwk.
        yaa itu dehh yang aku rasain pas kenalan di awal, kaya ngerasa aneh gitu
        <b>"*masa si nama nya c doangg*"</b> tapi emang itu panggilan nyaa.

        <br><br>

        AKUUUU..... MANGGILNYA BUKAN C TAPIIII
        <b>CEYYYY</b> pengen beda aja si dari orang oranggg, soalnya aku gamau di samain
        sama orang.

        <br><br>

        setelah 4 tahun apa ya kalo ga salah aku baru ketemu c lg,
        pokonyaa terakhir itu smp dehh abistu uda gaperna ketemu lg.
        TAPI....... aku suka stalk akun scc nya sii di akun ituu ✌🏼✌🏼
        ketemu lg nya juga aneh bgtt lg menurut akuu, masa ngajak si kk main tp ngajak aku jg!!??
        maksudnya gimana yakk??? tp ternyata itu katanya spikk ajaa 🆙🆙

        truss besok nya main lg denggg, dan itu kayanya first time main ber2 gasi??
        iyaalaa mana perna kita mainn.

        setelah kurang lebih sebulan ga ke bogor lg,
        tp malem ituu c ajak aku ke bogor KE KINAA.
        disana aku banyak cerita c jugaa.

        aku suka deh c yappingg kaya seneng aja dengerin nyaa,
        udaa dehh dari main itu jadi dekett sm c,
        tp sebenernya aku tu takutt gitu klo di ajak main,
        takutnya banyakk diem huhu 😭

        lebih ke takut salah ngomong gituu,
        sedangkan c anak nyaa ekstrovertt bgtttttt,
        apa aja, kayanya si dia diem klo cengengg aja dehh hehe,
        soalnya c tu <b>cengenggg</b> 👎🏼👎🏼👎🏼👎🏼

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    if st.button("➡️"):
        st.session_state.halaman = 3
        st.rerun()


# ==============================
# HALAMAN 3 - PENUTUP SEMENTARA
# ==============================
elif st.session_state.halaman == 3:

    st.markdown(
        "<div class='emoji'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='judul-cerita'>.</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='cerita'>

        ternyata dari yang awalnya cuma kenal satu huruf,
        terus dipanggil beda sendiri jadi <b>ceyyyy</b>,
        akhirnya malah jadi sedeket ini wkwkwk 🤎

        <br><br>

        lucu juga yaa kalo dipikir-pikir,
        dari yang awalnya takut bakal banyak diem,
        takut salah ngomong,
        malah akhirnya bisa cerita banyak dan
        betah dengerin c yappinggg 😭

        <br><br>

        dan ternyata...
        perjalanan kita baru mulai dari sini 🌽🤎

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    if st.button("➡️"):
        st.session_state.halaman = 1
        st.rerun()
