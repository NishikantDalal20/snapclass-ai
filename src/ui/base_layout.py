import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
                .stApp{
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #E0E3FF !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                    background: #E0E3FF !important;
                }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
           /* @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');*/
            
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
            /* Hide Top tool bar of streamlit */   
                
            #MainMenu, footer, header {
                visibility:hidden
            }
            
            .block_container {
                padding-top:1.5rem !important
            }

            h1{
                /*font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;*/
                font-family: 'Poppins', sans-serif !important;
                font-size: 3.2rem !important;
                font-weight: 700 !important;
                line-height: 1.1 !important;
                margin-bottom: 0.2rem !important;
                letter-spacing: 1px;
                margin-bottom:0rem !important;
            } 
                   
            h2{
                /*font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;*/
                font-family: 'Poppins', sans-serif !important;
                font-size: 2rem !important;
                font-weight: 600 !important;
                line-height: 1.1 !important;
                margin-bottom: 0.3rem !important;
                color: #5865F2;

                margin-bottom:0rem !important;
            }    

            h3, h4, p{
                /*font-family: 'Outfit', sans-serif;*/
                font-family: 'Poppins', sans-serif !important;
                font-weight: 400;
            }
                
            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button:hover{
                transform: scale(1.05)
            }
        </style>
    """, unsafe_allow_html=True)
