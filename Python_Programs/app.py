import streamlit as st
import base64

def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(
    page_title="QuickCalc",
    page_icon="🧮"
)
img = get_base64("Python_Programs/images/calculator_background.jpeg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
language = st.selectbox(
            "Select Preferred Language",
            ["English", "ಕನ್ನಡ", "हिंदी"]
)
if language == "English":
    st.title("QuickCalc")
    first_num = st.number_input("Give 1st number", step = 1)
    second_num = st.number_input("Give 2nd number", step = 1)
    operation = st.selectbox(
                    "Select operation",
                    ["Addition", "Subtraction", "Multiplication", "Division"]
    )
    if operation == "Addition":
         st.write(f"Sum is {first_num + second_num}")
    elif operation == "Subtraction":
        st.write(f"Difference is {first_num - second_num}")
    elif operation == "Multiplication":
        st.write(f"Product is {first_num * second_num}")
    elif operation == "Division":
        st.write(f"Quotient is {first_num / second_num}")

elif language == "ಕನ್ನಡ":
    st.title("ಕ್ವಿಕ್‌ಕ್ಯಾಲ್ಕ್")
    first_num = st.number_input("1 ನೇ ಸಂಖ್ಯೆಯನ್ನು ನೀಡಿ", step=1)
    second_num = st.number_input("2 ನೇ ಸಂಖ್ಯೆಯನ್ನು ನೀಡಿ.", step=1)
    operation = st.selectbox(
        "ಕಾರ್ಯಾಚರಣೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        ["ಸ೦ಕಲನ", "ವ್ಯವಕಲನ", "ಗುಣಾಕಾರ", "ವಿಭಾಗ"]
    )
    if operation == "ಸ೦ಕಲನ":
        st.write(f"ಮೊತ್ತವು {first_num + second_num}")
    elif operation == "ವ್ಯವಕಲನ":
        st.write(f"ವ್ಯತ್ಯಾಸವೆಂದರೆ {first_num - second_num}")
    elif operation == "ಗುಣಾಕಾರ":
        st.write(f"ಉತ್ಪನ್ನವು {first_num * second_num}")
    elif operation == "ವಿಭಾಗ":
        st.write(f"ಅಂಶವು {first_num / second_num}")

if language == "हिंदी":
    st.title("क्विककैल्क")
    first_num = st.number_input("पहला नंबर दें", step = 1)
    second_num = st.number_input("दूसरा नंबर दें", step = 1)
    operation = st.selectbox(
                    "ऑपरेशन चुनें",
                    ["जोड़ना", "घटाव", "गुणा", "विभाजन"]
    )
    if operation == "जोड़ना":
         st.write(f"योग है {first_num + second_num}")
    elif operation == "घटाव":
        st.write(f"फ़र्क यह है कि {first_num - second_num}")
    elif operation == "गुणा":
        st.write(f"प्रोडक्ट है {first_num * second_num}")
    elif operation == "विभाजन":
        st.write(f"भागफल है {first_num / second_num}")