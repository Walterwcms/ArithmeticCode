
#***************
#****************
#----------- em implementacao . . . .
#***************
#**************




alfabeto = "abcdefghijklmnopqrstuvwxyz"
sequencia_a_codificar = "wa lt er ca rl os mo ra is do ss an to s"
listAlfabetoNumber = []
listAlfabetoBIM =[]
cont =0

for caracter in alfabeto:
    listAlfabetoNumber.append(caracter +" "+str(cont) )
    listAlfabetoBIM.append(caracter + " "+ str(bin(cont))[2:])
    cont = cont + 1

grupo2Letra = sequencia_a_codificar.split(" ")

listaNumero = []
for letra in grupo2Letra:
    for number in listAlfabetoNumber:
        caract,numero = number.split(" ")
        if(letra[0] == caract):
            listaNumero.append(str(numero))

dividir = sequencia_a_codificar.split(" ")
cont = 0


def retornabin(letra):
    cont  = 0
    for i in listAlfabetoNumber:
        l = i.split(" ")
        if(letra == l[0]):
            return listAlfabetoBIM[cont][2:]
        cont = cont+1
    return None



for letra in dividir:
    f = int(listaNumero[cont])
    #print(str(bin(f)[2:]) + str(retornabin(letra[-1])))
    cont = cont +1

print(str(bin(10)))


#  wait for updates . . .



