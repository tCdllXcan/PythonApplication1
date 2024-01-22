from multiprocessing.connection import Client
from openai import OpenAI
OpenAI()

response = Client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {
      "role": "system",
      "content": "ileri seviye uzman kod geli�tirici bir uzman asistan rol� yap"
    },
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant",
      "content": "Tabii, elbette yard�mc� olabilirim. Size baz� uzman kod geli�tirme s�re�leri ile ilgili rehberlik ve ipu�lar� verebilirim. Hangi konularda destek istedi�inizi daha spesifik �ekilde belirtirseniz, size daha etkili bir �ekilde yard�mc� olabilirim. �rne�in, kod yazma s�recinin optimizasyonu, g�venlik standartlar�, test otomasyonu, API entegrasyonu gibi konularda tecr�be ve rehberlik sunabilirim. Yard�mc� olmam� istedi�iniz tam olarak nedir?"
    }
  ],
  temperature=1.79,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
