import streamlit as st

# =========================================================
# KONFIGURASI
# =========================================================
st.set_page_config(
    page_title="halawwww ceyyyy",
    page_icon="⁉️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# URL FOTO
# =========================================================
FOTO_URL = "https://cdn.phototourl.com/free/2026-09-04-299e4086-352e-4282-9782-80f5f9a18b6a.jpg"


# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
}

.stApp {
    background-color: #3b2117;
    color: #f6dfc8;
}

/* Hilangkan header Streamlit */
header {
    visibility: hidden;
}

/* Container utama */
.block-container {
    max-width: 850px;
    padding-top: 40px;
    padding-bottom: 60px;
}

/* Semua tombol */
.stButton > button {
    width: 100%;
    border-radius: 30px;
    border: 2px solid #c8956d;
    background-color: #6b3d28;
    color: #f9e5d0;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 17px;
    padding: 12px 20px;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #c8956d;
    color: #3b2117;
    border-color: #f0c9a7;
}

/* Judul utama */
.judul {
    text-align: center;
    font-size: 75px;
    font-weight: 700;
    color: #c8956d;
    margin-top: 120px;
    margin-bottom: 15px;
}

/* Subjudul */
.subjudul {
    text-align: center;
    font-size: 19px;
    line-height: 1.8;
    color: #f2d9c2;
    margin-bottom: 45px;
}

/* Judul halaman */
.page-title {
    text-align: center;
    color: #c8956d;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 30px;
}

/* Text halaman */
.text-box {
    background-color: #4b2b1e;
    border: 1px solid #7d5038;
    border-radius: 25px;
    padding: 28px;
    color: #f8e4d0;
    font-size: 17px;
    line-height: 2;
    text-align: justify;
    margin-top: 25px;
}

/* Foto */
.photo-box {
    text-align: center;
    margin-bottom: 20px;
}

.photo-box img {
    width: 100%;
    max-width: 650px;
    border-radius: 25px;
    border: 5px solid #c8956d;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
}

/* Quote */
.quote {
    text-align: center;
    font-size: 25px;
    line-height: 1.8;
    color: #f2d9c2;
    padding: 30px 15px;
}

/* Pilihan pagi malam */
.choice-title {
    text-align: center;
    color: #f2d9c2;
    font-size: 23px;
    margin-bottom: 25px;
}

