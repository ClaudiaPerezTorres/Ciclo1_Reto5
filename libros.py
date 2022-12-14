#-*- coding: utf-8 -*-

def estadisticasAutor(db):
   """
   Retorna un diccionario con los nombres de los autores de los libros como llave y
   para cada uno la cantidad de libros correspondientes (valor entero)
   """
   resultado = {}
   for libro in db:
     if libro["author"] in resultado:
       resultado[libro["author"]]+=1
     else:
       resultado[libro["author"]]=1    
   return resultado


def estadisticasFecha(db):
   """
   Retorna un diccionario que tienen como llaves los años en que se publicaron libros (valor entero) y
   para cada año la cantidad de libros correspondientes (valor entero)
   """
   resultado = {}
   for anios in db:
     if anios["year"] in resultado:
       resultado[anios["year"]]+=1
     else:
       resultado[anios["year"]]=1
   return resultado

def estadisticasPais(db):
   """
   Retorna un diccionario con los paises como llave y como valor un diccionario en donde las llaves son los
   idiomas de escritura y el valor es la cantidad total de páginas de dichos libros . 
   """
   resultado = {}
   for paises in db:
     if paises["country"]  in resultado:
       for paginas in resultado[paises["country"]]:
         if paginas in resultado[paises["country"]]:
           resultado[paises["country"]][paginas]+=int(paises["pages"])
     else:
       resultado[paises["country"]]={paises["language"]:paises["pages"]}

   return resultado
  