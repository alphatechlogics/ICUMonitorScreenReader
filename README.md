# ICU Monitor Data Extraction App 📊💉

Welcome to the ICU Monitor Data Extraction app! This app utilizes OpenAI's Vision API to analyze ICU monitor images, extract vital signs like heart rate (HR), blood pressure (BP), oxygen saturation (SpO2), respiratory rate (RR), temperature, and more. The app displays these vital signs in a user-friendly table format. 🌟

![](https://raw.github.com/alphatechlogics/ICUMonitorScreenReader/aa06d78473ff2f845d6a5bcafa5b3a2987b1c540/Screenshot%202025-06-17%20231241.png)

## 🧑‍💻 How It Works

1. **Upload ICU Monitor Image**: Upload an image from a patient monitor.
2. **Image Analysis**: The app uses OpenAI's Vision API to analyze the uploaded image and extract vital signs.
3. **Data Extraction**: The extracted vital signs such as HR, BP, SpO2, and more are parsed and displayed in a structured tabular format.
4. **Streamlit Interface**: The app provides a user-friendly interface where users can upload images and view the extracted data.

## 🔧 Installation and Setup

### Prerequisites

- Python 3.10 or above
- An OpenAI API key (set up via `.env` for local development or Streamlit Secrets for deployment).

### 1. Clone the repository

```bash
git clone https://github.com/alphatechlogics/ICUMonitorScreenReader.git
cd icu-monitor-data-extraction
```

### 2. **Create a virtual environment**

```bash
python3 -m venv env
source env/bin/activate
# On Windows:env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

- **Locally:** Create a .env file in the root of the project and add your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key
```

- Streamlit Deployment: Store the OpenAI API key in the .streamlit/secrets.toml file as:

```toml
[general]
OPENAI_API_KEY = "your-openai-api-key"
```

### 5. Run the app locally

```bash
streamlit run app.py
```

The app will open in your browser at http://localhost:8501.

🧑‍⚕️ **Features**

- **ICU Monitor Image Analysis**: Analyze uploaded images from ICU monitors.
- **Vital Sign Extraction**: Extracts and displays vital signs such as heart rate (HR), blood pressure (BP), oxygen saturation (SpO2), respiratory rate (RR), and temperature.
- **Structured Data Display**: Displays the extracted data in a neat tabular format using pandas.
- **Dynamic API Key Handling**: Automatically uses API key from `.env` file locally and from Streamlit Secrets when deployed.

⚙️ **Key Technologies**

- **OpenAI Vision API**: Used to extract and analyze the content from the ICU monitor images.  
  Learn more about OpenAI's Vision API here: [OpenAI Vision API Documentation](https://platform.openai.com/docs/guides/vision)
- **Streamlit**: Provides an easy-to-use web interface for the app.
- **Python Libraries**:
  - `openai`: OpenAI API wrapper.
  - `streamlit`: For creating the web interface.
  - `Pillow`: For image processing.
  - `python-dotenv`: For loading environment variables locally.
  - `pandas`: For handling and displaying extracted data in a tabular format.

💡 **Usage**

- **Upload Image**:  
  Click the "Upload ICU Monitor Image" button and select an image of an ICU monitor display (JPG, JPEG, PNG).

- **View Data**:  
  Once the image is uploaded, the app will display the vital signs extracted from the image in a structured table.

### Example Extracted Data:

| Heart Rate (HR) | Blood Pressure | Oxygen Saturation (SpO2) | Temperature | Respiratory Rate (RR) |
| --------------- | -------------- | ------------------------ | ----------- | --------------------- |
| 75 bpm          | 120/80 mmHg    | 98%                      | 37.0°C      | 16 breaths/min        |
