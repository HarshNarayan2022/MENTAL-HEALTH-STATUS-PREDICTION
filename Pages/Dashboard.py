import streamlit as st


st.set_page_config(
    page_title="Dashboard",
    page_icon="🎃",
    layout="wide",
    initial_sidebar_state="expanded",
)

page_bg_img_link = f"""
<style>
[data-testid="stAppViewContainer"]> .main{{

background-image: url(https://images.unsplash.com/photo-1633977264259-b3517c187e3d?auto=format&fit=crop&q=80&w=1964&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D);
background-size:cover;


}}
</style>
"""

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]> .main{{


background-color: #FFDEE9;
background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%);


}}


[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0)

}}
[data-testid="stToolbar"]{{
right : 2 rem;
}}

[data-testid="stSidebar"] > div:first-child{{


background: linear-gradient(to right bottom,
                 rgba(255,225,225,0.7),
                 rgba(255,225,225,0.3));
                 }}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)


with st.sidebar:
    # st.markdown(
    #     '<div style=" font-family: Mali, cursive;text-align: center; font-size:30px; color:#ff725e; margin :10px">Mental Health</div>',
    #     unsafe_allow_html=True,
    # )

    st.image(
        "Mental health-pana.png",
        width=320,
    )


def show_explore_page():
    # st.set_page_config(
    #     layout="wide",
    #     initial_sidebar_state="expanded",
    # )

    title = st.markdown(
        '<div style=" font-family: Mali, cursive;text-align: center; font-size:3.5rem; color: rgb(69, 90, 100); margin-bottom :20px">Dashboard</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<iframe  width="1200" height="700" src="https://app.powerbi.com/reportEmbed?reportId=9c44667c-980c-4fd8-92ed-ff57b547a72d&autoAuth=true&ctid=51b942db-4e9b-4228-b3f4-777327ee4809" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    show_explore_page()
