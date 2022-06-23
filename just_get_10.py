from tkinter import *
from random import random
import os

class game_window:

     def __init__(self, win):
          self.win = win
          self.canvas = Canvas(self.win, width=2000, height=2000, background='black')
          self.main_menu()

     def create_board(self, size, board_changed):

          self.size = size

          if board_changed == []:
               self.board_g = board_generation.create_default_board(size, [0.1, 0.2, 0.3])
          else:
               self.board_g = board_changed
               
          self.board = Canvas(self.win, width=size*100, height=size*100)
          self.canvas.place(x=0, y=0)

          a, b = 0, 0

          colors = {1: 'green', 2: 'blue', 3: 'orange', 4: 'red', 5: 'pink', 6: 'yellow', 7: 'purple', 8: 'brown', 9: 'grey', 10: 'white'}

          for i in range(size):
               width = 0

               if i != 0:
                    b = b + 100
               
               for j in range(size):
                    color = colors.get(self.board_g[j][a])
                    self.board.create_rectangle(b, width, b+100, width+100, fill=color, outline = 'white')
                    self.board.create_text(b+50, width+50, font=("Arial", 20), text=str(self.board_g[j][a]), fill="white")
                    width += 100
               a += 1
     
          self.board.pack(pady=0)
          self.board.bind('<Button-1>', self.click)

          self.max_score = Label(self.win, text="Maximum : " + str(board_infos.largest_case(self.board_g)), bg="black", font=("Arial", 15), fg="white")
          self.max_score.pack(pady=5)
          self.victory(board_infos.largest_case(self.board_g))

          self.game_over()


     def victory(self, max_score):
          if max_score == 10:
               self.board.destroy()
               self.max_score.destroy()
               self.victory = Label(self.win, text="Congratulations, you won!", bg="black", font=("Arial", 20), fg="white")
               self.victory.pack(pady=80)
               self.play_again = Button(self.win, text='Play again', bd='10', command=lambda:[self.restart()])
               self.play_again.pack(pady=50)


     def game_over(self):
          not_playable = 0
          for x in range(self.size):
               for y in range(self.size):
                    if board_infos.action_left(self.board_g, x, y) == False:
                         not_playable += 1
                    if not_playable == self.size*self.size:
                         self.board.destroy()
                         self.max_score.destroy()
                         self.game_over = Label(self.win, text="Oups, game over!", bg="black", font=("Arial", 20), fg="white")
                         self.game_over.pack(pady=80)
                         self.play_again = Button(self.win, text='Play again', bd='10', command=lambda:[self.restart()])
                         self.play_again.pack(pady=50)

     
     def restart(self):
          self.win.destroy()
          os.startfile("just_get_10.py")


     def click(self, event):
          x = event.x
          y = event.y

          x = self.get_pos(x)
          y = self.get_pos(y)

          if board_infos.action_left(self.board_g, y, x):
               self.board.destroy()
               self.max_score.destroy()
               board_modification.destroy_neighbourhood(self.board_g, y, x)
               new_board = board_modification.falling_off(self.board_g, [0.1, 0.2, 0.3])
               self.create_board(self.size, new_board)


     def get_pos(self, num):
          string_num = str(num)
          map_object = map(int, string_num)
          separate_digit_list = list(map_object)
          if len(separate_digit_list) < 3:
               return 0
          return separate_digit_list[0]


     def main_menu(self):
          self.canvas_main = Canvas(self.win, width=2000, height=2000, background='black')
          self.canvas_main.place(x=0, y=0)

          self.title = Label(self.win, text="Just Get 10", bg="black", font=("Arial", 30), fg="white")
          self.title.pack(pady=10)

          labelframe = LabelFrame(self.win)
          grid = Canvas(labelframe, width=100, height=100, background='black', borderwidth=0)
          grid.pack(side=RIGHT, fill=BOTH, expand=1)
          labelframe.pack(pady=200)

          self.btn4x4 = Button(grid, text='4x4', bd='20', command=lambda:[self.create_board(4, []), self.canvas_main.destroy(), self.btn4x4.destroy(), self.btn5x5.destroy(), self.btn6x6.destroy(), self.btn7x7.destroy(), self.btn8x8.destroy(), grid.destroy(), labelframe.destroy()])
          self.btn5x5 = Button(grid, text='5x5', bd='20', command=lambda:[self.create_board(5, []), self.canvas_main.destroy(), self.btn4x4.destroy(), self.btn5x5.destroy(), self.btn6x6.destroy(), self.btn7x7.destroy(), self.btn8x8.destroy(), grid.destroy(), labelframe.destroy()])
          self.btn6x6 = Button(grid, text='6x6', bd='20', command=lambda:[self.create_board(6, []), self.canvas_main.destroy(), self.btn4x4.destroy(), self.btn5x5.destroy(), self.btn6x6.destroy(), self.btn7x7.destroy(), self.btn8x8.destroy(), grid.destroy(), labelframe.destroy()])
          self.btn7x7 = Button(grid, text='7x7', bd='20', command=lambda:[self.create_board(7, []), self.canvas_main.destroy(), self.btn4x4.destroy(), self.btn5x5.destroy(), self.btn6x6.destroy(), self.btn7x7.destroy(), self.btn8x8.destroy(), grid.destroy(), labelframe.destroy()])
          self.btn8x8 = Button(grid, text='8x8', bd='20', command=lambda:[self.create_board(8, []), self.canvas_main.destroy(), self.btn4x4.destroy(), self.btn5x5.destroy(), self.btn6x6.destroy(), self.btn7x7.destroy(), self.btn8x8.destroy(), grid.destroy(), labelframe.destroy()])

          self.btn4x4.pack(side=LEFT, padx = 20)
          self.btn5x5.pack(side=LEFT, padx = 20)
          self.btn6x6.pack(side=LEFT, padx = 20)
          self.btn7x7.pack(side=LEFT, padx = 20)
          self.btn8x8.pack(side=LEFT, padx = 20)


