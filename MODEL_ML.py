import numpy as np
import pickle
import streamlit as st
import pandas as pd
from PIL import Image


load_model = pickle.load(open('model.pkl','rb'))


def tablet_prediction(input_data):
    
    input_data_as_numpy_array = np.asanyarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
        return 'Cok Ucuz'
    elif (prediction[0]==2):
        return 'Pahali'
    elif (prediction[0]==1):
        return 'Normal'
    else:
        return 'Ucuz'
    
def main():
    
  
    page_icon = Image.open("tablet.png")
    st.set_page_config(page_title="Tablet Fiyat Tahmin",layout="wide",page_icon=page_icon)
    st.title(":rainbow[Miuul Bitirme Projesi: Tablet Fiyat Tahmin]")
    st.header('Tablet Tahmin Verileri', divider='rainbow')   # alt başlık ekler

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write("")

    with col2:
        st.image("./assets/tablet.png",width=800, caption="Tablet Fiyat Tahmin")

    with col3:
        st.write("")


    main_tab, model_tab = st.tabs(["Veri Seti", "Model"])

    left_col, right_col = main_tab.columns(2,gap="small")


    main_tab.code("import pandas as pd") #kod satiri olarak isleme
    main_tab.code("df = pd.read_csv('tablet.csv')")


    # st.sidebar.title("Tablet Fiyat Tahmin")
    # st.sidebar.write("Tablet fiyatinin tahmini icin Model sekmesinde belirtilen"
    #                      " alan ozelliklerini girdikten sonnra, tahmin butonu ile "
    #                      "tablet fiyatinin hangi fiyat araliginda oldugunu tahmin edebilirsiniz.")
    
    with model_tab:
        BataryaGucu = st.slider('Batarya Gucu mAH', 500, 2000, 1500)
        Bluetooth = st.slider('Bluetooth', 0, 1, 1)
        MikroislemciHizi = st.slider('Mikroislemci Hizi Mhz', 0.5, 2.9,1.5)
        CiftHat = st.slider('CiftHat', 0, 1, 1)
        OnKameraMP = st.slider('On Kamera MP', 0, 19, 5)
        G4 = st.slider('4G', 0, 1, 1)
        DahiliBellek = st.slider('Dahili Bellek GB', 2, 64, 32)
        Kalinlik = st.slider('Kalinlik cm', 0.1, 1.0,0.85)
        Agirlik = st.slider('Agirlik gr', 80, 200,120)
        CekirdekSayisi = st.slider('CekirdekSayisi', 1, 8, 8)
        ArkaKameraMP = st.slider('Arka Kamera MP', 0, 20, 20)
        CozunurlukYukseklik = st.slider('Cozunurluk Yukseklik', 0, 1960, 1500)
        CozunurlukGenislik = st.slider('Cozunurluk Yukseklik', 500, 1998, 1500)
        RAM = st.slider('Ram MB', 400, 3998, 1500)
        BataryaOmru = st.slider('Batarya Omru Gun', 2, 20, 10)
        G3 = st.slider('3G', 0, 1, 1)
        Dokunmatik = st.slider('Dokunmatik', 0, 1, 1)
        WiFi = st.slider('WiFi', 0, 1, 1)

        #model_tab.title("Tablet Fiyat Tahmin")
        #tahmin = ''
        if st.button("Fiyat Tahmini"):
            tahmin = np.array([BataryaGucu,Bluetooth,MikroislemciHizi,CiftHat,OnKameraMP,G4,DahiliBellek,Kalinlik,Agirlik,CekirdekSayisi,ArkaKameraMP,CozunurlukYukseklik,CozunurlukGenislik,RAM,BataryaOmru,G3,Dokunmatik,WiFi])
            tahmin = tablet_prediction(tahmin)
            print(tahmin)
            st.success(tahmin)


    @st.cache_data
    def get_data():
        df = pd.read_csv("tablet.csv")
        return df

    main_tab.dataframe(get_data(), height=500,width=2200)

    

    #model_tab.title("Tablet Tahmin")


#input_data = (1563,1,1.7,0,10.0,1,10,0.9,119,7,4,500,732,1734.0,14,0,0,0)

if __name__ == '__main__':
    main()

# """
# BataryaGucu,
# Bluetooth,
# MikroislemciHizi,
# CiftHat,
# OnKameraMP,
# 4G,
# DahiliBellek,
# Kalinlik,
# Agirlik,
# CekirdekSayisi,
# ArkaKameraMP,
# CozunurlukYukseklik,
# CozunurlukGenislik,
# RAM,
# BataryaOmru,
# 3G,
# Dokunmatik,
# WiFi
# """
