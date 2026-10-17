class Pessoa:  # Cria o molde
    def __init__(self, altura, peso, nome): #construimos com as propriedades
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def andar(self): #crianmos um comportamentos
        print(f"{self.nome}Você andou dois passos") #acessamos um propridades 

comida =Pessoa(1.78, 80, "matheus")
pessoa1 = Pessoa ()

dicionario = [
    {    
    "nome": comida.nome,
    "paso_pessoa": comida.peso,
    "altura_pessoa": comida.altura
},
{
    "nome": pessoa1.nome,
    "paso_pessoa": pessoa1.peso,
    "altura_pessoa": pessoa1.altura
}
]

for i in range(len(dicionario)):
    print("O nome é:")
    print(dicionario[i]["nome_pessoa"])

    print("O peso é:")
    print(dicionario[i]["peso_pessoa"])

    print("A altura é:")
    print(dicionario[i]["altura_pessoa"])