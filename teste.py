def ler_arquivo_texto(nome):
    nome_arquivo = nome+".txt"
    resultado = {}
    with open(nome_arquivo, 'r') as arquivo:
        for line in arquivo:
            resultado[line.split(':')[0].strip()]= line.split(':').pop().strip()
    return resultado


def ler_arquivo_chave(nome):
    nome_arquivo = nome+".txt"
    resultado = []
    with open(nome_arquivo, 'r') as arquivo:
        for line in arquivo:
            resultado.append(line.strip())
    # ordenar palavras chave
    resultado.sort()
    return resultado


def criar_indice(texto, palavrasChave):
    result = {}
    '''
    Recebemos a lista de palavras chave já ordenada. Basta agora verificar para cada linha do texto
    se a palavra existe e adicionala ao dicionario. Cada palavra chave já é adicionada em ordem alphabetica.
    '''
    for palavra_chave in palavrasChave:
        for linha in texto:
            numero_linha_atual = linha.split().pop()
            if palavra_chave in texto[linha]:
                result.setdefault(palavra_chave, []).append(numero_linha_atual)
    print(result)
    print("## Indice criado.  ##")
    return result


def listar(meuIndice):
    for item in meuIndice.items():
        print(item[0], end='')
        for valores in item[1]:
            print(" {0}".format(valores), end='')
        print("")


def pesquisa(chave, indice_pesquisa):
    if chave in indice_pesquisa:
        print(chave, end='')
        for valores in indice_pesquisa[chave]:
            print(" {0}".format(valores), end='')
        print("")
    else:
        print("A chave {0} nao existe no indice.".format(chave))


def main():
    meu_indice = {}
    while(True):
        try:
            print("## Selecione uma opcao ## \n Este programa requer que os arquivos chaves.txt"
                  " e texto.txt estejam na mesma pata do script python. ")
            print("1- Listagem\n2-Criacao de indice\n3-Pesquisa\n4-Sair")
            num = int(input("Digite o exercicio desejado:  "))
            if num == 1:
                if not meu_indice:
                    meu_indice=criar_indice(ler_arquivo_texto("texto"), ler_arquivo_chave("chaves"))
                listar(meu_indice)
                input("Pressione enter para continuar.")
            elif num == 2:
                meu_indice=criar_indice(ler_arquivo_texto("texto"), ler_arquivo_chave("chaves"))
                input("Pressione enter para continuar.")
            elif num == 3:
                chavePesquisa = input("Digite a chave de pesquisa:")
                if(not meu_indice):
                    meu_indice=criar_indice(ler_arquivo_texto("texto"), ler_arquivo_chave("chaves"))
                pesquisa(chavePesquisa, meu_indice)
                input("Pressione enter para continuar.")
            elif num == 4:
                print("Adeus.")
                break
            else:
                print("\nNão encontrei essa opção, digite o valor novamente.")
        except :
                print("\nO valor digitado nao era um numero, porfavor digite um numero.")
                input("Pressione enter para continuar.")


if __name__ == '__main__':
    main()