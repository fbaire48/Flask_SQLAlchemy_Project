# 1. Preview:
![Imagem 1](1.png)

***
# 2. Passo a Passo:

## 2.1. :file_folder: Abra a pasta "codigo" em sua IDE:


## 2.2. :books: Dependências:

**Opção 1:**

    pip install flask, flask_sqlalchemy, sqlalchemy, mysqlclient

**Opção 2:**

    pip install -r requirements.txt


## 2.3. :floppy_disk: Query MySQL necessária:

```sql
CREATE DATABASE empresa;

USE empresa;
```


## 2.4. :scroll: Rodar o arquivo  "app.py" 
:warning: Fique atento:

``` python
"mysql://root:" "@localhost/empresa"
```

Se o seu usuário for diferente de **root** ou se **existir senha**, faça as alterações necessárias.

**Exemplo:**
- Usuário: `lab`
- Senha: `123456`

``` python
"mysql://lab:123456@localhost/empresa"
```
