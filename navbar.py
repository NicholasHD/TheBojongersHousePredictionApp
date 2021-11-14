import streamlit as st

def show_navbar_page():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
       <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FF4B4B;">
         <a class="navbar-brand"  target="_blank">THE BOJONGERS</a>
         <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
         </button>
         <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
         </ul>
        </div>
        </nav>
""", unsafe_allow_html=True)