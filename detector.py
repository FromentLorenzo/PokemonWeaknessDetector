import pyautogui
from PIL import Image
import pytesseract

# Spécifiez les coordonnées de la région de l'écran à capturer (x, y, largeur, hauteur)
region = (300, 40, 380, 100)
screenshot = pyautogui.screenshot(region=region)

# Convertissez la capture d'écran en une image Pillow
image = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())

# Affichez l'image


# Utilisez pytesseract pour extraire du texte de l'image
text = pytesseract.image_to_string(image)

# Vérifiez si le mot que vous cherchez est présent dans le texte
if "votre_mot" in text:
    print("Le mot a été détecté à l'écran.")
else:
    print("Le mot n'a pas été détecté à l'écran.")

print(text)


# Spécifiez les coordonnées de la région de l'écran à capturer (x, y, largeur, hauteur)
region = (100, 100, 800, 600)
screenshot = pyautogui.screenshot(region=region)

# Convertissez la capture d'écran en une image Pillow
image = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())

# Affichez l'image
image.show()


