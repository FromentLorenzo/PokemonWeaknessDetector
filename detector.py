import pyautogui
from PIL import Image
import pytesseract
import requests
import Levenshtein

def get_pokemon_names():
    # Faites une requête pour obtenir les données des Pokémon à partir de l'URL
    url = "https://pokebuildapi.fr/api/v1/pokemon"
    response = requests.get(url)
    
    # Vérifiez si la requête s'est terminée avec succès
    if response.status_code == 200:
        # Analysez le contenu JSON de la réponse
        data = response.json()
        
        # Extrait les noms des Pokémon dans une liste
        pokemon_names = [pokemon["name"] for pokemon in data]
        
        return pokemon_names
    else:
        # En cas d'échec de la requête, retournez une liste vide
        return []

# Spécifiez les coordonnées de la région de l'écran à capturer (x, y, hauteur, largeur)
region = (300, 70, 280, 68)
screenshot = pyautogui.screenshot(region=region)

# Convertissez la capture d'écran en une image Pillow
image = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())
image.show()

# Utilisez pytesseract pour extraire du texte de l'image
text = pytesseract.image_to_string(image)
morceaux = text.split(' ', 1)
text = morceaux[0]
# Affichez le texte extrait
print("Texte extrait de l'image:", text)

# Formatez l'URL avec le nom du Pokémon extrait
url = f"https://pokebuildapi.fr/api/v1/pokemon/{text}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Extrait les informations du Pokémon
    name = data["name"]
    print(f"Nom : {name}")
    filtered_resistances = [resistance for resistance in data["apiResistances"] if resistance["damage_multiplier"] in {2, 4}]

    # Affichez les résistances avec damage_multiplier égal à 2 ou 4
    for resistance in filtered_resistances:
        print(resistance)
    
else:
    # Texte extrait
    extracted_text = text  # Remplacez par le texte réel

    # Liste de noms de Pokémon
    pokemon_names = get_pokemon_names()

    # Trouver le Pokémon le plus similaire
    best_match = min(pokemon_names, key=lambda name: Levenshtein.distance(extracted_text, name))
    print(f"Le Pokémon le plus similaire est {best_match}")

    # Formatez l'URL avec le nom du Pokémon le plus similaire
    url = f"https://pokebuildapi.fr/api/v1/pokemon/{best_match}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extrait les informations du Pokémon similaire
        name = data["name"]
        print(f"Nom : {name}")
        filtered_resistances = [resistance for resistance in data["apiResistances"] if resistance["damage_multiplier"] in {2, 4}]

        # Affichez les résistances avec damage_multiplier égal à 2 ou 4
        for resistance in filtered_resistances:
            print(resistance)
