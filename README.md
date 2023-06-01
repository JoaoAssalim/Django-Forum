# Time Limit Excedeed Forum to Devs - Social Media

## Configuração do sistema.
Esse tópico da documentação tem como objetivo realizar a configuração do sistema para o ambiente de desenvolvimento.

### Virtualenv
O primeiro passo após clonar o repositório é realizar a criação da virtualenv.
```
  virtualenv venv
```
Depois de criar a venv é necessário atilava para que as dependências do projeto sejam instaladas.
```
  venv/Scripts/Activate
```
Com a venv ativa vamos instalar as dependências do projeto que se encontram no arquivo requirements.txt.
```
  pip install -r  requirements.txt
```

### Migrações
```
  python manage.py makemigrations
  python manage.py migrate_schemas
```
