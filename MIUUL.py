# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:27:14 2024

@author: tutku.ozkal
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import PIL.Image as Image

def half_divider():
    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    col2.divider()

def new_line():
    st.markdown("<br>", unsafe_allow_html=True)

# Congratulation
def congratulation(key):
        col1, col2, col3 = st.columns([0.7,0.7,0.7])
        if col2.button("🎉 TEBRIKLER", key=key):
                st.balloons()
                st.markdown(":green[🥳 Bu Aşamayı Başarıyla Tamamladınız.]")


# Config
page_icon = Image.open("tablet.png")
st.set_page_config(layout="centered", page_title="Tablet Tahmin", page_icon=page_icon)

with st.sidebar:
      st.image("tablet.png", width=200)
      st.audio("Zerrin Özer Basit Numaralar.mp3",format="audio/wav")

# Title Page
st.markdown("<h1 style='text-align: center; '>📚 Egitim Zamani</h1>", unsafe_allow_html=True)
new_line()
st.markdown("Egitim Zamanına Hoş Geldiniz! Bu sekme, Veri Hazırlama ve Makine Öğrenimi ile ilgili temel kavramları anlamamıza yardımcı olmak için tasarlanmıştır. Başlamak için lütfen aşağıdan bir konu seçin.", unsafe_allow_html=True)
new_line()

# Tabs
tab_titles = ['🗺️ Genel Bakis 󠀠 󠀠 󠀠', '🧭 EDA 󠀠 󠀠 󠀠', "‍📀‍‍‍‍ Kayip Degerler 󠀠󠀠 󠀠 󠀠", "🔠 Kategorik Ozellikler 󠀠 󠀠 󠀠", "🧬 Ölçeklendirme ve Dönüşüm 󠀠 󠀠 󠀠"]
tabs = st.tabs(tab_titles)


# Overview
with tabs[0]:
    new_line()
    st.markdown("<h2 style='text-align: center; '>🗺️ Genel Bakis</h2>", unsafe_allow_html=True)
    new_line()
    
    st.markdown("""
    Bir Makine Öğrenimi modeli oluştururken, verileri hazırlamak ve modeli oluşturmak için bir dizi adımı izlemeniz gerekir. Aşağıda Makine Öğrenimi sürecindeki temel adımlar yer almaktadır:
    
    - **📦 Data Collection**: CSV dosyaları, veritabanları, API'ler vb. gibi çeşitli kaynaklardan veri toplama işlemidir. Veri kümeleri için en ünlü web sitelerinden biri [**Kaggle**](https://www.kaggle.com/). <br> <br>
    - **🧹 Data Cleaning**: Yinelenenleri kaldırarak, eksik değerleri ele alarak, aykırı değerleri işleyerek vb. verileri temizleme işlemidir. Bu adım çok önemlidir çünkü çoğu zaman veriler temiz değildir ve çok sayıda eksik değer ve aykırı değer içerir. <br> <br>
    - **⚙️ Data Preprocessing**: Verilerin analiz için uygun bir formata dönüştürülmesi sürecidir. Buna kategorik özelliklerin işlenmesi, sayısal özelliklerin işlenmesi, ölçeklendirme ve dönüştürme vb. dahildir. <br> <br>
    - **💡 Feature Engineering**: Ozelliklerin kendisi ile ilgilenen bir süreçtir. Özellik çıkarma, özellik dönüştürme ve özellik seçimi gibi birden fazla adımdan oluşur. <br> <br>
    - **✂️ Splitting the Data**: Verileri eğitim, doğrulama ve test kümelerine ayırma işlemidir. Eğitim seti modeli eğitmek için, doğrulama seti hiperparametreleri ayarlamak için ve test seti de modeli değerlendirmek için kullanılır. <br> <br>
    - **🧠 Building Machine Learning Models**: Makine Öğrenimi modellerini oluşturma sürecidir. Sınıflandırma ve regresyon görevleri için kullanılabilecek birçok Makine Öğrenimi modeli vardır. En ünlü modellerden bazıları Doğrusal Regresyon, Lojistik Regresyon, Karar Ağacı, Rastgele Orman, Destek Vektör Makinesi (SVM), K-En Yakın Komşular (KNN) ve Sinir Ağlarıdır. <br> <br>
    - **⚖️ Evaluating Machine Learning Models**: Sınıflandırma görevleri için doğruluk, kesinlik, geri çağırma, F1 puanı ve daha fazlası ve regresyon görevleri için ortalama karesel hata (MSE), kök ortalama karesel hata (RMSE), ortalama mutlak hata (MAE) ve R-kare gibi çeşitli ölçütler kullanarak Makine Öğrenimi modellerini değerlendirme sürecidir. <br> <br>
    - **📐 Tuning Hyperparameters**: en iyi modeli elde etmek için Makine Öğrenimi modellerinin hiperparametrelerini ayarlama işlemidir. Rastgele Orman için tahminci sayısı, KNN için komşu sayısı, Sinir Ağları için katman ve nöron sayısı ve daha fazlası gibi her model için ayarlanabilen birçok hiper parametre vardır. <br> <br>
    """, unsafe_allow_html=True)
    new_line()
    

