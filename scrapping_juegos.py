#Sistema Web Scrapping con Selenium
#Librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

#Funcion para Extaccion de los equipos
def Equipos(_indice):
    #Diccionario de equipos
    equipos = {'ARA':'TIGRES','ANZ':'CARIBES','CAR':'LEONES','LAG':'TIBURONES','ZUL':'AGUILAS','MAR':'BRAVOS',
    'LAR':'CARDENALES','MAG':'NAVEGANTES'}
    #Equipo Visitante
    equipoVisitante = driver.find_element(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div[" + str(_indice)+"]"+
    "/table/tbody/tr[1]/td[1]/strong").text
    #Equipo HomeClub
    equipoHome = driver.find_element(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div[" + str(_indice)+"]"+
    "/table/tbody/tr[2]/td[1]/strong").text
    equipoVisitante = equipos[equipoVisitante]
    equipoHome = equipos[equipoHome]
    return(equipoVisitante,equipoHome)

#Funcion del estado del partido
def Estado(_indice):
    #Item Estado del partido
    estadoPartido = driver.find_element(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div[" + str(_indice)+"]"+
    "/table/tbody/tr[3]/td").text
    estadoPartido = estadoPartido.lower()
    # F = Partido finalizado, D = Partido Demorado, Numero = Inning de juego, X = Otro
    # Estado inning -1 = Juego pausado o terminado, Estado inning 0 = Superior p 1 =Inferior
    if estadoPartido == "finalizado":
        inning = "F"
        estadoInning = -1
    else:
        estadoPartido = estadoPartido.split(' ')
        for palabra in estadoPartido:
            if palabra == "demorado":
                inning = "D"
                estadoInning = -1
                break
            elif palabra == "inning":
                if estadoPartido[2] == "▼":
                    inning = estadoPartido[1] 
                    estadoInning = "baja"
                else:
                    inning = estadoPartido[1] 
                    estadoInning = "alta"
                break
        else:
            inning = "X"
            estadoInning = -1
    return(inning,estadoInning)

