# Funções e Escopos

Em Python, todas as funções retornam algum valor, independente se 
possuem a declaração de return ou não.

Exemplo:

```python
def preenche_lista():
    pass


print("Lista: %s" % ([preenche_lista() for i in range(10)]))
```

O resultado desse código  uma lista cheio de None's. Perceba que 
utilizei a palavra pass, para dizer que nenhuma operação seria executada.

_...continua_

### Referências

- [is it possible to not return anything from a function in python?][1]
- [Python pass Statement][2]


[1]: https://stackoverflow.com/q/10067013
[2]: https://www.tutorialspoint.com/python/python_pass_statement.htm
