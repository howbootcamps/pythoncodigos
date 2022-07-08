# Instalação Django

## [Menu principal](./../README.md)

## Projeto 
  
Ambiente virtual do python
```
python3 -m venv .venv
```

Ativação ambiente virtual Linux
```
source .venv/bin/activate
```

Ativação ambiente virtual Windows
```
.venv\Scripts\activate.bat
``` 

instalação django
```
pip install django
``` 

criação projeto
```
django-admin startproject configuracoes .
```  

configurações de idioma.
no arquivo ***configuracoes/settings.py*** altere as constantes

    LANGUAGE_CODE = 'pt-br' 
    TIME_ZONE = 'America/Sao_Paulo'

criar um novo app 
```
python manage.py startapp projeto
```

```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

pip install mysqlclient
```



