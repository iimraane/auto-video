from openai import OpenAI
import requests

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

completion2 = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Vous êtes assistant capable d'aider à transformer des scripts en listes de mots-clés en anglais. Ces mots-clés seront ensuite utilisés pour rechercher des vidéos via l'API de Pexels. Votre tâche consiste à analyser le script donné, à identifier les mots et expressions importants, et à les présenter sous forme de liste de mots-clés."},
    {"role": "user", "content": f"J'ai un script que je veux utiliser pour rechercher des vidéos sur Pexels. Transformez ce script en une liste de mots-clés en anglais et ne me répondez qu'avec les mots-clés, séparés par des '/'. Voici le script : {content}"},
  ]
)

raw_article2 = completion2.choices[0].message.content
content2 = raw_article2.replace("**", "").replace("\n\n", "\n").replace("--", "")

keywords = content2.split("/")


# API PEXELS

API_KEY = 'nzrgfdPALGj5GanRXaoFF6DGmCizvCDXpsnhMrlthtMPRXK0oaAT1Iws'
BASE_URL = 'https://api.pexels.com/videos/search'

headers = {
    'Authorization': API_KEY
}

print(keywords)
print()
print()
for word in keywords:
    query = word
    params = {
        'query': query,
        'per_page': 1,
        'page': 1
    }


    response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)

    data = response.json()
    video = data['videos']

    
    print()
    video_url = video[0]["url"]
    print(f"{word}: {video_url}")

response.stream_to_file("output.mp3")