# Exploratory Data Analysis (EDA)
with tabs[1]:
    new_line()
    st.markdown("<h2 style='text-align: center; ' id='eda'>🧭 Kesifci veri Analizi (EDA)</h2>", unsafe_allow_html=True)
    # half_divider()
    new_line()
    st.markdown("Keşifsel Veri Analizi (KVA), temel özelliklerini özetlemek için veri setlerini genellikle görsel yöntemlerle analiz etme sürecidir. EDA, resmi modelleme veya hipotez testi görevinin ötesinde verilerin bize neler söyleyebileceğini görmek için kullanılır. Veri Hazırlama sürecinde önemli bir adımdır. EDA aynı zamanda Makine Öğrenimi sürecinin de ilk adımıdır. Bir model oluşturmadan önce verileri anlamak önemlidir. Bu, doğru modeli seçmenize ve hatalardan kaçınmanıza yardımcı olacaktır. EDA aynı zamanda örüntüleri bulmak, anormallikleri tespit etmek, hipotezleri test etmek ve özet istatistikler ve grafiksel gösterimler yardımıyla varsayımları kontrol etmek için de kullanılır.", unsafe_allow_html=True)
    new_line()


    st.markdown("<h6 > Aşağıda EDA icin bazı temel adımlar yer almaktadır:", unsafe_allow_html=True)
    st.markdown("- **Data Collection:** Bu, EDA'daki ilk adımdır. Veriler CSV dosyaları, veritabanları, API'ler vb. gibi çeşitli kaynaklardan toplanabilir.", unsafe_allow_html=True)
    st.markdown("- **Data Cleaning:** Bu, tekrar eden degerlerin kaldırılması, eksik değerlerin ele alınması, aykırı değerlerin ele alınması vb. yoluyla verilerin temizlenmesi sürecidir.", unsafe_allow_html=True)
    st.markdown("- **Data Preprocessing:** Bu, verilerin analiz için uygun bir formata dönüştürülmesi sürecidir. Buna kategorik özelliklerin işlenmesi, sayısal özelliklerin işlenmesi, ölçeklendirme ve dönüştürme vb. dahildir.", unsafe_allow_html=True)
    st.markdown("- **Data Visualization:** Bu, verilerin çubuk grafikler, histogramlar, dağılım grafikleri vb. gibi çeşitli grafikler kullanılarak görselleştirilmesi sürecidir.", unsafe_allow_html=True)
    st.markdown("- **Data Analysis:** Bu, verilerin ortalama, medyan, mod, standart sapma vb. gibi çeşitli istatistiksel yöntemler kullanılarak analiz edilmesi sürecidir.", unsafe_allow_html=True)
    st.markdown("- **Data Interpretation:** Bu, sonuç çıkarmak ve karar vermek için verileri yorumlama sürecidir.", unsafe_allow_html=True)
    new_line()

    # Data Collection with the code
    st.markdown("<h6> Aşağıda, aşağıdakiler kullanılarak yanıtlanabilecek bazı temel sorular yer almaktadır EDA:", unsafe_allow_html=True)
    st.markdown("- **Verilerin boyutu nedir?**", unsafe_allow_html=True)
    st.code("""df = pd.read_csv('data.csv') 
    df.shape""", language="python")

    st.markdown("- **Verilerdeki özellikler nelerdir?**", unsafe_allow_html=True)
    st.code("""df.columns""", language="python")

    st.markdown("- **Özelliklerin veri türleri nelerdir?**", unsafe_allow_html=True)
    st.code("""df.dtypes""", language="python")

    st.markdown("- **Verilerdeki eksik değerler nelerdir??**", unsafe_allow_html=True)
    st.code("""df.isnull().sum()""", language="python")

    st.markdown("- **Verilerdeki aykırı değerler nelerdir??**", unsafe_allow_html=True)
    st.code("""df.describe()""", language="python")

    st.markdown("- **Özellikler arasındaki korelasyonlar nelerdir??**", unsafe_allow_html=True)
    st.code("""df.corr()""", language="python")

    st.markdown("- **Özelliklerin dağılımları nelerdir?**", unsafe_allow_html=True)
    st.code("""df.hist()""", language="python")

    st.divider()

    # EDA with selected dataset
    new_line()
    st.subheader("Üzerinde EDA uygulamak için bir veri kümesi seçin")
    dataset = st.selectbox("Veri Setini Seciniz", ["Secim","Tablet"])
    new_line()

    if dataset == "Tablet":
   
        # Tablet Dataset
        st.markdown("Tablet fiyat tahminini kategorisel olarak belirleyen bir veri ele alindi. Bakkal Mahmut abi her geldiginde torununa tablet alacagini ve ozelliklerini bilmedigi icin normal bir sey olsun ifadesini kullandigi icin tuttuk data setinden model kurduk. Hic isimiz yoktu, dedeyi memnun edelim dedik. Dedeye sahip ciktik :)", unsafe_allow_html=True)
        new_line()

        # Perform EDA Process
        tablet2 = pd.read_csv('tablet2.csv')
        tablet = pd.read_csv('tablet.csv')
        # Read the data
        st.subheader("Verileri Okuma")
        st.write("Aşağıdaki kodu kullanarak verileri okuyabilirsiniz:")
        st.code("""import pandas as pd
tablet = pd.read_csv('tablet.csv')""", language="python")
        st.write(tablet2)

        # Data Size
        st.subheader("Veri Boyutu")
        st.write("Verilerin boyutu:")
        st.code("""tablet.shape""", language="python")
        st.write(tablet2.shape)
        st.markdown(f"Veri seti {tablet2.shape[0]} satir ve {tablet2.shape[1]} kolondan olusmaktadir.")
        new_line()

        # Data Types
        st.subheader("Veri tipleri")
        st.write("Özelliklerin veri türleri şunlardır:")
        st.code("""tablet.dtypes""", language="python")
        st.write(tablet2.dtypes)
        st.markdown("Veri seti 12 numerik ve 8 kategorik ozellikte veri icermektedir.")
        new_line()

        # Missing Values
        st.subheader("Eksik Değerler")
        st.write("Verilerdeki eksik değerler şunlardır:")
        st.code("""tablet.isnull().sum()""", language="python")
        st.write(tablet2.isnull().sum())
        st.markdown("Verilerin `RAM` ve `OnKameraMP` özelliklerinde eksik değerleri vardır.")
        new_line()

        # Description
        st.subheader("Description")
        st.write("Veriler hakkında Temel İstatistik bilgileri:")
        st.code("""tablet.describe()""", language="python")
        st.write(tablet2.describe())
        st.markdown("`.describe()` yöntemi, NaN değerleri hariç olmak üzere, bir veri kümesinin dağılımının merkezi eğilimini, dağılımını ve şeklini özetleyen tanımlayıcı istatistikler oluşturmak için kullanılır.")
        new_line()

        # Check the distribution of each feature using histograms and box plots with plotly express
        st.subheader("Özelliklerin Dağılımı")
        st.write("Her bir özelliğin dağılımı şöyledir:")
        st.markdown("<h6> FiyatAraligi </h6>", unsafe_allow_html=True)
        st.code("""fig = px.histogram(tablet, x='FiyatAraligi', marginal='box')
fig.show()""", language="python")
        fig = px.histogram(tablet2, x='FiyatAraligi', marginal='box')
        st.write(fig)
        new_line()

        st.markdown("<h6> RAM </h6>", unsafe_allow_html=True)
        st.code("""fig = px.histogram(tablet, x='RAM', marginal='box')
fig.show()""", language="python")
        fig = px.histogram(tablet2, x='RAM', marginal='box')
        st.write(fig)
        new_line()
        
        st.markdown("<h6> OnKameraMP </h6>", unsafe_allow_html=True)
        st.code("""fig = px.histogram(tablet, x='OnKameraMP', marginal='box')
fig.show()""", language="python")
        fig = px.histogram(tablet2, x='OnKameraMP', marginal='box')
        st.write(fig)
        new_line()
        
        st.markdown("<h6> ArkaKameraMP </h6>", unsafe_allow_html=True)
        st.code("""fig = px.histogram(tablet, x='OnKameraMP', marginal='box')
fig.show()""", language="python")
        fig = px.histogram(tablet2, x='ArkaKameraMP', marginal='box')
        st.write(fig)
        new_line()

        # Visualize the relationship between pairs of features using scatter plots
        st.subheader("Özellikler Arasındaki İlişki")
        st.write("Özellik çiftleri arasındaki ilişki şöyledir:")
        st.markdown("<h6> RAM vs FiyatAraligi </h6>", unsafe_allow_html=True)
        st.code("""fig = px.scatter(tablet, x='RAM', y='FiyatAraligi', color='OnKameraMP')
fig.show()""", language="python")
        fig = px.scatter(tablet2, x='RAM', y='FiyatAraligi', color='OnKameraMP')
        st.write(fig)
        new_line()

        # Use a heatmap to examine the correlation matrix and store it on fig variable
        st.subheader("Korelasyon Matrisi")
        st.write("Korelasyon matrisi şöyledir:")
        st.code("""fig = px.imshow(tablet.corr())
fig.show()""", language="python")
        fig = px.imshow(tablet.corr(), color_continuous_scale='Blues')
        st.write(fig)
        new_line()
        
