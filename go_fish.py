from utils import Card,Hand,Deck
import random
USER_NUM = random.choice([2,3,4])
USER = {0:'Alice',1:'Bob',2:'Amy',3:'John'}
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
	print("++++++++++++++++++++++++++++++++++++++++++++ CURRENT GAME STATUS ++++++++++++++++++++++++++++++++++++++++++++")
	# print bookstatus
	for i in range(USER_NUM):
		print("Player {}: books:{}, #cards:{}"\
			.format(USER[i],bookstatus[i],len(player_list[i].cards)))
	print("#cards in deck:{}".format(len(deck.cards)))

def is_valid_que(queface,pcards):
	if (queface in range(1,14)) and \
		(queface in [each.rank_num for each in pcards]):
			return True
	else:
		return False


def get_next_player(pindex):
	return (pindex+1)%USER_NUM

# keep asking until get valid input
# parameter: pcard: the in hand cards for current player
def ask_input(pindex,pcards):
	choices = [card.rank_num for card in pcards]
	return random.choice(choices)

def deal_with_query(pindex, hand_que, hand_ans, queface, deck):
	if queface in [each.rank_num for each in hand_ans.cards]:
		hand_over_cards = hand_ans.hand_over(queface)
		for each in hand_over_cards:
			hand_que.add_card(each)
		next_turn = get_next_player(pindex)
	else:
		print("go fish!")
		drew_card = deck.pop_card()
		hand_que.add_card(drew_card)
		if drew_card.rank_num == queface:
			next_turn = pindex
		else:
			next_turn = get_next_player(pindex)
	return next_turn

def has_books(hand):
	books = []
	cards = hand.cards
	all_nums = [each.rank_num for each in cards]
	for i in range(1,14):
		if all_nums.count(i)==4:
			books.append(i)
	return books


def is_win(hand_list,bookstatus,deck):
	# print(len(hand_list[0].cards),'  ',len(hand_list[1].cards))
	for each in hand_list:
		#print(len(each.cards))
		if len(each.cards)==0:
			show_game_status(deck,hand_list,bookstatus)
			return (bookstatus.index(max(bookstatus))+1)
	if len(deck.cards) == 0:
		show_game_status(deck,hand_list,bookstatus)
		return (bookstatus.index(max(bookstatus))+1)
	return 0

def update_status(bookstatus, hand_index, hand):
        the_books = has_books(hand)
        if len(the_books)>0:
                bookstatus[hand_index].extend(the_books)
                hand.remove_books(the_books)

def start_turn(pindex,my_deck,player_list,bookstatus):
	show_game_status(my_deck,player_list,bookstatus)
	print("+++++++++++ {}'s turn +++++++++++++".format(USER[pindex]))
	show_cards(pindex,player_list)
	queface = ask_input(pindex,player_list[pindex].cards)
	return queface

def play_gofish():
	my_deck,player_list,bookstatus = init_game()
	pindex = 0
	while not is_win(player_list,bookstatus,my_deck):
		queface = start_turn(pindex,my_deck,player_list,bookstatus)
		aindex = get_next_player(pindex)
		hand_que = player_list[pindex]
		hand_ans = player_list[aindex]
		next_turn = deal_with_query(pindex,hand_que,hand_ans,queface,my_deck)
		update_status(bookstatus,pindex,hand_que)
		update_status(bookstatus,aindex,hand_ans)
		pindex = next_turn

	print("+++++++++++++++ GAME OVER +++++++++++++++")
	print("{} wins the game with {} books".format(USER[is_win(player_list,bookstatus,my_deck)-1],max(bookstatus)))

if __name__ == "__main__":
	play_gofish()



