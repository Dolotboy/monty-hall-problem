import random

def generate_doors():
    doors = [0, 0, 1] 
    random.shuffle(doors)

    print(doors)
    return doors

def participate(doors, keep_door):
    initial_choice = random.randint(0, 2)
    print(f"You chose door #{initial_choice + 1}")

    presenter_choice = random.choice([i for i in range(len(doors)) if i != (initial_choice) and doors[i] == 0])
    print(f"Presenter openned the door #{presenter_choice + 1} and it's empty")

    final_result = 0
    if keep_door:
        final_result = doors[initial_choice] 
    else:
        new_choice = random.choice([i for i in range(len(doors)) if i != (initial_choice) and i != (presenter_choice)])
        final_result = doors[new_choice]
    
    if final_result == 1:
        print("You won")
    else:
        print("You lost")

    return final_result

def main():
    print("Monty Hall Problem")
    results_keep = []
    results_change = []
    nbr_of_game = 1000
    for i in range(nbr_of_game):
        doors = generate_doors()
        results_keep.append(participate(doors, True))
        results_change.append(participate(doors, False))

    print("On a total of "+ str(nbr_of_game) +" game, by keeping the same door, you won " + str(results_keep.count(1)) + " times")
    print("On a total of "+ str(nbr_of_game) +" game, by changing the door, you won " + str(results_change.count(1)) + " times")

if __name__ == "__main__":
    main()