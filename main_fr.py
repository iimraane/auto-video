from openai import OpenAI

subject = input("Veuillez entrez un sujet : ")

client = OpenAI(api_key="sk-None-oIksOxLleRb80Uv9mOoQT3BlbkFJQLKAX7hdRkkwEMFw6qqb")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Vous êtes un journaliste professionnel. Votre objectif est de fournir des informations précises, objectives et captivantes. Vérifiez toujours vos sources sur Internet, évitez les biais et assurez-vous que vos articles sont bien structurés et intéressants pour le lecteur. Utilisez un langage clair et accessible, et veillez à ce que chaque information soit présentée de manière équilibrée et factuelle. En plus de la rigueur journalistique, faites preuve de talent narratif pour maintenir l'attention du lecteur jusqu'à la fin du TikTok."},
    {"role": "user", "content": f"Rédigez un article captivant sur {subject} qui peut être lu en 1 minute sur TikTok. L'article doit être informatif, engageant et clair, tout en restant concis. Assurez-vous de captiver l'attention du public dès le début et de maintenir leur intérêt tout au long. Utilisez des phrases courtes et dynamiques, et mettez en avant les faits les plus importants et intéressants. Rédigez un article d'actualité sans utiliser de marqueurs de formatage comme '', '.n.n', et '--'.**"},
  ]
)
print()
print()
print()
print(completion.choices[0].message.content)
print()
print()
print()

raw_article = completion.choices[0].message.content
content = raw_article.replace("**", "").replace("\n\n", "\n").replace("--", "")

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input= f"{content}",
)

response.stream_to_file("output.mp3")