#Funcion de cantidad de partidos del dia
def CantidadPartidos():
    #Cantidad de partidos
    n_partidos = len(driver.find_elements(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div"))
    return n_partidos

#Funcion para la cantidad de carreras del partido
def Carreras(_indice):
    #Carreras Visitante
    carrerasHome = driver.find_element(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div[" + str(_indice)+"]"+
    "/table/tbody/tr[1]/td[2]").text
    #Carreras HomeClub
    carrerasVisitante = driver.find_element(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div[" + str(_indice)+"]"+
    "/table/tbody/tr[2]/td[2]").text
    return(carrerasHome,carrerasVisitante)

#Funcion para saber los jugadores numero del partido
def JugadoresNumero():
    #Jugador Visitante
    jugadorPitcher = driver.find_element(By.XPATH,"//div[@class = 'col-md-3 pbp-left-box m-b-md']/div[3]/div[2]/div/"+
    "small").text
    #Jugador HomeClub
    jugadorBateador = driver.find_element(By.XPATH,"//div[@class = 'col-md-3 pbp-left-box m-b-md']/div[4]/div[2]/div/"+
    "small").text
    #Extrayendo el numero del jugador Visitante
    jugadorPitcher = jugadorPitcher.split()
    jugadorPitcher = jugadorPitcher[1][1:] #Ejemplo #22 = 22
    #Extrayendo el numero del jugador HomeClub
    jugadorBateador = jugadorBateador.split()
    jugadorBateador = jugadorBateador[1][1:]
    return(jugadorPitcher,jugadorBateador)

#Funcion para saber los jugadores nombres del partido
def JugadoresNombre():
    #Jugador Visitante Nombre
    jugadorPitcher = driver.find_element(By.XPATH,"//div[@class = 'col-md-3 pbp-left-box m-b-md']/div[3]/div[2]/div/"+
    "strong").text
    #Jugador HomeClub Nombre
    jugadorBateador = driver.find_element(By.XPATH,"//div[@class = 'col-md-3 pbp-left-box m-b-md']/div[4]/div[2]/div/"+
    "strong").text

    jugadorPitcher = "P: " + jugadorPitcher
    jugadorBateador = "B: " + jugadorBateador
    return(jugadorPitcher,jugadorBateador)
    
#Funcion para saber la cantidad de Outs por partido
def CantidadOuts():
    #Outs del inning
    outs = driver.find_element(By.XPATH,"//div[@class = 'col-md-3 pbp-left-box m-b-md']/div[2]/div[3]/small/strong").text
    return(outs)

#Funcion para saber si hay jugadores en Base 
def EnBase():
    #Jugadores en base? Si = 1, No = 0
    #PRIMERA BASE
    try:
        elementoBase = driver.find_element(By.XPATH,"//div[@class = 'stadium-r1B']")
        primeraBase = 1
    except:
        primeraBase = 0
    #SEGUNDA BASE
    try:
        elementoBase = driver.find_element(By.XPATH,"//div[@class = 'stadium-r2B']")
        segundaBase = 1
    except:
        segundaBase = 0
    #TERCERA BASE
    try:
        elementoBase = driver.find_element(By.XPATH,"//div[@class = 'stadium-r3B']")
        terceraBase = 1
    except:
        terceraBase = 0
    return(primeraBase,segundaBase,terceraBase)

#Funcion para Eliminar a Magallanes de los partidos
def EliminaMagallanes(_partidos):
    npartido = 0
    for partido in _partidos:
        if partido[1] == "MAGALLANES":
            _partidos.pop(npartido)
            break
        else:
            npartido +=1
    return(_partidos)
    
#-------------------------------------------------------Configuraciones Selenium
PATH = Service("C:\chromedriver.exe") #Ruta del driver de GoogleChrome
driver = webdriver.Chrome(service = PATH) #Objeto con la direccion del driver (NO TOCAR)
url = "https://www.lvbp.com/" #URL Objetivo
driver.get(url) #Entrar a la URL objetivo

#-------------------------------------------------------Logica de recolecta de datos
partidos = []
for numeroPartido in range(1,CantidadPartidos()+1):
    inning,situacion = Estado(numeroPartido)
    if  situacion == -1:#Caso juego Finalizado, No Iniciado, Demorado
        #Inicializacion de las variables
        EquipoVisitante,EquipoHome = Equipos(numeroPartido)
        CarrerasVisitante,CarrerasHome = Carreras(numeroPartido)
        JugadorVisitante = JugadorHome = ""
        Outs = 0
        PrimeraBase = SegundaBase = TerceraBase = 0
        
        #Creacion y almacenamiento del Partido
        partido = [EquipoVisitante,EquipoHome,JugadorVisitante,JugadorHome,CarrerasVisitante,CarrerasHome,Outs,
        PrimeraBase,SegundaBase,TerceraBase,inning,situacion]
        partidos.append(partido)
    
    else:#Caso Juego Iniciado
        #Inicializacion de las variables
        EquipoVisitante,EquipoHome = Equipos(numeroPartido)
        CarrerasVisitante,CarrerasHome = Carreras(numeroPartido)

        #SubPaginaObjetivo 
        PaginaPartido = driver.find_element(By.XPATH, "//div[@id='h_scoreboard']/div[@class='row m-t-sm']/div[" 
        + str(numeroPartido)+"]")
        PaginaPartido.click()#Entrada a SubPagina

        #Inicializacion de variables de subpagina y condicional de jugadores
        if situacion == "baja":
            JugadorVisitante,JugadorHome = JugadoresNombre()
        else:
            JugadorHome,JugadorVisitante = JugadoresNombre()
        Outs = CantidadOuts()
        PrimeraBase,SegundaBase,TerceraBase = EnBase()

        #Creacion y Almacenamiento del partido
        partido = [EquipoVisitante,EquipoHome,JugadorVisitante,JugadorHome,CarrerasVisitante,CarrerasHome,Outs,
        PrimeraBase,SegundaBase,TerceraBase,inning,situacion]
        partidos.append(partido)

    urls = "http://192.168.4.100/pizarra/scrapping/partidos.php"

    ##############QUERY ARRAY ENVIADO POR POST########################
    JugadorHome = ""
    JugadorVisitante = ""
    infopartido = {'indice':numeroPartido,'EquipoVisitante': EquipoVisitante, 'EquipoHome': EquipoHome, 'JugadorVisitante': JugadorVisitante, 'JugadorHome': JugadorHome, 
    'CarrerasVisitante': CarrerasVisitante, 'CarrerasHome': CarrerasHome, 'Outs': Outs, 'PrimeraBase': PrimeraBase, 'SegundaBase': SegundaBase, 
    'TerceraBase': TerceraBase, 'inning': inning, 'situacion': situacion}
    
    response = requests.post(urls, data=infopartido)

    query = str(response.text) + "/n"
    #################################################################
    
#Eliminamos a magallanes de la lista
EliminaMagallanes(partidos)
driver.quit()#Cerrar la pagina
