# Busca informações de perfil de usuário do GitHub
Este programa busca informações de perfil de usuário do GitHub através de sua API. Ele coleta dados como nome completo, nome de usuário, biografia e número de repositórios públicos do usuário, bem como os nomes desses repositórios.

## Pré-requisitos
- Uma chave de API do GitHub (disponível [aqui](https://github.com/settings/tokens))

## Instalação
1. Clone este repositório ou faça o download dos arquivos.
2. Abra o arquivo `busca_info_github.py` em um editor de texto.
3. Insira sua chave de API do GitHub no lugar do texto `sua_chave_api` (variável [`api_key`](https://github.com/juniorcavicchioli/PyGitMonitor/blob/main/busca_info_github.py#L83) na linha 83).
4. Salve e feche o arquivo.

## Como usar
1. Abra um terminal na pasta onde está o arquivo busca_info_github.py.
2. Execute o comando python busca_info_github.py.
3. Digite o nome de usuário do GitHub que você deseja buscar as informações.
4. O programa exibirá as informações de perfil filtradas e o nome dos repositórios públicos do usuário, se houver.

### Exemplos de entrada e saída:

Exemplo real do dia 04-03-2023
```python
Digite o nome de usuário do GitHub desejado: juniorcavicchioli
Nome completo: Adilson Roberto Cavicchioli Junior
Nome de usuário do GitHub: juniorcavicchioli
Número de repositórios públicos: 10
Nomes dos repositórios públicos: calculadora, challengeIBM, fibonacci, logica-segundo-semestre, menu, prova-segundo-semestre-logica, PyGitMonitor, PythonWeatherAPI, techbridge, WalkingDog
```

Exemplo de um usuário inexistente
```python
Digite o nome de usuário do GitHub desejado: inexistente
O usuário inexistente não foi encontrado no GitHub.
```

Exemplo inventado caso todas as informações que são requisitadas existirem
```python
Digite o nome de usuário do GitHub desejado: timothee
Nome completo: Timothée Ravier
Nome de usuário do GitHub: timothee
Bio: Passionate about Python, compilers, and making programming easier for everyone.
Número de repositórios públicos: 3
Nomes dos repositórios públicos: micropython, micropython-lib, rpyc
```

## Contribuição
Este projeto é de código aberto e aceita contribuições. Sinta-se à vontade para fazer um fork e enviar uma pull request com suas melhorias

## Autor
Feito por [@juniorcavicchioli](https://github.com/juniorcavicchioli?tab=repositories). Entre em contato!

LinkedIn: [Adilson Roberto Cavicchioli Junior](https://www.linkedin.com/in/adilson-roberto-cavicchioli-junior-6816b7192?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BIpMh5bVEQOi82%2FRHJ6oxkg%3D%3D) <br>
Email: [cavicchioli.adilson@gmail.com](mailto:cavicchioli.adilson@gmail.com)

Sinta-se à vontade para me contatar caso tenha dificuldade em gerar uma chave para testar o programa, para perguntas, sugestões ou colaborações em projetos futuros!
