import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

df= pd.read_pickle("df_rfm.pkl")
c=0
st.title("DashBoard Marketing Campaigns")

image = Image.open('image.png')

st.image(image)
categories_count = df.RFM_Level.unique().tolist()
segmnent_count = ["Education","Marital_Status","AgeGroup"]
col1,col2,col3 = st.columns([1,1,1])
chosen_count = st.sidebar.selectbox(
   'Segment de client',categories_count
)
chosen_count2 = st.sidebar.selectbox(
   'Catégorie inter-segment (Treemap)',segmnent_count

)
df_filtered = df[df["RFM_Level"] == chosen_count]
df_plot = pd.DataFrame({'sum': [df_filtered.NumWebPurchases.sum(), df_filtered.NumCatalogPurchases.sum(), df_filtered.NumStorePurchases.sum()],},
                  index=['Achat sur le web', 'Achat catalogue', 'Achat en magasin'])
df_cmp = pd.DataFrame({'sum': [df_filtered.AcceptedCmp1.sum(), df_filtered.AcceptedCmp2.sum(), df_filtered.AcceptedCmp3.sum(),df_filtered.AcceptedCmp4.sum(),df_filtered.AcceptedCmp5.sum(),df_filtered.Response.sum()],},
                  index=['Campagne 1', 'Campagne 2', 'Campagne 3','Campagne 4','Campagne 5','Campagne recente'])
df_categ = pd.DataFrame({'sum': [df_filtered.MntWines.sum(), df_filtered.MntFruits.sum(), df_filtered.MntMeatProducts.sum(),df_filtered.MntFishProducts.sum(),df_filtered.MntSweetProducts.sum(),df_filtered.MntGoldProds.sum()],},
                  index=['Vin', 'Fruits', 'Viandes','Poissons','Sucrerie','Or'])
fig3 = fig = px.pie(df_plot, values='sum', names=df_plot.index,title=f'Repatition des achat des {chosen_count} ')
fig2 = px.bar(df_cmp, x=df_cmp.index, y="sum", title=f'Repatition des campagne des {chosen_count} ')
fig1 = px.bar(df_categ, x=df_categ.index, y="sum",title=f"Habitude d'achat des {chosen_count} ")
fig4 = px.treemap(df, path=[px.Constant("all"), 'RFM_Level',chosen_count2], values='M')

boxplot_chart = st.plotly_chart(fig3)

barplot_chat1 = st.plotly_chart(fig2)
barplot_chat2 = st.plotly_chart(fig1)
barplot_chat2 = st.plotly_chart(fig4, use_container_width=True)
