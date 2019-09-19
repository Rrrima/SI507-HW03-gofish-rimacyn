from utils import Card,Hand,Deck

USER = {0:'Alice',1:'Bob'}
USER_NUM = 2
# give cards to p1 and p2
# paprameter: num of player,  default=2
# return: two hand objects for p1 and p2
def init_game(num=USER_NUM):
	my_deck = Deck()
	my_deck.shuffle()
	player_list = my_deck.deal(num,7)
	bookstatus = [[] for i in range(num)]
	return (my_deck,player_list,bookstatus)

# show cards in player1/player2's hands
# output 
# -----------------------
# Player A/B: You have cards:
# + str(Card)
# + str(Card)
# + ...
# -----------------------
# parameter: pindex: index of player
#             player_list: [hand1,hand2,...]
# return: None
def show_cards(pindex,player_list):
	player = player_list[pindex]
	for each in player.cards:
		print(each)

# parameter: bookstatus: list of books for each player;
# deck: current deck
def show_game_status(deck,player_list,bookstatus):
	print("+++++++++ CURRENT GAME STATUS +++++++++++")
	# print bookstatus
	for i in range(USER_NUM):
		print("Player {}: books:{}, #cards:{}"\
			.format(USER[i],bookstatus[i],len(player_list[i].cards)))
	print("#cards in deck:{}".format(len(deck.cards)))

# keep asking until get valid input
def ask_input(pindex):
	pass

def deal_with_query(player, queface):
	pass

def uodate_status():
	pass

def is_win(all_books):
	pass

def start_turn(pindex,my_deck,plyaer_list,bookstatus):
	show_game_status(my_deck,player_list,bookstatus)
	print("+++++++++++ {}'s turn +++++++++++++".format(USER[pindex]))
	show_cards(pindex,player_list)
	ask_input(pindex)

def play_gofish():
	init_game()
	while not is_win():
		start_turn()
		deal_with_query()
		update_states()
	return (winner,status)

if __name__ == "__main__":
	my_deck,player_list,bookstatus = init_game()
	start_turn(0,my_deck,player_list,bookstatus)




