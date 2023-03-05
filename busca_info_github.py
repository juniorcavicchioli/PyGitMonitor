import requests

def get_user(usuario):
    """
    Faz uma requisição GET para a API do GitHub, buscando informações sobre um determinado usuário.
    Args:
        usuario (str): O nome do usuário do GitHub que deseja-se obter informações.
    Returns:
        dict: Um objeto JSON contendo as informações do usuário.
    Raises:
        requests.exceptions.HTTPError: Se ocorrer um erro HTTP durante a requisição.
    """
    try:
        url = f'{url_padrao}/users/{usuario}'
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status() # Levanta uma exceção caso a resposta da API seja inválida
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404: # Caso seja um erro 404 (Not Found)
            print(f'O usuário {usuario} não foi encontrado no GitHub.')
            exit()
        else:
            print(f'Ocorreu um erro ao buscar o usuário {usuario}.')
            exit()
    else:
        return resposta.json()
    

def get_repos(usuario):
    """
    Coleta e coloca na lista os nomes dos repositórios do usuário no GitHub.
    Args:
        usuario (str): O nome do usuário do GitHub que deseja-se obter informações sobre os repositórios.
    Returns:
        list: Uma lista de strings contendo os nomes dos repositórios do usuário.
    """
    repositorios = []
    url_repositorios = f'{url_padrao}/users/{usuario}/repos'
    res_repositorios = requests.get(url_repositorios, headers=headers)
    dados_repositorios = res_repositorios.json()
    for i in dados_repositorios:
        repositorios.append(i['name'])
    return repositorios


def filtro_dados(dados):
    """
    Filtra e retorna algumas informações específicas do perfil de um usuário do GitHub.
    Args:
        dados (dict): Um dicionário contendo os dados do perfil do usuário do GitHub.
    Returns:
        dict: Um dicionário com as seguintes informações do usuário do GitHub:
            - nome_completo (str): O nome completo do usuário.
            - nome_usuario (str): O nome de usuário do GitHub.
            - bio (str): A biografia do usuário.
            - num_repositorios (int): O número total de repositórios públicos do usuário.
    """
    nome_completo = dados['name']
    nome_usuario = dados['login']
    bio = dados['bio']
    num_repositorios = dados['public_repos']
    return {'nome_completo': nome_completo, 'nome_usuario': nome_usuario,
            'bio': bio, 'num_repositorios': num_repositorios}


def exibir_usuario(dados, repositorios):
    """
    Exibe as informações filtradas do perfil de um usuário do GitHub na saída padrão.
    Args:
        repositorios (list): Uma lista de strings contendo os nomes dos repositórios públicos do usuário do GitHub.
        dados (dict): Um dicionário contendo as informações filtradas do perfil do usuário do GitHub.
    Returns: None
    """
    print(f'Nome completo: {dados["nome_completo"]}')
    print(f'Nome de usuário do GitHub: {dados["nome_usuario"]}')
    if dados["bio"]:
        print(f'Bio: {dados["bio"]}')
    print(f'Número de repositórios públicos: {dados["num_repositorios"]}')
    if dados["num_repositorios"] > 0:
        print(f'Nomes dos repositórios públicos: {", ".join(repositorios)}')
        

# API key para usar a API do GitHub
api_key = 'sua_chave_api'
usuario = input('Digite o nome de usuário do GitHub desejado: ')
url_padrao = "https://api.github.com"
headers = {'Authorization': f'Token {api_key}'}

# Programa principal 
exibir_usuario(filtro_dados(get_user(usuario)), get_repos(usuario))
