import requests
q = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru')
quote = q.json()
rndmquote = quote['quoteText']
print(f'Случайная цитата: {rndmquote}')
