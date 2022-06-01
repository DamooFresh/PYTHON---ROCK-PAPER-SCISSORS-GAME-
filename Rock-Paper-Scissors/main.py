while True:
    game = ['R', 'P', 'S']
    words = ['rock', 'paper', 'scissors']
    letters = ['R', 'P', 'S']
    guess = input('pick an option between \"R\",\"P\" or \"S\": ')
    guess = guess.upper()
    
    if guess in letters:

        if guess == letters[0]:
            print(f"you pick {words[0]}")
        elif guess == letters[1]:
            print(f"you pick {words[1]}")
        elif guess == letters[2]:
            print(f"you pick {words[2]}")

        import random

        computer_option = random.choice(letters)
        if computer_option == letters[0]:
         print(f"Computer pick {words[0]}")

        elif computer_option == letters[1]:
         print(f"Computer pick {words[1]}")
        
        elif computer_option == letters[2]:
         print(f"Computer pick {words[2]}")

        
        if guess == 'R' and computer_option == 'S':
            print('Congratulations you win. Game Over!')

        elif computer_option == 'R' and guess == 'S':
            print('Computer wins. Game Over!')

        if guess == 'S' and computer_option == 'P':
            print('Congratulations you win. Game Over!')

        elif computer_option == 'S' and guess == 'P':
            print('Computer wins. Game Over!')

        if guess == 'P' and computer_option == 'R':
            print('Congratulations you win. Game Over!')
        
        elif computer_option == 'P' and guess == 'R':
            print('Computer wins. Game Over!')

        if guess == computer_option:
            print("\"It's\" a Tie. Kindly restart the game!")
                
        break
    
    else:
        print("Invalid option😥😥 Try again")
