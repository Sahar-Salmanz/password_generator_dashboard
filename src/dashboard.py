import streamlit as st
from src.password_generator import PINGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

"""Dashboard for password generation using Streamlit."""

st.image("./image/banner.png")
st.title(":zap: Password Generator")

option = st.radio(
    "Select a password generator", 
    ["Random Password", "Memorable Password", "PIN code"]
)

if option == "PIN code": 
    length = st.slider("Select the length of the PIN code", 4, 10)
    generator = PINGenerator(length)

elif option == "Random Password":
    length = st.slider("Select the length of the password", 8, 32)
    col1, col2 = st.columns(2)
    include_numbers = col1.toggle("Include numbers")
    include_symbols = col2.toggle("Include symbols")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

elif option == "Memorable Password":
    num_of_words = st.slider("Select the number of words", 2, 10)
    separator = st.text_input("Enter a separator character", value="-")
    capitalize = st.toggle("Capitalize words")
    generator = MemorablePasswordGenerator(num_of_words, separator, capitalize)
    
password = generator.generate()
st.write(fr"Your password is: ``` {password} ``` ")