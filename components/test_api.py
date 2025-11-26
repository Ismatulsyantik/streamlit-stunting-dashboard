

import google.generativeai as genai

genai.configure(api_key="AIzaSyDU0NqtlkBipEyr_4qaddpiHPQQ_MC6vl8")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Coba jelasin apa itu AI dalam 2 kalimat")
print(response.text)