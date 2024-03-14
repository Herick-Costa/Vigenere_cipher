print("\n\nCriptografia da Cifra de Vigenère\n")

mensagemB = input("\nDigite sua mensagem: ")
mensagem = mensagemB.replace(" ", "").lower()

chaveB = input("\n\nInsira a chave: ")
chaveB = chaveB.replace(" ", "").lower()

# Calcula quantas vezes a chave precisa ser repetida para igualar o comprimento da mensagem
repetitions = len(mensagem) // len(chaveB) + 1
chave = (chaveB * repetitions)[:len(mensagem)]

# Converte para numero e coloca em lista a mensagem
listaM = []
for h in mensagem:
    listaM.append(ord(h) - 97)

# Converte para numero e coloca em lista a chave
listaC = []
for c in chave:
    listaC.append(ord(c) - 97)
    
# Calcula o tamanho da lista de chaves
tam_chave = len(listaC)
cifra = []

# Aplica a fórmula para cada par de elementos da listaM e listaC
for i in range(len(listaM)):
    # Calcula a cifra usando a fórmula (M + K) mod 26
    cifra.append((listaM[i] + listaC[i % tam_chave]) % 26)

#print("\nCifra:", cifra)

# Inicializa uma string vazia para armazenar a mensagem decifrada
mensagem_decifrada = ""

# Converte os números da cifra de volta para letras do alfabeto
for numero in cifra:
    # Adiciona 97 ao número e converte para caractere ASCII
    letra = chr(numero + 97)
    # Adiciona a letra decifrada à mensagem
    mensagem_decifrada += letra

print("\nMensagem criptografada:\n\n", mensagem_decifrada + "\n\n")
