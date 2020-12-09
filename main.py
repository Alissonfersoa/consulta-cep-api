##Desenvolvido para consulta de CEP utilizando API web

import requests

def main():

    print('=====================')
    print('||  Consulta CEP   ||')
    print('=====================')
    print('\n')

    cep_input = input('Digite o CEP para consulta: ')

    if len(cep_input) != 8:
        print('CEP com digitos inválidos!')
        exit()

    #conecta com api para buscar informação do CEP
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('====> CEP ENCONTRADO <====')
        print('________________________________\n')
        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
        print('________________________________\n')
        
    else:
        print('{} - CEP inválido!! Insera um novo código'.format(cep_input))

    print('---------------------------------')
    option = int(input('Deseja realizar uma nova consulta? \n1- Sim\n2- Sair\n'))
    print('---------------------------------')
    if option == 1:
        main()
    else:
        print('Fechando execução .......\n')

if __name__ == '__main__':
    main()