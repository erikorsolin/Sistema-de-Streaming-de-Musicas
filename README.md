# Sitema de Streaming de Música em Python

Projeto semestral da matéria Programação Orientada a Objetos I (INE5402) da Universidade Federal de Santa Catarina (UFSC). O projeto foi realizado pelos estudantes [André Amaral Rocco](https://github.com/andrerocco) e [Erik Orsolin de Paula](https://github.com/erikorsolin).

## Introdução ao projeto
O objetivo do projeto foi de criar um sistema de Streaming de Música em Python utilizando o paradigma da orientação a objetos. 

### Como funciona?
O sistema tem dois tipos de usuário: **Artistas** e **Ouvintes**. Os usuários armazenam diversas informações em atributos, como seu nome, nome de usuário, data de nascimento, além de armazenarem um cartão de crédito. O cartão de crédito é uma classe em sí, a qual se comunica com a classe Usuário por meio de agregação.
Além disso, existem classes do tipo **Playlists** e do tipo **Música**. As playlists agrupam as músicas no sistema, além de conterem informações adicionais como um nome próprio e quantidade de músicas.
Usuários do tipo Artista podem adicionar e excluir músicas no sistema, além de poderem criar playlists ilimitadas. Já usuários do tipo Ouvinte podem seguir e deixar de seguir os artistas. Ouvintes também podem criar playlists, mas estão limitados em no máximo 2 playlists por conta (aplicação de polimorfismo).

O controle das classes do sistema ocorre por meio de um menu no arquivo ```main.py```. É possível fazer login em contas já criadas ou criar uma nova conta. A partir disso, o usuário consegue através do menu: 

1. Ver músicas disponíveis na plataforma
2. Ver artistas da plataforma
3. Seguir um artista _(apenas para ouvintes)_
4. Deixar de seguir um artista _(apenas para ouvintes)_
5. Adicionar nova música _(apenas para artistas)_
6. Remover uma música _(apenas para artistas)_
7. Ver todas suas músicas _(apenas para artistas)_
8. Criar uma playlist
9. Excluir uma playlist
10. Editar uma playlist
11. Ver informações das suas playlist
12. Ver informações do seu cartão de crédito
13. Deslogar

### Diagrama de funcionamento das classes
![Diagrama das classes referente ao projeto](/extra-src/DiagramaClasses.png "Diagrama de classes")