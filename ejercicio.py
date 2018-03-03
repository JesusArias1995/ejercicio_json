from funciones import clasificacion
import urllib.request, json 

with urllib.request.urlopen("http://apiclient.resultados-futbol.com/scripts/api/api.php?key=7171673be04cc06aa2426307d8b42836&tz=Europe/Madrid&format=json&req=tables&league=1&group=1") as url:
	datos=json.loads(url.read().decode())

for i in clasificacion(datos):
	print(i[0], i[1])