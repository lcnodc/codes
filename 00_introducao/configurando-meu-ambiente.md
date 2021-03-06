
# Configurando meu ambiente para desenvolvimento Python no Linux.

Vou relacionar os passos que fiz para configurar um ambiente de estudo de Python
em meu pc.

Obviamente, esta é só a forma que fiz naquela ocasião, podendo ser feita a 
mesma coisa de formas mais simples ou até mesmo mais complexa.

Como tudo roda em uma máquina virtual com o sistema Ubuntu 16.04, instalado do 
core, algumas libs não existiam e quando realizei a instalação do Python tive 
que instalar essas libs.

Outro detalhe, é que apesar de ter instalado o Ubuntu do core e em alguns 
casos pacote a pacote, ao final já tinha o Python nas versões 2.x e 3.x, mas 
optei por realizar uma nova instalação do Python em meu /home/${USER}/ pois 
gostaria de concentrar todas as versões que fosse utilizar em um só lugar.

Enfim, vamos lá...

### Instalando o Python

Primeiramente verifique se seu sistema já possui as libs abaixo, caso contrário,
instale todas. Serão úteis.

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \ xz-utils tk-dev
```

Baixe a versão desejada do Python:

```
wget http://www.python.org/ftp/python/3.3/Python...
tar -zxvf Python3.3.tgz
cd Python3.3
```

**Nota:**

*Utilizando a versão 3.3 do Python, tive que voltar nesse ponto, pois ao finalizar a instalação, notei que não tinha suporte a zlib.*

*Deste a forma, editei o arquivo /Modules/Setup e descomentei a seguinte linha:*

```
zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz
```

*alterando para o diretório /Modules/zlib. Compilei o módulo da zlib:*

```
./configure
make
sudo make install
```

*e de volta ao raiz do install do Python...*

```
make clean
./configure --prefix=/home/${USER}/.pythons/python3.3.
make
make install
```

### Instalando a virtualenv

```
wget http://pypi.python.org/packages/source/v/virtualenv/virtualenv-15.1.0.tar.gz
tar -zxvf virtualenv-15.1.0.tar.gz
cd virtualenv-15.1.0/
~/.pythons/python3.3/bin/python setup.py install
```

### Criando sua virtualenv

```
mkdir /home/${USER}/.virtualenvs
cd /home/${USER}/.virtualenvs
~/.pythons/python3.3/bin/virtualenv py3.3 --python=/home/${USER}/.pythons/python3.3/bin/python-x
```

### Ativando a virtualenv

```
cd ~/.virtualenvs/py3.3/bin
source ./activate

(py3.3)$ python
Python 3.3 (default, Jun 01 2017, 15:52:39) 
[GCC 5.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

(py3.3)$ deactivate
$ python
Python 3.3 (default, Jun 01 2017, 15:55:00) 
[GCC 5.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Pronto. Nesse ponto, você tem um ambiente praticamente pronto para seus estudos Python.

Lembrando que na maioria das distribuições Linux você já encontrará o Python nas versões 2.x e 3.x pronto para seus estudos. Como disse realizei a instalação adicional, mais por curiosidade e porque queria utilizar versões diferentes e centralizá-las em uma pasta local.

### Referências

- Building Python from source with zlib support, https://stackoverflow.com/q/12344970
- Common Build Problemns, https://github.com/pyenv/pyenv/wiki/Common-build-problems
- Is it possible to install another version of Python to Virtualenv?, https://stackoverflow.com/a/5507373
