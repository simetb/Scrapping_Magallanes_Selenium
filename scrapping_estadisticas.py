#Sistema Web Scrapping Selenium
#Librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Funcion que ingresa a la pagina de lanzadores
def SeleccionaPicheo():
    while True:
        try:
            driver.find_element(By.XPATH,"//a[@href='#pit']").click()
            time.sleep(1)
            break
        except:
            print("Error")

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
            print("Error")

#Funcion que Le Asigna un indice segun el nombre del equipo
def EscogeEquipo(_nombre):
    indiceEquipo = {"aguilas" : 0, "bravos" : 1, "cardenales" : 2, "caribes" : 3, "leones" : 4, "navegantes" : 5,
    "tiburones" : 6, "tigres" : 7}
    return(indiceEquipo[_nombre])

#Funcion que Extrea el nombre,apellido de los datos del usuario
def ExtraeNombreApellido(_datos):
    if _datos[0] == "#" or _datos[0] == "*": #En caso de que tenga # o * en la cadena
        nombre = _datos[1]
        apellido = ""
        for k in range(2,len(_datos)):
            apellido += _datos[k] + " "
    else:
        nombre = _datos[0]
        apellido = ""
        for k in range(1,len(_datos)):
            apellido += _datos[k] + " "
    return(nombre,apellido)

#---------------------------------------------------Configuraciones Selenium
PATH = Service("D:\Simet\Documents\chromedriver.exe") #Ruta del driver de GoogleChrome
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#Desactivas los switches innecesarios
driver = webdriver.Chrome(service = PATH,options=options) #Objeto con la direccion del driver (NO TOCAR)
url = "https://www.lvbp.com/" #URL Objetivo

#De Indice a Equipo
equipo = {0:"aguilas", 1:"bravos", 2:"cardenales",3:"caribes",4:"leones",5:"navegantes",6:"tiburones",7:"tigres"}

#Nombre de los equipos a evaluar
#aguilas bravos cardenales caribes leones navegantes tiburones tigres
#1-visitante 2-home
nombreEquipos = ["leones","navegantes"]

#Bateador Visitante y Lanzador Visitante
equipoBateadoresVisitante = []
equipoLanzadoresVisitante = []

#Bateador Home y Lanzador Home
equipoBateadoresHome = []
equipoLanzadoresHome = []



driver.get(url) #Entra a la URL Objetivo

#----------------------------------------Logica de Recolecta de datos 
#BATEADORES
print("BATEADORES")
nciclo = 0
for nombre in nombreEquipos:
    nciclo +=1
    indiceEquipo = EscogeEquipo(nombre) #Obtenemos el indice del equipo
    print(equipo[indiceEquipo],end = " ")
    EstadisticaEquipo(indiceEquipo) #Entremos a la estadisticas del equipo
    nbateadores = len(driver.find_elements(By.XPATH,"//div[@id = 'bat']/table/tbody/tr")) - 1 #Obtenemos la cantidad de elementos a evaluar
    
    #Recolecta de datos de los bateadores
    for indiceBateador in range( 1 ,nbateadores):      

        while True:
            try:
                #NOMBRE y APELLIDO
                jugador = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[1]/a").text.split()
                nombre,apellido = ExtraeNombreApellido(jugador)

                #POSICION
                posicion = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[2]").text

                #CI
                ci = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[10]").text

                #HR
                hr = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[9]").text

                #PEB
                peb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[18]").text

                #H
                h = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[6]").text

                #BB
                bb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[12]").text

                #VB
                vb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[4]").text

                #GP
                gp = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[21]").text

                #2B
                dosb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[7]").text

                #3B
                tresb = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[8]").text

                #SF
                sf = driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[16]").text

                break
            except:
                #Si hay un error ingresar de nuevo a la estadistica y esperar 1 segundo
                print("ERROR")
                EstadisticaEquipo(indiceEquipo)
                time.sleep(1)
        
        #NUMERO
        while True:
            try:
                #Ingresamos al perfil del jugador y extraemos su numero
                driver.find_element(By.XPATH,"//div[@id = 'bat']/table/tbody/tr["+ str(indiceBateador) +"]/td[1]/a").click()
                datos = driver.find_element(By.XPATH,"//div[@class = 'container main-bottom']/div/div[2]/h1").text.split()
                numero = datos[-1][1:]

                #Si el numero es -, colocar 0
                if numero == "-":
                    numero = 0
                break
            except:
                print("ERROR")
                time.sleep(1) 
        
        #Almacenar los datos
        if nciclo == 1:#CASO VISITANTE
            equipoBateadoresVisitante.append([nombre,apellido,posicion,ci,hr,peb,h,bb,vb,gp,dosb,tresb,sf,numero])
        else:#CASO HOME
            equipoBateadoresHome.append([nombre,apellido,posicion,ci,hr,peb,h,bb,vb,gp,dosb,tresb,sf,numero])

        EstadisticaEquipo(indiceEquipo)
    print("LISTO")

