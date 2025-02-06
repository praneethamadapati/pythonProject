def wordSearch(board, word):
    if not word:
        return False
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            for character in word:
                if character ==

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(wordSearch(board, word))