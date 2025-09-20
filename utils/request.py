import requests

class Request:
    pass

    def getData(self, url):
        try:
            response = requests.get(url)
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            raise Exception("Error fetching data")