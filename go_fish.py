from utils import Card,Hand,Deck

# give cards to p1 and p2
# paprameter: num of player,  default=2
# return: two hand objects for p1 and p2
def init_game():
	pass


# show cards in player1/player2's hands
# output 
# -----------------------
# Player A/B: You have cards:
# + str(Card)
# + str(Card)
# + ...
# -----------------------
# paprameter: {'pa','pb'}
# return: None

def show_cards(player):
	pass

def show_game_status():
	pass

def ask_input():
	pass

def deal_with_query():
	pass

def uodate_statis():
	pass

def is_win():
	pass

def start_turn():
	show_game_status()
	show_cards()
	ask_input()

def play_gofish():
	init_game();
	while not is_win():
		start_turn()
		deal_with_query()
		update_states()
	return (winner,states)

if __name__ == "__main__":
	(winner,states) = play_gofish()
	print(winner,states)




