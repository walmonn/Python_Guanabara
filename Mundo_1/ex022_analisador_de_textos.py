nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em MAIUSCULAS é {}".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras".format(len(nome) - nome.count(" "))) 
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print("Seu Primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))