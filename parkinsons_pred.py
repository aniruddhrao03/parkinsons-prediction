import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Load the model from the specified path
model_path = 'C:/Users/aniru/trafficsignclassification/saved_models/parkinsons_model.sav'
with open(model_path, 'rb') as f:
    parkinsons_model = pickle.load(f)

# Set page configuration
st.set_page_config(page_title="Parkinson's Disease Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Setting up the main interface
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Prediction", "Feature Description"], 
                           icons=['house', 'graph-up', 'info-circle'], menu_icon="cast", default_index=0)

# Home page
if selected == "Home":
    st.title("Parkinson's Disease Prediction App")
    st.write("This application predicts the likelihood of Parkinson's disease based on input features.")

# Prediction page
elif selected == "Prediction":
    st.title("Parkinson's Disease Prediction")

    # Define input columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Prediction button
    if st.button("Predict Parkinson's Status"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer,
                      Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1,
                      spread2, D2, PPE]
        user_input = [float(x) if x else 0 for x in user_input]  # Convert to float, handle empty strings

        # Make prediction
        prediction = parkinsons_model.predict([user_input])
        result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(result)

# Feature Description page
elif selected == "Feature Description":
    st.title("Feature Descriptions")

    st.write("Here are the descriptions of the features used in the prediction model:")

    with st.expander("Fundamental Frequency Measures"):
        st.write("""
        - **MDVP:Fo(Hz)**: Average vocal fundamental frequency
        - **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency
        - **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency
        """)

    with st.expander("Jitter Measures"):
        st.write("""
        - **MDVP:Jitter(%)**: Measure of variation in fundamental frequency
        - **MDVP:Jitter(Abs)**: Absolute measure of variation in fundamental frequency
        - **MDVP:RAP**: Relative amplitude perturbation
        - **MDVP:PPQ**: Five-point period perturbation quotient
        - **Jitter:DDP**: Average absolute difference of differences between jitter cycles
        """)

    with st.expander("Shimmer Measures"):
        st.write("""
        - **MDVP:Shimmer**: Measure of variation in amplitude
        - **MDVP:Shimmer(dB)**: Shimmer in decibels
        - **Shimmer:APQ3**: Three-point amplitude perturbation quotient
        - **Shimmer:APQ5**: Five-point amplitude perturbation quotient
        - **MDVP:APQ**: Eleven-point amplitude perturbation quotient
        - **Shimmer:DDA**: Average absolute difference of differences between shimmer cycles
        """)

    with st.expander("Noise Measures"):
        st.write("""
        - **NHR**: Noise-to-harmonics ratio
        - **HNR**: Harmonics-to-noise ratio
        """)

    with st.expander("Nonlinear Measures"):
        st.write("""
        - **RPDE**: Recurrence period density entropy
        - **DFA**: Detrended fluctuation analysis
        - **spread1**: Nonlinear measure of fundamental frequency variation
        - **spread2**: Nonlinear measure of variation in amplitude
        - **D2**: Nonlinear dynamical complexity measure
        - **PPE**: Pitch period entropy
        """)
        