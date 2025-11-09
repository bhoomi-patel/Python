import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time

class RobustAPIClient:
    """API client with comprehensive error handling"""
    
    def __init__(self, base_url, timeout=10, max_retries=3):
        self.base_url = base_url
        self.timeout = timeout
        self.session = self.create_session(max_retries)
    
    def create_session(self, max_retries):
        """Create session with retry strategy"""
        session = requests.Session()
        
        # Define retry strategy
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,  # Wait 1s, 2s, 4s between retries
            status_forcelist=[429, 500, 502, 503, 504],  # Retry on these errors
        )
        
        # Apply retry strategy
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        return session
    
    def safe_request(self, method, endpoint, **kwargs):
        """Make request with comprehensive error handling"""
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            
            # Check for successful status
            response.raise_for_status()
            
            # Try to parse JSON response
            try:
                return {
                    'success': True,
                    'data': response.json(),
                    'status_code': response.status_code
                }
            except ValueError:
                return {
                    'success': True,
                    'data': response.text,
                    'status_code': response.status_code
                }
                
        except requests.exceptions.Timeout:
            return {
                'success': False,
                'error': 'Request timeout',
                'error_type': 'timeout'
            }
        
        except requests.exceptions.ConnectionError:
            return {
                'success': False,
                'error': 'Connection failed',
                'error_type': 'connection'
            }
        
        except requests.exceptions.HTTPError as e:
            return {
                'success': False,
                'error': f'HTTP error: {e.response.status_code}',
                'error_type': 'http_error',
                'status_code': e.response.status_code
            }
        
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'error_type': 'unknown'
            }

# Example usage:
if __name__ == "__main__":
    client = RobustAPIClient("https://jsonplaceholder.typicode.com")
    result = client.safe_request("GET", "/posts/1")
    print(result)
