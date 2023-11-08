# Mayo 17, 2023. 7:33 p.m.

def validate(string):
	valid = "0123456789"
	expr = "[0-9]{2}/[0-9]{2}/[0-9]{4}"

	# Limpiar el string
	_ = ""
	for index, char in enumerate(string):
		if char == " ":
			string += "/"
		if char not in valid:
			continue
		_ += char
	string = _

	# Insertar slashes
	for index in 2, 5:
		if len(string) > index:
			string = string[:index] + "/" + string[index:]
			continue
		if len(string) == index - 1:
			string += "/"

	# Añadir ceros a la izquierda
	if len(string) > 1 and string[1] == "/":
		string = "0" + string
	if len(string) > 4 and string[4] == "/":
		string = string[0:3] + "0" + string[3:]

	# Validar la fecha
	if len(string) > 2 and not(0 < int(string[0:2]) <= 31):
		string = "01" + string[2:]
	if len(string) > 5 and not(0 < int(string[3:5]) <= 12):
		string = string[0:3] + "01" + string[5:]
	if len(string) > 10:
		string = string[0:10]

	return string

# Mayo 17, 2023. 8:05 p.m.