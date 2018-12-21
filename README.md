# WebTasklist
Prova prática para a seleção da Supero

Aplicação feita usando o framework [web2py](http://http://web2py.com/)

## Para rodar localmente

- Faça download do framework [aqui](https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip)
- Clone este repositório dentro da pasta `web2py/applications/`
- Inicie o servidor do web2py com o comando 
```python web2py.py```
- Acesse o endereço `http://localhost:8000/tasklist` no navegador


## Detalhes da aplicação
- Aplicação feita no modelo MVC;
- Definições de tabelas ficam em `models/02_tabelas.py`
- Controler da aplicação principal em `controllers/default.py`
- Views da aplicação principal dentro da pasta `views/default/*.html`


## Exemplos da API REST
O arquivo de controller `controllers/api.py` possui as funções da API REST básica.


O retorno é em formato json.

- Podemos consultar dados via GET usando o navegador:


Endpoint para acessar todas as tarefas cadastradas
```http://localhost:8000/tasklist/api/rest/tarefas```


Acessar detalhes de tarefa pelo seu id
```http://localhost:8000/tasklist/api/rest/tarefas?id=1```


Podemos adicionar novas tarefas via POST, exemplo usando curl:
```curl -d "titulo=tarefa adicionada via api" http://localhost:8000/tasklist/api/rest/tarefas```


E excuir também, passando com argumento o id da tarefa:
```curl -X DELETE http://localhost:8000/tasklist/api/rest/tarefas/5```

## Demonstração
Uma livedemo da aplicação pode ser acessada em http://volneyrock.pythonanywhere.com/web2tasklist

Para testar a api na liveapp troque o trecho `http://localhost:8000/tasklist` por `volneyrock.pythonanywhere.com/web2tasklist` na url. 

