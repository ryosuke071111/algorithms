#!/usr/bin/python
# coding: UTF-8

#import
import numpy as np #入力整数列Aの生成に使用

class Node:
    def __init__(self, data): #コンストラクタ
        self.data = data #ノードがもつ数値
        self.left = None #左エッジ
        self.right = None #右エッジ


class BST:
    def __init__(self, number_list): #コンストラクタ
        self.root = None #ルートノード初期化
        for node in number_list: #数値を持つ配列から二分木を生成
            self.insert(node) #挿入メソッドを使ってノードを挿入する
    #挿入
    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.data
                if data < entry:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data = data
                    return
    #検索機能(インターフェース)
    def search(self, search):
        searcher = self._search_bool(search)
        if searcher is None:
            print("Search target is not found.")
        elif searcher == True:
            print(str(search) + " is found!")
        elif searcher == False:
            print(str(search) + " is not found.")

    #検索機能本体(出力:boolean),深さ優先探索
    #nodeのvisitedはpopで代用
    def _search_bool(self, search):
        n = self.root
        if n is None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                print(node.data)
                if node.data == search:
                    return True
                if node.left is not None:
                    lst.append(node.left)
                if node.right is not None:
                    lst.append(node.right)

            return False

    def inorder(self,node): #中順探索 l->r->p^n
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

num = [60, 10, 50, 14, 9, 54, 57, 60, 53, 8, 9, 0, 70, 100]
print(num)
a = BST(num)
a.insert(9999)
print(str(a.root.data)+"が頂点の数字！")
# print(a.root.left.left.data)
# print(a.root.left.left.left.data)
a.search(100)
# print(lst)
# print(a.root.left.left.left.left.data)
# print(a.root.left.left.left.left.left.data)
# print(a.search(999999))

