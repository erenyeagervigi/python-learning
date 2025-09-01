import yfinance as yf
import requests
from twilio.rest import Client

url = "https://newsapi.org/v2/everything"
api_key = API_KEY
COMPANY_NAME = "Tesla Inc"
STOCKS = "TSLA"
#twilio info
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

#getting the stock prices
tesla = yf.Ticker(STOCKS)
data = tesla.history(period = "5d")

closing_prices = data['Close'].to_list()
yesterday = closing_prices[-1]
day_before_yesterday = closing_prices[-2]

difference = abs(yesterday - day_before_yesterday)
percentage = round(difference/yesterday *100)
print(percentage)

change_mark = "🔺" if difference > 0 else "🔻"

def news():
    parameters  = {
        "qInTitle": COMPANY_NAME,
        "apikey": api_key,
        "language": "en",
        "sortBy" : "publishedAt"
    }
    response = requests.get(url = url,params= parameters)
    data_news = response.json()['articles'][:3]
    for article in data_news:
        hint = article['title']
        brief = article['description']

        client = Client(account_sid,auth_token)
        message = client.messages.create(
            from_='whatsapp:NUMBER',
            to='whatsapp:NUMBER',
            body=f'{STOCKS}: {change_mark}{percentage}\n headline: {hint}\n brief: {brief}\n\n'
        )
        print(message.status)

if percentage > 2:
    news()
else:

    print(f"stocks are decreasing")
