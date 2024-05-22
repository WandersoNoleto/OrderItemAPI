## OrderItemApi 


  
### Funcionalidades 
1. Gerenciamento de usuários:
  - Crie um novo usuário com um nome de usuário e senha exclusivos;
  - Autenticar um usuário usando seu nome de usuário e senha;
  - Atualize as informações do perfil de um usuário (por exemplo, nome, e-mail, etc.);
  - Recupere as informações do perfil de um usuário.
    
2. Gerenciamento de itens:
  - Crie um novo item com nome e preço;
  - Atualize o nome e o preço de um item;
  - Excluir um item;
  - Recupere uma lista de todos os itens.
    
3. Gestão de Pedidos:
  - Crie um novo pedido para um usuário, contendo um ou vários itens;
  - Recupere todos os pedidos de um usuário;
  - Recupere detalhes de um pedido específico, incluindo os itens.


## :gear: Instalação
Estas instruções fornecerão uma cópia do projeto em funcionamento em sua máquina local para fins de desenvolvimento e teste.
O que você precisa para instalar o software e como instalá-lo


Primeiro, clone o repositório
```
git clone https://github.com/WandersoNoleto/OrderItemAPI.git
```
Instale as dependências listadas em requirements.txt
```
pip install -r requirements.txt
```
###### :key: Crie um arquivo .env e preencha as variáveis de acordo com [.env.example](https://github.com/WandersoNoleto/OrderItemAPI/blob/main/.env.example).
Gere uma nova chave Django e atribua o valor a SECRET_KEY (Python CLI):
```
from django.core.management import utils
print(utils.get_random_secret_key())
```

Por fim, rode o serviço
```
python3 manage.py runserver
```

## :world_map: Rotas
##### Você pode importar o arquivo <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/insomnia/insomnia-original.svg" width="10" height="10"> [insomnia_endpoints.json](https://github.com/WandersoNoleto/OrderItemAPI/blob/main/insomnia_endpoints.json) para testar as rotas no seu cliente HTTP Insomnia.
  #### Para utilizar as funcionalidades da API, é necessário passar seu `token` no header dos endpoints
  - Header:
    ```
    Authorizarion Token <seu_token>
    ```
### Usuários
- **Registrar usuário**: 
  - Rota: `/users/register/`
  - Method: `POST`
  - Corpo da Solicitação (JSON):
    ```json
    {
        "username": "usuário",
        "password": "senha"
    }
    ```
  - Corpo da resposta (200):
    ```json
    {
        "username": "usuário",
        "email": ""
    }
    ```

- **Gerar token de acesso**: 
  - Rota: `/users/auth/`
  - Method: `POST`
  - Corpo da Solicitação (JSON):
    ```json
    {
        "username": "usuário",
        "password": "senha"
    }
    ```
  - Corpo da resposta (200):
    ```json
    {
      "Access-token": "token"
    }
    ```

- **Ver informações de perfil de usuário**: 
  - Rota: `/users/profile/`
  - Method: `GET`
  - Corpo da Solicitação (JSON):
    ```json
    {
        "username": "usuário",
        "password": "senha"
    }
    ```
  - Corpo da resposta (200):
    ```json
    {
      "Access-token": "token"
    }
    ```
    
- **Atualizar de perfil de usuário**: 
  - Rota: `/users/profile/`
  - Method: `PATCH`
  - Corpo da Solicitação (JSON):
    ```json
    {
      "username": "atualizado",
      "email": "user@email.com",
      "first_name": "nome"
    }
    ```
  - Corpo da resposta (200):
    ```json
    {
      "id": 5,
      "username": "atualizado",
      "email": "user@email.com",
      "first_name": "nome",
      "last_name": ""
    }
    ```
### Itens
- **Listar itens**: 
  - Rota: `/items/`
  - Method: `GET`
  - Corpo da resposta (200):
    ```json
    {
    	"count": 4,
    	"next": null,
    	"previous": null,
    	"results": [
              {
                "id": 1,
                "name": "item1",
                "price": "22.06"
              },
              {
                "id": 2,
                "name": "item2",
                "price": "0.00"
              },
              {
                "id": 3,
                "name": "item3",
                "price": "18.20"
              }
    	]
    }
    ```
- **Obter informações de um item**: 
  - Rota: `/items/1/`
  - Method: `GET`
  - Corpo da resposta (200):
    ```json
    	{
    		"id": 1,
    		"name": "item",
    		"price": "0.00"
    	}


    ```

- **Atualizar informações de um item**: 
  - Rota: `/items/1/`
  - Method: `PATCH`
  - Corpo da Solicitação (JSON):
    ```json
    {
    		"name": "item_atualizado",
    }
  - Corpo da resposta (200):
    ```json
    	{
    		"id": 1,
    		"name": "item_atualizado",
    		"price": "0.00"
    	}
    
- **Excluir informações de um item**: 
  - Rota: `/items/1/`
  - Method: `DELETE`
  - Respota bem-sucedida: HTTP 204
 
### Pedidos
- **Listar Pedidos**: 
  - Rota: `/orders/`- Possível filtrar por `owner`para pegar os pedidos de um usuário específico
  - Method: `GET`
  - Corpo da resposta (200):
    ```json
    {
    	"count": 1,
    	"next": null,
    	"previous": null,
    	"results": [
            {
              "id": 1,
              "owner": 1,
              "tag": "Meu Pedido",
              "items": [
              {
                "id": 1,
                "name": "item1",
                "price": "18.20"
              }
        			],
              "created_at": "data de criação"
            },
    	]
    }
    ```
- **Listar pedido**: 
  - Rota: `/orders/1/`
  - Method: `GET`
  - Corpo da resposta (200):
    ```json

      {
            "id": 1,
            "owner": 1,
            "tag": "Meu Pedido",
            "items": [
            {
              "id": 1,
              "name": "item1",
              "price": "18.20"
            }
      			],
            "created_at": "data de criação"
    },
    ```

- **Criar pedido**: 
  - Rota: `/orders/`
  - Method: `POST`
  - Corpo da solicitação (JSON):
    ```json
    {
      "tag": "Meu Pedido",
      "items": [1, 2, 3]
    },
    ```
   - Corpo da resposta (200):
    ```json
    {
    	"id": 1,
    	"owner": 1,
    	"tag": "Meu Pedido",
    	"items": [
    		{
                        "id": 1,
                        "name": "item1",
                        "price": "18.20"
    		},
    		{
                        "id": 2,
                        "name": "item2",
                        "price": "18.20"
    		},
        {
                        "id": 3,
                        "name": "item3",
                        "price": "18.20"
    		}
    	],
    	"created_at": "data da criação"
    }
    ```

- **Atualizar pedido**: 
  - Rota: `/orders/1`
  - Method: `POST`
  - Corpo da solicitação (JSON):
    ```json
    {
      "tag": "Pedido atualizado",
      "items": [1, 2]
    },
    ```
  - Corpo da resposta (200):
    ```json
    {
      "id": 1,
      "owner": 1,
      "tag": "Pedido atualizado",
      "items": [
        {
          "id": 1,
          "name": "item1",
          "price": "18.20"
        },
        {
          "id": 2,
          "name": "item2",
          "price": "18.20"
        },
      ],
      "created_at": "data da criação"
    }
    ```

 - **Excluir pedido**: 
  - Rota: `/orders/1/`
  - Method: `DELETE`
  - Respota bem-sucedida: HTTP 204
