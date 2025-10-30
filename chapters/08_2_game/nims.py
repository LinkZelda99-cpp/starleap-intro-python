
def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over.  Player __ is the winner!"

    while pile > 0:
        # Player 1's turn
        valid_move = False
        while not valid_move:
            try:
                take = int(input(f"Player 1, there are {pile} stones left. How many do you take (1 to {min(max_stones, pile)})? "))
                if 1 <= take <= min(max_stones, pile):
                    pile -= take
                    valid_move = True
                else:
                    print(f"Invalid move. You must take between 1 and {min(max_stones, pile)} stones.")
            except ValueError:
                print("Please enter a valid number.")

        if pile == 0:
            print("Game over. Player 1 is the winner!")
            break

        # Player 2's turn
        valid_move = False
        while not valid_move:
            try:
                take = int(input(f"Player 2, there are {pile} stones left. How many do you take (1 to {min(max_stones, pile)})? "))
                if 1 <= take <= min(max_stones, pile):
                    pile -= take
                    valid_move = True
                else:
                    print(f"Invalid move. You must take between 1 and {min(max_stones, pile)} stones.")
            except ValueError:
                print("Please enter a valid number.")

        if pile == 0:
            print("Game over. Player 2 is the winner!")
            break
play_nims(10, 3)