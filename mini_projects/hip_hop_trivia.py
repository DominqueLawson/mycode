#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  If-Logic Script Mini Project"""


question_number = 0  # variable to hold the count of questions
answer = " "  # variable to hold the answer

# a variable for each question
question1 ="1. Who was the first rapper to get a grammy?"
question2 = "2. In what city was hip hop created?"
question3 = "3. What is O'Shea Jackson's rap name?"
question4 = "4. What hip hop duo created the movie Idlewild?"
question5 = "5. Which of the following record labels featured famous artists, such as Snoop Dogg, Dr. Dre, and Tupac?"

# variable for each answer
correct_answer1 = "Will Smith"
correct_answer2 = "New York City"
correct_answer3 = "Ice Cube"
correct_answer4 = "Outkast"
correct_answer5 = "Death Row"


# this function takes a question and it's correct answer to compare to the user input while giving the user 3 chance to get it correct
def trivia(question,correct_answer): 
    guess = 0
    while guess < 3:
        guess += 1
        answer = input(question)
        if answer == correct_answer: 
            print("Correct!")
            break
        elif guess == 3:    
            print("Sorry, the answer was", correct_answer)
            break
        else:                
            print("Sorry. Try again!")  
            
# while loop to get each question passed to an if statement which will call on the trivia function for the current question number information being passed to it as an argument
while question_number < 6:
    question_number += 1
    if question_number == 1:
        trivia(question1, correct_answer1)
    elif question_number == 2:
        trivia(question2, correct_answer2)
    elif question_number == 3:    
        trivia(question3, correct_answer3)
    elif question_number == 4:    
        trivia(question4, correct_answer4)
    elif question_number == 5:    
        trivia(question5, correct_answer5)
    else:
        print("Thanks for Playing Hip Hop Trivia, come back next week for more questions!!!!")    