#         # The Distribution of the Target
#         st.subheader("Hedefin Dağılımı")
#         st.write("Hedefin dağılımı şöyledir:")
#         st.code("""fig = px.histogram(tablet, x='OnKameraMP')
# fig.show()""", language="python")
#         fig = px.histogram(tablet2, x='OnKameraMP')
#         st.write(fig)
#         st.markdown("The target is imbalanced. The number of samples in the `Survived` class is less than the number of samples in the `Not Survived` class.")
#         new_line()

        # # Problem Type
        # st.subheader("Problem Type")
        # st.write("The problem type is:")
        # st.code("""tablet['FiyatAraligi'].value_counts()""", language="python")
        # st.write(tablet['FiyatAraligi'].value_counts())
        # st.markdown("The problem type is a binary classification problem. That is becuase the target is categorical and hanve only 2 possible values (Survived, Or Not Survived).")

        # Conclusion
        st.subheader("Veri setinden edinilen cikarimlar")
        st.write("EDA sürecinden, verilerin temiz olduğu ve Makine Öğrenimi sürecindeki bir sonraki adım için hazır olduğu sonucuna varabiliriz.")
        st.write("Aşağıda EDA sürecindeki kilit noktalar yer almaktadır:")
        st.markdown("- Veri seti `2000` satir ve `20` sutundan olusmaktadir.")
        st.markdown("- Veri setinde `12` sayısal özellik ve `8` kategorik özellik bulunmaktadır.")
        st.markdown("- Verilerde `RAM` ve `OnKameraMP` özelliklerinde eksik değerler var.")
        st.markdown("- Veri setinde aykiri deger gozlemlenmemistir.")
        st.markdown("- Veri setinde az olsa da `OnKameraMP` ve `ArkaKameraMP` arasinda bir korelason vardir.")
        st.markdown("- Veri setinde FiyatAraligi'nin her kategoriye ayni oradan dagildi tespit edilmistir.")
       
        new_line()

        congratulation("eda_tablet")

   

