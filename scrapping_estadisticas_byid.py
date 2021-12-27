#Sistema Web Scrapping Selenium
#Librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import time
import requests

#Funcion que ingresa a la pagina de Estadisticas
def EstadisticaEquipo(_indice):
    while True:
        try:
            driver.find_element(By.XPATH,"//div[@id ='navbar']/ul/li[5]").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"//div[@id ='navbar']/ul/li[5]/ul/li[" + str( 12 + _indice) + "]").click()
            time.sleep(1)
            break
        except:
            print("Error-Estadisticas")
            time.sleep(1)

#Funcion para Recolectar los Id de todos los bateadores
def RecolectaIdBateadores(_nbateadores):
    while True:
        idBateadores = []
        try:
            for k in range(_nbateadores):
                #Arma id
                jugador = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(k + 1) +"]/td[1]/a")
                id = jugador.get_attribute('href')
                id = [int(s) for s in re.findall(r'-?\d+\.?\d*', id)]
                idBateadores.append(id[0])
            return idBateadores
        except:
            print("Error-Bateadores")
            time.sleep(1)

#Funcion para Recolectar los Id de todos los Lanzadores
def RecolectaIdLanzadores(_nbateadores):
    while True:
        try:
            idLanzadores = []
            for k in range(_nbateadores):
                #Arma id
                jugador = driver.find_element(By.XPATH,"//div[@id = 'pit']/table/tbody/tr["+ str(k + 1) +"]/td[1]/a")
                id = jugador.get_attribute('href')
                id = (([int(s) for s in re.findall(r'-?\d+\.?\d*', id)]))
                idLanzadores.append(id[0])
            return idLanzadores
        except:
            print("Error-Lanzadores")
            time.sleep(1)

#Funcion que compara los Id
def ComparaId(_id,_id2):
    if _id == _id2:
        return True
    else:
        return False

#Funcion que recolecta los datos del bateador
def DatosBateador(_indice):
    while True:
        try:
            #POSICION
            posicion = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[2]").text
            #CI
            ci = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[10]").text
            #HR
            hr = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[9]").text
            #PEB
            peb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[18]").text
            #H
            h = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[6]").text
            #BB
            bb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[12]").text
            #VB
            vb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[4]").text
            #GP
            gp = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[21]").text
            #2B
            dosb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[7]").text
            #3B
            tresb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[8]").text
            #SF
            sf = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[16]").text
            #AVERAGE
            ave = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[17]").text[1:]
            #SLUGGING
            slg = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(_indice + 1) +"]/td[19]").text[1:]
            return(posicion,ci,hr,peb,h,bb,vb,gp,dosb,tresb,sf,ave,slg)
        except:
            print("Error-Datos Bateador")
            time.sleep(1)

#Funcion que recolecta los datos del Lanzador
def DatosLanzador(_indice):
    while True:
        try:
            #POSICION
            posicion = "P"
            #GANADOS
            ganados = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[2]").text
            #PERDIDOS
            perdidos = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[3]").text
            #SALVADO
            salvados = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[8]").text
            #IP
            ip = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[9]").text
            #STRIKES
            k = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[17]").text
            #BB
            bb = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[14]").text
            #CL
            cl = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[12]").text
            #EFE
            efe = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(_indice + 1)+"]/td[4]").text
            return(posicion,ganados,perdidos,salvados,ip,k,bb,cl,efe)
        except:
            print("Error-Datos Lanzador")
            time.sleep(1)

#Funcion para seleccionar picheo en el menu
def SeleccionaPicheo():
    while True:
        try:
            driver.find_element(By.XPATH,"//a[@href='#pit']").click()
            time.sleep(1)
            break
        except:
            print("Error")

#Funcion para seleccionar bateo en el menu
def SeleccionaBateo():
    while True:
        try:
            driver.find_element(By.XPATH,"//a[@href='#bat']").click()
            time.sleep(1)
            break
        except:
            print("Error")

#Funcion para Vaciar los elementos encontrados del vector
def Vaciado(m):
    cont = 0
    for k in range(len(m)):
        z = m[k-cont]
        if z == -1:
            m.pop(k-cont)
            cont +=1
    return m

#Funcion que da click en las estadisticas de la temporada
def Fase_Temporada(_fase):
    if _fase == "final":
        driver.find_element(By.XPATH,"//a[@href = '#w']").click()
    elif _fase == "semifinal":
        driver.find_element(By.XPATH,"//a[@href = '#l']").click()
    else:
        driver.find_element(By.XPATH,"//a[@href = '#tr']").click()
    

