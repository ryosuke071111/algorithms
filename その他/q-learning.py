#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import random

# "S": Start地点, "#": 壁, "数値": 報酬
RAW_Field = """
#,#,#,#,#,#,#
#,S,0,0,-10,0,#
#,0,-10,0,0,0,#
#,0,-10,0,-10,0,#
#,0,0,0,-10,0,#
#,0,-10,0,0,100,#
#,#,#,#,#,#,#
"""


# 定数
ALPHA = 0.2 # LEARNING RATIO
GAMMA  = 0.9 # DISCOUNT RATIO
E_GREEDY_RATIO = 0.2
LEARNING_COUNT = 1000


class Field(object):
        """ Fieldに関するクラス """

        def __init__(self, raw_field=RAW_Field):
                self.raw_field = raw_field
                self.set_field_data()
                self.start_point = self.get_start_point()

        def set_field_data(self):
                """ 文字列のfieldデータ(raw_field)を2次元配列(field_data)に格納 """
                self.field_data = []
                for line in self.raw_field.split("\n"):
                        if line.strip() != "":
                                self.field_data.append(line.split(","))

        def display(self, point=None):

                """ Fieldの情報を出力する. """
                field_data = copy.deepcopy(self.field_data)
                if not point is None:
                        x, y = point
                        field_data[y][x] = "@"
                else:
                        point = ""
                # print "----- Dump Field: %s -----" % str(point)
                # for line in field_data:
                #         print "\t" + "%3s " * len(line) % tuple(line)

        def get_actions(self, point):
                """ 引数で指定した座標から移動できる座標リストを獲得する. """
                x, y = point
                if self.field_data[y][x] == "#": sys.exit("Field.get_actions() ERROR: 壁を指定している.(x, y)=(%d, %d)" % (x, y))
                around_map = [(x, y-1), (x, y+1), (x-1 , y), (x+1, y)]
                return [(_x, _y) for _x, _y in around_map if self.field_data[_y][_x] != "#"]

        def get_val(self, point):
                """ 指定した座標のfieldの値を返す. エピソード終了判定もする. """
                x, y = point
                try:
                         v = float(self.field_data[y][x])
                         if v == 0.0: return v, False
                         else: return v, True
                except ValueError:
                        if self.field_data[y][x] == "S": return 0.0, False # start地点の時
                        sys.exit("Field.get_val() ERROR: 壁を指定している.(x, y)=(%d, %d)" % (x, y))

        def get_start_point(self):
                """ Field中の Start地点:"S" の座標を返す """
                for y, line in enumerate(self.field_data):
                        for x, v in enumerate(line):
                                if v == "S":
                                        return (x, y)
                sys.exit("Field.set_start_point() ERROR: FieldにStart地点がありません.")


class QLearning(object):
        """ class for Q Learning """

        def __init__(self, map_obj):
                self.Qvalue = {}
                self.Field = map_obj

        def learn(self, greedy_flg=False):
                """ 1エピソードを消化する. """
                state = self.Field.start_point
                #print "----- Episode -----"
                while True:
                        if greedy_flg:
                                action = self.choose_action_greedy(state)
                                self.Field.display(action)
                                print "\tstate: %s -> action:%s\n" % (state, action)
                        else: #default (Learning Mode)
                                action = self.choose_action(state)
                        if self.update_Qvalue(state, action):
                                break # finish this episode
                        else:
                                state = action # continue

        def update_Qvalue(self, state, action):
                """ Q値の更新を行う. """
                # 更新式:
                #       Q(s, a) <- Q(s, a) + alpha * {r(s, a) + gamma max{Q(s`, a`)} -  Q(s,a)}
                #               Q(s, a): 状態sにおける行動aを取った時のQ値      Q_s_a
                #               r(s, a): 状態sにおける報酬      r_s_a
                #               max{Q(s`, a`) 次の状態s`が取りうる行動a`の中で最大のQ値 mQ_s_a)
                Q_s_a = self.get_Qvalue(state, action)
                mQ_s_a = max([self.get_Qvalue(action, n_action) for n_action in self.Field.get_actions(action)])
                r_s_a, finish_flg = self.Field.get_val(action)
                # calculate
                q_value = Q_s_a + ALPHA * ( r_s_a +  GAMMA * mQ_s_a - Q_s_a)
                # update
                self.set_Qvalue(state, action, q_value)
                return finish_flg


        def get_Qvalue(self, state, action):
                """ Q(s,a)を取得する. s:state, a:action """
                try:
                        return self.Qvalue[state][action]
                except KeyError:
                        return 0.0

        def set_Qvalue(self, state, action, q_value):
                """ Q値に値を代入する. """
                self.Qvalue.setdefault(state,{})
                self.Qvalue[state][action] = q_value

        def choose_action(self, state):
                """ e-greedy法で行動を決める. """
                if E_GREEDY_RATIO < random.random():
                        #ランダムに行動選択
                        return random.choice(self.Field.get_actions(state))
                else:
                        # greedy法を適用する
                        return self.choose_action_greedy(state)

        def choose_action_greedy(self, state):
                """ greedy法で行動を決める. Q(s,a)の観点から選択. """
                best_actions = []
                max_q_value = -1
                for a in self.Field.get_actions(state):
                        q_value = self.get_Qvalue(state, a)
                        if q_value > max_q_value:
                                best_actions = [a,]
                                max_q_value = q_value
                        elif q_value == max_q_value:
                                best_actions.append(a)
                return random.choice(best_actions) # Q値の最大値が複数存在する場合はその中からランダムに選択

        def dump_Qvalue(self):
                """ Q値をdumpする. """
                print "##### Dump Qvalue #####"
                for i, s in enumerate(self.Qvalue.keys()):
                        for a in self.Qvalue[s].keys():
                                print "\t\tQ(s, a): Q(%s, %s): %s" % (str(s), str(a), str(self.Qvalue[s][a]))
                        if i != len(self.Qvalue.keys())-1: print '\t----- next state -----'


if __name__ == "__main__":

        # display Field information
        Field().display()
        # create QLearning object
        QL = QLearning(Field())
        # Learning Phase
        for i in range(LEARNING_COUNT):
                QL.learn() # Learning 1 episode
        # After Learning
        QL.dump_Qvalue() # Q値出力
        QL.learn(greedy_flg=True) # 学習結果をgreedy法で行動選択させてみる


# End of File #
