import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"C:\Users\Sathsara\Documents\Python Learning\Translation test\translationAPI\flash-medley-278816-b2012b874797.json"
translate_client=translate.Client()

text="Good Morning"
target='si'

output=translate_client.translate(

    text,
    target_language=target

)

print(output)