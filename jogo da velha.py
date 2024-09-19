import random
import os

'''criar função de jogada do jogador
  criar jogada da maquina usando random dentro do posi_free
  deixar o board aparecendo sempre com as posições atualizadas.
  regras que determina quem venceu
'''
alguem_ganhou = 'N'
Jogador = ' '
Maquina = ' '
ON = True
class Board:
    def __init__(self):
      global alguem_ganhou
      self.ON = True
      self.print_board
      self.posi = {
          1: ' ',
          2: ' ',
          3: ' ',
          4: ' ',
          5: ' ',
          6: ' ',
          7: ' ',
          8: ' ',
          9: ' ',
    }
    def print_board(self):
        '''Definição do board do jogo'''
        print(' {} | {} | {} '.format(self.posi[7],self.posi[8],self.posi[9]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.posi[4],self.posi[5],self.posi[6]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.posi[1],self.posi[2],self.posi[3]))
        print('')
        self.winner()

    def posi_is_valid(self, position):
      '''Valida as posições que o jogador escolher'''
      if self.posi[position] == ' ':
        return True
      else:
        return False
    
    def winner(self):
      global alguem_ganhou
      dictwin = {}
      '''define the winner'''
      for i in ['X','O']:
    #Horizontais    
        dictwin[i] = (self.posi[1] ==self.posi[2] ==self.posi[3] == i)
        dictwin[i] = (self.posi[4] ==self.posi[5] ==self.posi[6] ==i)or dictwin[i]
        dictwin[i] = (self.posi[7] ==self.posi[8] ==self.posi[9] ==i)or dictwin[i]
    #Verticais
        dictwin[i] = (self.posi[1] ==self.posi[4] ==self.posi[7] ==i)or dictwin[i]
        dictwin[i] = (self.posi[2] ==self.posi[5] ==self.posi[8] ==i)or dictwin[i]
        dictwin[i] = (self.posi[3] ==self.posi[6] ==self.posi[9] ==i)or dictwin[i]
    #diagonais
        dictwin[i] = (self.posi[1] ==self.posi[5] ==self.posi[9] ==i)or dictwin[i]
        dictwin[i] = (self.posi[3] ==self.posi[5] ==self.posi[7] ==i)or dictwin[i]

      if dictwin['X']:
        if Jogador == 'X' and Maquina == 'O':
          alguem_ganhou = 'S'
          print('Você venceu')
        else:
          alguem_ganhou = 'S'
          print('Maquina Venceu')
      elif dictwin['O']:
        if Jogador == 'O'and Maquina == 'X':
          alguem_ganhou = 'S'
          print('Você venceu')
        else:
          alguem_ganhou = 'S'
          print('Maquina Venceu')  
      else:
        if len(self.posi_free())> 0:
          print('Estou torcendo por você')
        else:
          print('Deu Velha mermão')
  
    def posi_free(self):
      espaco_livre =  [i for i,j in self.posi.items() if j == ' ' ]
      return espaco_livre
    

class Escolha_simbolo:
  def __init__(self):
    global Jogador, Maquina

  def simbolo(self):  
    global Maquina, Jogador
    escolha_jogador = int(input('    Escolha\n1 para: X \nou\n2 para: O '))
    while escolha_jogador < 1 or escolha_jogador > 2:
      escolha_jogador = int(input('    Escolha\n1 para: X \nou\n2 para: O ')) 
    if escolha_jogador == 1:
      Jogador = 'X'
      Maquina = 'O'
    else:
      Jogador = 'O'
      Maquina = 'X'
    return print('\nVocê escolheu: {}\nMaquina ficou com: {}'.format(Jogador,Maquina))
  
    

class Game:
  def __init__(self):
    global ON
    self.board = Board()
    self.choose = Escolha_simbolo()


  def printing_board(self):
    """Prints the board."""
    self.board.print_board()
  
  def moves(self):
    print('Escolha uma posição vazia')
    vazio = int(input())
    if vazio not in self.board.posi_free():
      print('Posição indisponivel')
    else:
      self.board.posi[vazio] = Jogador
      
      if len(self.board.posi_free())>0:
        self.board.posi[random.choice(self.board.posi_free())] = Maquina
      else:
        pass
      self.board.winner()

def fechar_jogo():
  global alguem_ganhou
  global ON
  ON = int(input('Deseja continuar jogando? 1 - Sim 2 - Não: '))
  ON = True if ON == 1 else False
  alguem_ganhou = 'N'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')    

def play():
  global alguem_ganhou
  while ON is True:
    game = Game()
    choose = Escolha_simbolo()
    board = Board()
    game.printing_board()
    choose.simbolo()
    while len(game.board.posi_free()) > 0:
        game.moves()
        limpar_tela()
        game.printing_board()
        
        if alguem_ganhou == 'S':
          break
        else:
          continue
    fechar_jogo()
    limpar_tela()

if __name__ == '__main__':
  play()

