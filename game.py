from IPython.display import clear_output

'''
Global variables
'''
ready = 'N'
counter = 1
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
(p1,p2) = ('','')

def welcome():
    '''
    Print welcome message
    '''
    print('Welcome to Tic Tac Toe!')
    start()

def start():
    '''
    Seperate player1 and player2 inputs
    '''
    global ready
    global p1,p2
    p1 = input('Player 1: Do you want to be X or O? ').upper()
    if p1 == 'X':
        p1,p2 = ('X','O')
    else:
        p1,p2 = ('O','X')
    print('Player1 will go first.')
    ready = input('Are you ready to play? Enter Y or N? ').upper()
    get_input()

def get_input():
    '''
    Get board position as inputs from players
    '''
    global board
    global ready
    if ready == 'Y':
        while True:
            try:
                inp = int(input('\nChoose your next position (1-9) : '))
                break
            except:
                print('Error in input value.Try again!')
        if check_available_cell(inp):
            draw_board(inp = inp)
        else:
            print('The cell is already filled.')
            get_input()
    else:
        ready = input('Are you ready to play? Enter Y or N? ').upper()
        get_input()
        
def draw_board(inp):
    '''
    Draw the board as per the inputs from the playes
    '''
    global board
    global counter        
    next_inp = ''
    play_again = 'N'
    if counter % 2 == 1:
        board[inp] = p1
    else:
        board[inp] = p2
    counter += 1
    clear_output()
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    if check_win() == True:
        print('We have a winner')
        play_again = input('Do you want to play again? Enter Y or N : ').upper()
    elif check_match_drawn() == True:
        print('Match drawn.')
        play_again = input('Do you want to play again? Enter Y or N : ').upper()
    else:
        get_input()
    if play_again == 'Y':
        replay()
    else:
        clear_output()
        print('Goodbye!!!')
        
def check_available_cell(inp):
    '''
    Check whether player input cell is empty
    '''
    if board[inp] == ' ':
        return True
    else:
        False
        
def check_match_drawn():
    blank_cell_count = 0
    for cell in board:
        if cell == ' ':
            blank_cell_count += 1
    if blank_cell_count == 0:
        return True
    else:
        return False
    
def check_win():
    '''
    Check for winning options for a player
    '''
    if board[1]==board[2]==board[3]=='X' or board[1]==board[2]==board[3]=='O':
        return True
    elif board[4]==board[5]==board[6]=='X' or board[4]==board[5]==board[6]=='O':
        return True
    elif board[7]==board[8]==board[9]=='X' or board[7]==board[8]==board[9]=='O':
        return True
    elif board[1]==board[5]==board[9]=='X' or board[1]==board[5]==board[9]=='O':
        return True
    elif board[7]==board[5]==board[3]=='X' or board[7]==board[5]==board[3]=='O':
        return True
    elif board[1]==board[4]==board[7]=='X' or board[1]==board[4]==board[7]=='O':
        return True
    elif board[2]==board[5]==board[8]=='X' or board[2]==board[5]==board[8]=='O':
        return True
    elif board[3]==board[6]==board[9]=='X' or board[3]==board[6]==board[9]=='O':
        return True
    else:
        return False
    
def replay():
    '''
    When players want to replay
    '''
    global ready 
    global counter
    global board
    global p1,p2
    ready = 'N'
    counter = 1
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    (p1,p2) = ('','')
    start()