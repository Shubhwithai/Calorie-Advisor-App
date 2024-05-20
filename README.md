# Calorie Advisor

## Description

Calorie Advisor is a Streamlit-based web application that utilizes the power of Google's Gemini Pro Vision API to estimate the calorie content of meals from images. Simply upload a photo of your food, and Calorie Advisor will analyze it to provide an estimated calorie breakdown for each item. 

## Features

* **Image-based calorie estimation:** Upload an image of your meal and receive estimated calorie information.
* **Itemized breakdown:** Calorie Advisor aims to identify individual food items in the image and provide a calorie estimate for each.
* **Easy-to-use interface:** The Streamlit interface makes the app accessible and user-friendly.

## Getting Started

### Prerequisites

* **Python 3.7 or later**
* **An active Google Cloud Project with billing enabled**
* **Google Gemini Pro Vision API enabled** 
* **A Google API Key:**  You can create one in your Google Cloud console. 

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/calorie-advisor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd calorie-advisor
   ```
3. Install the required packages:
    ```bash
   pip install -r requirements.txt
    ```
4. Set up your environment variables:
   Create a .env file in the project root.
   Add your Google API Key:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```
5. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   
## Limitations :
Calorie estimations are approximate: Calorie Advisor relies on image recognition and may not be perfectly accurate.

Portion sizes are estimated visually: Accuracy depends on the clarity of the image and the presentation of the food.

## Contributing:

Contributions are welcome! Please feel free to open issues or submit pull requests.
   