#---------------------------------------------------Configuraciones Selenium
PATH = Service("C:\chromedriver.exe") #Ruta del driver de GoogleChrome
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#Desactivas los switches innecesarios
driver = webdriver.Chrome(service = PATH,options=options) #Objeto con la direccion del driver (NO TOCAR)
url = "https://www.lvbp.com/" #URL Objetivo
urls = "http://192.168.4.100/pizarra/scrapping/estadisticas.php"
array = {'proceso':1}
response = requests.post(urls, data=array)

#----------------------------------------Logica de Recolecta de datos 
#Equipo a indice
equipo = {"aguilas":0, "bravos":1, "cardenales":2, "caribes":3, "leones":4, "navegantes":5,"tiburones":6,"tigres":7}
#Ids a buscar

results = response.text[:-1].split("-")#<----------------------------ID QUE SE VAN A BUSCAR
print(results)
ids = [int(x) for x in results]
driver.get(url) #Entra a la URL Objetivo
EstadisticaEquipo(equipo["navegantes"]) #Seleccionamos el equipo
Fase_Temporada("semifinal")# Seleccionamos el estado de la temporada final semifinal o regular
#Obtenemos los id para comparar
nbateadores = len(driver.find_elements(By.XPATH,"//div[@id = 'bat']/table/tbody/tr")) - 1 #Cantidad de bateadores a evaluar
idsBateadores  = RecolectaIdBateadores(nbateadores)
copiaBateadores = RecolectaIdBateadores(nbateadores)
SeleccionaPicheo()
nlanzadores = len(driver.find_elements(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr")) - 3 #Cantidad de lanzadores a evaluar
idsLanzadores  = RecolectaIdLanzadores(nlanzadores)
copiaLanzadores = RecolectaIdLanzadores(nlanzadores)  

##########################PROCESO###############################
for k in range(len(ids)):
    SeleccionaBateo()
    encontrado = False
    for j in range(nbateadores):
        if ids[k] != -1:
            encontrado = ComparaId(ids[k],idsBateadores[j])
            if encontrado:
                posicion,ci,hr,peb,h,bb,vb,gp,dosb,tresb,sf,ave,slg = DatosBateador(j)#<----------------------RESULTADOS SI ES BATEADOR
                estadisticas = {'proceso':2, 'posicion':posicion,'ci': ci, 'hr': hr, 'peb': peb, 'h': h, 'bb': bb, 'vb': vb, 'gp': gp, 'dosb': dosb, 'tresb': tresb, 'sf': sf,'ave' : ave,'slg' : slg,'id':ids[k]}
                ids[k] = -1
                idsBateadores[j] = -1
                response = requests.post(urls, data=estadisticas)
                break

    if not(encontrado):
        SeleccionaPicheo()
        for j in range(nlanzadores):
            if ids[k] != -1:
                encontrado = ComparaId(ids[k],idsLanzadores[j])
                if encontrado:
                    posicion,ganados,perdidos,salvados,ip,strikes,bb,cl,efe = DatosLanzador(j)#<----------------------RESULTADO SI ES PITCHER
                    estadisticas = {'proceso':2, 'posicion':posicion,'ganados': ganados, 'perdidos': perdidos, 'salvados': salvados, 'ip': ip, 'strikes': strikes, 'bb': bb, 'cl': cl, 'efe': efe,'id':ids[k]}
                    ids[k] = -1
                    idsLanzadores[j] = -1
                    break

#VACIAR ELEMENTOS ENCONTRADOS
ids = Vaciado(ids)
idsBateadores = Vaciado(idsBateadores)
idsLanzadores = Vaciado(idsLanzadores)

#ELEMENTOS SOBRANDES DEL SISTEMA
if len(ids) != 0:
    print("Algunos ids no fueron encontrados en el sistema...")
    print(ids)

#ELEMENTOS SOBRANTES DE BATEADORES
if len(idsBateadores) != 0:
    SeleccionaBateo()
    print("\nAlgunos ids no fueron buscados en la liga BATEADORES ...")
    for k in range(len(idsBateadores)):
        encontrado = False
        for j in range(nbateadores):
            encontrado = ComparaId(idsBateadores[k], copiaBateadores[j])
            if encontrado:
                jugador = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(j+1) +"]/td[1]/a").text
                print("ID: ",idsBateadores[k]," - ", jugador)
                break

#ELEMENTOS SOBRANTES LANZADORES
if len(idsLanzadores) != 0:
    SeleccionaPicheo()
    print("\nAlgunos ids no fueron buscados en la liga LANZADORES...")
    for k in range(len(idsLanzadores)):
        encontrado = False
        for j in range(nlanzadores):
            encontrado = ComparaId(idsLanzadores[k], copiaLanzadores[j])
            if encontrado:
                jugador = driver.find_element(By.XPATH,"//div[@id = 'pit']/table/tbody/tr["+ str(j+1) +"]/td[1]/a").text
                print("ID: ",idsLanzadores[k]," - ", jugador)
                break

#Cerramos la pagina
driver.quit()
