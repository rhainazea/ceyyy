import streamlit as st
import base64

st.set_page_config(
    page_title="Halawwww Ceyyyy 🤎",
    page_icon="🤎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================================
# FOTO
# =========================================================
# Letakkan foto dengan nama "1001279694.jpg"
# di folder yang sama dengan file Python ini.

with open("1001279694.jpg", "rb") as f:
    photo = base64.b64encode(f.read()).decode()


# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background: #3A2118;
    color: #F4E5D7;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* =========================
   JUDUL
========================= */

.main-title {
    text-align: center;
    color: #C99B7A;
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 10vw, 6rem);
    font-weight: 700;
    line-height: 1.05;
    margin-top: 15vh;
    margin-bottom: 25px;
}

/* =========================
   SUBTITLE
========================= */

.subtitle {
    text-align: center;
    color: #F1D9C8;
    font-family: 'DM Sans', sans-serif;
    font-size: 1.1rem;
    line-height: 1.7;
    margin-bottom: 30px;
}

/* =========================
   FOTO
========================= */

.photo-card {
    background: #F0DED0;
    padding: 12px;
    border-radius: 22px;
    box-shadow: 0 12px 35px rgba(0,0,0,.28);
    margin: 20px auto 30px;
    max-width: 680px;
}

.photo-card img {
    width: 100%;
    display: block;
    border-radius: 15px;
}

/* =========================
   CERITA
========================= */

.story {
    background: #F0DED0;
    color: #3A2118;
    padding: 30px;
    border-radius: 22px;
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    line-height: 1.85;
    box-shadow: 0 10px 30px rgba(0,0,0,.20);
}

.story-title {
    text-align: center;
    color: #7D4E3B;
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 20px;
}

.back-text {
    text-align: center;
    color: #C99B7A;
    font-family: 'DM Sans', sans-serif;
    margin-top: 30px;
}

/* =========================
   BUTTON
========================= */

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 999px;
    background: #C99B7A;
    color: #3A2118;
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    padding: .8rem 1.2rem;
    transition: .2s ease;
}

.stButton > button:hover {
    background: #E0B99D;
    transform: translateY(-2px);
}

/* =========================
   HP
========================= */

@media (max-width: 600px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .main-title {
        margin-top: 10vh;
    }

    .story {
        padding: 22px 20px;
        font-size: .98rem;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = 1


# =========================================================
# HALAMAN 1
# =========================================================

if st.session_state.page == 1:

    st.markdown(
        """
        <div class="main-title">
            halawwww<br>
            ceyyyy 🤎
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            pasti bingung yaa ini apa wkwk 🤭<br>
            biar ga bingung kamu klik ini yaa ↓
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🤎 klik ini buat lanjut 🤎"):
        st.session_state.page = 2
        st.rerun()


# =========================================================
# HALAMAN 2
# =========================================================

else:

    st.markdown(
        """
        <div class="main-title"
             style="margin-top:2vh;font-size:3rem;">
            halawwww ceyyyy 🤎
        </div>
        """,
        unsafe_allow_html=True
    )

    # FOTO
    st.markdown(
        f"""
        <div class="photo-card">
            <img src="data:image/jpeg;base64,{photo}">
        </div>
        """,
        unsafe_allow_html=True
    )

    # CERITA
    story = """
halawww inii nama nya c yg poni nya patah patah kaya jagunggg 🤪🤪

pasti orang asing denger nama nya aneh karna cuma satu huruf wkwk yaa itu dehh yang aku rasain pas kenalan di awal, kaya ngerasa aneh gitu "masa si nama nya c doangg" tapi emang itu panggilan nyaa.

AKUUUUU..... MANGGILNYA BUKAN C TAPIIII CEYYYY 😭

pengen beda aja si dari orang oranggg, soalnya aku gamau di samain sama orang.

setelah 4 tahun apa ya kalo ga salah aku baru ketemu c lg, pokonyaa terakhir itu smp dehh abistu uda gaperna ketemu lg.

TAPI.......

aku suka stalk akun scc nya sii di akun ituu ✌🏼✌🏼

ketemu lg nya juga aneh bgtt lg menurut akuu, masa ngajak si kk main tp ngajak aku jg!!??

maksudnya gimana yakk, tp ternyata itu katanya spikk ajaa 🫢🫢

truss besok nya main lg denggg, dan itu kayanya first time main ber2 gasi??

iyaalaa mana perna kita mainn.

setelah kurang lebih sebulan ga ke bogor lg, tp malem ituu c ajak aku ke bogor KE KINAA.

disana aku banyak cerita c jugaa, aku suka deh c yappingg kaya seneng aja dengerin nyaa.

udaa dehh dari main itu jadi dekett sm c.

tp sebenernya aku tu takutt gitu klo di ajak main takutnya banyakk diem huhu.

lebih ke takut salah ngomong gituu, sedangkan c anak nyaa ekstrovertt bgtttttt.

apa aja, kayanya si yaa dia diem klo cengengg aja dehh hehe.

soalnya c tu cengenggg 👎🏼👎🏼👎🏼👎🏼
"""

    story_html = "<br><br>".join(
        paragraph.replace("\n", "<br>")
        for paragraph in story.strip().split("\n\n")
    )

    st.markdown(
        f"""
        <div class="story">

            <div class="story-title">
                🤎 sedikit cerita tentang cey 🤎
            </div>

            {story_html}

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="back-text">
            hehe segitu dulu ceritanyaaa 🫶🏻
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← balik lagi"):
        st.session_state.page = 1
        st.rerun()
