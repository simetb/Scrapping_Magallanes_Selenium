import requests

urls = "http://localhost/pizarra/scrapping/partidos.php"

infopartido = {'indice':5, 'EquipoVisitante': 'TIBURONES', 'EquipoHome': 'CARIBES', 'JugadorVisitante': 25, 'JugadorHome': 42, 
'CarrerasVisitante': 2, 'CarrerasHome': 3, 'Outs': 1, 'PrimeraBase': 0, 'SegundaBase': 1, 'TerceraBase': 0, 'inning': 4, 'situacion': 2}

response = requests.post(urls, data=infopartido)
print(response.text)