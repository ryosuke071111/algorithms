def tower_of_hanoi(n, from_stack, to_stack, tmp):
    """
    from_stackからto_stackへディスクを動かす。
    """
    if n == 1:
        # 1枚の円盤なら移して返す
        print(f"Move {n} disk from {from_stack} to {to_stack}.")
        return
    # 上からn-1番目の円盤をAからCへ、Bを中間に使う
    tower_of_hanoi(n-1, from_stack, tmp, to_stack)
    # 残りの円盤をAからCへ
    print(f"Move {n} disk from {from_stack} to {to_stack}.")
    # 上からn-1番目の円盤をBからCへ、Aを中間に使う
    tower_of_hanoi(n-1, tmp, to_stack, from_stack)

tower_of_hanoi(10, "A", "C", "B")
