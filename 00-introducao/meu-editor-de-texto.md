# Meu editor de texto

Indo direto ao ponto: Vamos utilizar __**Sublime 3**__.

Suas principais características são:

- Leve 
- Agilidade
- Customizável
- Multiplataforma

Talvez, futuramente acabe fazendo uso de mais alguma ferramenta, mas por hora, 
ficarei somente com esse editor.

### Instalação

Para começar os trabalhos, realize o download do arquivo de instalação:

Para arquivo tar.bz2:
```
tar -jxf sublime_text_x.tar.bz2
```
Para arquivo .deb:
```
dpkg -i sublime_text_x.deb
```
Existe também a opção de fazer o download e instalação diretamente de um dos 
[repositórios][1]

### Comandos básicos

- **Goto Anything:** Ctrl + P, abre uma lista de seleção que possui um campo de 
busca por arquivos abertos ou que pertencem a um projeto. O campo serve para 
filtrar o conteúdo da lista à medida em que digitamos o nome do arquivo que 
queremos abrir.
- **Goto Symbol:** Ctrl + R, abre uma lista de seleção na qual podemos escolher um 
dos símbolos (identificadores) contidos no arquivo atual e leva o cursor para 
a linha em que ele está definido.
- **Goto Definition:** F12, ao ser acionado, o comando leva você para a posição da 
definição do símbolo que está sob o cursor. (ST3)
- **Goto Symbol in Project:** Ctrl + Shift + R, abre uma caixa de pesquisa para 
que você escolha um símbolo dentre os que existem no projeto e leva o cursor 
para a definição do símbolo selecionado. (ST3)
- **Goto Symbol:** CTRL + /, insere comentários.
- **Goto Line Number:** CTRL + g, vai para uma linha no arquivo atual.
- **Deleta a linha atual:** CTRL + Shift + k.
- **Multi-Edit:** Selecione uma palavra e pressione CTRL+d até selelcionar todas 
as palavras iguais e inicio a edição.
- **Multi-Edit com o mouse:** CTRL + click e vai selecionando todas as palavras 
que deseja editar simultaneamente.


### Configuração

São várias as opções de configuração, mas vou citar aqui algumas que já fiz e 
estou gostando. Provavelmente, com o passar do tempo, sentirei a necessidade 
de outras customizações e/ou desfazer algumas.

Vá em preferences >> Settings e será aberto um arquivo texto, para inserir suas
preferências. 

Detalhe, há dois paineis:

- O da esquerda: são as configurações padrão. Geralmente não altero.
- O da direto: provavelmente ainda vazio. É só inserir suas preferências entre 
as chaves, separando por um vírgula cada customizações.

Seguem alguns exemplos:

```
{

    // Tamanho da Fonte
    // Poderá sobreescrever a existente
    "font_size": 12,

    // Estilo de cores
    "ignored_packages":
    [
        "Vintage"
    ], 

    // Tamanho do tab
    "tab_size": 4,

    // Converte tab para espaços
    "translate_tabs_to_spaces": true,

    // Barra Vertical
    "rulers": [72, 80, ],

    // Quebra de linha automática
    "word_wrap": true,

    // Tamanho da quebra de linha
    "wrap_width": 80, 

}
```

### Plugins

Também são várias as opções de plugins e por isso, inicialmente citarei alguns,
mas provavelmente voltarei para registrar outras opções interessantes:

- **Package Control:** Controla a instalação de todos os pacotes adicionais
- **SublimeCodeIntel:** Autocomplete de código
- **Python PEP 8 Autoformat:** Autoformata o código de acordo com a PEP8
- **Anaconda:** Adiciona algumas funcionalidade de IDE ao editor
- **GitGutter:** Funcionalidades de controle de versão
- **Markdown Preview:** Edição e visualização de arquivos Markdown

### Referências:

- Real Python, [Setting Up Sublime Text 3 for Full Stack Python Development][2].
- SublimeText Dicas, [Sublime Text como IDE para Python][3].
- SublimeText, [Documentation][4].

[1]: https://www.sublimetext.com/docs/3/linux_repositories.html
[2]: https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/
[3]: http://sublimetextdicas.com.br/sublime-text-como-ide-para-python/
[4]: https://www.sublimetext.com/docs/3/
