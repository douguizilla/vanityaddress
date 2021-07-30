#Aluno: Douglas Gomes de Paula - 11621BCC013
import hashlib
from random import *
# foi necessário usar o comando "pip install base58" antes de fazer o import abaixo
import base58
   
def isVanity(hash, nick):
    #transformo em listas para poder iterar e comparar a semelhança
    hash_ = str(hash)

    tam = list(range(0, len(nick)))
    ok = 0
    for i in tam:
        #somo 3 devido o prefixo do valor vindo da base58 da hash é sempre b'3, sendo somente a partir do indice 3 os valores que me interessa
        if(hash_[i+3] == nick[i].lower() or hash_[i+3] == nick[i].upper()):
            print(hash)
            ok += 1
            #print("Ok count " + str(ok))
            if(ok == len(nick)): 
                return 1
        else: 
            break
    
    return -1

def getVanity(nickname):

    #sorteio um numero
    num = 1

    while True:

        #converto para string
        numberString = str(num)
        num += 1

        #crio uma hash para esse numero, essa hash será meu endereço
        hash = hashlib.sha224(numberString.encode()).hexdigest()

        #converto a hash para base58, por padrao sempre vem com b'
        b58 = base58.b58encode(hash)

        #teste de saída
        if(isVanity(b58, nickname) > 0): break

    return (b58, hash, numberString)

#buscando por um Vanity Address para "dgs" que é DouGlaS, que é pegando uma letra e pulando duas.
#resolvi fazer isso pois deixei o codigo rodando mais de 3h e nao conseguiu chegar em 'doug'

(vanityAddress, publickey, privatekey) = getVanity("dgs")
print((vanityAddress, publickey, privatekey))

#resultou em:
#(b'3dgSStwz3ozeF9eZ1YYBEYbyNw4wfDacp3P3tGZLA5kyGrRf3oy6CjQNnW1z5Yd3s94re3rSaxG3R', 'a4067cf5e783771c4a958ecc76f0a6976bc666e899e4c8cb40c6f7b0', '112')

#buscando para "Xaiane"
(vanityAddress1, publickey1, privatekey1) = getVanity("Xaia")
print((vanityAddress1, publickey1, privatekey1))

#resultou em:
#(b'2XaiaN5Mi9tYyru6Y8f3dBSbfMZEFStgFV64gSkMucoVLrxrKtXpZLxMphdtkGYQqT8RiNHtNvf4x', '8e81c4c92fb4e6f999ae34640cc19839f7fdba33ee6ee1a5e58fdee5', '282637')

#buscando para "Jipe"
(vanityAddress1, publickey1, privatekey1) = getVanity("Jipe")
print((vanityAddress1, publickey1, privatekey1))

#resultou em:
#(b'2Jipecp1pfjWFWFY3bYiHGfnf9vZz7mZNsaJDXyLGoKn4WXXwfLY7VVmyzWgfLWRE7TaY2imWcfwV', '0587305bde7aa9f16b4967fd8cf219cd46b8fa6f82a5105012206218', '6834')


#para achar a chave publica a partir do vanityAddress basta usar 'base58.decode(publickey)'
#coloquei a privatekey também pois nao vi problema, por ser apenas para fins didáticos