# Missing Values
with tabs[2]:

    new_line()
    st.markdown("<h2 align='center'> ‍📀‍‍‍‍ Eksik Değerler </h1>", unsafe_allow_html=True)
    
    # What is Missing Values?
    new_line()
    st.markdown("Eksik değerler, gözlemdeki bir değişken için saklanmayan değerlerdir. Eksik değerler verilerde `NaN` veya `None` ile temsil edilir. Eksik değerler gerçek dünya veri kümelerinde yaygındır. Eksik değerler, insan hataları, veri toplama hataları veya veri işleme hataları gibi birçok nedenden kaynaklanabilir. Eksik değerler Makine Öğrenimi sürecinde sorunlara neden olabilir. Bunun nedeni, çoğu Makine Öğrenimi algoritmasının eksik değerleri işleyememesidir. Bu nedenle, verileri Makine Öğrenimi sürecinde kullanmadan önce eksik değerleri ele almamız gerekir.", unsafe_allow_html=True)
    new_line()

    # Why we should handle the missing values?
    st.markdown("#### ❓ Kayıp değerleri neden ele almalıyız?")
    st.markdown("Eksik değerler Makine Öğrenimi sürecinde sorunlara neden olabilir. Bunun nedeni, çoğu Makine Öğrenimi algoritmasının eksik değerleri işleyememesidir. Bu nedenle, verileri Makine Öğrenimi sürecinde kullanmadan önce eksik değerleri ele almamız gerekir.", unsafe_allow_html=True)
    new_line()

    # How to Handle Missing Values?
    st.markdown("#### 🧐 Eksik Değerler Nasıl Ele Alınır?")
    st.markdown("Eksik değerleri ele almanın birçok yolu vardır. Aşağıda eksik değerleri ele almanın en yaygın yolları verilmiştir:")
    new_line()

    st.markdown("#### 🌎 Genel Olarak")
    st.markdown("**Eksik Değerleri Düşürün:** Eksik değerleri veri setinden cikartabiliriz. Bu, eksik değerleri ele almanın en kolay yoludur. Ancak, bu yöntem önerilmez. Bunun nedeni, verilerden bazı bilgileri kaybedecek olmamızdır. Bu yüzden bu derste bu yöntemi kullanmayacağız.")
    st.markdown("- **Eksik değerler içeren satırları veri setinden cikartin**: bu durumda verilerden bazı bilgileri kaybedeceğiz, ayrıca verilerden bazı örnekleri de kaybedeceğiz. Kayıp değerlerin sayısı azsa bu yöntemi kullanabiliriz, ancak kayıp değerlerin sayısı fazlaysa verilerden çok fazla bilgi kaybederiz.")
    st.markdown("- **Eksik değerler içeren sütunları veri setinden cikartin:**, bu durumda verilerden bazı bilgileri kaybedeceğiz, ayrıca verilerden bazı özellikleri de kaybedeceğiz. Eksik değerlerin sayısı azsa, sütunu (özelliği) bırakmaya gerek yoktur, bunun yerine eksik değerler içeren satırları (örnekleri) bırakabilir veya sonraki yöntemlerde göreceğimiz gibi eksik değerleri doldurabiliriz. <br> Eksik değerlerin sayısı büyükse, eksik değerler içeren sütunu (özelliği) düşürebiliriz. Büyük derken, eksik değerlerin yüzdesinin toplam örnek sayısının %50'sinden fazla olduğunu kastediyorum.")
    new_line()

    st.markdown("##### 🔷 Sayısal Özellikler İçin")

    st.markdown("- **Ortalama ile doldur**: eksik değerleri özelliğin ortalaması ile doldurabiliriz. Bu yöntem, özellikte aykırı değer yoksa önerilir. Çünkü ortalama aykırı değerlere karşı hassastır.")
    st.latex(r''' \mu = \frac{1}{n} \sum_{i=1}^{n} x_i ''')
    new_line()

    st.markdown("- **Medyan ile doldur**: eksik değerleri özelliğin medyanı ile doldurabiliriz. Bu yöntem, özellik aykırı değerlere sahipse önerilir. Çünkü medyan aykırı değerlere karşı hassas değildir.")
    st.latex(r''' \tilde{x} = \begin{cases} x_{\frac{n+1}{2}} & \text{if n is odd} \\ \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{if n is even} \end{cases} ''')
    new_line()

    st.markdown("- **Mod ile doldur**: eksik değerleri özelliğin modu ile doldurabiliriz. Özellik kategorik ise bu yöntem önerilir.")
    st.latex(r''' mode = \text{the most frequent value} ''')
    new_line()

    st.markdown("##### 🔶 Kategorik Özellikler İçin")
    st.markdown("- **En sık rastlanan değerle doldur**: eksik değerleri özelliğin en sık rastlanan değeriyle doldurabiliriz.")
    st.latex(r''' mode = \text{the most frequent value} ''')
    new_line()
    new_line()

    # How to Handle Missing Values in Python?
    st.markdown("#### 🐍 Python'da Eksik Değerler Nasıl Ele Alınır?")
    st.markdown("Bu bölümde, Python'daki önceki yöntemleri kullanarak eksik değerleri nasıl ele alacağımızı öğreneceğiz.")
    new_line()
    
    # Drop the rows that contain missing values
    st.markdown("- Eksik değerler içeren satırları cikartin")
    st.code("""df.dropna(axis=0, inplace=True)""", language="python")
    new_line()

    # Drop the columns that contain missing values
    st.markdown("- Eksik değerler içeren sütunları cikartin")
    st.code("""df.dropna(axis=1, inplace=True)""", language="python")
    new_line()
    
    # Fill with mean
    st.markdown("- Ortalama ile doldurun")
    st.code("""df[feature] = df[feature].fillna(df[feature].mean())""", language="python")
    new_line()

    # Fill with median
    st.markdown("- Medyan ile doldurun")
    st.code("""df[feature] = df[feature].fillna(df[feature].median())""", language="python")
    new_line()

    # Fill with mode
    st.markdown("- Mod ile doldurun")
    st.code("""df[feature] = df[feature].fillna(df[feature].mode()[0])""", language="python")
    new_line()

    # Fill with the most frequent value
    st.markdown("- En Sık Kullanılan Değer ile Doldurun")
    st.code("""df[feature] = df[feature].fillna(df[feature].mode()[0])""", language="python")

    # Perform Missing Values on the Dataset
    st.divider()
    st.markdown("#### Üzerinde Eksik Değerleri Doldurma İşlemi Gerçekleştirmek için Veri Kümesini Seçin")
    dataset = st.selectbox("Veri Setini Seciniz", ["Select", "Tablet"])

    if dataset == "Select":
        pass
    
    elif dataset == "Tablet":

        df = pd.read_csv("tablet.csv")
        st.markdown("#### Veri Seti")
        st.write(df)

        st.markdown("#### Kayıp Değerler:")
        st.markdown("Veri Kümesindeki Eksik Değerler şunlardır:")
        st.code("""df.isnull().sum()""", language="python")
        st.write(df.isnull().sum())
        st.markdown("Veri kümesinde eksik değerler var. Bu yüzden eksik değerleri ele almamız gerekiyor.")
        st.code("""null_val_df = df.isnull().sum()
null_val_df[null_val_df>0]""", language="python")
        null_val_tit = df.isnull().sum()
        st.write(null_val_tit[null_val_tit>0])
        new_line()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h5 align='left'> <b>RAM</b> Feature", unsafe_allow_html=True)
            new_line()
            st.write(f"Kayıp değer sayisi: **{df[['RAM']].isnull().sum().values[0]}** ")
            st.write(df[['RAM']].describe().T[['mean','50%']])
            st.write(f"Kayıpların Yüzdesi **{12/len(df):.3f}%**")
            st.markdown("Uygulanan Metod: :green[Mean]")

        with col2:
            pass

        with col3:
            st.markdown("<h5 align='left'> <b> OnKameraMP </b> Feature", unsafe_allow_html=True)
            new_line()
            st.write(f"Kayıp değer sayisi: **{null_val_tit[null_val_tit>0][0]}**")
            #st.code("df[['OnKameraMP']].isnull().sum().values[0] / len(df)")
            st.write(df[['OnKameraMP']].describe().T[['mean','50%']])
            st.write(f"Kayıpların Yüzdesi  **{5/len(df):.3f}%**")
            st.markdown("Uygulanan Metod: :green[Mean]")
        # Fill the age feature with the mean
        st.divider()
        st.markdown("#### Eksik değerlerin doldurulması")
        new_line()

        st.markdown("##### `RAM` icin uygulanan `Mean` metodu")
        st.code("""df['RAM'] = df['RAM'].fillna(df['RAM'].mean())""", language="python")
        new_line()
        
        st.markdown("##### `OnKameraMP` icin uygulanan `Mean` metodu")
        st.code("""df['OnKameraMP'] = df['OnKameraMP'].fillna(df['OnKameraMP'].mean())""", language="python")
        new_line()
        
        
        # Drop the Cabin feature
        # st.markdown("##### The `Cabin` Feautre with the `Drop the Column`")
        # st.code("""df.drop('Cabin', axis=1, inplace=True)""", language="python")
        # new_line()


        # # Fill the Embarked feature with the most frequent value
        # st.markdown("##### The `Embarked` Feautre with the `Fill with the Most Frequent Value`")
        # st.code("""df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])""", language="python")
        # new_line()

        congratulation("missing_titanic")
        


