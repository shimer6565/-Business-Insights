import streamlit as st
import codecs
import streamlit.components.v1 as stc
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

def dashboardPage(db, w = 1255, h = 1000):
    file = codecs.open(db, 'r')
    page = file.read()
    stc.html(page, width = w, height = h, scrolling = False)

header = st.container()
dashboard = st.container()

with header:
    st.image("bi.jpg", width=250)

with st.sidebar:
    selected = option_menu(
        menu_title = "Business Insights",
        options = ["Sales Analysis", "Revenue Analysis", "Profit Analysis"],
        default_index=0,
    )

if selected == "Sales Analysis":
    st.header(f"{selected}")
    dashboardPage('salesAnalysis.html')
elif selected == "Revenue Analysis":
    st.header(f"{selected}")
    dashboardPage('revenueAnalysis.html')
elif selected == "Profit Analysis":
    st.header(f"{selected}")
    dashboardPage('profitAnalysis.html')