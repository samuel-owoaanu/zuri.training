from random import choice as rand_choice

game_db = [
    'R',
    'P',
    'S'
]

winning_scheme={
    'R' : {
        'R' : 0.5,
        'P' : 0,
        'S' : 1,
    },
    'P' : {
        'R' : 1,
        'P' : 0.5,
        'S' : 0,
    },
    'S' : {
        'R' : 0,
        'P' : 1,
        'S' : 0.5,
    },
}

def decide_winner(player_score, cpu_score):
    if player_score > cpu_score:
        return '!!! Player wins !!!'
    if player_score < cpu_score:
        return '!!! CPU wins !!!'
    else:
        return 'You tied!'

def get_cpu_choice() -> str:
    return rand_choice(game_db)
    
def get_player_choice() -> str:
    player_input = input("Pick an option between \n'R - for rock' \n'P - for paper' \n'S - for scissors' \n'Q - for quit' \n\n>>")
    player_input = player_input.upper()
    if player_input == 'R':
        return 'R'
    elif player_input == 'P':
        return 'P'
    elif player_input == 'S':
        return 'S'
    elif player_input == 'Q':
        return 'Q'
    else:
        return 'error'

def get_cpu_score(player_choice, cpu_choice):
    return winning_scheme[cpu_choice][player_choice]
    

def get_player_score(player_choice, cpu_choice):
    return winning_scheme[player_choice][cpu_choice]

def print_moves(player_choice, cpu_choice):
    name_db ={
        'R' : 'Rock',
        'P' : 'Paper',
        'S' : 'Scissors'
    }
    return f"\nPlayer ({name_db[player_choice]}) : CPU ({name_db[cpu_choice]})"
    
def start_game():
    
    player_input = ''
    while player_input.upper() != 'Q':   
        print("--- Rock Paper Scissors ---")
        print("---- Play against CPU ----\n")
        
        player_input = get_player_choice()
        cpu_choice = get_cpu_choice()
        if player_input.upper() == 'Q':
            break
        elif player_input == 'error':
            print('your input is invalid, try again \n\n')
            continue
        
        player_score = get_player_score(player_input, cpu_choice)    
        cpu_score = get_cpu_score(player_input, cpu_choice)
        
        print(print_moves(player_input, cpu_choice))
        print(decide_winner(player_score, cpu_score), "\n\n")
        
    print("Thanks for playing my Game :) \n")
    
    
start_game()