from multiprocessing.connection import Client
from openai import OpenAI
OpenAI()

response = Client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {
      "role": "system",
      "content": "ileri seviye uzman kod geliþtirici bir uzman asistan rolü yap"
    },
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant",
      "content": "Tabii, elbette yardýmcý olabilirim. Size bazý uzman kod geliþtirme süreçleri ile ilgili rehberlik ve ipuçlarý verebilirim. Hangi konularda destek istediðinizi daha spesifik þekilde belirtirseniz, size daha etkili bir þekilde yardýmcý olabilirim. Örneðin, kod yazma sürecinin optimizasyonu, güvenlik standartlarý, test otomasyonu, API entegrasyonu gibi konularda tecrübe ve rehberlik sunabilirim. Yardýmcý olmamý istediðiniz tam olarak nedir?"
    }
  ],
  temperature=1.79,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
