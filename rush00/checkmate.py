def checkmate(text_board: str):
    board = [list(line.strip()) for line in text_board.strip().split('\n')]
    all_type = ('P', 'B', 'R', 'Q', 'K')
 
    # check กระดาน
    size = len(board)
    if (not board or not board[0]):
        return print("No chessboard.")

    for row in board:
        if len(row) != size:
            return print("Not a square board")

    # check K
    n = 0
    king_pos = None
    for i in range(size):
        for j in range(size):
            if (board[i][j] == 'K'):
                n+=1
                king_pos = i, j            
    
    if (n == 0):
        return print("King is not.")
    elif (n > 1):
        return print("King is more than 1.")
    
    k_y, k_x = king_pos

    # Checkmate Rook and Queen
    # ทิศบน
    for y in range(k_y - 1, -1, -1):
        cur = board[y][k_x]

        if cur not in all_type: continue

        if cur in ('R', 'Q'):
            print("Success")
            return
        break

    # ทิศล่าง
    for y in range(k_y + 1, size):
        cur = board[y][k_x]

        if cur not in all_type: continue

        if cur in ('R', 'Q'):
            print("Success")
            return
        break

    # ทิศขวา
    for x in range(k_x + 1, size):
        cur = board[k_y][x]

        if cur not in all_type: continue

        if cur in ('R', 'Q'):
            print("Success")
            return
        break

    # ทิศซ้าย
    for x in range(k_x - 1, -1, -1):
        cur = board[k_y][x]

        if cur not in all_type: continue

        if cur in ('R', 'Q'):
            print("Success")
            return
        break

    # Checkmate Bishop and Queen
    # ทแยงซ้ายบน
    for i in range(1, size):
        y, x = k_y - i, k_x - i
        if not (0 <= y < size and 0 <= x < size): break
        cur = board[y][x]
        if cur not in all_type: continue
        if cur in ('B', 'Q'):
            print("Success")
            return
        break

    # ทแยงขวาบน
    for i in range(1, size):
        y, x = k_y - i, k_x + i
        if not (0 <= y < size and 0 <= x < size): break
        cur = board[y][x]
        if cur not in all_type: continue
        if cur in ('B', 'Q'):
            print("Success")
            return
        break

    # ทแยงซ้ายล่าง
    for i in range(1, size):
        y, x = k_y + i, k_x - i
        if not (0 <= y < size and 0 <= x < size): break
        cur = board[y][x]
        if cur not in all_type: continue
        if cur in ('B', 'Q'):
            print("Success")
            return
        break

    # ทแยงขวาล่าง
    for i in range(1, size):
        y, x = k_y + i, k_x + i
        if not (0 <= y < size and 0 <= x < size): break
        cur = board[y][x]
        if cur not in all_type: continue
        if cur in ('B', 'Q'):
            print("Success")
            return
        break

    # Checkmate Pawn
    p_y = k_y + 1
    if p_y < size:
        for p_x in [k_x - 1, k_x + 1]:
            if (0 <= p_x < size):
                if board[p_y][p_x] == 'P':
                    print("Success")
                    return
                
    print("Fail")
    return