#LANZADORES
print("LANZADORES")
nciclo = 0
for nombre in nombreEquipos:
    nciclo +=1
    indiceEquipo = EscogeEquipo(nombre) #Obtenemos el indice del equipo
    print(equipo[indiceEquipo],end = " ")
    EstadisticaEquipo(indiceEquipo)#Ingresamos a las estadisticas del equipo
    SeleccionaPicheo()#Seleccionamos la opcion de picheo
    nlanzadores = len(driver.find_elements(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr")) - 3 #Cantidad de lanzadores a evaluar
    for indiceLanzador in range(1,nlanzadores):
        while True:
            try:
                jugador = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[1]/a").text.split()
                #NOMBRE Y APELLIDO
                nombre,apellido = ExtraeNombreApellido(jugador)

                #POSICION
                posicion = "P"

                #GANADOS
                ganados = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[2]").text

                #PERDIDOS
                perdidos = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[3]").text

                #SALVADO
                salvados = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[8]").text

                #IP
                ip = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[9]").text

                #STRIKES
                k = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[17]").text

                #BB
                bb = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[14]").text

                #CL
                cl = driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[12]").text
                break
            except:
                #En caso de error re ingresar a las estadisticas y picheo y esperar un segundo
                print("ERROR")
                EstadisticaEquipo(indiceEquipo)
                SeleccionaPicheo()
                time.sleep(1)
            
        while True:
                #NUMERO
            try:
                #Ingresamos al perfil del jugador y obtenemos el numero
                driver.find_element(By.XPATH,"//div[@id = 'pit' ]/table/tbody/tr["+str(indiceLanzador)+"]/td[1]/a").click()
                datos = driver.find_element(By.XPATH,"//div[@class = 'container main-bottom']/div/div[2]/h1").text.split()
                numero = datos[-1][1:]
                if numero == "-":#Si el numero es - se colocara 0 por defecto
                    numero = 0
                break
            except:
                print("ERROR")
                time.sleep(1)

        #ALMACENAR DATOS
        if nciclo == 1:#CASO VISITANTE
            equipoLanzadoresVisitante.append([nombre,apellido,posicion,ganados,perdidos,salvados,ip,k,bb,cl,numero])
        else:#CASO HOME
            equipoBateadoresHome.append([nombre,apellido,posicion,ganados,perdidos,salvados,ip,k,bb,cl,numero])  
        
        EstadisticaEquipo(indiceEquipo)
        SeleccionaPicheo()
    print("LISTO")
driver.close()

print(equipoBateadoresHome)
print(equipoLanzadoresVisitante)
print(equipoLanzadoresHome)
print(equipoBateadoresVisitante)
####################################################
###############EXPLICACION MATRICES#################
####################################################

#MATRICES DE BATEADORES
#equipoBateadores[Jugador][Estadistica]
#equipoBateadores[N][0] = NOMBRE
#equipoBateadores[N][1] = APELLIDO
#equipoBateadores[N][2] = POSICION
#equipoBateadores[N][3] = CI
#equipoBateadores[N][4] = HR
#equipoBateadores[N][5] = PEB
#equipoBateadores[N][6] = H
#equipoBateadores[N][7] = BB
#equipoBateadores[N][8] = VB
#equipoBateadores[N][9] = GP
#equipoBateadores[N][10] = 2B
#equipoBateadores[N][11] = 3B
#equipoBateadores[N][12] = SF
#equipoBateadores[N][12] = NUMERO DEL JUGADOR

#MATRICES DE LANZADORES
#equipoLanzadores[Jugador][Estadistica]
#equipoLanzadores[N][0] = NOMBRE
#equipoLanzadores[N][1] = APELLIDO
#equipoLanzadores[N][2] = POSICION = 'P'
#equipoLanzadores[N][3] = JG
#equipoLanzadores[N][4] = JP
#equipoLanzadores[N][5] = JS
#equipoLanzadores[N][6] = IP
#equipoLanzadores[N][7] = STRIKES
#equipoLanzadores[N][8] = BB
#equipoLanzadores[N][9] = CL
#equipoLanzadores[N][7] = NUMERO DEL JUGADOR



