"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    nom1 = input('Digite um nome:\n')
    nom2 = input('Digite um segundo nome:\n')
    nom3 = input('Digite um terceiro nome:\n')
    apresentação = [nom1,nom2,nom3]
    for i in range(len(apresentação)):
      for j in range(len(apresentação) - 1):
        if apresentação[j] < apresentação[j+1]:
          apresentação[j], apresentação[j+1]= apresentação[j+1], apresentação[j]
    print(apresentação[0]) 
    print(apresentação[1])
    print(apresentação[2])



if __name__ == '__main__':
    main()
