# Configurando Python no Windows

### Executando scripts Python no Windows

No linux, para transformar um arquivo em executável devemos alterar suas 
permissões e chamar o arquivo seguido de um ponto e uma barra:

```
$ arquivo.py
$ chmod +x arquivo.py
$ ./arquivo.py
```

Já no Windows, por padrão, arquivos de extensão .py não são executados
automaticamente.

Para isso, devemos informar ao sistema que essa extensão deve ser 
executada por um aplicativo específico. Utilizando o prompt execute os 
seguinte comandos.

```
assoc .py=Python.File
```
Associando a extensão do tipo de arquivo.

```
ftype Python.File=C:\Path\to\pythonw.exe "%1" %*
```
Associando o tipo de arquivo ao executável desejável.

E pronto. Agora é só chamar o arquivo .py no cmd que ele será executado.
Obs: Quando passar algum argumento, utilizar aspas.

```
c:\>my_program.py 
Hello World
```

### Referências

Python.org. [Using Python on Windows][1]



[1]: https://docs.python.org/3.3/using/windows.html
