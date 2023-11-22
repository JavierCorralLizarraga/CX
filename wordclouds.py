# imports generales
import pandas as pd
import numpy as np
!pip install scipy
from scipy.stats import norm
from math import sqrt
import pprint
import os
import openpyxl
from openpyxl.utils import column_index_from_string

# declaramos la macro funcion que hara todo lo del word cloud
# imports de la funcion per se
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
!pip install nltk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stoplist = list(stopwords.words('spanish'))

stoplist.append('jubilado')

from sklearn.feature_extraction.text import TfidfVectorizer

def word_cloud(vector):
  corpus = vector.to_string(index = False)
  # le quitamos las stopwords y \n
  # Convert text to lowercase and split to a list of words
  nltk.download('punkt')
  tokens = word_tokenize(corpus.lower())
  # Remove stop words
  tokens_wo_stopwords = [t for t in tokens if t not in stoplist]
  # le aplicamos tfidf para sacar as palabras mas comunes becas
  vectorizer = TfidfVectorizer()
  vectors = vectorizer.fit_transform([corpus])
  feature_names = vectorizer.get_feature_names_out()
  dense = vectors.todense()
  denselist = dense.tolist()
  df = pd.DataFrame(denselist, columns=feature_names)
  df = df.transpose().sort_values(0, ascending= False)
  wordcloud = WordCloud(stopwords=stoplist, background_color='white', colormap = 'Reds').generate(df.to_string())
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.figure()
  plt.imshow(wordcloud, interpolation="bilinear")
  plt.axis("off")

# obtiene el nombre del unico archivo de excel que se acaba de subir
cwd = os.getcwd()
files = os.listdir(cwd)
excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
excel_filename = excel_files[0]
print("_________________________")
print("El nombre del archivo de excel es:", excel_filename)

#se actualiza el nombre del archivo de MA y el IC requerido
# excel_filename = '' # descomenta si quieres utilizar un nombre personalizado
column_letter = 'F'  # declaramos la letra de la columna que queremos

file_path = excel_filename
df = pd.read_excel(file_path)
column_index = column_index_from_string(column_letter) - 1
column_data = df.iloc[:, column_index]
column_data = column_data.dropna()
# column_data = valida() # podria validar los datos pero se vuelvea complejo
print("la siguiente es la informacion que se tomara") # deberian ser solo numeros (probablemente enteros) # pero si no lo es solo toma los valores numericos
column_data

word_cloud(column_data)

