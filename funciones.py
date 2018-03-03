def clasificacion(dict):
	clas=[]
	for i in dict.get("table"):
		clas.append([i.get("pos"), i.get("team"), i.get("points")])
	return clas

def equiposgolesfavor(dict):
	equipos=[]
	for i in dict.get("table"):
		if i.get("gf")>i.get("ga"):
			equipos.append([i.get("team"), i.get("gf"), i.get("ga")])
	return equipos

def rangopuntos(dict, puntosmin, puntosmay):
	rango=[]
	for i in dict.get("table"):
		if i.get("points")>=puntosmin and i.get("points")<=puntosmay:
			rango.append([i.get("pos"), i.get("team"), i.get("points")])
	return rango

def competicion(dict, cat):
	comp=[]
	for i in dict.get("table"):
		if cat=="Champions League" and i.get("mark")==1:
			comp.append([i.get("pos"), i.get("team"), i.get("points")])
		elif cat=="Europa League" and i.get("mark")==2:
			comp.append([i.get("pos"), i.get("team"), i.get("points")])
		elif cat=="Descenso" and i.get("mark")==3:
			comp.append([i.get("pos"), i.get("team"), i.get("points")])
	return comp

def pelea(dict, comp):
	pelea=[]
	for i in dict.get("table"):
		if comp=="1" and int(i.get("pos"))<8:
			pelea.append([i.get("pos"), i.get("team"), i.get("points")])
		elif comp=="2" and int(i.get("pos"))>4 and int(i.get("pos"))<11:
			pelea.append([i.get("pos"), i.get("team"), i.get("points")])
		elif comp=="3" and int(i.get("pos"))>14:
			pelea.append([i.get("pos"), i.get("team"), i.get("points")])
	return pelea

