def forward_viterbi(y, X, sp, tp, ep):
    T = {}
    for state in X:
        ##          prob.      V. path  V. prob.
        T[state] = (sp[state], [state], sp[state])
    for output in y:
        U = {}
        for next_state in X:
            total = 0
            argmax = None
            valmax = 0
            for source_state in X:
                (prob, v_path, v_prob) = T[source_state]
                p = ep[source_state][output] * tp[source_state][next_state]
                prob *= p
                v_prob *= p
                total += prob
                if v_prob > valmax:
                    argmax = v_path + [next_state]
                    valmax = v_prob
            U[next_state] = (total, argmax, valmax)
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
