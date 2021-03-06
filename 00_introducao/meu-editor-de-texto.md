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


### Configuração - Settings

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

### Snippets

São trechos de códigos, geralmente inseridos com a utilização de um atalho de teclado.

- **Criando um novo snippet:** tools >> Developter >> New Snippet...

Um template será aberto para definição de seu snippet.

```xml
<snippet>
    <content><![CDATA[
Hello, ${1:this} is a ${2:snippet}.
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
    <!-- <tabTrigger>hello</tabTrigger> -->
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <!-- <scope>source.python</scope> -->
</snippet>
```
Para personalizar seu snippet, realize as seguintes alterações:

- Em _content_, insira o conteúdo do seu snippet.
- Em _tabTrigger_ defina o nome do snippet;
- Em _scope_ define o tipo de arquivo que utilizará o snippet;

Ao final, seu arquivo deverá ter mais ou menos o seguinte formato:

```xml
<snippet>
    <content><![CDATA[
Meu primeiro ${1:snippet}.
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
    <tabTrigger>meu_snippet</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <scope>source.python</scope>
</snippet>
```

No exemplo acima, foi definido ${1:snippet} como ponto de parada do cursor. Ou seja, uma variável que poderá ser alterada 
quando seu snippet for inserido.

Salve o arquivo: CTRL+ s, o que deve ser feito em {$USER}/.config/sublime-text-3/Packages/User/

Para inserir o snippet, utilize CTRL+Shift+P e selecione-o na lista. Caso não aparecer na lista, digite snippet e a relação de todos os snippets será listada.

- **Criando um atalho para seu novo snippet:** Preferences >> Key Bindings

Dois paineis semelhantes ao das configurações se abrirão. Entre com o código abaixo, 
no painel da direita. 

```
{ "keys": ["ctrl+1"], "command": "insert_snippet", "args": {"name": "Packages/User/myFunction.sublime-snippet"} }
```

O painel da esquerda, refere-se aos atalhos já existentes e pode ser utilizado para verificar 
a combinação de teclas já existentes.

Procure um comando que ainda não esteja sendo utilizado e insira em keys.
Na chave name, informe o endereço do arquivo xml do seu snippets e pronto.

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
- SublimeText Dicas, [Snippets: como criar atalhos para trechos de código ou texto][5].
- Millwardesque, [Speed up development using keyboard-triggered snippets in Sublime Text 2][6].

[1]: https://www.sublimetext.com/docs/3/linux_repositories.html
[2]: https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/
[3]: http://sublimetextdicas.com.br/sublime-text-como-ide-para-python/
[4]: https://www.sublimetext.com/docs/3/
[5]: http://sublimetextdicas.com.br/snippets-como-criar-atalhos-para-trechos-de-codigo-ou-texto/
[6]: http://www.millwardesque.com/speed-development-using-keyboard-triggered-snippets-sublime-text-2/
