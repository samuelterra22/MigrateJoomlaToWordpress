# import hashlib
#
# m = hashlib.md5()
# m.update("Image1625".encode('utf-8'))
# print(m.hexdigest())
# print("ab62275605c41a191b9e46f582304ada")




from PIL import Image
import requests
from io import BytesIO

response = requests.get("http://corregofundo.mg.gov.br/media/k2/items/src/ab62275605c41a191b9e46f582304ada.jpg")
img = Image.open(BytesIO(response.content))
