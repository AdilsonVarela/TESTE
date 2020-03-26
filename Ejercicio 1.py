#!/usr/bin/env python
# coding: utf-8

# #                                           EJERCICIO 1

# ### La lista de sentimientos y sus respectivos valores.

# In[1]:


valores = {} 
for linea in open("Sentimientos.txt"): 
    termino, valor = linea.split("\t") 
    valores[termino] = int(valor) 
print (valores.items())


# ### Leyendo archivos de Tweets.

# 1- Los tweets se pueden encontrar en el archivo Tweets.txt. Tenga en cuenta que cada línea en el archivo Tweets.txt contiene una cadena JSON. La función json.loads del paquete interno de python se usó para leer cada línea del archivo Tweewts.txt.
# A continuación se muestra un ejemplo de cada línea de archivo tweets.txt leída con json.loads.
# 

# In[15]:


import json
for line in open('Tweets.txt', 'r'):
        valor=json.loads(line)
        print(valor)


# 2- Tenga en cuenta que las salidas son diccionario anidado, para descomprimir estas claves y valores, se ha escrito una función llamada print_json que tiene como datos de parámetro y k (valor) por defecto 0. 

# In[20]:


def print_json(data,k):
   
        if type(data) == dict:
                for k, v in data.items():
                    if (isinstance(v,str) or isinstance(v,dict)):
                        print_json(v,k)

        else: 
                print (k,":",data)


# 3- Llame a la función print_json para descomprimir el diccionario anidado

# In[21]:


import json
for line in open('Tweets.txt', 'r'):
        valor=json.loads(line)
        print_json(valor,0)


# 4- Conociendo los sentimientos en el archivo sentemientos.txt, tomamos la iniciativa de que no todos los tweets en el archivo Tweets.txt nos interesan. Por ejemplo, todos los tweets con valores enteros, valores nulos y None son descartados.

# ### Interpretación del Ejercicio:

# 5- El requisito de hacer ejercicio de forma resumida, verifique si los sentimientos del archivo sentimiento.txt contienen los tweets del archivo Tweets.txt, si el sentimiento contiene tweets, debe representarse con la suma de sus valores respectivos, valores que se calculan en sentimentos.txt. También se observa que estamos interesado en comparar los valores del archivo Tweets.txt con la clave del archivo sentimientos.txt, en el que se descartan las claves del archivo Tweets.txt.
# 
# 
Por Ejemplo:

SENTIMENTOS: ugly = -3
SENTIMENTOS: better = 2
SENTIMENTOS: beautiful = 3

---------- COMPROBAR-----------
EL SEGUINTE TWEET: ['You', 'better', 'believe', 'your', 'beautiful'] , TIENE UN SENTIMIENTO ASSOCIADO DE: 5
# 6- Para calcular la suma de valores de sentimientos, se creó una función llamada soma_valor que recibe una lista de valores de sentimeintos que contiene tweets. El guión sigue

# In[22]:


def soma_valor(valor):
    soma = 0
    for i in valor:
        soma+=i
  
    return soma


# ###  GUIÓN COMPLETO PARA EL EJERCICIO 1

# In[ ]:


# ---------------------------archivo de lectura sientimiento.txt------------
valores = {} 
for linea in open("Sentimientos.txt"): 
    termino, valor = linea.split("\t") 
    valores[termino] = int(valor) 
#print (valores.items())


# In[24]:


#----------------------funcion soma_valor -------------------
def soma_valor(valor):
    soma = 0
    for i in valor:
        soma+=i
  
    return soma


# In[23]:


#----------------------funcion print_json -------------------

def print_json(data,k):
    
        if type(data) == dict:
                for k, v in data.items():
                    if (isinstance(v,str) or isinstance(v,dict)):
                        print_json(v,k)

        else:
            valor=[]
            data=data.split(" ")
            if (type(data) is list and data !=None) : 
                
                for tweet in data:
                    
                    for sent, k in valores.items():
                        if sent.upper() == tweet.upper():
                            valor.append(k)
                            print("SENTIMENTOS:", sent,"=",k,)                            
                           

                num_ass=soma_valor(valor)
                if num_ass != 0:
                    print("---------- COMPROBAR-----------")
                    print("EL SEGUINTE TWEET:",data,"," " ""TIENE UN SENTIMIENTO ASSOCIADO DE:",num_ass)
                    print("-----------------------------------------------------------------------------------------------")

                          


# In[25]:


# ---------------------------archivo de lectura sientimiento.txt------------
import json
for line in open('Tweets.txt', 'r'):
        valor=json.loads(line)
        print_json(valor,0)


# ### Conclusión y observaciones finales.

# 7- El ejercicio fue útil para articular la teoría con la práctica que probablemente servirá para que el alumno tenga un buen ajuste en el mundo de los negocios. Creo que el propósito del ejercicio se logró de acuerdo con mi comprensión e interpretación del ejercicio. Aunque no es obligatorio, se deben agregar algunas tareas, como limpiar los tweets, eliminar imágenes y validar los datos con la función regesp. Tenga en cuenta que a  los sentimeitos que no tienen tweets se les asigna un valor de 0. Esto se hace con un else después de la condición (if num_ass! = 0 :), no se presentó debido a la claridad de las salidas.

# ##### -----------------------------------------------------FIM-------------------------------------------

# ######  PS. El texto fue escrito en portugués y traducido al español con google translate

# In[ ]:





# In[ ]:




