
# 1 номер
import requests

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    superheroes = ['Hulk', 'Captain America', 'Thanos']
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    
   
    response = requests.get(url)
    if response.status_code == 200:
        all_heroes = response.json()
        intelligence = {}
        

        for hero in all_heroes:
            if hero['name'] in superheroes:
                hero_intelligence = hero['powerstats']['intelligence']
                intelligence[hero['name']] = hero_intelligence
        
        if intelligence:  
            the_smartest_superhero = max(intelligence, key=intelligence.get)
    
    return the_smartest_superhero


if __name__ == "__main__":
    print(get_the_smartest_superhero())
    

# 2 номер
import requests

def get_the_smartest_superhero(superhero_ids) -> str:
    the_smartest_superhero = ''
    url = 'https://akabab.github.io/superhero-api/api' 
    intelligence = {}

    for hero_id in superhero_ids:
        response = requests.get(f"{url}/id/{hero_id}.json")
        if response.status_code == 200:
            hero = response.json()
            hero_intelligence = hero['powerstats']['intelligence']
            intelligence[hero['name']] = int(hero_intelligence)  
            
    if intelligence:  
        the_smartest_superhero = max(intelligence, key=intelligence.get)
    
    return the_smartest_superhero

if __name__ == '__main__':
    assert get_the_smartest_superhero([332, 149, 655]) == 'Thanos'