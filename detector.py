import pyautogui
from PIL import Image
import pytesseract
import requests

# Spécifiez les coordonnées de la région de l'écran à capturer (x, y, hauteur, largeur)
region = (300, 70, 280, 68)
screenshot = pyautogui.screenshot(region=region)

# Convertissez la capture d'écran en une image Pillow
image = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())

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
    print("Aucun Pokémon ne correspond à votre recherche.")