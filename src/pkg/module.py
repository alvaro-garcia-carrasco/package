import yaml
import requests

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        result = 'infinite'
    else:
        result = a / b
    return result
