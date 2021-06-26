import tkinter as tk
import random
# import base64

# TODO: encrypt save file


class GUI:
    def __init__(self):
        """ commands that get run as soon as the game gets initialized"""
        # initializing variables
        self.boundary = 0

        # initializing board setup
        self.board_setup()
        self.ready_question()
        self.runUI()

    def board_setup(self):
        """ Creating the board """
        self.master = tk.Tk()
        self.master.title('Aim trainer')
        self.master.geometry('+{}+{}'.format(700, 300))
        # self.master.geometry('1280x720')
        self.master.configure(background='white')
        self.master.resizable(0, 0)

    def runUI(self):
        """ run the UI """
        self.master.mainloop()

    def ready_question(self):
        """ asks the user if they are ready to play the aim trainer game """
        self.game_question = tk.Label(self.master, text='Are you ready to practice your aim?')
        self.game_question.grid(columnspan=2, row=0, column=0)
        self.ready_button = tk.Button(self.master, text='Ready', command=self.set_difficulty, width=10)
        self.ready_button.grid(row=1, column=0)
        self.quit_button = tk.Button(self.master, text='Quit', command=self.master.destroy, width=10)
        self.quit_button.grid(row=1, column=1)

    """ set your difficulty """

    def set_difficulty(self):
        self.master.destroy()
        self.board_setup()
        self.difficulty_label = tk.Label(self.master, text='choose which difficulty you want:')
        self.difficulty_label.grid(columnspan=3, row=0)
        self.easy_button = tk.Button(self.master, text='Easy', command=self.choose_easy_difficulty)
        self.easy_button.grid(row=1, column=0)
        self.medium_button = tk.Button(self.master, text='Medium', command=self.choose_medium_difficulty)
        self.medium_button.grid(row=1, column=1)
        self.hard_button = tk.Button(self.master, text='Hard', command=self.choose_hard_difficulty)
        self.hard_button.grid(row=1, column=2)
        self.runUI()

    def choose_easy_difficulty(self):
        """ chose easy difficulty """
        self.boundary = 4
        self.game_loop()

    def choose_medium_difficulty(self):
        """ chose medium difficulty """
        self.boundary = 9
        self.game_loop()

    def choose_hard_difficulty(self):
        """ chose hard difficulty """
        self.boundary = 14
        self.game_loop()

    """ these commands under this line will be the actual game commands """

    def game_loop(self):
        """ puts the user in the actual game loop phase """
        self.master.destroy()
        self.board_setup()
        self.set_boundaries()
        self.set_values()
        self.create_map()
        self.random_button()
        self.master.after(10000, lambda: self.master.destroy())
        self.runUI()

        # this should be after the game is done
        self.board_setup()
        self.game_over()
        self.runUI()


    def set_boundaries(self):
        """ initializes boundaries for aim trainer game"""

        # initializing the GUI variables
        self.user_points = 0
        self.user_points_var = tk.StringVar(self.master)
        self.button = tk.StringVar(self.master)
        correction = self.boundary + 1
        more_correct = correction + 1

        self.top_label = tk.Label(self.master, text='aim trainer')
        self.top_label.grid(columnspan=self.boundary, row=0)
        self.bottom_label = tk.Label(self.master, textvariable=self.user_points_var)
        self.bottom_label.grid(columnspan=self.boundary, row=correction)
        if self.boundary == 4:
            try:
                with open('highscores.txt', 'r') as file:
                    s = 0
                    temp_score = 0
                    for lines in file:
                        split_lines = lines.split()
                        print('DEBUG: should be split lines', split_lines)
                        if split_lines[0] == 'easy':
                            if int(split_lines[1]) > temp_score:
                                temp_score = int(split_lines[1])
                            temp_label = 'High Score: {}'.format(temp_score)
                            s += 1
                    if s == 0:
                        temp_label = 'High Score: 0'
                    self.high_score_label = tk.Label(self.master, text=temp_label)
                    self.high_score_label.grid(columnspan=self.boundary, row=more_correct)
            except FileNotFoundError:
                self.high_score_label = tk.Label(self.master, text='High Score: 0')
                self.high_score_label.grid(columnspan=self.boundary, row=more_correct)
        elif self.boundary == 9:
            try:
                with open('highscores.txt', 'r') as file:
                    s = 0
                    temp_score = 0
                    for lines in file:
                        split_lines = lines.split()
                        if split_lines[0] == 'medium':
                            if int(split_lines[1]) > temp_score:
                                temp_score = int(split_lines[1])
                            temp_label = 'High Score: {}'.format(temp_score)
                            s += 1
                    if s == 0:
                        temp_label = 'High Score: 0'
                    self.high_score_label = tk.Label(self.master, text=temp_label)
                    self.high_score_label.grid(columnspan=self.boundary, row=more_correct)
            except FileNotFoundError:
                self.high_score_label = tk.Label(self.master, text='High Score: 0')
                self.high_score_label.grid(columnspan=self.boundary, row=more_correct)
        elif self.boundary == 14:
            try:
                with open('highscores.txt', 'r') as file:
                    s = 0
                    temp_score = 0
                    for lines in file:
                        split_lines = lines.split()
                        if split_lines[0] == 'hard':
                            if int(split_lines[1]) > temp_score:
                                temp_score = int(split_lines[1])
                            temp_label = 'High Score: {}'.format(temp_score)
                            s += 1
                    if s == 0:
                        temp_label = 'High Score: 0'
                    self.high_score_label = tk.Label(self.master, text=temp_label)
                    self.bottom_label.grid(columnspan=self.boundary, row=more_correct)
            except FileNotFoundError:
                self.high_score_label = tk.Label(self.master, text='High Score: 0')
                self.high_score_label.grid(columnspan=self.boundary, row=more_correct)
        else:
            print('DEBUG: something went wrong')

    def set_values(self):
        """ sets values for initialized boundaries """
        self.label_text = 'Your score: {}'.format(self.user_points)
        self.user_points_var.set(self.label_text)
        print("DEBUG: should be label text", self.label_text)

    def create_map(self):
        """ create space of buttons """
        for i in range(1, self.boundary):
            for j in range(1, self.boundary):
                self.map_label = tk.Label(self.master, width=3, height=2)
                self.map_label.grid(row=i, column=j)

    def random_button(self):
        """ adds a random button """

        # since randint parameters are both inclusive!
        inclusive_correction = self.boundary - 1

        # actual button space
        self.random_x = random.randint(1, inclusive_correction)
        self.random_y = random.randint(1, inclusive_correction)
        print('DEBUG: should be random x and y', self.random_x, self.random_y)
        self.new_button = tk.Button(self.master, width=2, height=1, command=self.button_pressed,
                                    textvariable=self.button, bg='blue')
        self.new_button.grid(row=self.random_x, column=self.random_y)

    def button_pressed(self):
        """ when a button is pressed """
        print("DEBUG: a button is pressed")
        self.add_score()
        self.new_button.destroy()
        self.random_button()

    def add_score(self):
        """ add a point to the user for clicking the button """
        self.user_points += 1
        print("DEBUG, shouldve added a score", self.user_points)
        # initializing the GUI variables
        self.set_values()

    def game_over(self):
        """ adds the labels and buttons for game over """

        with open('highscores.txt', 'a') as file:
            if self.boundary == 4:
                easy_format = 'easy {}\n'.format(self.user_points)
                file.write(easy_format)
            elif self.boundary == 9:
                medium_format = 'medium {}\n'.format(self.user_points)
                file.write(medium_format)
            elif self.boundary == 14:
                hard_format = 'hard {}\n'.format(self.user_points)
                file.write(hard_format)

        score_text = 'You got {} points!'.format(self.user_points)
        self.score_label = tk.Label(self.master, text=score_text)
        self.score_label.grid(columnspan=2, row=0)
        self.play_again = tk.Label(self.master, text='would you like to play another game?')
        self.play_again.grid(columnspan=2, row=1)
        self.play_again_button_yes = tk.Button(self.master, command=self.game_loop, text='Yes', width=5)
        self.play_again_button_yes.grid(row=2, column=0)
        self.play_again_button_no = tk.Button(self.master, command=self.new_game, text='No', width=5)
        self.play_again_button_no.grid(row=2, column=1)

    def new_game(self):
        """ when the user doesnt want to play same settings and wants to restart game after finishing one """
        self.master.destroy()
        self.board_setup()
        self.ready_question()
        self.runUI()


if __name__ == '__main__':
    game_instance = GUI()

#  exec(base64.b64decode(my_code))
