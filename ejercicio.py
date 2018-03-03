from funciones import clasificacion, equiposgolesfavor, rangopuntos, competicion
import urllib.request, json 

with urllib.request.urlopen("http://apiclient.resultados-futbol.com/scripts/api/api.php?key=7171673be04cc06aa2426307d8b42836&tz=Europe/Madrid&format=json&req=tables&league=1&group=1") as url:
	datos=json.loads(url.read().decode())

for i in clasificacion(datos):
	print(i[0], i[1])

for n in equiposgolesfavor(datos):
	print(n[0], "GF:", n[1], "GC:", n[2])

puntosmin=input("Dime los puntos minimos: ")
puntosmax=input("Dime los puntos maximos: ")
for r in rangopuntos(datos, puntosmin, puntosmax):
	print(r[0], r[1], r[2])

compe=input("Dime alguna de estas opciones (Champions League / Europa League / Descenso): ")
for c in competicion(datos, compe):
	print(c[0], c[1], c[2])
