# API Keys - Simple string tokens
# OAuth - Secure authorization standard
# JWT Tokens - Stateless authentication

'''API Key Authentication'''
# import requests
# # method 1 - query parameter
# def api_key_in_params(api_key):
#     params = {'api_key':api_key , 'q':'python'}
#     response = requests.get('https://api.example.com/search',params=params)
#     return response.json()

# # method 2 - header authentication
# def api_key_in_header(api_key):
#     headers = {'X-API-Key':api_key}
#     response = requests.get('https://api.example.com/data',headers=headers)
#     return response.json()

# # method 3 - bearer token
# def bearer_token_auth(token):
#     headers={'Authorization':f'Bearer{token}'}
#     response = requests.get('https://api.example.com/protected',headers=headers)
#     return response.json()

'''session management'''
import requests

class APIClient:
    """Professional API client with session management"""
    
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'User-Agent': 'MyApp/1.0'
            })
    
    def get(self, endpoint, params=None):
        """Make GET request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET error: {e}")
            return None
    
    def post(self, endpoint, data=None):
        """Make POST request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST error: {e}")
            return None
    
    def close(self):
        """Close session"""
        self.session.close()

# Usage
client = APIClient('https://api.example.com', 'your-api-key')
data = client.get('/users/123')
client.close()
                 