states = ('Rainy', 'Sunny')

observations = ('walk', 'shop', 'clean')

start_probability = {'Rainy': 0.6, 'Sunny': 0.4}

transition_probability = {
    'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
    }

emission_probability = {
    'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
    }

def forward_viterbi(y, X, sp, tp, ep):
    T = {}
    for state in X:
        ##          prob.      V. path  V. prob.
        T[state] = (sp[state], [state], sp[state])
        print("T[state]",T[state],"状態",state)
        print("状態",state)
        print('-'*20)
        print("\n")
    for output in y:
        U = {}
        print('-'*20)
        print('各観測結果をもとに計算',"観測結果","★★★★★★★★★★★",output,"★★★★★★★★★★★")
        print('T',T,"状態",state)
        for next_state in X:
            print("★★next_state★★",next_state)
            total = 0
            argmax = None
            valmax = 0
            for source_state in X:
                (prob, v_path, v_prob) = T[source_state]
                p = ep[source_state][output] * tp[source_state][next_state]
                prob *= p
                v_prob *= p
                total += prob
                print('★★★source_state★★★',source_state)
                print('**T[source_state]***',T[source_state])
                print('total：',total)
                print("v_prob（）：",v_prob)
                print("prob（初期状態から現在状態までの全経路の確率）：",prob)
                print("vpath(現在状態までのビタビ経路)",v_path)
                print('-'*10+"このソースループ終わり"+'-'*10)
                if v_prob > valmax:
                  argmax = v_path + [next_state]
                  valmax = v_prob
            U[next_state] = (total, argmax, valmax)
            print('U',U[next_state])
            print('-'*10+"このnext_state終わり"+'-'*10)
            print("\n")
            print("\n")
        T = U
    ## apply sum/max to the final states:
    total = 0
    argmax = None
    valmax = 0
    for state in X:
        (prob, v_path, v_prob) = T[state]
        total += prob
        if v_prob > valmax:
            argmax = v_path
            valmax = v_prob
    return (total, argmax, valmax)
print(observations)
print(forward_viterbi(observations,states,start_probability,transition_probability,emission_probability))
