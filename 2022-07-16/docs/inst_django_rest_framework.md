# django rest framework

## [Menu principal](./../README.md#main-section)

## Instalação

    pip install djangorestframework
    pip install markdown
    pip install django-filter 


## Configuração 

No arquivo ***configuracoes/settings.py*** adicionar o 'rest_framework' aos APPS

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]


no arquivo ***configuracoes/urls.py*** 

    ...
    from rest_framework import routers

    router = routers.DefaultRouter()
    
    urlpatterns = [
        ...
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]

## Paginação
A paginação permite controlar quantos objetos por página são retornados. Para habilitá-lo, adicione as seguintes linhas ***configuracoes/settings.py***

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    }