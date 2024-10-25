import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image

# Load the API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image, prompt):
    """Send image to Google's AI and get calorie information"""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content([image[0], prompt])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def prepare_image(uploaded_file):
    """Convert uploaded image to format required by Google's AI"""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return None

def main():
    st.set_page_config(page_title="Calorie Advisor", page_icon="🍽️")
    
    st.title("🍽️ Calorie Advisor")
    st.write("Upload a photo of your food to get detailed calorie information!")

    uploaded_file = st.file_uploader(
        "Upload your food image (jpg, jpeg, or png)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Your Food Image", use_column_width=True)

        if st.button("Calculate Calories"):
            with st.spinner("Analyzing your food..."):
                # Updated prompt to get more specific responses
                prompt = """
                Analyze the food items in this image and provide a detailed breakdown.
                Give specific calorie estimates for each visible item.
                
                Please format your response exactly like this:
                
                🍽️ FOOD ITEMS AND CALORIES:
                1. [Food Item] - [X] calories
                2. [Food Item] - [X] calories
                (List all visible items)
                
                📊 TOTAL CALORIES: [Sum] calories
                
                🔍 NUTRITIONAL BREAKDOWN:
                • Protein: [X]g
                • Carbs: [X]g
                • Fats: [X]g
                
                💡 HEALTHY EATING TIPS:
                • [Specific tip about this meal]
                • [Suggestion for making this meal healthier]
                
                Important: Provide specific numbers and avoid any disclaimers about estimation accuracy.
                """

                image_data = prepare_image(uploaded_file)
                if image_data is not None:
                    response = get_gemini_response(image_data, prompt)
                    
                    # Display the response in a clean format
                    st.success("Analysis Complete!")
                    st.markdown(response)

if __name__ == "__main__":
    main()
