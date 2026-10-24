from src.services.pessoa_service import PessoaService
from src.services.arquivo_pessoa_service import ArquivoPessoaService


def main():
    pessoa_service = PessoaService()
    arquivo_service = ArquivoPessoaService()

    pessoa = pessoa_service.criar_pessoa()

    print(pessoa.apresentar())

    arquivo_service.salvar_pessoa(pessoa)


if __name__ == "__main__":
    main()