import requests
import time
from pprint import pprint


def find_uk_city(coordinates:list) -> str:
    api = '68077924f2a5f854424769gxq30d650' 
    url = 'https://geocode.maps.co/reverse'

    uk_city = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    
    for latitude, longitude in coordinates:
        response = requests.get(f'{url}?lat={latitude}&lon={longitude}&api_key={api}')
        # city = response.json().get('address', {}).get('city')
        print(latitude, longitude, '--->', end=' ')
        if response.status_code == 200:
            data = response.json()
            address = data.get('address', {})
            city = address.get('city')
            if city in uk_city:
                return city
       
        time.sleep(0.1)

if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'
    print(find_uk_city(_coordinates))