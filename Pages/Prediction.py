import streamlit as st

import os
import numpy as np
import pandas as pd


import tensorflow as tf


st.set_page_config(
    page_title="prediction",
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

[data-baseweb="tab-list"]{{
    display : flex ;
    justify-content:center;
    gap:3rem;
    
    border-radius: 15px;
    background-color: hsla(7.2, 100%, 77.1%, 0.62);

}}

[data-testid="stMarkdownContainer"] > p {{
color : black;
font-size:16px;
font-family: Open Sans, sans-serif;
}}

[data-testid="baseButton-secondary" ] {{
background-color: white;
}}
</style>
"""
st.markdown(page_bg_img_link, unsafe_allow_html=True)

with st.sidebar:
    # st.markdown(
    #     '<div style=" font-family: Mali, cursive;text-align: center; font-size:30px; color:#ff725e; margin :10px">Mental Health</div>',
    #     unsafe_allow_html=True,
    # )

    st.image(
        "Mental health-pana.png",
        width=320,
    )


@st.cache_resource
def Load_mode():
    model = tf.keras.models.load_model("train.h5")
    return model


# @st.cache_resource
# def Load_mode():
#     with open("train.pkl", "rb") as file:
#         model = pickle.load(file)
#     return model


# to play with streamlit css properties we use streamlit coponents

import streamlit.components.v1 as components


def Prediction():
    if os.path.exists("Sourcedata.csv"):
        df = pd.read_csv("Sourcedata.csv", index_col=None)
    else:
        df = None
    title = st.markdown(
        '<div style=" font-family: Mali, cursive;text-align: center; font-size:3.5rem; color: rgb(69, 90, 100); margin-bottom :4rem; ">Intersted to know Mental Health Status!</div>',
        unsafe_allow_html=True,
    )
    Age = st.slider("What is your age?", 0, 100)
    # Age = st.number_input("Enter your age!")
    cols = st.columns([1, 1])
    with st.container():
        with cols[0]:
            Sex = st.radio("Select Gender", ["Male", "Female"])
        with cols[1]:
            Location = st.radio("Select your Location", ["Urban", "Rural"])

    with st.container():
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Coping Strategies ",
                "Shyness ",
                "Loneliness ",
                "Self Esteem ",
                "Life satisfaction ",
            ]
        )
        with tab1:
            # Coping Strategies
            # CS- Self Distraction

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left; color:black;">Self Distraction : </div>',
                unsafe_allow_html=True,
            )
            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    SD1 = st.radio(
                        "1 - I've been turning to work or other activities to take my mind off things.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
                with cols[1]:
                    SD2 = st.radio(
                        "2 - I've been doing something to think about it less, such as going to movies, watching TV, reading, daydreaming, sleeping or shopping.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

            # CS- Denial

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left;">Denial : </div>',
                unsafe_allow_html=True,
            )
            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    D1 = st.radio(
                        "1 - I've been saying to myself, this isn't real.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
                with cols[1]:
                    D2 = st.radio(
                        "2 - I've been refusing to believe that it has happened.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

            # CS - Venting

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left;">Venting : </div>',
                unsafe_allow_html=True,
            )

            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    V1 = st.radio(
                        "1 - I've been saying things to let my unpleasant feelings escape.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

                with cols[1]:
                    V2 = st.radio(
                        "2 - I've been expressing my negative feelings.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

            # CS - Self-blame

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left;">Self-blame : </div>',
                unsafe_allow_html=True,
            )

            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    SB1 = st.radio(
                        "1 - I've been criticizing myself.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
                with cols[1]:
                    SB2 = st.radio(
                        "2 - I've been blaming myself for things that happened.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

            # CS - Behavioural Disengagement

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left;">Behavioural Disengagement : </div>',
                unsafe_allow_html=True,
            )

            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    BD1 = st.radio(
                        "1 - I've been giving up trying to deal with it.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
                with cols[1]:
                    BD2 = st.radio(
                        "2 - I've been giving up the attempt to cope.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

            # CS - Acceptance

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left;">Acceptance : </div>',
                unsafe_allow_html=True,
            )

            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    A1 = st.radio(
                        "1 - I've been accepting the reality of the fact that it has happened.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
                with cols[1]:
                    A2 = st.radio(
                        "2 - I've been learning to live with it.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )

            # cs- Active Coping

            st.markdown(
                '<div style="margin-top: 40px; color:black; font-size: 1.6rem;font-weight: 300;text-align: left;">Active Coping : </div>',
                unsafe_allow_html=True,
            )

            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    AC1 = st.radio(
                        "1 - I've been concentrating my efforts on doing something about the situation I'm in.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
                with cols[1]:
                    AC2 = st.radio(
                        "2 - I've been taking action to try to make the situation better.",
                        options=["Never", "Rarely", "Sometimes", "Often", "Very Often"],
                    )
        with tab2:
            # Shyness
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    S1 = st.radio(
                        "1 - I feel tense when I'm with people I don't know.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
                with cols[1]:
                    S2 = st.radio(
                        "2 - I am socially somewhat awkward.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
                with cols[2]:
                    S3 = st.radio(
                        "3 - I am often uncomfortable at parties and other social functions.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    S4 = st.radio(
                        "4 - When in a group of people, I have trouble thinking of the right things to talk about.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
                with cols[1]:
                    S5 = st.radio(
                        "5 - It is hard for me to act natural when I am meeting new people.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
                with cols[2]:
                    S6 = st.radio(
                        "6 - I feel nervous when speaking to someone in authority.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    S7 = st.radio(
                        "7 - I have trouble looking someone right in the eye.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
                with cols[1]:
                    S8 = st.radio(
                        "8 - I feel inhibited in social situations.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
                with cols[2]:
                    S9 = st.radio(
                        "9 - I am more shy with members of the opposite sex.",
                        options=[
                            "Not at all",
                            "Slightly",
                            "Moderately",
                            "Very",
                            "Completely",
                        ],
                    )
        with tab3:
            # Loneliness
            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    L1 = st.radio(
                        "1 - I am a lonely person.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[1]:
                    L2 = st.radio(
                        "2 - I always will be a lonely person.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )

            cols = st.columns([1, 1])
            with st.container():
                with cols[0]:
                    L3 = st.radio(
                        "3 - Other people think of me as a lonely person.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[1]:
                    L4 = st.radio(
                        "4 - I always was a lonely person.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
        with tab4:
            # Self Esteem
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    SE1 = st.radio(
                        "1 - On the whole, I am satisfied with myself.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[1]:
                    SE2 = st.radio(
                        "2 - I feel that I have a number of good qualities..",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[2]:
                    SE3 = st.radio(
                        "3 - I am able to do things as well as most other people.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    SE4 = st.radio(
                        "4 - I feel that I'm a person of worth, at least on an equal plane with others.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[1]:
                    SE5 = st.radio(
                        "5 - I take positive attitude toward myself.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )

        with tab5:
            # Life satisfaction
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    LS1 = st.radio(
                        "1 - In most ways my life is close to my ideal.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[1]:
                    LS2 = st.radio(
                        "2 - The conditions of my life are excellent.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )

                    with cols[2]:
                        LS3 = st.radio(
                            "3 - I am satisfied with my life.",
                            options=[
                                "Strongly Disagree",
                                "Disagree",
                                "Neutral",
                                "Agree",
                                "Strongly Agree",
                            ],
                        )
            cols = st.columns([1, 1, 1])
            with st.container():
                with cols[0]:
                    LS4 = st.radio(
                        "4 - So far I have gotten the important things I want in life.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
                with cols[1]:
                    LS5 = st.radio(
                        "5 - If I could live my life over  I would change almost nothing.",
                        options=[
                            "Strongly Disagree",
                            "Disagree",
                            "Neutral",
                            "Agree",
                            "Strongly Agree",
                        ],
                    )
            run = st.button("Submit")

    ##Data gathering is completed for prediction##

    # making dataframe of data given by user for prediction

    df = pd.DataFrame(
        {
            "Age": [Age],
            "Sex": [Sex],
            "Location": [Location],
            "SD1": [SD1],
            "SD2": [SD2],
            "D1": [D1],
            "D2": [D2],
            "V1": [V1],
            "V2": [V2],
            "SB1": [SB1],
            "SB2": [SB2],
            "BD1": [BD1],
            "BD2": [BD2],
            "A1": [A1],
            "A2": [A2],
            "AC1": [AC1],
            "AC2": [AC2],
            "S1": [S1],
            "S2": [S2],
            "S3": [S3],
            "S4": [S4],
            "S5": [S5],
            "S6": [S6],
            "S7": [S7],
            "S8": [S8],
            "S9": [S9],
            "L1": [L1],
            "L2": [L2],
            "L3": [L3],
            "L4": [L4],
            "SE1": [SE1],
            "SE2": [SE2],
            "SE3": [SE3],
            "SE4": [SE4],
            "SE5": [SE5],
            "LS1": [LS1],
            "LS2": [LS2],
            "LS3": [LS3],
            "LS4": [LS4],
            "LS5": [LS5],
        }
    )

    # user data preprocessing
    # Gender
    def clean_gender(x):
        if x == "Male":
            return 1
        elif x == "Female":
            return 0
        elif x == "There is no other gender. It’s either him/her":
            return 1
        elif x == "Non binary":
            return 0
        return int(x)

    df["Sex"] = df["Sex"].apply(clean_gender)

    # Location
    def clean_location(x):
        if x == "Urban":
            return 1
        if x == "Rural":
            return 0
        return int(x)

    df["Location"] = df["Location"].apply(clean_location)

    # General_Psychopathology AND Shyness
    def clean_General_Psychopathology(x):
        if x == "Not at all":
            return 1
        elif x == "Slightly":
            return 2
        elif x == "Moderately":
            return 3
        elif x == "Very":
            return 4
        elif x == "Completely":
            return 5
        return int(x)

    # General_Psychopathology AND Shyness
    def clean_General_Psychopathology(x):
        if x == "Not at all":
            return 1
        elif x == "Slightly":
            return 2
        elif x == "Moderately":
            return 3
        elif x == "Very":
            return 4
        elif x == "Completely":
            return 5
        return int(x)

    df["S1"] = df["S1"].apply(clean_General_Psychopathology)
    df["S2"] = df["S2"].apply(clean_General_Psychopathology)
    df["S3"] = df["S3"].apply(clean_General_Psychopathology)
    df["S4"] = df["S4"].apply(clean_General_Psychopathology)
    df["S5"] = df["S5"].apply(clean_General_Psychopathology)
    df["S6"] = df["S6"].apply(clean_General_Psychopathology)
    df["S7"] = df["S7"].apply(clean_General_Psychopathology)
    df["S8"] = df["S8"].apply(clean_General_Psychopathology)
    df["S9"] = df["S9"].apply(clean_General_Psychopathology)

    # Coping Strategies
    def Coping_Strategies(x):
        if x == "Never":
            return 1
        elif x == "Rarely":
            return 2
        elif x == "Sometimes":
            return 3
        elif x == "Often":
            return 4
        elif x == "Very Often":
            return 5
        return int(x)

    df["SD1"] = df["SD1"].apply(Coping_Strategies)
    df["SD2"] = df["SD2"].apply(Coping_Strategies)

    df["D1"] = df["D1"].apply(Coping_Strategies)
    df["D2"] = df["D2"].apply(Coping_Strategies)

    df["V1"] = df["V1"].apply(Coping_Strategies)
    df["V2"] = df["V2"].apply(Coping_Strategies)

    df["SB1"] = df["SB1"].apply(Coping_Strategies)
    df["SB2"] = df["SB2"].apply(Coping_Strategies)

    df["BD1"] = df["BD1"].apply(Coping_Strategies)
    df["BD2"] = df["BD2"].apply(Coping_Strategies)

    df["A1"] = df["A1"].apply(Coping_Strategies)
    df["A2"] = df["A2"].apply(Coping_Strategies)

    df["AC1"] = df["AC1"].apply(Coping_Strategies)
    df["AC2"] = df["AC2"].apply(Coping_Strategies)

    # Loneliness & Self_Esteem & Life_Satisfaction

    def Loneliness_Self_Esteem_Life_Satisfaction(x):
        if x == "Strongly Disagree":
            return 1
        elif x == "Disagree":
            return 2
        elif x == "Neutral":
            return 3
        elif x == "Agree":
            return 4
        elif x == "Strongly Agree":
            return 5
        return int(x)

    df["L1"] = df["L1"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["L2"] = df["L2"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["L3"] = df["L3"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["L4"] = df["L4"].apply(Loneliness_Self_Esteem_Life_Satisfaction)

    df["SE1"] = df["SE1"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["SE2"] = df["SE2"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["SE3"] = df["SE3"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["SE4"] = df["SE4"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["SE5"] = df["SE5"].apply(Loneliness_Self_Esteem_Life_Satisfaction)

    df["LS1"] = df["LS1"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["LS2"] = df["LS2"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["LS3"] = df["LS3"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["LS4"] = df["LS4"].apply(Loneliness_Self_Esteem_Life_Satisfaction)
    df["LS5"] = df["LS5"].apply(Loneliness_Self_Esteem_Life_Satisfaction)

    # Rename the column afer taking mean within each section

    df["Self_Distraction"] = df[["SD1", "SD2"]].mean(axis=1)
    df["Denial"] = df[["D1", "D2"]].mean(axis=1)
    df["Venting"] = df[["V1", "V2"]].mean(axis=1)
    df["Self_Blame"] = df[["SB1", "SB2"]].mean(axis=1)
    df["Behavioural_Disengagement"] = df[["BD1", "BD2"]].mean(axis=1)
    df["Acceptance"] = df[["A1", "A2"]].mean(axis=1)
    df["Active_Coping"] = df[["AC1", "AC2"]].mean(axis=1)
    df["Shyness"] = df[["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]].mean(
        axis=1
    )
    df["Loneliness"] = df[["L1", "L2", "L3", "L4"]].mean(axis=1)
    df["Self_Esteem"] = df[["SE1", "SE2", "SE3", "SE4", "SE5"]].mean(axis=1)
    df["Life_Satisfaction"] = df[["LS1", "LS2", "LS3", "LS4", "LS5"]].mean(axis=1)

    # Drop cloumns old columns after making new columns by using old clumns
    df = df.drop(
        [
            "SD1",
            "SD2",
            "D1",
            "D2",
            "V1",
            "V2",
            "SB1",
            "SB2",
            "BD1",
            "BD2",
            "A1",
            "A2",
            "AC1",
            "AC2",
            "S1",
            "S2",
            "S3",
            "S4",
            "S5",
            "S6",
            "S7",
            "S8",
            "S9",
            "L1",
            "L2",
            "L3",
            "L4",
            "SE1",
            "SE2",
            "SE3",
            "SE4",
            "SE5",
            "LS1",
            "LS2",
            "LS3",
            "LS4",
            "LS5",
        ],
        axis=1,
    )

    # prediction
    # Age, Gender , General_Psychopathology ,Self_Distraction,Denial,Venting,Self_Blame,Behavioural_Disengagement,Acceptance,Active_Coping,Shyness,Loneliness,Self_Esteem,Life_Satisfaction
    if run:
        model = Load_mode()

        X = np.array(
            [
                df["Age"],
                df["Sex"],
                df["Location"],
                df["Self_Distraction"],
                df["Denial"],
                df["Venting"],
                df["Self_Blame"],
                df["Behavioural_Disengagement"],
                df["Acceptance"],
                df["Active_Coping"],
                df["Shyness"],
                df["Loneliness"],
                df["Self_Esteem"],
                df["Life_Satisfaction"],
            ]
        ).reshape(1, 14)

        health = model.predict(X)

        # Training set predictions converted to categories

        if health >= 1 and health < 2:
            health_2 = "Healthy"
        elif health >= 2 and health <= 3.5:
            health_2 = "Mild"
        else:
            health_2 = "Severe"

        # st.markdown(f" Mental condition seems {health}.")

        st.markdown(
            '<div style="  color:black; font-size: 1.5rem; font-weight: 50; "> Results: </div>',
            unsafe_allow_html=True,
        )

        if health_2 == "Healthy":
            st.markdown(
                '<div style=" padding-left: 40px; padding-right: 40px; padding-top: 20px; padding-bottom: 20px;  color:black; font-size: 1.4rem;border-radius:1rem; font-weight: 50;background-color:rgba(61, 166, 198, 0.22) "> Hello! your answers indicate that you are doing great in your life. We are here to remind you to keep up the great work in maintaining and prioritizing your mental well-being. Whether you are enjoying your favorite activities or connecting with loved ones, keep making those positive choices and taking care of yourself. Wishing you continued wellness and happiness, cheers!</div>',
                unsafe_allow_html=True,
            )

        elif health_2 == "Mild":
            st.markdown(
                '<div style="      padding-left: 40px; padding-right: 40px;padding-top: 20px; padding-bottom: 20px; color:black; font-size: 1.4rem;border-radius:1rem; font-weight: 50;background-color:rgba(61, 166, 198, 0.22) ">  Hello there, based on your answers you seem to do well but we observe that you are struggling to keep up with it. It is completely normal to face challenges. We recommend considering a chat with friends, family, or a mental health professional for additional support. Remember, taking steps for your mental well-being is a positive choice. </div>',
                unsafe_allow_html=True,
            )
        elif health_2 == "Severe":
            st.markdown(
                '<div style="      padding-left: 40px; padding-right: 40px;padding-top: 20px; padding-bottom: 20px; color:black; font-size: 1.4rem;border-radius:1rem; font-weight: 50;background-color:rgba(61, 166, 198, 0.22) ">Hey there, looks like you might be going through a tough time, consider talking to a mental health professional or someone you trust. They can provide support and guidance. Remember, it is okay to seek help. Take care.</div>',
                unsafe_allow_html=True,
            )
        return health_2


if __name__ == "__main__":
    Prediction()
