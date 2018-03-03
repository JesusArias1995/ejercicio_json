from funciones import clasificacion, equiposgolesfavor, rangopuntos, competicion, pelea
import urllib.request, json 

with urllib.request.urlopen("http://apiclient.resultados-futbol.com/scripts/api/api.php?key=7171673be04cc06aa2426307d8b42836&tz=Europe/Madrid&format=json&req=tables&league=1&group=1") as url:
	datos=json.loads(url.read().decode())

print("Elige una opción: ")
print("1. Clasificacion de la liga")
print("2. Equipos con más goles a favor que en contra.")
print("3. Consulta de clasificacion en un rango de puntos.")
print("4. Equipos en Champions, Europa League o Descenso.")
print("5. Pelea en la clasificacion por puestos.")
print("0. Salir")
print("")
menu=input("Introduce el número de opcion que desea realizar: ")

while menu!="0":
	if menu=="1": 
		for i in clasificacion(datos):
			print(i[0], i[1])
		menu=input("Elige otra opcion: ")

	if menu=="2":
		for n in equiposgolesfavor(datos):
			print(n[0], "GF:", n[1], "GC:", n[2])
		menu=input("Elige otra opcion: ")

	if menu=="3":
		puntosmin=input("Dime los puntos minimos: ")
		puntosmax=input("Dime los puntos maximos: ")
		for r in rangopuntos(datos, puntosmin, puntosmax):
			print(r[0], r[1], r[2])
		menu=input("Elige otra opcion: ")

	if menu=="4":
		compe=input("Dime alguna de estas opciones (Champions League / Europa League / Descenso): ")
		for c in competicion(datos, compe):
			print(c[0], c[1], c[2])
		menu=input("Elige otra opcion: ")

	if menu=="5":
		print("1. Pelea por un puesto en Champions")
		print("2. Pelea por un puesto en Europa League")
		print("3. Pelea por la permanencia")
		print("0. Salir")

		menu=input("Introduce el numero de accion que desea realizar: ")
		while menu!="0":
			if menu=="1":
				for p in pelea(datos, menu):
					if int(p[0])<5:
						print(p[0], p[1], p[2], "*")
					if int(p[0])>4:
						print(p[0], p[1], p[2])

				menu=input("Introduce otra opcion:")

			if menu=="2":
				for p in pelea(datos, menu):
					if int(p[0])>4 and int(p[0])<7:
						print(p[0], p[1], p[2], "*")
					if int(p[0])>6:
						print(p[0], p[1], p[2])

				menu=input("Introduce otra opcion:")

			if menu=="3":
				for p in pelea(datos, menu):
					if int(p[0])>17:
						print(p[0], p[1], p[2], "*")
					if int(p[0])<18:
						print(p[0], p[1], p[2])

				menu=input("Introduce otra opcion:")
		menu=input("Elige otra opcion: ")
