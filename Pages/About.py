import streamlit as st

st.set_page_config(
    page_title="About US",
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

[data-testid="stMarkdownContainer"] {{
display: flex;
justify-content: center;
align-items: center;


}}

[data-testid="stMarkdownContainer"] > p > a > img {{
height : 30px;


}}



</style>
"""
st.markdown(page_bg_img_link, unsafe_allow_html=True)
with st.sidebar:
    st.image("Mental-Health-Status.png")
    st.image(
        "https://png.pngtree.com/png-vector/20230728/ourmid/pngtree-ask-clipart-cartoon-character-illustration-student-cartoon-of-young-boy-in-vector-png-image_6797449.png"
    )


def about_page():
    title = st.image("About-US.png")

    st.markdown(
        '<div style=" font-family: Mali, cursive; font-size:20px; color:black;">We are the students of M.Sc Data Science . We developed this web application by sharing each others knowledge and working together as a team.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("""---""")

    with st.container():
        col = st.columns([1, 1, 1])
        # HARSH #
        with col[0]:
            st.image(
                "https://png.pngtree.com/png-vector/20230816/ourmid/pngtree-cartoon-boy-with-glasses-and-a-backpack-clipart-vector-png-image_6988507.png"
            )
            st.markdown(
                '<div style=" font-family: Mali, cursive;text-align: center; font-size:24px; color:black;">Harsh Narayan</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div style=" font-family: Mali, cursive;text-align: center; font-size:16px; color:black;">Masters in Data Science</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                "[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/harsh-narayan-377907264/)"
            )
        # SHAMEEK #
        with col[1]:
            st.image(
                "https://png.pngtree.com/png-vector/20230801/ourmid/pngtree-cute-cartoon-child-with-glasses-and-backpack-holding-up-a-peace-vector-png-image_6824599.png"
            )
            st.markdown(
                '<div style=" font-family: Mali, cursive;text-align: center; font-size:24px; color:black;">Shameek Bhowmick</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div style=" font-family: Mali, cursive;text-align: center; font-size:16px; color:black;">Masters in Data Science</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                "[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/shameek-bhowmick-3481131a8/)"
            )
        # SAKSHI #
        with col[2]:
            st.image(
                "https://png.pngtree.com/png-vector/20230728/ourmid/pngtree-iready-clipart-cartoon-school-girl-cartoon-with-book-and-pencil-vector-png-image_6803048.png"
            )
            st.markdown(
                '<div style=" font-family: Mali, cursive;text-align: center; font-size:24px; color:black;">Sakshi Panhalkar</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div style=" font-family: Mali, cursive;text-align: center; font-size:16px; color:black;">Masters in Data Science</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                "[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/sakshi-panhalkar-7188061b4/)"
            )

    # with st.container():
    #     col = st.columns([1, 2])
    #     with col[0]:
    #         st.image("Robot.svg", width=350)
    #     with col[1]:
    #         st.title("Models Used:")
    #         st.write(
    #             """1. [BERTopic](https://maartengr.github.io/BERTopic/api/bertopic.html#:~:text=BERTopic%20is%20a%20topic%20modeling,words%20in%20the%20topic%20descriptions.)
    #             is a topic modeling technique that leverages BERT embeddings and c-TF-IDF to create dense clusters allowing for easily interpretable topics whilst keeping important words in the topic descriptions."""
    #         )
    #         st.write(
    #             """2. [KeyBERT](https://maartengr.github.io/KeyBERT/#:~:text=KeyBERT%20is%20a%20minimal%20and,most%20similar%20to%20a%20document.)
    #             is a minimal and easy-to-use keyword extraction technique that leverages BERT embeddings to create keywords and keyphrases that are most similar to a document."""
    #         )
    #         st.write(
    #             """3. Convolutional Neural Networks (CNNs) are used for text classification. CNNs can identify patterns in text data, such as bigrams, trigrams, or n-grams. CNNs are translation invariant, so they can detect these patterns regardless of their position in the sentence."""
    #         )


if __name__ == "__main__":
    about_page()
