from openai import OpenAI

subject = input("Veuillez entrez un sujet : ")

client = OpenAI(api_key="sk-None-oIksOxLleRb80Uv9mOoQT3BlbkFJQLKAX7hdRkkwEMFw6qqb")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a professional journalist. Your goal is to provide accurate, objective, and captivating information. Always verify your sources on internet, avoid biases, and ensure your articles are well-structured and interesting to the reader. Use clear and accessible language, and make sure each piece of information is presented in a balanced and factual manner. In addition to journalistic rigor, demonstrate narrative talent to keep the reader's attention throughout the end of the tiktok."},
    {"role": "user", "content": f"Write a captivating article on {subject} that can be read in 1 minute on TikTok. The article should be informative, engaging, and clear, while remaining concise. Make sure to capture the audience's attention right from the beginning and keep their interest throughout. Use short, dynamic sentences, and highlight the most important and interesting facts. Write a breaking news article without using formatting markers like '**'', '\.n\.n', and '--''.''"}
  ]
)

raw_article = completion.choices[0].message.content
content = raw_article.replace("**", "").replace("\n\n", "\n").replace("--", "")



response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input= f"{content}",
)

print()
print()
print()
print(content)
print()
print()
print()

response.stream_to_file("output.mp3")
