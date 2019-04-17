class Cell:
    """
    cell of one-way list
    """
    def __init__(self, data): # コンストラクタ
        self.data = data
        self.next_pointer = None

class OnewayList:
    '''
    '''
    def __init__(self):  # コンストラクタ
        self.head = None

    def last(self):
        cell = self.head
        # 空の時
        if not cell:
            return None

        # 空でないとき
        while not cell.next_pointer == None:
            # 次のポインタが空になるまで
            cell = cell.next_pointer
        return cell

    def add(self, data):
    added_cell = Cell(data)
    last_cell = self.last()

    if not last_cell:
        self.head = added_cell
    else:
        last_cell.next_pointer = added_cell


    # def get_index_cell(self, index):
    #     '''
    #     if index=0, return head
    #     '''
    #     cell = self.head
    #     for i in range(index):
    #         cell = cell.next_pointer
    #     return cell



    # def insert(self, index, data):
    #     '''
    #     '''
    #     added_cell = Cell(data)

    #     # 先頭へ追加する場合
    #     if index == 0:
    #         added_cell.next_pointer = self.head
    #         self.head = added_cell
    #         return

    #     # indexへ追加する場合
    #     if index > 0:
    #         pre_cell = self.get_index_cell(index-1)
    #         next_cell = pre_cell.next_pointer

    #         pre_cell.next_pointer = added_cell
    #         added_cell.next_pointer = next_cell

    # def del_head(self):
    #     head_cell = self.head
    #     self.head = head_cell.next_pointer
    #     del head_cell

    # def delete(self, index):
    #     '''
    #     削除対象がnullでない前提
    #     '''
    #     if index == 0:
    #         self.del_head()
    #         return

    #     if index > 0:
    #         pre_cell = self.get_index_cell(index-1)
    #         del_target_cell = pre_cell.next_pointer
    #         next_cell = del_target_cell.next_pointer
    #         pre_cell.next_pointer = next_cell

    #         del del_target_cell



a = OnewayList()
a.add(50)
a.add(510)
a.add(0)
a.add(1)
a.add(40000)
# print(a.to_list())
# a.print()
print(a.get_index_cell(2))
