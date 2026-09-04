import streamlit as st

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================

st.set_page_config(
    page_title="halawwww ceyyyy 🤎",
    page_icon="🌽",
    layout="centered"
)

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = 1


# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

    /* =========================
       BACKGROUND
    ========================= */

    .stApp {
        background-color: #352016;
    }

    header {
        visibility: hidden;
    }

    .block-container {
        max-width: 850px;
        padding-top: 4rem;
        padding-bottom: 4rem;
    }


    /* =========================
       SEMUA TEKS
    ========================= */

    p, span, label, div {
        color: white;
    }


    /* =========================
       HALAMAN UTAMA
    ========================= */

    .welcome {
        text-align: center;
        margin-top: 100px;
    }

    .welcome-emoji {
        font-size: 45px;
        margin-bottom: 15px;
    }

    .welcome-title {
        color: white !important;
        font-size: 65px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }

    .welcome-text {
        color: white !important;
        font-size: 20px;
        line-height: 1.8;
        margin-bottom: 45px;
    }


    /* =========================
       JUDUL CERITA
    ========================= */

    .story-title {
        text-align: center;
        color: white !important;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 30px;
    }


    /* =========================
       KOTAK CERITA
    ========================= */

    .story-box {
        background-color: #4A2B1E;
        border: 2px solid #81563E;
        border-radius: 25px;
        padding: 35px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.25);
    }

    .story-text {
        color: white !important;
        font-size: 18px;
        line-height: 2;
        text-align: justify;
    }

    .story-text b {
        color: white !important;
    }


    /* =========================
       TOMBOL
    ========================= */

    div.stButton > button {
        width: 100%;
        height: 55px;

        background-color: #B9825B;
        color: white !important;

        border: none;
        border-radius: 18px;

        font-size: 18px;
        font-weight: 700;

        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #96633F;
        color: white !important;
        transform: scale(1.02);
    }


    /* =========================
       PENUTUP
    ========================= */

    .ending {
        text-align: center;
        margin-top: 100px;
    }

    .ending-emoji {
        font-size: 50px;
        margin-bottom: 20px;
    }

    .ending-title {
        color: white !important;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 30px;
    }


</style>
""", unsafe_allow_html=True)


# ==================================================
# HALAMAN 1
# ==================================================

if st.session_state.page == 1:

    st.markdown("""
        <div class="welcome">

            <div class="welcome-emoji">
                🌽🤎
            </div>

            <div class="welcome-title">
                halawwww ceyyyy
            </div>

            <div class="welcome-text">
                pasti bingung yaa ini apa wkwk 🤭<br>
                biar ga bingung kamu klik ini yaa
            </div>

        </div>
    """, unsafe_allow_html=True)

    if st.button("🤎 klik di sini 🤎"):
        st.session_state.page = 2
        st.rerun()


# ==================================================
# HALAMAN 2
# ==================================================

elif st.session_state.page == 2:

    st.markdown("""
        <div class="story-title">
            halawww inii c 👋🏻🌽
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story-box">

        <div class="story-text">

        halawww inii nama nya c yg poni nya patah patah kaya
        jagunggg 🤪🤪

        <br><br>

        pasti orang asing denger nama nya aneh karna cuma satu huruf
        wkwk. yaa itu dehh yang aku rasain pas kenalan di awal,
        kaya ngerasa aneh gitu

        <b>"masa si nama nya c doangg"</b>

        tapi emang itu panggilan nyaa.

        <br><br>

        <b>AKUUUU..... MANGGILNYA BUKAN C TAPIIII CEYYYY</b> 😭

        <br><br>

        pengen beda aja si dari orang oranggg, soalnya aku gamau
        di samain sama orang.

        <br><br>

        setelah 4 tahun apa ya kalo ga salah aku baru ketemu c lg,
        pokonyaa terakhir itu smp dehh abistu uda gaperna ketemu lg.

        <br><br>

        <b>TAPI.......</b>

        aku suka stalk akun scc nya sii di akun ituu ✌🏼✌🏼

        <br><br>

        ketemu lg nya juga aneh bgtt lg menurut akuu,
        masa ngajak si kk main tp ngajak aku jg!!??

        <br><br>

        maksudnya gimana yakk 😭

        <br><br>

        tp ternyata itu katanya spikk ajaa 🫢🫢
        truss besok nya main lg denggg.

        <br><br>

        dan itu kayanya <b>first time main ber2</b> gasi??

        <br><br>

        iyaalaa mana perna kita mainn.

        <br><br>

        setelah kurang lebih sebulan ga ke bogor lg,
        tp malem ituu c ajak aku ke bogor KE KINAA.

        <br><br>

        disana aku banyak cerita c jugaa.
        aku suka deh c yappingg kaya seneng aja dengerin nyaa.

        <br><br>

        udaa dehh dari main itu jadi dekett sm c.

        <br><br>

        tp sebenernya aku tu takutt gitu klo di ajak main,
        takutnya banyakk diem huhu 😭

        <br><br>

        lebih ke takut salah ngomong gituu.

        <br><br>

        sedangkan c anak nyaa ekstrovertt bgtttttt.
        apa aja, kayanya si dia diem klo cengengg aja dehh hehe.

        <br><br>

        soalnya c tu <b>cengenggg</b> 👎🏼👎🏼👎🏼👎🏼

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("🌽 lanjut lagi yukkk"):
        st.session_state.page = 3
        st.rerun()


# ==================================================
# HALAMAN 3
# ==================================================

elif st.session_state.page == 3:

    st.markdown("""
        <div class="ending">

            <div class="ending-emoji">
                🥹🤎🌽
            </div>

            <div class="ending-title">
                jadiii begitulah awalnya...
            </div>

        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story-box">

        <div class="story-text">

        ternyata dari yang awalnya cuma kenal satu huruf,
        terus dipanggil beda sendiri jadi <b>ceyyyy</b>,
        akhirnya malah jadi sedeket ini wkwkwk 🤎

        <br><br>

        lucu juga yaa kalo dipikir-pikir.

        <br><br>

        dari yang awalnya takut bakal banyak diem,
        takut salah ngomong,
        malah akhirnya bisa cerita banyak dan
        betah dengerin c yappinggg 😭

        <br><br>

        dan ternyata...

        <br><br>

        <b>perjalanan kita baru mulai dari sini 🌽🤎</b>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("🤎 balik ke awal"):
        st.session_state.page = 1
        st.rerun()
