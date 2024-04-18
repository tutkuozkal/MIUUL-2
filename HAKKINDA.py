
import streamlit as st
import requests
import PIL.Image as Image


def new_line():
    st.markdown("<br>", unsafe_allow_html=True)


# Define a function to load the Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Config
page_icon = Image.open("tablet.jpg")
st.set_page_config(layout="centered", page_title="Tablet Tahmin", page_icon=page_icon)


# Create the About page
def main():
    # Title Page
    st.markdown("<h1 align='center'> 🔎Proje Hakkinda", unsafe_allow_html=True)
    new_line()

    # What is?
    st.markdown("## <h1 align='center'> Mahmut amca ne ister isimli makine ogrenmesi calismamizi :blue[Sn. Bicem hanim] ve :blue[Sn. Hidayet] bey ve ben :blue[Tutku] bir ekip olarak hazirladik.", unsafe_allow_html=True)
    st.markdown("## <h2 align='center'> Ilk calismamiz oldugu icin gordugumuz hatalari oldugu gibi biraktik, cikarimlarda bulunarak sonraki projelerimiz ve yol haritamiz icin notlarimizi aldik.", unsafe_allow_html=True)
    #st.markdown("Resim birseyler birseyler eklenecek.\n  Video cekip buraya da koyabiliriz... \n ")
    

                

if __name__ == "__main__":
    main()
