DESCRIPTION_CREATE_USER = """
Criação de um novo usuário. Para registrar um novo usuário:

- `name`: Deve ter um nome.
- `email`: Deve ter nome único e com 3 caracteres ou mais.
- `password`: Deve ser uma string
- `is_active`: Deve ser boleano (`true` ou `false`).
- `is_admin`: Deve ser boleano (`true` ou `false`).
Se o usuário for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`_id`, que é o id da novo usuário em nosso banco de dados.
"""

DESCRIPTION_CREATE_ADDRESS = """ 

    Deve ser informado os dados do usuário na qual o endereço será vinculado. O endereço deve ser uma lista de dicionários.

    - `user`: 
        - `name`: Deve ter um nome.
        - `email`: Deve ter nome único e com 3 caracteres ou mais
        - `password`: Deve ser uma `string`
        - `is_active`: Deve ser boleano (`true` ou `false`)
        - `is_admin`: Deve ser boleano (`true` ou `false`)
    - `address`: 
        - `street`: Deve ter um nome de uma rua ou avenida, junto com o número da residência. Deve ser do tipo `string`
        - `cep`: Deve ter um número de cep, mas deve ser uma `string`
        - `district`: Deve ter um nome de um distrito
        - `city`: Deve ter um nome de uma cidade
        - `state`: Deve ter um nome de um estado
        - `is_delivery`: Deve ser boleano (`true` ou `false`)

Se o endereço for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`_id`, que é o id da novo endereço em nosso banco de dados.

Caso o usuário já tenha algum endereço cadastrado, o novo endereço será adicionado a lista de endereços que 
já consta no sistema. Se for adicionado corretamente, a API retornará sucesso (código HTTP 202).
"""

DESCRIPTION_CREATE_PRODUCT = """ 
    Criação de novo produto. Ele deve conter: 

    - `name`: Deve ter um nome
    - `description`: Deve ter uma descrição
    - `price`: Deve ter um preço do tipo `float` e maior do que 0.01 
    - `category`: Deve ter uma categoria de mercado, exemplo: laticínios, frios, etc
    - `quant_stock`: Deve ter uma quantidade do tipo `int` e maior que 0


Se o produto for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com os campos
`_id`, que é o id da novo produto em nosso banco de dados, e `code` 
que é o código da nova música em nosso sistema.
"""


DESCRIPTION_CREATE_CART = """
    Para a criação do carrinho devem ser informados os seguintes dados:

    - `user`: 
        - `email`: Deve ter nome único e com 3 caracteres ou mais
    - `product`: 
        - `code`: Deve ser uma `str` com o código cadastrado no sistema
        - `quantity`: Deve ser a quantidade do produto no formato `int`

Se o carrinho for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`_id`, que é o id da novo carrinho em nosso banco de dados.

Caso o usuário já tenha algum carrinho cadastrado e em aberto, o novo produto será adicionado a lista de items que 
já consta no sistema. Se for adicionado corretamente, a API retornará sucesso (código HTTP 202).

"""