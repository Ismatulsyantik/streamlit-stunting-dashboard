

import google.generativeai as genai

genai.configure(api_key="AIzaSyCQgOnGpVFL31lzpW3eZ6Z7pXxX_cwkThk")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Coba jelasin apa itu AI dalam 2 kalimat")
print(response.text)