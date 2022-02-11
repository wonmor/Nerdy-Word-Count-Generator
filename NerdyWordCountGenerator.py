# PySimpleGUI is an API that implements GUI to a python script with ease
import PySimpleGUI as sg

# ---------------------
# Nerdy Word Count Generator
# For ICS3U1 - Grade 11 Intro. to Computer Programming
# Offered Under Garth Webb Secondary School
# Written by John Seong
#
# Works Cited
# My Head, 2022, My Head Publishing Company
# ---------------------

# Apply a system-wide theme to the program
sg.theme('SystemDefaultForReal')

# Button press counter
pressCount = 0

# A list that stores all the answers
answers = []

# A dictionary that stores all the questions
quest = {
    0: 'What is your name?',
    1: 'What is your favourite subject?',
    2: 'Who is your favourite teacher?',
    3: 'What country do you reside in?',
    4: 'What is the most disgusting object you can ever think of?'
}

# A function that generates a parargraph using the variables that contain user's input
def GenerateText():
    # A global variable that stores the word count
    global wordCount
    # Remove periods from the name of the teacher as it may potentially cause unintentional line breaks
    answers[2] = answers[2].replace('.', '')
    # Paragraph string variable utilizing the f-string method
    paragraph = f'I, {answers[0]}, would like to introduce {answers[2]} to explain the concept of {answers[1]}. The ‘hero’ starts their journey in {answers[3]}, where the hero and others are constrained by an unknown force called ‘{answers[1]},’ which likely by its description indicates human fear or the unwillingness to explore outside of one’s comfort zone. Then, one of the prisoners, who will soon become a ‘hero,’ breaks the chain and sets themself free, follows the source of the light, {answers[2]}, and starts to question {answers[1]} on an existential level. Here, the being of ‘light’ is almost depicted as the innate motivation or curiosity of {answers[1]}; in other words, the hero faces ‘the call to adventure’ stage in {answers[3]}. As the hero transitions from the cave into the outer world, they experience a radical change in his original worldview and cognition, as the environment he faces very much contradicts the deep-rooted beliefs about {answers[3]} they had since the beginning. This is best represented by the hero’s inability to look directly at things during daytime — due to the sun and its glare — which the hero describes as the process of pain and rage. This officially becomes the first threshold guardian that {answers[0]} encounters, where he faces immense temptations to return to {answers[3]} where they feel the most comfortable but gain nothing, or to sustain against the adversity, grow and become the very person they were meant to be: {answers[2]}. The hero faces challenges whilst adapting themself to the outside world results in the mastery of {answers[1]}: the revelation, death, and rebirth, in other words. {answers[0]} then asks deep philosophical questions about {answers[1]} and its function, successfully completing the last cycle of the hero’s journey: the atonement, where they make amends for their old beliefs. The hero receives a valuable gift from {answers[2]} as a result of their journey: {answers[4]}, which in this case indicates the divine nature of {answers[1]}, and the philosophical implications that the hero has drawn from their experience. The hero then returns to {answers[3]} and becomes the mentor of all the other potential explorers and those who undertake the next Hero’s Journey in {answers[1]}, which the mentor finds difficult to convince to their peers who have never been outside of {answers[3]}. This is well depicted in the reading where the mentor counterintuitively faces hate and voices of doubt, which teaches a valuable lesson to the audience: what does it mean to be ‘radically’ open-minded, and why is it so important to do so? Why does {answers[4]} lead to destruction and resistance to open up? And finally, what does it mean to be {answers[2]} in each and every one of us’s life, and how do we gain {answers[4]} in this seemingly superficial world?'
    # Calculate the word count
    wordCount = len(paragraph.split())
    # Line break after every period and question marks
    paragraph = paragraph.replace('.', '.\n\n')
    paragraph = paragraph.replace('?', '?\n\n')
    # Print the final product
    return paragraph

# Set the layout, which contains the textbox and the buttons
layout = [[sg.Text('Welcome to Nerdy Word Count Generator!', key='INTRO_TEXT')],
          [sg.Text(quest[0], size=(50, 1), key='TEXT_OUTPUT')], # Output field
          # Input field
          [sg.Input(key='TEXT_INPUT', do_not_clear=False)],
          # Buttons
          [sg.Button('Enter', bind_return_key=True), sg.Button('Quit')]]

# Set the window name
window = sg.Window('Nerdy Word Count Generator', layout)

# Event loop
while True:
    # For debugging purposes
    event, values = window.read()
    print(event, values)

    # Routing states to different actions
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    # If enter key or button is pressed but not when the input field is empty...
    if event == 'Enter' and values['TEXT_INPUT']:
        if pressCount == 4:
            # Store the answer for the previous question
            answers.append(str(values['TEXT_INPUT']))
            # Output the finished product
            window['TEXT_OUTPUT'].update(GenerateText())
            # Resize the text field
            window['TEXT_OUTPUT'].set_size((245, 28))
            # Update the title
            window['INTRO_TEXT'].update(f'FINAL PRODUCT • TOTAL WORD COUNT: {wordCount}')
            # Disable the enter button
            window['Enter'].update(visible=False)
            # Disable the input field
            window['TEXT_INPUT'].update(visible=False)
        else:
            # Store the answer for the previous question
            answers.append(str(values['TEXT_INPUT']))
            # Move onto the next question
            pressCount += 1
            # Update the text field
            window['TEXT_OUTPUT'].update(quest[pressCount])
            # window['TEXT_OUTPUT'].update(values['TEXT_INPUT'])

# Close the window
window.close()
