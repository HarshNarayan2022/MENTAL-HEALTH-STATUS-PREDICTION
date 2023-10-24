import streamlit as st
import json
import requests


from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Introduction",
    page_icon="🎃",
    layout="wide",
    initial_sidebar_state="expanded",
)

page_bg_img_link = f"""
<style>
[data-testid="stAppViewContainer"]> .main{{

# background-image: url(https://www.orfonline.org/wp-content/uploads/2022/10/mental-health-wellness-during-covid-19.jpg);
# background-size:cover;
# background-position: left;
# background-repeat:no-repeat;
# background-attachment:local;
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
st.markdown(page_bg_img_link, unsafe_allow_html=True)
with st.sidebar:
    st.image("Mental-Health-Status.png")
    st.image(
        "https://png.pngtree.com/png-vector/20230728/ourmid/pngtree-ask-clipart-cartoon-character-illustration-student-cartoon-of-young-boy-in-vector-png-image_6797449.png"
    )


# once we excuted this bottom code one time then it will cash it and it is available for next time again


def Intro():
    # first gif

    url = requests.get(
        "https://lottie.host/9126a15a-1827-4182-8e10-0125511bd4a8/mrrTAfOYfT.json"
    )

    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    else:
        print("Error in URL")
    # second gif

    path = "aim.json"
    with open(path, "r") as file:
        url = json.load(file)

        # Main title
        st.image("Introduction.png")
    # st.markdown(
    #     '<div style="background-color:black; border-radius:7px 3vw;border: solid black; margin-bottom:3rem;   border: solid; text-align: center; color:white; font-size:40px;">Analysis & Prediction of Mental Health Status</div>',
    #     unsafe_allow_html=True,
    # )

    # Section First
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            url_json,
            # change the direction of our animation
            reverse=True,
            # height and width of animation
            height=500,
            width=500,
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality="high",
            # THis is just to uniquely identify the animation
            key="Car",
        )
    with col2:
        st.markdown(
            '<div style=" font-family: Mali, cursive;text-align: center; font-size:50px; color:black;">About Us</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div style=" font-family: Mali, cursive;margin:1rem 1rem; font-size:22px; color:black;">Mental health includes our emotional, psychological, and social well-being. It affects how we think, feel, and act. It also helps determine how we handle stress, relate to others, and make choices. Mental health is important at every stage of life, from childhood and adolescence through adulthood.</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style=" font-family: Mali, cursive;margin:1rem 1rem; font-size:22px; color:black;">Over the course of your life, if you experience mental health problems, your thinking, mood, and behavior could be affected. Many factors contribute to mental health problems, we aim to find those factors.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("""---""")

    # Section second
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div style=" font-family: Mali, cursive;text-align: center; font-size:50px; color:black;">We Aim To</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style=" font-family: Mali, cursive;margin:1rem 1rem; font-size:34px; color:black;">Analyse</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style=" font-family: Mali, cursive;margin:1rem 1rem; font-size:22px; color:black;">Get an idea of what factors affect the overall mental health of a person</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style=" font-family: Mali, cursive;margin:1rem 1rem; font-size:34px; color:black;">Predict</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style=" font-family: Mali, cursive;margin:1rem 1rem; font-size:22px; color:black;">Predict the mental health status of a person based on the selected factors</div>',
            unsafe_allow_html=True,
        )

    with col2:
        st_lottie(
            url,
            # change the direction of our animation
            reverse=False,
            # height and width of animation
            height=500,
            width=500,
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality="high",
            # THis is just to uniquely identify the animation
            key="head",
        )


if __name__ == "__main__":
    Intro()
