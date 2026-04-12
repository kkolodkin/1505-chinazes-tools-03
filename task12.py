import requests
def run():
    q = requests.get('https://v2.jokeapi.dev/joke/Programming')
    joker = q.json()
    if joker['type'] == 'twopart':
        joke1 = joker['setup']
        joke2 = joker['delivery']
        print(f'{joke1}')
        print(f'{joke2}')
    if joker['type'] == 'single':
        joke3 = joker['joke']
        print(f'{joke3}')
