import requests


def operation_tres_compliquee(nombre1, nombre2):
    return nombre1 + nombre2


def operation_web(url):
    return requests.get(url)
