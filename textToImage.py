import google.generativeai as genai
import requests

# Configure Gemini API key
genai.configure(api_key="AIzaSyAMIYlVIEwSUSJxwwSHoG7SJcWVbspx2cg")

def text_to_image(prompt_text):
    # Set the model for text-to-image generation
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Generate image based on the prompt
    response = model.generate_image(prompt_text)

    # Save the image to file
    image_url = response.data[0]['url']
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        with open('generated_image.png', 'wb') as f:
            f.write(image_response.content)
        print("Image saved successfully as 'generated_image.png'")
    else:
        print("Failed to retrieve the image")

if __name__ == "__main__":
    # Prompt text input from user or other sources
    prompt_text = input("Enter the text to generate an image: ")

    # Call the function to generate the image
    text_to_image(prompt_text)
