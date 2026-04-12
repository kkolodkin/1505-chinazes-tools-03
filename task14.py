import requests
text_to_translate=input("Введите текст на английском ( до 200 символов): ")[:200]
url="https://api.mymemory.translated.net/get?q=Hello&langpair=en|ru"
params= {
    "q": text_to_translate,
    "langpair": "en|ru"
}

response=requests.get(url, params=params)
data= response.json()
translated_text=data["responseData"]
["translatedText"]

print(f"Перевод: {data['responseData']['translatedText']}")
