from collections import deque

class Puzzle:
  def __init__(self, panel_list, state_list, size):
    self.panel_list = panel_list
    self.state_list = state_list
    self.state_list.append(panel_list)
    self.size = size

  def generate_next_panel(self, puzzle):
    zero_pos = puzzle.panel_list.index(0)
    col = zero_pos // self.size
    row = zero_pos % self.size

    def get_next_panel():
      panel_list = puzzle.panel_list[:]
      n = panel_list[next_pos]  #もともと入っていた数字のポジションを変数に代入して
      panel_list[next_pos] = 0  #そのポジショんを0に変更
      panel_list[zero_pos] = n  #0の入っていたところに数字を入れる
      return panel_list

      #現在のパネルの位置によって0のパネルの位置を設定している
    if self.size > col + 1:
      next_pos = (col + 1) * self.size + raw
      panel_list = get_next_panel()
      yield tuple(panel_list)

    if col -1 >= 0:
      next_pos = (col -1) * self.size + raw
      panel_list = get_next_panel()
      yield tuple(panel_list)

    if self.size > raw + 1:
      next_pos = col * self.size + raw + 1
      panel_list = get_next_panel()
      yield tuple(panel_list)

    if raw - 1>0:
      next_pos = col * self.size + raw - 1
      panel_list = get_next_panel()
      yield tuple(panel_list)

  def result_print(self):
    for si in self.state_list:
      print(s)

def bfs(size, goal, panel_list):
  puzzle = Puzzle(panel_list, [], size)
  queue = queue(puzzle)
  checked_dict = {}

  for next_panel in puzzle.generate_next_panel(puzzle):
    next_puzzle = Puzzle(list(next_panel), puzzle.state_list[:], size)

    if next_panel in checked_dict:[@]
      continue

    if list(next_panel) == goal:
      return next_puzzle

    checked_dict[next_panel] = True
    queue.append(next_puzzle)

size = 3
goal =[1,2,3,4,5,6,7,8,0]
panel_list = [1,2,3,4,5,6,7,8,0]

puzzle = bfs(size, goal, panel_list)

puzzle.result_print()