class board_generation:

     def create_default_board(n, chance):
          board = []
          for i in range(n):
               row = []
               for j in range(n):
                    row.append(board_generation.random_case(chance))

               board.append(row)
          return board

     def random_case(chance):
          n = random()
          chance3 = chance[2]
          chance2 = chance[1]
          chance1 = chance[0]

          if chance3 < n <= 1:
               return 1
          if chance2 < n <= chance3:
               return 2
          if chance1 < n <= chance2:
               return 3
          if 0 <= n <= chance1:
               return 4

class board_modification:

     def create_neighbourhood(board, neighbourhood, x, y):
          if [x, y] not in neighbourhood:
               neighbourhood.append([x, y])

          case = board[x][y]

          pos_up = x - 1
          pos_down = x + 1
          pos_left = y - 1
          pos_right = y + 1

          if pos_up >= 0:
               if board[pos_up][y] == case:
                    if [pos_up, y] not in neighbourhood:
                         neighbourhood.append([pos_up, y])
                         board_modification.create_neighbourhood(board, neighbourhood, pos_up, y)

          if pos_down < len(board):
               if board[pos_down][y] == case:
                    if [pos_down, y] not in neighbourhood:
                         neighbourhood.append([pos_down, y])
                         board_modification.create_neighbourhood(board, neighbourhood, pos_down, y)

          if pos_left >= 0: 
               if board[x][pos_left] == case:
                    if [x, pos_left] not in neighbourhood:
                         neighbourhood.append([x, pos_left])
                         board_modification.create_neighbourhood(board, neighbourhood, x, pos_left)

          if pos_right < len(board):
               if board[x][pos_right] == case:
                    if [x, pos_right] not in neighbourhood:
                         neighbourhood.append([x, pos_right])
                         board_modification.create_neighbourhood(board, neighbourhood, x, pos_right)

          return neighbourhood


     def destroy_neighbourhood(board, x, y):

          neighbourhood = board_modification.create_neighbourhood(board, [], x, y)

          if len(neighbourhood) <= 1:
               return

          for case in neighbourhood:
               if [x, y] != case:
                    board[case[0]][case[1]] = 0
               else:
                    board[x][y] += 1


     def falling_off(board, chance):
          for i in range(1, len(board)):
               for a in range(len(board)):
                    if board[i][a] == 0:
                         for b in range(i, 0, -1):
                              board[b][a] = board[b - 1][a]
                              board[b - 1][a] = 0

          for i in range(len(board) - 1, -1, - 1):
               for a in range(len(board) - 1, -1, -1):
                    if board[i][a] == 0:
                         board[i][a] = board_generation.random_case(chance)

          return board

class board_infos:

     def largest_case(board):
          largest = 1
          for row in board:
               for case in row:
                    if case > largest:
                         largest = case
          return largest

     def neighbour(board, x, y): 
          pos_up = x - 1
          pos_down = x + 1
          pos_left = y - 1
          pos_right = y + 1

          if pos_up < 0:
               pos_up = 0

          if pos_down > len(board) - 1:
               pos_down = len(board) - 1

          if pos_right > len(board) - 1:
               pos_right = len(board) - 1

          if pos_left < 0:
               pos_left = 0

          neighbour = False
          case = board[x][y]

          if pos_up != x:
               if board[pos_up][y] == case:
                    neighbour = True
          if pos_down != x:
               if board[pos_down][y] == case:
                    neighbour = True
          if pos_left != y:
               if board[x][pos_left] == case:
                    neighbour = True
          if pos_right != y:
               if board[x][pos_right] == case:
                    neighbour = True
          
          return neighbour

     def action_left(board, x, y):
          for a in range(len(board)):
               for b in range(len(board)):
                    if board_infos.neighbour(board, x, y) == False:
                         return False
                    else:
                         return True

window=Tk()
game_window=game_window(window)
window.title('Just Get 10')
window.geometry('1000x700')
window.mainloop() 