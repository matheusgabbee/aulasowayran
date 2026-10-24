from src.models.arquivo_pessoa import ArquivoPessoa
from src.models.erros_arquivo_pessoa import ErroArquivoPessoa


class ArquivoPessoaService:
    def salvar_pessoa(self, pessoa):
        arquivo_pessoa = ArquivoPessoa(pessoa)

        try:
            caminho = arquivo_pessoa.salvar()
            print(f"Arquivo salvo com sucesso: {caminho}")

        except ErroArquivoPessoa as erro:
            print(f"Erro ao salvar os dados: {erro}")