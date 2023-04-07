#***********************************
# Universidade Técnica do Atlâtico (UTA)
# Walter dos santos
# wsantos@uta.cv
#************************

#Em ArithmeticDevCode  tem as pricipais funcoes: encode e decode
import ArithmeticDevCode

'''''
TabelaFrequencia = {
    "a": 14.63,"e": 12.57,
    "o": 10.73,"s": 7.81,
    "r": 6.53,"i": 6.18,
    "n": 5.05,"d": 4.99,
    "m": 4.74,"u": 4.63,
    "t": 4.34,"c": 3.88,
    "l": 2.78,"p": 2.52,
    "v": 1.67,"g": 1.3,
    "h": 1.28,"q": 1.2,
    "b": 1.04,"f": 1.02,
    "z": 0.46,"j": 0.4,
    "x": 0.21,"k": 0.02,
    "w": 0.01,"y": 0.01,
    }
sequenciaCaracteres = "waltercarlosmorais"
'''
TabelaFrequencia = {
        "E":0.5, "I":0.25, "L":0.125, "T":0.125,
    }
sequenciaCaracteres = "LEIT"


# ArithmeticCoding retorna um objeto,em que tem a funcao: encode e decode
AE = ArithmeticDevCode.ArithmeticCoding(TabelaFrequencia)

print("Menssagem Original: "+ str(sequenciaCaracteres))
print("------------------ Tabela -----------------------------------------------------------")

#-------------------------CODIFICACAO-------------------------------------------------------------
encoder, mensagemCodificada = AE.encode(sequenciaCaracteres,AE.probability_table)
print("--------------------------------------------------------------------------------------")
print("Media da Menssagem Codificada: "+str(mensagemCodificada))
#-------------------------------------------------------------------------------------------------

#-------------------------DESCODIFICACAO----------------------------------------------------------
print("------------------------------descodificacao-----------------------------------------------")
decoder, decoded_msg = AE.decode(mensagemCodificada,len(sequenciaCaracteres),AE.probability_table)
print("--------------------------------------------------------------------------------------")
print("Menssagem descodificada: "+str(decoded_msg))
#--------------------------------------------------------------------------------------------------


# retorna true se a sequenciaCaracteres inicial corresponde ao descodificado
print("Menssagem foi bem descodificada? "+str(sequenciaCaracteres == decoded_msg))


