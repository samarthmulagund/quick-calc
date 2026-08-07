import streamlit as st
import base64

def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(
    page_title="QuickCalc - Simple operation calculator",
    page_icon="🧮"
)
img = get_base64("Python_Programs/images/calc-backdrop.jpeg")
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
    if "first_number" not in st.session_state:
        st.session_state.first_number = None

    if "operation" not in st.session_state:
        st.session_state.operation = None
    if "expression" not in st.session_state:
        st.session_state.expression = ""
    st.title("QuickCalc")
    nums = st.text_input("Give numbers", step = 0.5)
    result = 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("+"):
            st.session_state.expression += nums + "+"
    with col2:
          if st.button("-"):
              st.session_state.expression += nums + "-"
    with col3:
        if st.button("X"):
            st.session_state.expression += nums + "X"
    with col4:
        if st.button("÷"):
            st.session_state.expression += nums + "÷"
        if st.button("="):
            st.session_state.expression += nums
            answer = eval(st.session_state.expression)
            st.success("Answer:", answer)
            st.session_state.expression = ""

elif language == "ಕನ್ನಡ":
    st.title("ಕ್ವಿಕ್‌ಕ್ಯಾಲ್ಕ್")
    if "first_number" not in st.session_state:
        st.session_state.first_number = None

    if "operation" not in st.session_state:
        st.session_state.operation = None

    nums = st.number_input("2 ನೇ ಸಂಖ್ಯೆಯನ್ನು ನೀಡಿ.", step=1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("+"):
            st.session_state.first_number = nums
            st.session_state.operation = "+"
    with col2:
        if st.button("-"):
            st.session_state.first_number = nums
            st.session_state.operation = "-"
    with col3:
        if st.button("X"):
            st.session_state.first_number = nums
            st.session_state.operation = "*"
    with col4:
        if st.button("÷"):
            st.session_state.first_number = nums
            st.session_state.operation = "/"
    equal_to = st.button("=")
    answer = 0
    if not equal_to:
        second_number = nums

        if st.session_state.operation == "+":
            answer = st.session_state.first_number + second_number

        elif st.session_state.operation == "-":
            answer = st.session_state.first_number - second_number

        elif st.session_state.operation == "*":
            answer = st.session_state.first_number * second_number

        elif st.session_state.operation == "/":
            if second_number != 0:
                answer = st.session_state.first_number / second_number
            else:
                answer = "Cannot divide by zero"
    else:
        st.success(f"Result = {answer}")
if language == "हिंदी":
    st.title("क्विककैल्क")
    first_num = st.number_input("पहला नंबर दें", step = 1)
    second_num = st.number_input("दूसरा नंबर दें", step = 1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("+"):
             st.write(f"योग है {first_num + second_num}")
    with col2:
        if st.button("-"):
            st.write(f"फ़र्क यह है कि {first_num - second_num}")
    with col3:
        if st.button("X"):
            st.write(f"प्रोडक्ट है {first_num * second_num}")
    with col4:
        if st.button("÷"):
            st.write(f"भागफल है {first_num / second_num}")