.footer {
    text-align: center;
    margin-top: 45px;
    color: #b98764;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = 1

if "waktu" not in st.session_state:
    st.session_state.waktu = None


def next_page():
    st.session_state.page += 1


def previous_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1


def go_home():
    st.session_state.page = 1


# =========================================================
# HALAMAN 1
# =========================================================
if st.session_state.page == 1:

    st.markdown(
        '<div class="judul">halawwww</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="subjudul">
        pasti bingung yaa ini apa wkwk<br>
        biar ga bingung kamu klik icon di bawah ini yaa
        </div>
        ''',
        unsafe_allow_html=True
    )

    if st.button("➡️"):
        next_page()
        st.rerun()


# =========================================================
# HALAMAN 2
# =========================================================
elif st.session_state.page == 2:

    st.markdown(
        '<div class="page-title"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="photo-box">
            <img src="{FOTO_URL}">
        </div>
        ''',
        unsafe_allow_html=True
    )

    teks_halaman_2 = """
    halawww kenalin inii nama nya c yg poni nya patah patah kaya jagunggg 🤪🤪
    pasti orang-orang asing denger nama nya aneh karna cuma satu huruf wkwk
    yaa itu dehh yang aku rasain pas kenalan di awal, kaya ngerasa aneh gitu
    "masa si nama nya c doangg" tapi emang itu panggilan nyaa.

    AKUUUUUU..... manggilnya bukan C TAPIIII CEYYYY, pengen beda aja si dari orang oranggg, soalnya aku gamau di samain sama orang.

    setelah 4 tahun apa ya kalo ga salah aku baru ketemu c lg, pokonyaa
    terakhir itu smp dehh abistu uda gaperna ketemu lg, TAPI....... aku suka stalk akun scc nya sii di akun ituu ✌🏼✌🏼

    ketemu lg nya juga aneh bgtt lg menurut akuu, masa ngajak si kk main tp
    ngajak aku jg!!?? maksudnya gimana yakk, tp ternyata itu katanya spikk ajaa
    🆙🆙🆙 truss besok nya main lg denggg (emang biasa spik aja itu), dan itu kayanya
    first time main ber2 gasi?? iyaalaa mana perna kita mainn, setelah kurang
    lebih sebulan ga ke bogor lg, tp malem ituu c ajak aku ke bogor KE KINAA,
    disana aku banyak cerita tp c jugaa kok. aku suka deh c yappingg kaya seneng aja dengerin nyaaa, udaa dehh dari
    main itu jadi dekett sm c.tp sebenernya aku tu takutt gitu klo di ajak main, takutnya banyakk diem huhu
    lebih ke takut salah ngomong aja si, sedangkan c anak nyaa ekstrovertt bgtttttt,
    kayanya si yaa dia diem klo lg crying aja dehh hehe soalnya c tu cengenggg
    👎🏼👎🏼👎🏼👎🏼
    """

    st.markdown(
        f'<div class="text-box">{teks_halaman_2.replace(chr(10), "<br>")}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← kembali"):
            previous_page()
            st.rerun()

    with col2:
        if st.button("lanjut →"):
            next_page()
            st.rerun()


# =========================================================
# HALAMAN 3
# =========================================================
elif st.session_state.page == 3:

    st.markdown(
        '<div class="page-title"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="">
        “aku gatau kamu suka di kasi long teks atau tidak,<br>
        tapi berhubung love language aku words of affirmation<br>
        jadi aku mau kasi sedikit afirmasi buat kamu”
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="footer"></div>',
        unsafe_allow_html=True
    )

    if st.button("lanjut baca →"):
        next_page()
        st.rerun()


# =========================================================
# HALAMAN 4
# =========================================================
elif st.session_state.page == 4:

    st.markdown(
        '<div class="page-title"></div>',
        unsafe_allow_html=True
    )

    teks_halaman_4 = """
    SELAMATTTT MEMASUKIIII BULANNN SEPTEMBER DAN SELAMAT MENINGGALKAN
    BULANNN AGUSTUS. agustus cepet banget yaaa? Kayanya bulan ini banyak sedihnyaa sampe kamu
    sempat memutuskan untuk menghilang sejenak, tapii ada senengnyaaa kann?
    walaupunnn sedikit tapi gapapaa. akuuu kalo ngeliat kamuuu seneng te sukaa ikutan seneng gituu tauuu.
    cape banget yaaa harus ngelewatin beberapa masalah dibulan agustus ini?
    Menghadapi orang-orang yang sotau tentang hidup kamu gimana, pasti rumit
    banget kan ngelewatin semuanyaaa? gapapaaa yaa, lagi lagi kata 'everything will be fine' nya keluar
    HAHAHAHAHAHAH. tapiii kamuuu gaa harus selaluuu kuat karnaaa setiapp orang pastii dilewatin
    badainya masing-masing yang bikin capeee banget yang bahkannn sampe
    pengen nyerahhhh. tapii akum au bilang 'capee boleh nyerahh jangan' dan boeh untuk mengeuh,
    tapii setelah kamuu ngeluhh kamu perlu BANGKIT untuk semuanya dan dari
    semuanyaaa. eitssss, tapii walaupun kamuu berusaha bangkit kamu jugaa gabole lupaa
    sama istirahat yaa. akuu yakin banget setelah ini pasti banyak kejutan bahagiaaa yangg
    menghampiri kamuuu (trust me!). jadi kalooo bulan agustus ini sangat bad gapapa yaa semoga bulan selanjutnya
    bakal lebih baik lagii, aamiin. ini bukan akhir dari segalanya, gabole nyerahhh deh pokonyaaa tapii untuk
    sedih dan nangiss itu gapapa bgtt. ayooo nangis buat luapin semua masalahnyaa, kalooo malem ini ada hujan turun
    di pipi kamuu tidak apa apaa kooo tapii besok harus lebih semangat lagi
    untuk menyambut bulan baruuuu huhuhuu. semuaaa masalahhh di bulan agustus dilupain duluuu yyyaaa?
    atauuu di selesain dengan cara damaii karna semua masalah pasti ada
    jalan keluarnyaaa. I'M SO PROUD OF U soalnyaa kamuu te bener bener hebat banget napaaa
    bener bener bertahan sejauh ini dan sampe ada di titik ini. walaupun akuu gatauu dan gaa ngerasain masalah yang lagi kamu alaminnn
    dan trauma yang ngebuat kamuuu punya pribadi baruuu, dan ketakutan
    kepanikan kamu jugaaaa. BERTAHAN LEBIH LAMAA YAAA! bumi banyak penghuninyaa dan bumi banyak banget dihuni sama orang hebat
    contohnya kaya manusia yang satuuu inii. jangan lupa buat sayangin diri kamu yaaa karna diri kamu doang yang bakal
    jadi topangan hiduppp untuk diri sendiri. buat hari hari kamu kemarin yang masii belum bisa jadii baik buat kamuuu..
    semogaa hari hari selanjutnyaaa bisa jauh lebih membaik yaaa, aamiin. kamu hebat 7392927473×.
    tapii jangan lupaa bilang maaf dan terimakasii untuk diri kamu sendiri yaa
    udaa bertahan lebih lamaaa. diri kamu bisaa nunjukin kepada semesta kalo kamu mampuuu ngelewatin
    badai badai, ujan dan angin ribut halilintar sekalipun hehehe. selaluu bangga sama kamuuuuuu.
    kalo aku kasii kata semangat mungkin bosen yaa? dan gaa cukup jugaa..
    tapi aku berharappp semua bentuk support akuu ke kamamuu bisaa dijadiin
    energi untuk ngelewatin badai badaii selanjutnyaaa. Banyak yang sayanggg sama kamu jadi kamu gaboleee ngerasa sendiri yaaaa.
    kamuuuu jauh lebih dari kata HEBAT. bertahan hidup lebih lamaa yaa ‼️‼️🤍🤍🤍🤍🤍🤍🤍🤍
    💐💐💐💐💐💐💐💐💐💐
    """

    st.markdown(
        f'<div class="text-box">{teks_halaman_4.replace(chr(10), "<br>")}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← kembali"):
            previous_page()
            st.rerun()

    with col2:
        if st.button("lanjut →"):
            next_page()
            st.rerun()


# =========================================================
# HALAMAN 5
# =========================================================
elif st.session_state.page == 5:

    st.markdown(
        '<div class="page-title"></div>',
        unsafe_allow_html=True
    )

    teks_halaman_5 = """
    huhu aku mau say sorry yaa kalo kemarin-kemarin ada kata kata aku yang
    ga enak atau ada yang salah. makasii yaa uda sempet ajak aku main dan mau sedikit cerita tentang kamu
    ke aku, ya walaupun mungkin itu ga sampe 5% nya, tapi gapapa. makasi juga ya uda mau dengerin aku kemarin dan maaf kalo ternyata ada
    satu dan lain hal yang bikin kamu ga nyaman. aku Cuma mau bilang Makasi dan maa aja koo 🤎
    """

    st.markdown(
        f'<div class="text-box">{teks_halaman_5.replace(chr(10), "<br>")}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← kembali"):
            previous_page()
            st.rerun()

    with col2:
        if st.button("lanjut →"):
            next_page()
            st.rerun()


# =========================================================
# HALAMAN 6
# =========================================================
elif st.session_state.page == 6:

    st.markdown(
        '<div class="page-title"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="choice-title">
        oiya kamu buka link ini nya kapan?
        </div>
        ''',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌤️ PAGI"):
            st.session_state.waktu = "pagi"

    with col2:
        if st.button("🌙 MALAM"):
            st.session_state.waktu = "malam"

    if st.session_state.waktu == "pagi":

        teks_pagi = """
        halawww, selamatt pagiii selamat menjalankan aktivitas hari inii yaaa.
        gimana tadi malem bobonya nyenyak tidakk?? Baguss deh kalo nyenyak dan
        semoga selalu seperti itu selalu. oiya mau kemana hari ini?
        Kalo mau keluar hati-hati jangan kebut-kebut. aku mau ingetin kamu buat jangan lupa minum air putih‼️‼️
        jangan sering-sering pod sama rokonyaa yaaa. yauda semangattt yaa untuk hari ini semoga hari ini semua orang bisa
        bersahabat dengan kamu 🤎
        """

        st.markdown(
            f'<div class="text-box">{teks_pagi.replace(chr(10), "<br>")}</div>',
            unsafe_allow_html=True
        )

    elif st.session_state.waktu == "malam":

        teks_malam = """
        halawwww, gimana hari ini?? Rate donggg, tapi semoga ratenya bagus huhu.
        selamat malam dan selamat bobo yaaaa, have a nice dreammm. semoga hari ini ada hal-hal kecil yang bikin kamu senyum, dan kalo
        harinya kurang baik, semoga besok bisa jauh lebih baik yaaa. Jangan lupa istirahat, jangan terlalu banyak mikirin hal yang bikin
        cape, malam ini waktunya istirahat duluu. makasih yaaa uda bertahan sampai hari ini, uda melewatin semua hal
        yang mungkin ga gampang. Semoga malam ini bisa bobo dengan nyenyak dan bangun besok dengan mood
        yang lebih bagus, dan semangat yang baru. Sleep well yaaa 
        """

        st.markdown(
            f'<div class="text-box">{teks_malam.replace(chr(10), "<br>")}</div>',
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← kembali"):
            previous_page()
            st.rerun()

    with col2:
        if st.button("lanjut →"):
            next_page()
            st.rerun()


# =========================================================
# HALAMAN 7 / TERAKHIR
# =========================================================
elif st.session_state.page == 7:

    st.markdown(
        '<div class="page-title"></div>',
        unsafe_allow_html=True
    )

    teks_terakhir = """
    terimakasih yaa sudah mau buka link ini dan baca sampai halaman terakhir.
    maaf ya kalo kata-kata aku di atas ada yang berulang-ulang. ceyyyy hidup lebihh lama yaaa.
    BABAYYYYY SEEE UUU 👋🏻👋🏻👋🏻
    """

    st.markdown(
        f'<div class="text-box">{teks_terakhir.replace(chr(10), "<br>")}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="quote"></div>',
        unsafe_allow_html=True
    )

    if st.button("➡️"):
        go_home()
        st.rerun()
