import streamlit as st

st.set_page_config(
    page_title = "Paddy Yield Forecaster — NCP Sri Lanka",
    page_icon  = "🌾",
    layout     = "wide"
)

st.title("🌾 Seasonal Paddy Yield Forecasting")
st.subheader("North Central Province, Sri Lanka (1995–2025)")

st.markdown("""
Welcome to the Paddy Yield Forecasting Dashboard.

This application presents the findings of a study on seasonal 
paddy yield forecasting in the **North Central Province of 
Sri Lanka** using rainfall and temperature data from the 
**Maha Illuppallama meteorological station**.

**Use the sidebar to navigate between pages.**
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Districts",      "2")
col2.metric("Seasons",        "2")
col3.metric("Years Covered",  "1995–2025")
col4.metric("Best ML Model",  "SVR")

st.markdown("---")
st.info("""
**Districts:** Anuradhapura & Polonnaruwa  
**Seasons:** Maha (Oct–Mar) & Yala (Apr–Sep)  
**Weather Station:** Maha Illuppallama  
**Forecasting Model:** Support Vector Regression (SVR)
""")