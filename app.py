from openai import OpenAI
import streamlit as st
from PIL import Image
import io
import base64
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file (only for local development)
load_dotenv()

# Check if running in Streamlit deployment or locally and get API key
if "OPENAI_API_KEY" in os.environ:
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Local development
else:
    openai_api_key = st.secrets["OPENAI_API_KEY"]  # Streamlit Secrets

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Function to convert the image to base64
def image_to_base64(image):
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

# Function to analyze the image using OpenAI's Vision API
def analyze_image(image):
    # Convert image to base64
    image_base64 = image_to_base64(image)
    
    # Send request to OpenAI Vision API with enhanced prompt
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Ensure you're using the correct vision-enabled model
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Please extract the following vital signs from the ICU monitor image: Heart rate (HR), Blood pressure, Oxygen saturation (SpO2), Respiratory rate (RR), Temperature, and any other relevant clinical data."},
                    {
                        "type": "image_url", 
                        "image_url": {
                            "url": "data:image/png;base64," + image_base64  # Include base64 image string
                        }
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    
    # Correct way to access the content
    extracted_content = response.choices[0].message.content
    return extracted_content

# Streamlit app interface
st.title("ICU Monitor Data Extraction using OpenAI Vision API")

# Upload the ICU monitor image
uploaded_image = st.file_uploader("Upload ICU Monitor Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Open and display the uploaded image
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded ICU Monitor Image", use_container_width=True)

    # Analyze the image using OpenAI Vision API
    with st.spinner("Analyzing image..."):
        extracted_data = analyze_image(img)

    # Display the extracted data from the image
    st.write("Extracted Data from ICU Monitor Image:")
    st.text(extracted_data)

    # Try to parse the extracted data into structured information
    vital_signs = {}
    lines = extracted_data.split("\n")
    for line in lines:
        if "Heart Rate" in line or "HR" in line:
            vital_signs["Heart Rate (HR)"] = line
        if "Blood Pressure" in line or "/" in line:
            vital_signs["Blood Pressure"] = line
        if "SpO2" in line:
            vital_signs["Oxygen Saturation (SpO2)"] = line
        if "Temperature" in line:
            vital_signs["Temperature"] = line
        if "Respiratory Rate" in line or "RR" in line:
            vital_signs["Respiratory Rate (RR)"] = line

    # Display structured data in tabular format
    if vital_signs:
        df = pd.DataFrame([vital_signs])
        st.dataframe(df)
    else:
        st.warning("No vital signs detected in the image.")
