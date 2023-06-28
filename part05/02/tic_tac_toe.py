# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
	if x > 2 or y > 2:
		return False
	if x < 0 or y < 0:
		return False
	if game_board[y][x] != '':
		return False
	if piece != "X" and piece != 'O':
		return False
	game_board[y][x] = piece
	return True
