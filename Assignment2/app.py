import joblib
import pandas as pd
import streamlit as st


# --- App Layout ---

# 1. Title
st.title('Objective Movie Review Sentiment Analyzer')
# 2. Short description of what the app does.
st.text("This app accepts any movie review the user inputs and intelligently returns the sentiment of the words, positive or negative.")
# 3. Load the Saved Model
@st.cache_data
def load_model():
    """Loads the pre-trained model and target names."""
    model = joblib.load('./sentiment_model.pkl')
    return model

# 4. Create the User Input Interface

user_text = st.text_area("Enter a movie review to analyze:", "Enter text here...", height=200)
# 5. Add analyze button & Write an if block that checks if the "Analyze" button has been pressed
if st.button("Analyze"):
    # Make sure the user has entered some text before trying to make a prediction.
    if not user_text:
        st.write("Please write review before analyzing.")
    else:
        # Load the model and class names
        model = load_model()
        category = ["Negative","Positive"]
        prediction = model.predict([user_text])[0]
        pred = category[int(prediction)]
        prediction_proba = model.predict_proba([user_text])
        st.subheader('Prediction Result:')
        if pred == "Positive":
            st.success(f"Predicted Sentiment: {pred} \U0001F44D")
        else:
            st.error(f"Predicted Sentiment: {pred} \U0001F44E")
        st.subheader('Prediction Probabilities:')
        st.bar_chart(pd.DataFrame(prediction_proba, columns=category),color=["#FF0000","#228B22"])
