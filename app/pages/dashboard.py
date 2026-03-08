import os
import pandas as pd
import streamlit as st;                              st.set_page_config( 'Main Page', ':bar_chart:', 'wide' )
from streamlit_lottie import st_lottie
import json
import sqlite3
import plotly.express as px
from utils.style import apply_figure_layout

st.markdown(
    """
    <style>
    /* Sidebar right border */
    [data-testid="stSidebar"] {
        border-right: 4px solid #0F52BA;  /* sapphire color */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
        .st-emotion-cache-8gkzs6 p {
            font-size: 25px !important;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        section[data-testid="stSidebar"] input {
            border: 2px solid #0a2342 !important;
            border-radius: 8px !important;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Sidebar right border */
    [data-testid="stSidebar"] {
        border-right: 4px solid #0F52BA;  /* sapphire color */
    }


    /* ── Sidebar label font (Code, Stock, etc.) ── */
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] .stTextInput label p,
    [data-testid="stSidebar"] .stMultiSelect label p {
        font-size: 22px !important;
        font-weight: 700 !important;
        color: #0a2342 !important;
    }

    /* ── Multiselect selected tag text ── */
    [data-testid="stSidebar"] .stMultiSelect span[data-baseweb="tag"] span {
        font-size: 18px !important;
        font-weight: 600 !important;
    }


    /* ── Sidebar nav item text ── */
    [data-testid="stSidebarNav"] a span {
        font-size: 20px !important;
        font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

conn = sqlite3.connect( 'app/db/Stock.db' )
df = pd.read_sql( 'SELECT * FROM PT;', conn )

anim = json.load(open("app/lottie-anims/Growth-Graph.json"))



st.markdown(  '<h1 style = "font-family:times new roman; font-size:65px;text-align:center;margin-top:-150px;margin-left:-35px;" >Performance Analysis Dashboard</h1>',unsafe_allow_html=True)



# SideBar
code = st.sidebar.multiselect( 'Code:',options = list(df['الكود'].unique()),default = list(df['الكود'].unique()), help= 'Conductor Code' )
in_stock = st.sidebar.multiselect( 'Stock', options = ['غير متاح','متاح'], default= ['غير متاح','متاح'], help= 'متاح او غير متاح' )
material = st.sidebar.multiselect( 'Material', options = list(df['المادة الخام'].unique()), default=list(df['المادة الخام'].unique()), help= 'المونيوم او نحاس' )

download_df = st.sidebar.button( 'Download the dataset ?' )     # Download dataset button

with st.sidebar :  st_lottie( anim, height=300, speed=3, loop=True, width= 150 )


def filter_data( df: pd.DataFrame, code: str, in_stock: str, material: str ) -> pd.DataFrame :
    code = code if len( code ) != 0 else df['الكود'].unique()
    return df.query( 'الكود == @code and متاح == @in_stock and `المادة الخام` == @material' )

df = filter_data( df, code, in_stock, material )
#st.dataframe(  df )

# KPIs Section
no_of_unique_conductors_types = len( df )
no_of_types = int( df['النوع'].nunique() )
no_of_stock_items = int( df[ df['متاح'] == 'متاح' ]['العدد'].sum() )


kpi_1, kpi_2, kpi_3 = st.columns( 3)
kpi_1.markdown( f'<h3 style = "font-size:50px;" >إجمالى عدد <br>conductors<br><div style = "margin-left:17%;font-size:65px;" >{ no_of_unique_conductors_types }</div></h3>', unsafe_allow_html=True )
kpi_2.markdown( f'<h3 style = "font-size:50px;" >عدد الأنواع<br><div style = "margin-left:17%;font-size:65px;" >{ no_of_types }</div></h3>', unsafe_allow_html=True )
kpi_3.markdown( f'<h3 style = "font-size:50px;" >إجمالى عدد القطع<br><div style = "margin-left:17%;font-size:65px;" >{ no_of_stock_items }</div></h3>', unsafe_allow_html=True )


c_11, c_12 = st.columns( [ 0.7, 0.3 ] )

fig_11 = px.histogram( df, x = 'النوع', template= 'simple_white', text_auto=True, color = 'متاح', height = 550,
                    barmode= 'stack', color_discrete_map= { 'متاح' : '#0F52BA', 'غير متاح' : '#A6C5D7'  })
fig_11.update_traces(
    hovertemplate="<b>%{x}</b><br>العدد: %{y}<extra></extra>"
)
fig_11 = apply_figure_layout( fig_11,  ' ', ylabel_text= 'التعداد' );     c_11.plotly_chart( fig_11, use_container_width=True )


fig_12 =px.sunburst( df, path = [ 'النوع', 'الامبير', 'مقاس' ], color = 'النوع', values= 'العدد',  color_discrete_sequence= ['#0F52BA'],
                 height= 600, width = 900)
fig_12.update_traces( hovertemplate="<b>%{label}</b><br>العدد=%{value}<extra></extra>" )
fig_12 = apply_figure_layout( fig_12, ' ' );     c_12.plotly_chart( fig_12 )



fig_21 = px.treemap(df,path=['مقاس'],template='simple_white',color_discrete_sequence=['#0F52BA']).update_traces(hovertemplate="<b>%{label}</b><br>" +"Count: %{value}<br>")
fig_21 = apply_figure_layout(fig_21,  ' ');             st.plotly_chart( fig_21 )

















@st.dialog("Download Confirmation")
def download_dialog():
    st.write(f"<p style = 'font-size:20px;' >The Dataset you will download's having:<br>Codes: { code }<br>Stock: { in_stock }<br>Material: {material}<br>shape: {df.shape}</p>", unsafe_allow_html= True)
    st.dataframe( df )
    




if download_df:
    download_dialog()