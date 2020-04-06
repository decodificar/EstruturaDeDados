# Nome da Disciplina: Estrutura de Dados
# Turma: Engenharia da Computação - Noturno 3B
# Jade Denice Jaquetta Pereira, 1900789
# Data de envio: 05.04.2020
# Professor: JORGE CARLOS VALVERDE REBAZA


"""
Pergunta 1: Likes de Postagens em Redes Sociais.
"""
# classe para rede social
class GestorPostagens:
    # iniciando construtor
    def __init__(self, posts):
        self.posts = []

    """
    1) Registrar um novo post:
    """

    # função para criar postagem
    def novoPost(self):
        post = 0
        self.posts.append(post) # pega a lista posts e adiciona um novo valor para ela, ou seja um post novo
        print('Post número', post, 'foi criado com sucesso.')

        print('A lista de postagens é a seguinte: ')
        
        indice = 0 
        while indice < len(post):
            print('indice: ', indice)
            indice += 1

        likes = 0
        print('Likes: ', likes)
    
    '''
    2) Registrar um número específico de likes a uma postagem:
    '''     
    def registraLikes(self):
        numPost = int(input('Ingresse o número do post ao qual você quer dar likes: '))
        
        # Com esse for e if estou verificando se há o valor que o usuário informou dentro da lista
        resultado = False
        self.posts = posts
        for i in range(len(posts)):
            if posts[i] == numPost:
                resultado = True
        if resultado == True:
            posts(numPost)

        likes = int(input('Ingresse o número de likes que vocêr quer atribuir: '))
        for i in posts:
            likes += i
        return likes

        print('Índice: ', posts)
        print('Likes: ', likes)

def menu(self):
    '''
    Menu
    '''
    print('Menu Sistema Gestor de Postagens')
    print('''
            1. Criar um Post
            2. Dar likes a um post
            3. Top Posts com mais likes''')
    opc = int(input('Digite uma opção: '))
    if opc == 1: 
        opcao = GestorPostagens()
        opcao.novoPost()
        retornar = int(input('Aperte R para voltar: '))
    if opc == 2:
        opcao = GestorPostagens
        opcao.registraLikes()
        retornar = int(input('Aperte R para voltar: '))
    if opc == 3:
        
        









    

        


test = GestorPostagens()
test.novoPost()
test.novoPost()
test.novoPost()