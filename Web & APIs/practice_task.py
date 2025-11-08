# Practice Task 1: GitHub User Info
'''import requests
def get_github_info(username):
    url=f"https://api.github.com/users/{username}"
    res = requests.get(url)

    if res.status_code==200:
        user_data = res.json()
        return {
            'name':user_data.get('name','N/A'),
            'public_repos': user_data.get('public_repos', 0),
            'followers': user_data.get('followers', 0),
            'following': user_data.get('following', 0),
            'bio': user_data.get('bio', 'No bio available')
        }
    else:
        return f"Error : User ' {username} ' not found"

#test
user_info = get_github_info('octocat')
print(user_info)'''

# Practice Task 2: Cryptocurrency Prices
import requests
def get_crypto_price(coins=['bitcoin','ethereum','cardano']):
    """Get cryptocurrency prices from CoinGecko API (free, no key needed)"""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(coins),
        'vs_currencies' : 'usd',
        'include_24hr_change':'true'
    }

    try:
        res = requests.get(url,params=params)
        res.raise_for_status()

        data = res.json()
        crypto_info = {}

        for coin in coins:
            if coin in data:
                crypto_info[coin] = {
                    'price': data[coin]['usd'],
                    'change_24h':data[coin].get('usd_24h_change',0)
                }
            return crypto_info
    except requests.exceptions.RequestException as e :
           print(f"Error fetching crypto prices : {e}")
           return {}
# test
crypto_prices = get_crypto_price()
for coin , info in crypto_prices.items():
    price = info['price']
    change = info['change_24h']
    print(f"{coin.title()}: ${price:,.2f} ({change:+.2f}%)")