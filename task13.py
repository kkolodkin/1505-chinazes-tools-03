import requests

def run():
    q = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    fact = q.json()
    rndmfact = fact['text']
    print(f'Случайный факт: {rndmfact}')
