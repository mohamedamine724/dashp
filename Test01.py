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

### Mongo Connection ###
myclient = pymongo.MongoClient("mongodb://192.168.56.102:27017/")
mydb = myclient["projecte"]
mycol = mydb["consum"]


### FUNCTIONS ###

#Crea el JSON final.
class Dia:
  #un dia i una array de class Consum
  def __init__(self, dia, objArray):
    self._id = dia
    #self.dia = dia
    self.consum = objArray

##"dia": "2019-01-01",
##"dades": [
##  {
##    "hora": "00:00",
##    "consum_directe": 1.2,
##    "consum": 24,
##    "energ_obtn_xarxa": 22
##  },
##  {
##    "hora": "01:00",
##    "consum_directe": 1.5,
##    "consum": 22,
##    "energ_obtn_xarxa": 27
##  }
##]

#Classe la cual le paso los campos del csv i genera un JSON_Object.
    
class Consum:
  def __init__(self, diahora, consum_directe, consum, energia_xarxa):
    self.diahora = diahora
    self.consum_directe = consum_directe
    self.consum = consum
    self.energia_xarxa = energia_xarxa


# Funcion para obtener la fecha del nombre del fichero.
def GetDateCSVFileName(nomfitxer):
    year = nomfitxer.split("_")[4]
    month = nomfitxer.split("_")[5]
    day = nomfitxer.split("_")[6]
    day2 = day[:2]   
    x = datetime.datetime(int(year), int(month), int(day2))
    return (x)

def CheckIfExists(nom):
    for x in mycol.find({"_id": name}):
        if x == "":
          print("no hay nada.. HACER EL INSERT NORMALMENTE")

        else:
          print("DELETE AND AFTER TO THE INSERT ¿?¿? UPDATE")
          mycol.deleteOne( { "_id": name } )

arr = os.listdir("C:/Users/Mohamed Boulaayoun/Desktop/Projecte - Mohamed/Fase1 - Scripting CSV_JSON/Prova Fitxers Excels")




logging.basicConfig(filename='./logs.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)



### FUNCTIONS ###
#Crea el JSON 
class Dia:
  #un dia i una array de class Consum
  def __init__(self, dia, objArray):
    self._id = dia
    #self.dia = dia
    self.consum = objArray

##"dia": "2019-01-01",
##"dades": [
##  {
##    "diahora": "2018-10-03 00:00",
##    "consum_directe": 1.2,
##    "consum": 24,
##    "energ_obtn_xarxa": 22
##  },
##  {
##    "diahora": "2018-10-03 01:00",
##    "consum_directe": 1.5,
##    "consum": 22,
##    "energ_obtn_xarxa": 27
##  }
##]

#Classe la cual le paso los campos del csv i genera un JSON_Object.
    
class Consum:
  def __init__(self, diahora, consum_directe, consum, energia_xarxa):
    self.diahora = diahora
    self.consum_directe = consum_directe
    self.consum = consum
    self.energia_xarxa = energia_xarxa




for nom_fitxer in arr:
  ruta = "C:/Users/Mohamed Boulaayoun/Desktop/Projecte - Mohamed/Fase1 - Scripting CSV_JSON/Prova Fitxers Excels/"+nom_fitxer
  try:
    nom_fitxer_clean = GetDateCSVFileName(nom_fitxer)
    print(nom_fitxer_clean)
    #nom_fitxer+"."
    #Generar el JSON para luego hacer el Insert en MongoDB.
    # Extreure el dia del nom dl fitxer
    #ruta = "C:/Users/Mohamed Boulaayoun/Desktop/Projecte - Mohamed/Fase1 - Scripting CSV_JSON/Prova Fitxers Excels/"+nom_fitxer
    #print(ruta)
    row = pd.read_excel(ruta, sheet_name='d13f7961-ff45-41d3-b295-ad7f7c1', names =['datahora','Consumido directamente','Consumo','Energía obtenida de la red'])
    #print(nom_fitxer_clean)
    dia2 = str(str(nom_fitxer_clean.year)+"-"+str(nom_fitxer_clean.month)+"-"+str(nom_fitxer_clean.day))

    s = mycol.find_one( {'_id': dia2})
    print(s)
    if s == "":
      salida = "Afegint el document del dia: "+dia2
      print(salida)
    else:
      print("Borrando el fichero: {0}".format(dia2))
      mycol.delete_one({'_id': dia2})

    #print(nom_fitxer_clean.year)
    d = Dia(dia2,[]);

    for i in row.index[1:]:
         # Dia Hora
         dia = row['datahora'][i]
         
     
         ### CONSUMO ###
         #Obtener el campo consumo directo.
         consum_directe = row['Consumido directamente'][i]

         consum = row['Consumo'][i]


         #Obtener la energia de xarxa.
         energia_xarxa = row['Energía obtenida de la red'][i]

         #Generación del nuevo formato de la fecha i hora
         data_hora = dia
         
         #Creo el objeto Consum con los campos del CSV.
         c = Consum(data_hora,consum_directe,consum,energia_xarxa)

         
         #Añadir el object C a una array consum de la Classe Dia:
         d.consum.append(c.__dict__) 
         
         #PASSAR EL C.___DICT___
        #Hago el INSERT al mongo con
    mycol.insert_one(d.__dict__);

    #Escribir el LOG
    s = nom_fitxer+" "+"OK"
    logging.info(s)

    #Mover el file a la carpeta OK.
    shutil.move(ruta, "./OK")
    

  except:
    s2 = nom_fitxer+" "+str(sys.exc_info()[1])
    logging.warning(s2)

    #Mover el file a la carpeta KO.
    shutil.move(ruta, "./KO")

print("Final de l'execució")
##
##
##fileList = os.listdir("./OK")
##for fileName in fileList:
##  if fileName != "":
##    os.remove("./OK"+"/"+fileName)
##
##fileList = os.listdir("./KO")
##for fileName in fileList:
##  if fileName != "":
##    os.remove("./KO"+"/"+fileName)


##    db.consum.deleteOne({'_id': ISODate("2018-11-08 00:00:00")})

##    #s = 'ISODate("{0}")'.format(nom_fitxer_clean)
##    #dt = ('({ " id " : ISODate("{0}")})').format(nom_fitxer_clean)
##    s = ObjectId("%s") % (nom_fitxer_clean)
##    #s = "ObjectId('{0}')".format(nom_fitxer_clean)
##    myquery = { "_id" : s }
##    print(s)
##    
##    
##    print(myquery)
##
##    mycol.delete_one(myquery)
    
    #5print(s)
    #x = ISODate("2018-11-07 00:00:00")
##    mongo.mycol.delete_one(myquery)(
    #mycol.delete_one(dt)
    
