import requests

def run():
    r = requests.get('https://api.adviceslip.com/advice')
    a = r.json()
    b = a['slip']['advice']
    print(b)
