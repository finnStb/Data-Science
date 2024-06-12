import random
import logging

def simulation_1_dice():
    """
    1. with a unfair dice, the probability of point 2 is twice than point 1,
    probability of point 3 is triple than point 1, and so on.
    What is the expected value and variance of this dice? -8 pt

    P(⚁) = 2 * P(⚀)
    P(⚂) = 3 * P(⚀)
    P(⚃) = 4 * P(⚀)
    P(⚄) = 5 * P(⚀)
    P(⚅) = 6 * P(⚀)

    A die has 6 sides, so the sum of all probabilities should be 1.0.
    ==> P(⚀) + P(⚁) + P(⚂) + P(⚃) + P(⚄) + P(⚅) = 1.0    | insert the relative values of P(⚁), P(⚂), P(⚃), P(⚄), P(⚅)
    <=> P(⚀) + 2 * P(⚀) + 3 * P(⚀) + 4 * P(⚀) + 5 * P(⚀) + 6 * P(⚀) = 1.0
    <=> 21 * P(⚀) = 1.0
    <=> P(⚀) = 1 / 21

    Insert the values of P(⚀) to the equations of P(⚁), P(⚂), P(⚃), P(⚄), P(⚅)
    ==> P(⚁) = 2 / 21
    ==> P(⚂) = 3 / 21
    ==> P(⚃) = 4 / 21
    ==> P(⚄) = 5 / 21
    ==> P(⚅) = 6 / 21
    """

    # calculate the expected value
    expected_value = 1 * 1/21 + 2 * 2/21 + 3 * 3/21 + 4 * 4/21 + 5 * 5/21 + 6 * 6/21
    print(f"Expected value: {expected_value}")  # 4.333333333333333

    # calculate the variance
    variance = (1 - expected_value) ** 2 * 1 / 21 + (2 - expected_value) ** 2 * 2 / 21 + (3 - expected_value) ** 2 * 3 / 21 + (4 - expected_value) ** 2 * 4 / 21 + (5 - expected_value) ** 2 * 5 / 21 + (6 - expected_value) ** 2 * 6 / 21
    print(f"Variance: {variance}")  # 2.2222222222222223


def simulation_2_monty_hall(number_of_experiment: int, log_prints: bool = False):
    """
    2. write a python / R function to simulate the Goat-car door open problem (Monty Hall problem) 100 times.
    write the conclusion and what do you think? -15pt

    Input: number of experiment
    output:     1. the success time if you change
                 2. the success time if you do not change

    Monty Hall problem:
    - a game where the player is shown three doors; behind one is a car and behind the other two are goats.
    1. The player picks a door.
    2. The host, who knows what is behind the doors, opens one of the remaining doors which has a goat.
    3. The player is given the option to switch to the other unopened door.
    4. The player wins what is behind the door they choose.
    """

    # Set up logging
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')  # INFO, DEBUG

    games_played = 0
    games_won = 0

    for i in range(10000):
        logging.debug(f"Game {i + 1}")

        # create a list of 3 doors with 2 goats and 1 car, in random order
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        logging.debug(f"[Secret] Doors: {doors}")

        # 1. The player picks a door
        player_choice = random.choice(range(3))
        logging.debug(f"Player chooses door: {player_choice} ({doors[player_choice]})")

        # 2. The host opens one of the remaining doors which has a goat
        random_goat_door = random.choice([i for i in range(3) if i != player_choice and doors[i] == 'goat'])
        doors[random_goat_door] = 'opened'
        logging.debug(f"[Opened] Doors: {doors}")

        # 3. The player is given the option to switch to the other unopened door
        # (number of experiment: 1 = change, 2 = not change)
        if number_of_experiment == 1:
            player_choice = [i for i in range(3) if i != player_choice and doors[i] != 'opened'][0]

        # 4. The player wins what is behind the door they choose
        if doors[player_choice] == 'car':
            games_won += 1
        games_played += 1

    logging.info(f"Games played: {games_played}")
    logging.info(f"Games won: {games_won}")
    logging.info(f"Win rate: {games_won / games_played * 100:.2f}%")

    """
    discussion:
    - The probability of winning the car if you change the door is 2/3 or about 66.67%.
    - The probability of winning the car if you do not change the door is 1/3 or about 33.33%.
    This is due to the host revealing a goat door, no matter if the player initially chose the car or a goat. 
    
    Think about it this way:
    Staying on the initial door is equivalent to choosing one door out of three where only one door has a car, 
    while switching is equivalent to choosing one door out of three where two doors have a car.
    """


# 3. - 6 and 12 sided dice
    """
    3. I have a bag in front of me containing a
    6-sided die (with number 1 to 6) and a 12-sided die (with number 1 to 12).
    My friend pulls one out at random, rolls it once, and tells me that the number is 5.
    What is the probability that my friend pulled out the 6-sided die? -7pt

    I like to solve these kind of conditional probability problems using a conditional probability table:
    Events:
    6sd = 6-sided die
    12sd = 12-sided die
    5 = number 5 is rolled
    not5 = number 5 is not rolled

    So we can already say:
    P(6sd) = 1/2
    P(12sd) = 1/2
    P(5 | 6sd) = 1/6
    P(not5 | 6sd) = 5/6
    P(5 | 12sd) = 1/12
    P(not5 | 12sd) = 11/12

    Creating the table using multiplication of the probability values above:
    |      | 5    | not5  |     |
    |------|------|-------|-----|
    | 6sd  | 1/12 | 5/12  | 1/2 |
    | 12sd | 1/24 | 11/24 | 1/2 |
    |      | 3/24 | 21/24 | 1   |

    P(6sd | 5) = P(6sd and 5) / P(5) = (1/12) / (3/24) = 2/3 = 66.66667%
    P(12sd | 5) = P(12sd and 5) / P(5) = (1/24) / (3/24) = 1/3 = 33.33333%

    So to answer the question:
    the probability that my friend pulled out the 6-sided die given that the number 5 is rolled is 66.66667%.
    """



    """
    4. Romeo and Juliet would like to meet.
    Romeo will pick a random time between 9:00- 10:00 and Juliet pick a random time between 9:30 - 10:00  independently
    and waits for the other for 10 minutes and leave if they don't see the other.
    What is the probability that the two will meet? - bonus 10pt
    
    While trying to solve this problem, I realized that this problem can be solved using an area visualization.
    For easier reading, I simplified the problem to a 60 minute time frame, so Romeo arrives between 0 and 60 minutes,
    and Juliet between 30 and 60 minutes.
    
    Take a look at the visualization in "romeo and juliet.png" now, please.
    
    Without the question if the two would meet, there is an area 60 min * 30 min = 1800 min^2, which represents the 
    total possibilities of the arriving times of the two, which are not quantised but fluid, which is why I used an 
    area.
    
    In this area, there is a smaller area inside which represents the possibilities of the two meeting. Any point in 
    this "meet area" has an arriving time <= 10 minutes than the other. It doesn't matter which one arrives first, 
    as long as the other arrives within 10 minutes. In the png sketch, it is the blue and yellow area. 
    This area can be counted and is 550 min^2 in size.
    So: P(meeting) = (550 min^2) / (1800 min^2) = 0.3055555555 = 30.555555555%

    """








if __name__ == '__main__':
    simulation_1_dice()
    # simulation_2_monty_hall(1, log_prints=False)
