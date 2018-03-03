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
