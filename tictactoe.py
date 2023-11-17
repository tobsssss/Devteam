def tic_tac_toe(board):
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result = "NO WINNER"
    def boom(line):
        check = set()
        for a in line:
            check.add(a)
        if len(check) == 1:
            wincombo = list(check)
            if wincombo[0] != "":
                return(str(wincombo[0]))
    for hori in board:
        if boom(hori) != None:
            result = boom(hori)
    for vert in list(zip(*board)):
        if boom(vert) != None:
            result = boom(vert)
    updolist = []
    for u in range(len(board)):
        updolist.append(board[u][u])
    if boom(updolist) != None:
            result = boom(updolist)
    duplist = []
    for d in range(len(board)):
        duplist.append(board[len(board)-1-d][d])
    if boom(duplist) != None:
            result = boom(duplist)
    return result
