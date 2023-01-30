import pandas as pd
from googletrans import Translator


data = pd.read_csv("hindi.csv")
print(data)


translator = Translator()
translations = {}
for column in data.columns:
    unique = data[column].unique()
    for element in unique:
        translations[element] = translator.translate(element,src='la').text
for i in translations.items():
    print(i)

data.replace(translations, inplace=True)
print(data)


# pip install googletrans==3.1.0a0 - Error Becuase module version missmatch
