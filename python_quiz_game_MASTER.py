def user_tries():
    """
    Input:
        tries (int): Selected tries by the user.
    Behavior:
        User is prompted to enter maximum tries
    Return:
        A variable that contains the maximum tries entered by the user
    """
    entered_tries = int(input("Please enter maximum tries: "))
    return entered_tries
chosen_tries = user_tries()


game_data = {
   "easy": {
        "quiz": """A ___1___ is an error in a program.
The ___2___ function causes the Python interpreter to display a value on the screen.
A ___3___ is a set of instructions that specifies a computation.
An ___4___ loop is a loop which the terminating condition is never satisfied or for 
which there is no terminating condition.""",
        "answers": ["bug", "print", "program", "infinite"],
       "tries": chosen_tries,
       "blanks": ["___1___","___2___","___3___","___4___"]
    },
   'medium': {
        "quiz": """A ___1___ makes program smaller by eliminating repetitive codes.
A function that returns a value is widely called a ___2___ function.
A function that does not return a value is widely called a ___3___ function.
A ___4___ is used inside a function to refer to the value passed as an argument.""",
        "answers": ["function", "fruitful", "void", "parameter"],
       "tries": chosen_tries,
       "blanks": ["___1___","___2___","___3___","___4___"]
    },
   "hard": {
        "quiz": """An ___1___ is a general process for solving a category of problems.
The syntax for calling a function in another module by specifying the 
module name followed by a period and the function name is called a ___2___ notation.
The order in which statements are executed during a program run is called the flow of ___3___.
A variable used in a loop to add up or accumulate a result is called an ___4___ loop.""",
        "answers": ["algorithm", "dot", "execution", "accumulator"],
       "tries": chosen_tries,
       "blanks": ["___1___","___2___","___3___","___4___"]
    }
}


def choose_quiz():
    """
    Input:
        level (str): Selected level by the user.
    Behavior:
        User is prompted to enter a level
        If the user input is invalid
    Return:
        A dict mapping key to the corresponding game data depending on which level was chosen by the user.
    """
    entered_difficulty = input("Please select difficulty!\nPossible choices are: *easy* *medium* *hard*\n>>>").lower()
    while True:
        if entered_difficulty in game_data:
            return entered_difficulty
        print("\n**********Invalid Difficulty-Input!**********\n")
        entered_difficulty = input("Please select difficulty!\nPossible choices are: *easy* *medium* *hard*\n").lower()


def replace_blank(quiz, blanks, entered_answer):
    """
    Input:
        quiz (str): The quiz parahraph with blanks
        blanks (list(str)): The list of all the blanks in the quiz
        entered_answer (str): The correctly entered  answer to be filled in the quiz
    
    Behavior:
        Replaced the relvant blank in the quiz with the correct answer and returns the updated quiz.
    
    Return:
        quiz (str): The quiz updated with the correct answer
    """
    quiz = quiz.split() #split method to turn the string to a list for iteration purpose
    for blanks_space in quiz:
        if blanks_space in blanks:
            quiz = " ".join(quiz) #after iteration, join method to turn the list back to string for replacement purpose
            quiz = quiz.replace(blanks_space, entered_answer)
            print(quiz)
            break #break if blanks_space in blanks
    return quiz
    
        
def start_quiz():
    """
    Input:
        answer (str): Selected answer by user.
    Behavior:
        Depending on the given level it launches the main game logic.
        It checks the user entered answer.
        If the user guesses right the current blanks is replaced 
        with the right answer then the quiz is print.
        This process happens until all blanks are found.
        If the user guesses wrong, the user will be given another try.
        Try amount depends on chosen level
        If the user reaches the try maximum the game will end.
    Return:
        None.
    """
    chosen_quiz = choose_quiz()
    quiz = game_data[chosen_quiz]["quiz"]
    answers = game_data[chosen_quiz]['answers']
    tries = game_data[chosen_quiz]['tries']
    #blanks = game_data[chosen_quiz]["blanks"]
    print(quiz)
    for index, answer in enumerate(answers, 1):
        while tries > 0:
            entered_answer = input("\nWhat should substitute for __" + str(index) + "__?").lower()
            if entered_answer == answer:
                print("\n**********Correct!**********\n")
                quiz = quiz.replace("___" + str(index) + "___", entered_answer)
                print(quiz)
                #quiz = replace_blank(quiz, blanks, entered_answer)
                break #break if answer is correct
            else:
                #if answer is wrong, decrement by one
                tries -= 1
                # as long as tries is > 0 jump back to the loop
            if tries > 0: print ("\nWrong answer! You have " + str(tries) + " left! Please try again!")
            else: print("\nGAME OVER! You have run out of tries!")
                
start_quiz()
input("\nPress ENTER to exit")