# Categorical Features
with tabs[3]:

    new_line()
    st.markdown("<h2 align='center'> ‍🔠‍‍‍‍ Kategorik Özellikler </h1>", unsafe_allow_html=True)

    # What is Categorical Features?
    new_line()
    st.markdown("Kategorik özellikler, sonlu bir değer kümesine sahip olan özelliklerdir. Kategorik özellikler nominal özellikler olarak da adlandırılır. Kategorik özellikler iki türe ayrılabilir: **Ordinal Özellikler** ve **Nominal Özellikler**.", unsafe_allow_html=True)
    new_line()

    # Ordinal Features
    st.markdown("#### 🔷 Ordinal Ozellikler")
    st.markdown("Ordinal özellikler, bir sırası olan sonlu bir değer kümesine sahip kategorik özelliklerdir. Örneğin, `Size` özelliği `Small`, `Medium` ve `Large` değerlerine sahip olabilir. Boyut özelliğinin değerlerinin bir sırası vardır. Bunun nedeni `Small` < `Medium` < `Large` olmasıdır. Bir başka örnek de `Eğitim` özelliğidir. Eğitim özelliği `Lise`, `Lisans`, `Yüksek Lisans` ve `Doktora` değerlerine sahip olabilir. Eğitim özelliğinin değerleri bir sıraya sahiptir. Çünkü `Lise` < `Lisans` < `Yüksek Lisans` < `Doktora` olarak siralayabiliriz.", unsafe_allow_html=True)
    new_line()

    # Nominal Features
    st.markdown("#### 🔶 Nominal Özellikler")
    st.markdown("Nominal özellikler, sırası olmayan sonlu bir değer kümesine sahip kategorik özelliklerdir. Örneğin, `Cinsiyet` özelliği `Erkek` ve `Kadın` değerlerine sahip olabilir. Cinsiyet özelliğinin değerlerinin bir sırası yoktur. Çünkü `Male` değeri `Female` değerinden küçük değildir ve `Female` değeri `Male` değerinden küçük değildir.", unsafe_allow_html=True)
    new_line()

    # How to Handle Categorical Features?
    st.markdown("#### 🧐 Kategorik Özellikler Nasıl Ele Alınır?")
    st.markdown("Kategorik özellikleri işlemenin birçok yolu vardır. Aşağıda kategorik özellikleri işlemenin en yaygın yolları verilmiştir:")

    st.markdown("- One Hot Encoding")
    st.markdown("- Ordinal Encoding")
    st.markdown("- Label Encoding")
    st.markdown("- Count Frequency Encoding")
    st.markdown("Bir sonraki bölümde her bir yöntemi inceleyeceğiz ve Python'da nasıl uygulanacağını ve nasıl çalıştığını göreceğiz.")
    st.divider()

    # One Hot Encoding
    st.subheader("🥇 One Hot Encoding")
    st.markdown("One Hot Encoding, kategorik özellikleri ikili özelliklere dönüştürerek kategorik özellikleri sayısal özelliklere kodlamak için kullanılan bir yöntemdir. One Hot Encoding nominal özellikler için kullanılır. One Hot Encoding aynı zamanda Kukla Değişkenler olarak da adlandırılır. One Hot Encoding kategorik özelliklerin kodlanması için en yaygın yöntemdir. Bunun nedeni One Hot Encoding'in kategorik özelliklerin değerleri arasında herhangi bir sıra varsaymamasıdır.", unsafe_allow_html=True)
    new_line()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**One Hot Encoding Oncesi**")
        st.dataframe(pd.DataFrame(np.array(['a','b','c','b','a']) ),width=250, height=250)

    with col2:
        st.write("**One Hot Encoding Sonrasi**")
        st.dataframe(pd.DataFrame(np.array([[1,0,0],[0,1,0],[0,0,1],[0,1,0],[1,0,0]]) ),width=250, height=250)

    new_line()
    st.write("Gördüğümüz gibi, `col1` kategorik özelliği `col1_a`, `col1_b` ve `col1_c` olmak üzere üç ikili özelliğe dönüştürülmüştür. `Col1` kategorik özelliğinin değerleri `a`, `b` ve `c`dir. Böylece, `a` değeri `[1,0,0]`, `b` değeri `[0,1,0]` ve `c` değeri `[0,0,1]` haline dönüştürülür.")
    # new_line()
    st.code("""from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
df['feature'] = encoder.fit_transform(df[['feature']])""", language="python")
    new_line()
    new_line()

    # Ordinal Encoding
    st.subheader("♾️ Ordinal Encoding")
    st.markdown("Ordinal Encoding, kategorik özellikleri sayısal özelliklere dönüştürerek kategorik özellikleri sayısal özelliklere uygulamak için kullanılan bir yöntemdir. Ordinal Encoding sıralı özellikler için kullanılır.")
    new_line()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Ordinal Encoding Oncesi**")
        st.dataframe(pd.DataFrame(np.array(['a','b','c','b','a']) ),width=250, height=250)

    with col2:
        st.write("**Ordinal Encoding Sonrasi**")
        st.dataframe(pd.DataFrame(np.array([1,2,3,2,1]) ),width=250, height=250)

    new_line()
    st.write("Gördüğümüz gibi, `col1` kategorik özelliği `col1` sayısal özelliğine dönüştürülmüştür. Kategorik özellik `col1`in değerleri `a`, `b` ve `c`dir. Böylece, `a` değeri `1`e, `b` değeri `2`ye ve `c` değeri `3`e dönüştürülür.")
    st.code("""from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder()
df['feature'] = encoder.fit_transform(df[['feature']])""", language="python")
    new_line()
    new_line()

    # Label Encoding
    st.subheader("🏷️ Label Encoding")
    st.markdown("Etiket Kodlama, kategorik özellikleri sayısal özelliklere dönüştürerek kategorik özellikleri sayısal özelliklere kodlamak için kullanılan bir yöntemdir. Etiket Kodlama sıralı özellikler için kullanılır. Etiket Kodlaması Sıra Kodlamasına benzer. Label Encoding ile Ordinal Encoding arasındaki fark, Label Encoding'in kategorik özelliklerin değerleri arasında herhangi bir sıra varsaymamasıdır ve label encoding sadece bir özellik için kullanılan bir yöntemdir, birden fazla özellik için kullanırsanız Python ile hata verecektir.")
    new_line()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Label Encoding Oncesi**")
        st.dataframe(pd.DataFrame(np.array(['a','b','c','b','a']) ),width=250, height=250)

    with col2:
        st.write("**Label Encoding Sonrasi**")
        st.dataframe(pd.DataFrame(np.array([1,2,3,2,1]) ),width=250, height=250)

    new_line()
    st.write("Gördüğümüz gibi, `col1` kategorik özelliği `col1` sayısal özelliğine dönüştürülmüştür. Kategorik özellik `col1`in değerleri `a`, `b` ve `c`dir. Böylece, `a` değeri `1`e, `b` değeri `2`ye ve `c` değeri `3`e dönüştürülür.")
    st.code("""from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['feature'] = encoder.fit_transform(df['feature'])""", language="python")
    new_line()
    new_line()

    # # Count Frequency Encoding
    # st.subheader("〰️ Count Frequency Encoding")
    # st.markdown("Count Frequency Encoding is a method for encoding the categorical features to numerical ones by Transforming the categorical features into numerical features. Count Frequency Encoding is used for nominal features. Count Frequency Encoding is similar to One Hot Encoding. The difference between Count Frequency Encoding and One Hot Encoding is that Count Frequency Encoding does not transform the categorical features into binary features, instead, it transforms the categorical features into numerical features. Count Frequency Encoding is better than One Hot Encoding. That is because Count Frequency Encoding does not increase the number of features in the data. So, Count Frequency Encoding is better than One Hot Encoding.")
    # new_line()
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.write("**Before Count Frequency Encoding**")
    #     st.dataframe(pd.DataFrame(np.array(['a','b','c','b','a']) ),width=250, height=250)

    # with col2:
    #     st.write("**After Count Frequency Encoding**")
    #     st.dataframe(pd.DataFrame(np.array([2/5, 2/5, 1/5, 2/5, 2/5]) ),width=250, height=250)

    # new_line()
    # st.write("As we can see, the categorical feature `col1` is transformed into a numerical feature `col1`. The values of the categorical feature `col1` are `a`, `b`, and `c`. So, the value `a` is transformed into `2/5`, the value `b` is transformed into `2/5`, and the value `c` is transformed into `1/5`.")
    # st.code("""df['feature'] = df['feature'].map(df['feature'].value_counts(normalize=True))""", language="python")

    # new_line()
    # new_line()

    # Perform Categorical Features on the Dataset
    st.divider()
    st.markdown("#### Üzerinde Kategorik Özellikler Uygulamak için Veri Kümesi Seçin")
    dataset = st.selectbox("Veri Setini Seciniz", ["Select","Tablet"], key = "categorical_data")

    if dataset == 'Tablet':

        df = pd.read_csv("tablet2.csv")
        st.markdown("#### Veri Seti")
        st.write(df)

        st.markdown("### Kategorik Özellikler:")
        st.markdown("#### Veri Setindeki Kategorik Özellikler şunlardır:")
        st.code("""df.select_dtypes(include='object').columns""", language="python")
        col1, col2, col3 = st.columns(3)
        col1.markdown("Kategorik Özellikler")
        col1.write(df.select_dtypes(include='object').columns)
        col2.markdown("Benzersiz Değerlerin Sayısı")
        col2.write(df.select_dtypes(include='object').nunique())
        col3.markdown("Benzersiz Değerlerin Yüzdesi")
        col3.write(df.select_dtypes(include='object').nunique() / len(df))
        st.markdown("Veri kümesi kategorik özelliklere sahiptir. Bu nedenle, kategorik özellikleri ele almamız gerekir.")
        new_line()

        col1, col2, col3 = st.columns(3)
        with col1:
                st.markdown("<h5 align='left'> <b> Renk </b> Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['RAM']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['RAM']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")

        with col2:
             st.markdown("<h5 align='left'> Bluetooth Feature", unsafe_allow_html=True)
             new_line()
             st.write(f"Benzersiz deger sayisi: **{df[['Bluetooth']].nunique().values[0]}** ")
             st.write(f"Yuzde: **{df[['Bluetooth']].nunique().values[0] / len(df):.2f}%** ")
             #st.write("The used method: :green[Drop the Column]")

        with col3:
                st.markdown("<h5 align='left'> CiftHat Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['CiftHat']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['CiftHat']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[One Hot Encoding]")

        #new_line()
        new_line()
        col1, col2, col3 = st.columns(3)

        with col1:
                st.markdown("<h5 align='left'> <b> 4G </b> Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['4G']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['4G']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")

        with col2:
                st.markdown("<h5 align='left'> 3G Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['3G']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['3G']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")
                
        with col3:
                st.markdown("<h5 align='left'> Dokunmatik Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['Dokunmatik']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['Dokunmatik']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")
        
        new_line()
        col1, col2, col3 = st.columns(3)

        with col1:
                st.markdown("<h5 align='left'> <b> WiFi </b> Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['WiFi']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['WiFi']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")

        with col2:
                st.markdown("<h5 align='left'> FiyatAraligi Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['FiyatAraligi']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['FiyatAraligi']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")
                
        with col3:
                st.markdown("<h5 align='left'> Renk Feature", unsafe_allow_html=True)
                new_line()
                st.write(f"Benzersiz deger sayisi: **{df[['Renk']].nunique().values[0]}** ")
                st.write(f"Yuzde: **{df[['Renk']].nunique().values[0] / len(df):.2f}%** ")
                #st.write("The used method: :green[Drop the Column]")


        st.divider()
        new_line()
        st.markdown("#### Kategorik Özelliklerin Kodlanması")
        new_line()

        # Drop the Name feature
        st.markdown("##### `Renk` veri setinden `Drop` ile cikarildi")
        st.code("""df.drop('Name', axis=1, inplace=True)""", language="python")
        new_line()

        # One Hot Encoding the Sex & Embarked features
        st.markdown("##### `Bluetooth` & `CiftHat` & `4G` & `3G` Uygulanan `One Hot Encoding`")
        st.code("df = pd.get_dummies(df, columns=['Bluetooth','CiftHat','4G','3G'])", language="python")
        new_line()
        
        st.markdown("##### `Dokunmatik` & `WiFi` Uygulanan `One Hot Encoding`")
        st.code("df = pd.get_dummies(df, columns=['Dokunmatik','WiFi'])", language="python")
        new_line()
        
        st.markdown("##### `FiyatAraligi` Uygulanan `Label Encoding`")
        st.code("df = pd.get_dummies(df, columns=['FiyatAraligi'])", language="python")
        new_line()


        #congratulation("categorical_Tablet")



