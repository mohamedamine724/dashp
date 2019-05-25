import pymongo
import pandas as pd
import csv
import json
import os
import sys
import datetime
import logging
import shutil
import dateutil.parser
from pandas import ExcelWriter
from pandas import ExcelFile
from bson.objectid import ObjectId

### MongoDB Connection ###
myclient = pymongo.MongoClient("mongodb://192.168.56.105:27017/")
mydb = myclient["projecte"]
mycol = mydb["consum"]


### CLASS ###

#Crea el JSON definitiu.

class Dia:
  #un dia i una array de class Consum
  def __init__(self, dia, objArray):
    self._id = dia
    #self.dia = dia
    self.consum = objArray


# Aquesta clase li paso els camps del csv i genera un JSON_Object
    
class Consum:
  def __init__(self, diahora, consum_directe, consum, energia_xarxa):
    self.diahora = diahora
    self.consum_directe = consum_directe
    self.consum = consum
    self.energia_xarxa = energia_xarxa


### FUNCTIONS ###
    
# Funció per obtenir la data del nom del fitxer.

def GetDateCSVFileName(nomfitxer):
    year = nomfitxer.split("_")[4]
    month = nomfitxer.split("_")[5]
    day = nomfitxer.split("_")[6]
    day2 = day[:2]   
    x = datetime.datetime(int(year), int(month), int(day2))
    return (x)



# Carregar tots els fitxers en una array

arr = os.listdir("C:/Users/Mohamed Boulaayoun/Desktop/Projecte - Mohamed/Fase1 - Scripting CSV_JSON/Fitxers Excels")


# Configuració del fitxers de logs

logging.basicConfig(filename='./logs.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)



# El For fa un recorregut de tota la carpeta i va trancant els fitxer un a un
for nom_fitxer in arr:

  ruta = "C:/Users/Mohamed Boulaayoun/Desktop/Projecte - Mohamed/Fase1 - Scripting CSV_JSON/Fitxers Excels/"+nom_fitxer

  try:
    nom_fitxer_clean = GetDateCSVFileName(nom_fitxer)
        
    row = pd.read_excel(ruta, sheet_name='d13f7961-ff45-41d3-b295-ad7f7c1', names =['datahora','Consumido directamente','Consumo','Energía obtenida de la red'])
    
    dia2 = str(str(nom_fitxer_clean.year)+"-"+str(nom_fitxer_clean.month)+"-"+str(nom_fitxer_clean.day))

    # Comprovació si el fitxer existeix a la base de dades #
    s = mycol.find_one( {'_id': dia2})
        
    if s is None:
      salida = "Afegint el document del dia: "+dia2
      print(salida)
    else:
      print("Esborrant el document: {0}".format(dia2))
      mycol.delete_one({'_id': dia2})

    
    d = Dia(dia2,[]);

    for i in row.index[1:]:
         # Obtenir Dia/Hora
         dia = row['datahora'][i]
         
     
         ### CONSUM ###
         
         # Obtenir el camp del consum directe
         consum_directe = row['Consumido directamente'][i]

         # Obtenir el camp del consum
         consum = row['Consumo'][i]


         # Obtenir la energia de xarxa 
         energia_xarxa = row['Energía obtenida de la red'][i]

         data_hora = dia
         
         # Creació del objecte "Consum" amb els camps del fitxer 
         c = Consum(data_hora,consum_directe,consum,energia_xarxa)

         
         # Afegim el objecte c(Consum) a una array dels consums de la Classe Dia
         d.consum.append(c.__dict__) 
         
         
    # Fer INSERT al Mongo
    mycol.insert_one(d.__dict__);

    # Escriure l'esdeveniment en el fitxer LOG
    s = nom_fitxer+" "+"OK"
    logging.info(s)

    # Moure el fitxer a la carpeta OK (A vegades quan intento moure el fitxer a la carpeta KO i el fitxer ja es troba en la carpeta peta el programa
    # already exists, controlo això amb un try catch i elimino el fitxer.)
    try:
      shutil.move(ruta, "./OK")
    except:
      os.remove(ruta)

  except:
    # Escriure l'esdeveniment en el fitxer LOG
    s2 = nom_fitxer+" "+str(sys.exc_info()[1])
    logging.warning(s2)

    # Moure el fitxer a la carpeta KO (A vegades quan intento moure el fitxer a la carpeta KO i el fitxer ja es troba en la carpeta peta el programa
    # already exists, controlo això amb un try catch i elimino el fitxer.)
    try:
      shutil.move(ruta, "./KO")
    except:
      os.remove(ruta)

# Final d'execució
print("Final de l'execució")

