import random
tools = ['Rock','Paper','Scissors']
def rules():
    print("Winning rules of the game ROCK PAPER SCISSORS are:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

def user_choose_tool():
    print("Choose between : ")
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')
    while True:
        choice = input('Enter your choice: ')
        try:
            choice = int(choice)
            if 0 < choice < 4:
                tool = tools[choice-1]
                print(f'User choice is : {tool}')
                return tool
            else: 
                print('Enter a valid input (1 / 2 / 3)')
        except ValueError:
            print('Enter a valid input (1 / 2 / 3)')

def computer_choose_tool():
    computer_tool_index = random.randint(1,3)
    computer_tool = tools[computer_tool_index-1]
    print("\nNow it's Computer's Turn...")
    print(f"Computer choice is: {computer_tool}")
    return computer_tool

def play_round():
    if user_tool == computer_tool:
        print("<== It's a tie ! ==>")
    elif user_tool == 'Rock':
        if computer_tool == 'Scissors':
            print('<== Player wins! ==>')
        elif computer_tool == 'Paper':
            print('<== Computer wins! ==>')
    elif user_tool == 'Paper':
        if computer_tool == 'Rock':
            print('<== Player wins! ==>')
        elif computer_tool == 'Scissors':
            print('<== Computer wins! ==>')
    elif user_tool == 'Scissors':
        if computer_tool == 'Paper':
            print('<== Player wins! ==>')
        elif computer_tool == 'Rock':
            print('<== Computer wins! ==>')

def start_new_game():
    while True:
        restart = input('\nDo you want to play again? (Y/N)\n')
        if restart.isalpha():
            restart = restart.upper()
            if restart == 'Y':
                user_tool = user_choose_tool()
                computer_tool = computer_choose_tool()
                print(f'{user_tool} vs {computer_tool}')
                play_round()
            elif restart == 'N':
                print('Thanks for playing!')
                break
            else:
                print('Enter a valid input')
# Implement
rules()
user_tool = user_choose_tool()
computer_tool = computer_choose_tool()
print(f'\n{user_tool} vs {computer_tool}\n')
play_round()
start_new_game()
