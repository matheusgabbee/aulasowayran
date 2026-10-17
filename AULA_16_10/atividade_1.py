class Pessoa: # crio a classe pessoa
    def __init__(self, idade, nome): # recebo nome e idade
        self.idade = idade # guardo a idade
        self.nome = nome # guardo o nome
    def apresentar(self): # crio a apresentação
        return "Meu nome é {} e minha idade é {}.".format(self.nome, self.idade) # monto a frase com nome e idade
    
class ArquivoPessoa: # crio a classe para mexer no arquivo
    def __init__(self, nome_arquivo, tipo_arquivo=".txt"): # recebo o nome e o tipo do arquivo
        self.nome_arquivo = nome_arquivo # guardo o nome do arquivo
        self.tipo_arquivo = tipo_arquivo # guardo o tipo do arquivo
        
    def exibir(self): # mostro o conteúdo do arquivo
        with open(self.nome_arquivo + self.tipo_arquivo, "r", encoding="utf-8") as arquivo: # abro o arquivo para ler
            print(arquivo.read()) # leio e mostro o conteúdo
    def escrever(self, pessoa, mensagem): # escrevo os dados da pessoa

        with open(self.nome_arquivo + self.tipo_arquivo, "w", encoding="utf-8") as arquivo: # abro o arquivo para escrever
            arquivo.write(pessoa.apresentar() + "\n") # escrevo a apresentação
            arquivo.write(mensagem + "\n") # escrevo a mensagem

    def adicionar(self, pessoa, mensagem): # adiciono novos dados
        with open(self.nome_arquivo + self.tipo_arquivo, "a", encoding="utf-8") as arquivo: # abro o arquivo para adicionar
            arquivo.write(pessoa.apresentar() + "\n") # adiciono a apresentação
            arquivo.write(mensagem + "\n") # adiciono a mensagem

arquivo = ArquivoPessoa("pessoas") # crio o arquivo pessoas.txt
pessoa1 = Pessoa(33, "Ariana Grande") # crio a primeira diva
pessoa2 = Pessoa(36, "Taylor Swift") # crio a segunda diva
pessoa3 = Pessoa(42, "Beyoncé") # crio a terceira diva
pessoa4 = Pessoa(32, "Lady Gaga") # crio a quarta diva
pessoa5 = Pessoa(31, "Rihanna") # crio a quinta diva
pessoa6 = Pessoa(41, "Britney Spears") # crio a sexta diva
pessoa7 = Pessoa(30, "Dua Lipa") # crio a sétima diva
pessoa8 = Pessoa(40, "Katy Perry") # crio a oitava diva
pessoa9 = Pessoa(27, "Miley Cyrus") # crio a nona diva
pessoa10 = Pessoa(29, "Selena Gomez") # crio a décima diva

arquivo.escrever(pessoa1, "amooo cantar e entregar tudo nos meus shows, bee!")
arquivo.adicionar(pessoa2, "migaaa, amo compor músicas e criar hits!")
arquivo.adicionar(pessoa3, "sou uma diva do pop, aceita que dói menos!")
arquivo.adicionar(pessoa4, "amooo música e atuação, sou uma artista completa, mona!")
arquivo.adicionar(pessoa5, "minhas músicas são tudo, os fãs que lutem!")
arquivo.adicionar(pessoa6, "sou um ícone do pop, meu amor, uma lenda!")
arquivo.adicionar(pessoa7, "cantar e dançar? faço os dois, gataaa!")
arquivo.adicionar(pessoa8, "nasci pra brilhar no palco, bee!")
arquivo.adicionar(pessoa9, "amo explorar novos estilos, sou versátil, mona!")
arquivo.adicionar(pessoa10, "compartilho minha música porque o mundo merece esse talento!")
arquivo.exibir()