# Scaling & Transformation
with tabs[4]:

    new_line()
    st.markdown("<h2 align='center'> 🧬 Ölçeklendirme </h1>", unsafe_allow_html=True)

    # What is Scaling & Transformation?
    new_line()
    st.markdown(" :green[Veri Ölçekleme], verileri belirli bir aralığa ölçeklemek için bir yöntemdir, çünkü veriler farklı aralıklara sahip olabilir ve bir özellik daha yüksek bir aralığa sahip olduğunda, model üzerinde daha yüksek bir etkiye sahip olacak ve **bias** ekleyecektir. Bu nedenle, verileri belirli bir aralığa ölçeklememiz gerekir.")
    st.markdown(" :green[Veri Dönüşümü], verileri belirli bir dağılıma dönüştürmek için kullanılan bir yöntemdir, çünkü veriler farklı dağılımlara sahip olabilir ve bir özellik farklı bir dağılıma sahip olduğunda, model üzerinde daha yüksek bir etkiye sahip olacak ve **yanlılık** ekleyecektir. Bu nedenle, verileri belirli bir dağılıma dönüştürmemiz gerekir. Bu yöntem özellikle verilerin aykırı değerlere ve yüksek çarpıklığa sahip olduğu durumlarda uygulanır.")
    new_line()

    # Why we should scale the data?
    st.markdown("##### 📏 Verileri neden ölçeklendirmeliyiz?")
    st.markdown("Verilerin ölçeklendirilmesi bazı Makine Öğrenimi algoritmaları için önemlidir. Bunun nedeni, bazı Makine Öğrenimi algoritmalarının veri aralığına duyarlı olmasıdır. Örneğin, K-En Yakın Komşular algoritması veri aralığına duyarlıdır. Bu nedenle, verileri K-En Yakın Komşular algoritmasında kullanmadan önce verileri ölçeklendirmemiz gerekir. Bir başka örnek de Destek Vektör Makinesi algoritmasıdır. Destek Vektör Makinesi algoritması veri aralığına duyarlıdır. Bu nedenle, verileri Destek Vektör Makinesi algoritmasında kullanmadan önce verileri ölçeklendirmemiz gerekir.", unsafe_allow_html=True)
    new_line()

    # Why we should transform the data?
    st.markdown("##### ➰ Verileri neden dönüştürmeliyiz?")
    st.markdown("Verilerin dönüştürülmesi bazı Makine Öğrenimi algoritmaları için önemlidir. Bunun nedeni, bazı Makine Öğrenimi algoritmalarının verilerin dağılımına duyarlı olmasıdır. Örneğin, Doğrusal Regresyon algoritması verilerin dağılımına duyarlıdır. Bu nedenle, verileri Doğrusal Regresyon algoritmasında kullanabilmemiz için önce verileri dönüştürmemiz gerekir. Bir başka örnek ise Lojistik Regresyon algoritmasıdır. Lojistik Regresyon algoritması verilerin dağılımına duyarlıdır. Bu nedenle, verileri Lojistik Regresyon algoritmasında kullanmadan önce verileri dönüştürmemiz gerekir.", unsafe_allow_html=True)
    # new_line()
    st.divider()

    # How to scale data
    st.subheader("🧮 Ölçeklendirme Yöntemleri")
    st.markdown("Verileri ölçeklendirmenin birçok yolu vardır. Aşağıdakiler, verileri ölçeklendirmenin en yaygın yollarıdır:")

    st.markdown("1. Min-Max Scaling")
    st.markdown("2. Standard Scaling")
    st.markdown("3. Robust Scaling")
    st.markdown("4. Max Absolute Scaling")

    st.markdown("Asagidaki bölümde her bir yöntemi inceleyeceğiz ve Python'da nasıl uygulanacağını ve nasıl çalıştığını göreceğiz.")
    new_line()

    # Min-Max Scaling
    st.markdown("##### Min-Max Scaling")
    st.markdown("Min-Maks Ölçeklendirme, verileri belirli bir aralığa ölçeklendirmek için kullanılan bir yöntemdir. Min-Maks Ölçeklendirme Normalleştirme olarak da adlandırılır. Min-Maks Ölçeklendirme, verileri ölçeklendirmek için kullanılan en yaygın yöntemdir. Bunun nedeni Min-Maks Ölçeklemenin basit ve kolay uygulanabilir olmasıdır. Min-Maks Ölçekleme normal dağılıma sahip özellikler için kullanılır. Min-Maks Ölçekleme, aykırı değerleri olmayan özellikler için kullanılır. Min-Maks Ölçekleme, sonlu bir aralığa sahip özellikler için kullanılır. Min-Maks Ölçekleme, sonlu bir değer kümesine sahip özellikler için kullanılır. Min-Maks Ölçekleme, bir sıraya sahip sonlu bir değer kümesine sahip özellikler için kullanılır. Min-Maks Ölçekleme, sırası olmayan sonlu bir değer kümesine sahip özellikler için kullanılır. Min-Maks Ölçekleme, sırası olmayan ve aykırı değerleri bulunmayan sonlu bir değer kümesine sahip özellikler için kullanılır. Min-Maks Ölçekleme, sırası olmayan ve aykırı değerlere sahip sonlu bir değer kümesine sahip özellikler için kullanılır. Ölçeklendirilmiş verilerin aralığı 0 ila 1 arasındadır.", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    col1.latex(r''' x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}} ''')
    col2.latex(r''' Z \in [0, 1] ''')
    new_line()

    st.code("""from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['feature'] = scaler.fit_transform(df[['feature']])""", language="python")
    new_line()
    new_line()

    # Standard Scaling
    st.markdown("##### Standard Scaling")
    st.markdown("Standart Ölçeklendirme, verileri belirli bir aralığa ölçeklendirmek için kullanılan bir yöntemdir. Standart Ölçekleme aynı zamanda Standartlaştırma olarak da adlandırılır. Standart Ölçekleme normal dağılıma sahip özellikler için kullanılır. Standart Ölçekleme aykırı değerlere sahip özellikler için kullanılır. Standart Ölçekleme, sınırlı bir aralığa sahip özellikler için kullanılır. Standart Ölçekleme, sonlu bir değer kümesine sahip özellikler için kullanılır. Standart Ölçekleme, bir düzene sahip sonlu bir değer kümesine sahip özellikler için kullanılır. Standart Ölçekleme, sırası olmayan sonlu bir değer kümesine sahip özellikler için kullanılır. Standart Ölçekleme, sırası olmayan ve aykırı değerleri bulunmayan sonlu bir değer kümesine sahip özellikler için kullanılır. Standart Ölçekleme, sırası olmayan ve aykırı değerlere sahip sonlu bir değer kümesine sahip özellikler için kullanılır. Ölçeklendirilmiş verilerin aralığı -1 ile 1 arasındadır.", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.latex(r''' x_{scaled} = \frac{x - \mu}{\sigma} ''')
    col2.latex(r''' Z \in [-1, 1] ''')
    new_line()

    st.code("""from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['feature'] = scaler.fit_transform(df[['feature']])""", language="python")
    new_line()
    
    congratulation("categorical_Tablet")
    #st.divider()

 
