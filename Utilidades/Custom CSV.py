# Abril 4, 10:13 a.m.
# Módulo a ser usado en el proyecto porque al ver la sintáxis del módulo csv de Python me dió pereza aprenderlo

# Empezando a trabajar a las 8:55 p.m.

def load(file):
	with open(file, "r") as file_:
		content = []
		for data in file_:
			data = data.split(",")
			content.append({"item":data[0], "cost":data[1], "date":data[2]})
		return content

print(load("xd.ldf"))

# Abril 4, 9:05 p.m.
