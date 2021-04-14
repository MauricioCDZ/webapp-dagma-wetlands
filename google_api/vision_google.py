import os, io
from google.cloud import vision_v1

from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'humedales-cali-token.json'
client = vision_v1.ImageAnnotatorClient()

file_name = 'ave1.jpg'
image_path = os.path.join('/home/mauricio/Documentos/graduation_project/google_api', file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)
response = client.safe_search_detection(image=image)
safe_search = response.safe_search_annotation

likelihood = ('Unknown', 'Very Unlikely', 'Unlikely', 
              'Possible', 'Likely', 'Very Likely')

likelihood1 = (
              'Possible', 'Likely', 'Very Likely')

print('adult: {0}'.format(likelihood[safe_search.adult]))
print('spoof: {0}'.format(likelihood[safe_search.spoof]))
print('medical: {0}'.format(likelihood[safe_search.medical]))
print('violence: {0}'.format(likelihood[safe_search.violence]))
print('racy: {0}'.format(likelihood[safe_search.racy]))

if likelihood[safe_search.adult] in likelihood1:
    print("estoy")
else:
    print("No estoy")