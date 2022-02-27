#!/usr/bin/env python
# coding: utf-8

# # Taller 1.
# 
# ## Johader Guillermo Cuellar Medina.

# ### Descripción de uno.
# 
# * En la primera imagen se describe por qué cada país es considerado el más hermoso, es una visualización interactiva donde se sitúa el mouse reacciona un pupop animado informado atreves de él la documentación principal del lugar seleccionado.
#     McCandless, D. (2021, diciembre 8). Because every country is the most beautiful at something. Information Is Beautiful. https://informationisbeautiful.net/visualizations/because-every-country-is-the-most-beautiful-at-something/
#     
# 
# *   Se evidencia en la segunda visualización la cantidad de ataques recientes y notables de ransomware, se trata de una clase de malware que representa un riesgo para los equipos y se basa en bloquear el dispositivo donde la persona paga un rescate para poder seguir usándolo.
#     McCandless, D. (2021, junio 23). Ransomware attacks. Information Is Beautiful. https://informationisbeautiful.net/visualizations/ransomware-attacks/
# 

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('C:/Users/johad/OneDrive/Escritorio/MI INFO/guardado/Universidad Santo tomas/Semestre 20221/VISUALIZACION PYTHON/data1.jpg')
plt.imshow(img)
plt.show()


# * ¿Qué?

# Se puede ver en la imagen que cuenta con áreas por colores para identificar a cada país, como dato adicional cuenta con las palabras del porque ese país es considerado hermoso.
#     

# * ¿Por qué?

# Se implementa una visualización para ubicar a cada país en el mapa correspondiente y adjuntar en el mismo la característica del porque es considerado hermoso.

# * ¿Cómo?

# Relaciona los datos por medio de marcas de área para un solo gráfico, codificando cada país y asignando un color para diferenciarlo a los demás, adicionalmente, ubica la variable o la característica para identificarlo porque es considerado hermoso.

# ### Marcas y Canales

# * Canales

# Canal Color, Canal de tamaños, Canal de Posición, Vertical, Horizontal.

# * Marcas

# Marca de área

# ### Reglas Generales 

# Se visualiza la información en una sola escena y no es difícil perder la información. En cuanto al zoom y filtros cumplen.

# ### Recomendaciones

# Se debe considerar la variable de la característica por el cual el país es conocido como hermoso, ya que algunas se sobre oponen, considero que se debe tener en cuenta el canal de posición espacial.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('C:/Users/johad/OneDrive/Escritorio/MI INFO/guardado/Universidad Santo tomas/Semestre 20221/VISUALIZACION PYTHON/data2.jpg')
plt.imshow(img)
plt.show()


# * ¿Qué?

# Se visualiza en área de circunferencia la cantidad de ataques de ransomware por marca comercial desde el año 2016 al año 2021, según la visualización existen 7 marcas a las cuales se les ha realizado bloqueos de dispositivos en los 5 años de análisis.

# * ¿Por qué?

# Se permite identificar los datos más relevantes y comparar por medio de los tamaños los valores de las marcas relacionadas.

# * ¿Cómo?

# La información se clasifica de manera un poco desordenada por medio de áreas circulares y en dos tipos de colores principales. considero que es una visualización interactiva que nos brinda una información más detallada al poner el mouse sobre el circulo.

# ### Marcas y Canales.

# * Marca de área - Circulos.

# * Canales - Color, Tamaño y de Posición.

# ### Reglas Generales.

# Cumple con una sola escena, con oclusión, es decir que falta información ya que solo se visualizan 7 marcas significativas.

# ### Recomendaciones.

# Se recomienda realizar la participación de más colores, con degradados por cantidad de datos, con cambios de marcas con tipos de áreas u otras.

# 20-06-2022

# 
