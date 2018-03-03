def clasificacion(dict):
	clas=[]
	for i in dict.get("table"):
		clas.append([i.get("team"), i.get("points")])
	return clas

