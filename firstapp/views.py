from django.shortcuts import render

def home(request):
    import requests
    import json

    # grab prices
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,LTC,XLM,EOS&tsyms=EUR')
    price = json.loads(price_request.content)

    # grab news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'firstapp/home.html', {'api': api, 'price':price})


def prices(request):
    import requests
    import json

    if request.method == 'POST':
        quote = request.POST['quote'].upper()
        crypto_request = requests.get(
            'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + str(quote) + 'S&tsyms=EUR')
        crypto = json.loads(crypto_request.content)

        return render(request, 'firstapp/prices.html', {'quote': quote, 'crypto': crypto})


    else:
        notfound = True
        return render(request, 'firstapp/prices.html', {'notfound': notfound})