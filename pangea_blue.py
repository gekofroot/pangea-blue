#    Pangea Blue is a minimal hangman clone based around country names.
#    Copyright (C) 2022 gekofroot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed WITHOUT ANY WARRANTY; 
#    See the GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.




# import modules
from random import choice, shuffle
from os import sys
from time import sleep
from tkinter import *
from countries import *

def main():

    # globals
    global WCBG
    global FONT
    global font_size
    global window_width
    global window_height
    global correct_letters
    global correct_guess
    global incorrect_guess
    global current_fg
    global current_bg
    global current_ac
    global current_ac_2
    global country_name
    global correct_guess_list
    global numbers_guessed
    global increment_guess
    global countries
    global games_played
    global highest_streak
    global current_streak
    global current_percentage
    global correct_total
    global incorrect_total
    global correct_out_of
    global incorrect_out_of
    global letters_correct
    global letters_incorrect

    # variables
    WCBG = "#77ff77"
    FONT=("Monospace", 14)
    font_size = 14
    FG="#000000"
    BG="#ffeedd"
    AC="#fffedd"
    AC_2="#fffeee"
    BD=4
    RLF=GROOVE
    RLF_2=RAISED
    RLF_3=FLAT
    current_fg=FG
    current_bg=BG
    current_ac=AC
    current_ac_2=AC_2
    window_width = 400
    window_height = 400
    correct_letters = ""
    correct_guess = ""
    incorrect_guess = ""
    increment_guess = 0
    numbers_guessed = 0
    games_played = 0
    highest_streak = 0
    current_streak = 0
    current_percentage = 0
    correct_total = 0
    incorrect_total = 0
    correct_out_of = 0
    incorrect_out_of = 0
    letters_correct = 0
    letters_incorrect = 0
    
    MAIN_WINDOW = Tk()
    MAIN_WINDOW.geometry(f"{window_width}x{window_height}")
    MAIN_WINDOW.title("Pangea Blue")
    
    countries = []
    regions = [
            region_europe, region_america, region_asia, 
            region_africa, region_oceania,
            ]

    # select random country
    for group in regions:
        for country in group:
            countries.append(country)
    shuffle(countries)    
    country_name = choice(countries)

    # initialize list
    correct_guess_list = []
    for number in range(len(country_name)):
        correct_guess_list += "-"
    
    # fill correct letters
    for item in correct_guess_list:
        correct_letters += item
    
    #functions
    def guide_show():
        """open user guide"""

        guide_frame.lift()
        stats_frame.lower()

    def close_guide_show():
        """close user guide"""
        
        guide_frame.lower()
    
    def stats_show():
        """show stats window"""
        
        stats_frame.lift()
        guide_frame.lower()

    def close_stats_show():
        """close stats window"""

        stats_frame.lower()
    
    # set regions
    def region_get(reg, reg_name):
        """shuffle selected region and select randomly generated country"""
        
        # globals
        global countries

        display_region.configure(text=reg_name)
        countries = []
        regions = [reg]
        
        # select random country
        for group in regions:
            for country in group:
                countries.append(country)
        shuffle(countries)
        country_name = choice(countries)
        play_again()

    def select_region_europe():
        region_get(region_europe, "Europe")

    def select_country_northern_europe():
        region_get(countries_northern_europe, "Northern Europe")

    def select_country_southern_europe():
        region_get(countries_southern_europe, "Southern Europe")

    def select_country_eastern_europe():
        region_get(countries_eastern_europe, "Eastern Europe")

    def select_country_western_europe():
        region_get(countries_western_europe, "Western Europe")

    def select_region_america():
        region_get(region_america, "America")

    def select_country_caribbean():
        region_get(countries_caribbean, "Caribeean")

    def select_country_north_america():
        region_get(countries_north_america, "North America")

    def select_country_central_america():
        region_get(countries_central_america, "Central America")

    def select_country_south_america():
        region_get(countries_south_america, "South America")

    def select_country_latin_america():
        region_get(countries_latin_america, "Latin America")

    def select_region_asia():
        region_get(region_asia, "Asia")

    def select_country_central_asia():
        region_get(countries_southern_asia, "Central Asia")

    def select_country_southern_asia():
        region_get(countries_southern_asia, "Southern Asia")

    def select_country_southeastern_asia():
        region_get(countries_southeastern_asia, "Southeastern Asia")

    def select_country_middle_east_asia():
        region_get(countries_middle_east_asia, "Middle East Asia")

    def select_country_eastern_asia():
        region_get(countries_eastern_asia, "Eastern Asia")

    def select_country_western_asia():
        region_get(countries_western_asia, "Western Asia")

    def select_region_africa():
        region_get(region_africa, "Africa")

    def select_country_northern_africa():
        region_get(countries_northern_africa, "Northern Africa")

    def select_country_southern_africa():
        region_get(countries_southern_africa, "Southern Africa")

    def select_country_central_africa():
        region_get(countries_central_africa, "Central Africa")

    def select_country_eastern_africa():
        region_get(countries_eastern_africa, "Eastern Africa")

    def select_country_western_africa():
        region_get(countries_western_africa, "Western Africa")

    def select_region_oceania():
        region_get(region_oceania, "Oceania")

    def select_country_melanesia():
        region_get(countries_melanesia, "Melanesia Oceania")

    def select_country_micronesia():
        region_get(countries_micronesia, "Micronesia Oceania")

    def select_country_polynesia():
        region_get(countries_polynesia, "Polynesia Oceania")

    def select_region_all():
        """shuffle all regions and select randomly generated country"""
        
        global countries
        
        display_region.configure(text="All Regions")
        countries = []
        regions = [
                region_europe, region_america, region_asia, 
                region_africa, region_oceania,
                ]
        
        # select random country
        for group in regions:
            for country in group:
                countries.append(country)
        shuffle(countries)    
        country_name = choice(countries)
        play_again()
    
    # shuffle region
    def shuffle_region_all():
        """shuffle all regions and select randomly generated region"""
        
        regions = [
                select_region_europe, select_region_america, select_region_asia, 
                select_region_africa, select_region_oceania,
                ]
        shuffle(regions)
        random_region = choice(regions)
        random_region()
        play_again()

    # insert punctuation
    def insert_punctuation(name):
        """inserts puncuation where needed"""
        
        global correct_letters
        global numbers_guessed
        global correct_guess_list

        init_count = 0
        puncuation_type = [" ", "-", "\'", "."]
        for letter in name:
            count = 0
            for item in range(len(punctuation_type)):
                if punc_type[count] == letter:
                    correct_guess_list[init_count] = punctuation_type[count]
                    correct_letters = ""
                    numbers_guessed += 1
                    for item in correct_guess_list:
                        correct_letters += item
                count += 1
            init_count += 1
        return name
    insert_punctuation(country_name)

    
    def letter_entered():
        """
        once input has been recieved,
        determine whether or not input data occurs in country name
        """
        
        # globals
        global WCBG
        global correct_letters
        global correct_guess
        global incorrect_guess
        global country_name
        global correct_guess_list
        global numbers_guessed
        global increment_guess
        global font_size
        global games_played
        global highest_streak
        global current_streak
        global current_percentage
        global correct_total
        global incorrect_total
        global correct_out_of
        global incorrect_out_of
        global letters_correct
        global letters_incorrect

        correct_guess_container.configure(bg=current_ac)
        incorrect_guess_container.configure(bg=current_ac)

        user_guess = get_letter_guess.get()
        
        invalid_characters = [
                "1", "2", "3", "4", "5", "6", "7", "8",
                "9", "0", "!", "@", "#", "$", "%", "^", 
                "&", "*", "*", "(", ")", "+", "{", "}", 
                "|", ":", "\"", "<", ">", "?", "[", "]", 
                "\\", ";", "\'", ",", "/", "_", "=", "~", 
                "`", "-", ".",
                ]

        # answer key
        if user_guess == ":answer":
            current_streak = 0
            show_streak.configure(text=(f"Streak: {current_streak}"))
            if games_played > 0:
                current_percentage = (correct_total / games_played) * 100
            else:
                current_percentage = 0
            stats_highest_streak.configure(text=(f"Streak\n\n{highest_streak}"))
            stats_current_percentage.configure(text=(f"Win\nPercentage\n\n{current_percentage:.2f}"))
            get_letter_guess.configure(disabledbackground=current_ac, state=DISABLED)
            letter_guess_button.configure(text="", command="", state=DISABLED)
            sleep(1)
            display_user_message.configure(text=(f"{country_name}"), fg="#000000", bg="#ffbb99")
            play_again_message.configure(text="play again", activebackground="#ccddff", state=NORMAL)
            quit_game_message.configure(text="quit", activebackground="#ccddff", state=NORMAL)
        else:
            # ensure valid input
            if user_guess in invalid_characters:
                display_user_message.configure(text=(f"[  {user_guess}  ]\nentry must be a letter"), font=10, fg="#ff4400", bg="#ffffff")
                get_letter_guess.delete(0, END)
            else:
                user_guess = user_guess.strip()

                # ensure one character per entry
                if len(user_guess) > 1:
                    display_user_message.configure(text=(f"[  {user_guess}  ]\nonly one character allowed per entry"), font=10, fg="#ff4400", bg="#ffffff")
                    get_letter_guess.delete(0, END)
                elif len(user_guess) == 1:
                    display_user_message.configure(text="", font=("Monospace", font_size), fg=current_fg, bg=current_bg)
                    
                    # check if user guess is the beginning of country name
                    if  user_guess.capitalize() == country_name[0]:
                        if user_guess not in correct_letters:
                            user_guess = user_guess.capitalize()
                        if user_guess.capitalize() in correct_letters:
                            if user_guess.lower() in country_name:
                                user_guess = user_guess.lower()
                    
                    # multiple capital letters within name
                    elif user_guess.capitalize() in country_name:
                        if user_guess.capitalize() not in correct_letters:
                            user_guess = user_guess.capitalize()
                        if user_guess.capitalize() in correct_letters:
                            if user_guess.lower() in country_name:
                                user_guess = user_guess.lower()

                    # letter is correct
                    if user_guess in country_name:
                        if user_guess not in correct_letters:
                            correct_guess += user_guess
                            letters_correct += 1
                            stats_letters_correct.configure(text=(f"Correct\nLetters\n\n{letters_correct}"))
                            correct_guess_container.configure(text=(f"{correct_guess}"))

                        # letter has not been guessed yet
                        if user_guess not in correct_letters:
                            
                            count = 0
                            for letter in country_name:
                                if user_guess == letter:
                                    correct_guess_list[count] = user_guess
                                    numbers_guessed += 1
                                count += 1

                            correct_letters = ""
                            for item in correct_guess_list:
                                correct_letters += item
                                display_current_completion.configure(text=(f"{correct_letters}"))
                            display_user_message.configure(text=(f"[ {user_guess} ]"))
                            get_letter_guess.delete(0, END)

                            # country name guessed correctly
                            if numbers_guessed == len(country_name):
                                games_played += 1
                                current_streak += 1
                                if current_streak >= highest_streak:
                                    highest_streak = current_streak
                                correct_total += 1
                                current_percentage = (correct_total / games_played) * 100
                                show_streak.configure(text=(f"Streak: {current_streak}"))
                                stats_highest_streak.configure(text=(f"Highest\nStreak\n\n{highest_streak}"))
                                stats_correct_out_of.configure(text=(f"Wins\n\n{correct_total} / {games_played}"))
                                stats_incorrect_out_of.configure(text=(f"Losses \n\n{incorrect_total} / {games_played}"))
                                stats_current_percentage.configure(text=(f"Win\nPercentage\n\n{current_percentage:.2f} %"))
                                get_letter_guess.configure(disabledbackground=current_ac, state=DISABLED)
                                letter_guess_button.configure(text="", command="", state=DISABLED)
                                display_user_message.configure(text="")
                                display_current_completion.configure(activeforeground="#ffffff", fg="#000000", bg=WCBG)
                                play_again_message.configure(text="play again", activebackground="#ccddff", state=NORMAL)
                                quit_game_message.configure(text="quit", activebackground="#ccddff", state=NORMAL)
                        else: 
                            # repeat correct guess
                            correct_guess_container.configure(bg=WCBG)
                            display_user_message.configure(text=(f"[ {user_guess} ]"))
                            get_letter_guess.delete(0, END)
                    
                    # letter not in country name
                    elif user_guess not in country_name:
                        if user_guess.capitalize() not in country_name:
                            if user_guess not in incorrect_guess:
                                incorrect_guess += user_guess
                                letters_incorrect += 1
                                stats_letters_incorrect.configure(text=(f"Incorrect\nLetters\n\n{letters_incorrect}"))
                                incorrect_guess_container.configure(text=(f"{incorrect_guess}"))
                                increment_guess += 1
                                display_user_message.configure(text=(f"[ {user_guess} ]"))
                                get_letter_guess.delete(0, END)
                            else:
                                # repeat incorrect guess
                                incorrect_guess_container.configure(bg="#ffbb99")
                                display_user_message.configure(text=(f"[ {user_guess} ]"))
                                get_letter_guess.delete(0, END)

                            # guess limit reached
                            if increment_guess > 4:
                                games_played += 1
                                if current_streak > highest_streak:
                                    highest_streak = current_streak
                                current_streak = 0
                                incorrect_total += 1
                                current_percentage = (correct_total / games_played) * 100
                                show_streak.configure(text=(f"Streak: {current_streak}"))
                                stats_highest_streak.configure(text=(f"Highest\nStreak\n\n{highest_streak}"))
                                stats_correct_out_of.configure(text=(f"Wins\n\n{correct_total} / {games_played}"))
                                stats_incorrect_out_of.configure(text=(f"Losses\n\n{incorrect_total} / {games_played}"))
                                stats_current_percentage.configure(text=(f"Win\nPercentage\n\n{current_percentage:.2f} %"))
                                get_letter_guess.configure(disabledbackground=current_ac, state=DISABLED)
                                letter_guess_button.configure(text="", state=DISABLED)
                                sleep(1)
                                display_user_message.configure(text=(f"{country_name}"), fg="#000000", bg="#ffbb99")
                                play_again_message.configure(text="play again", activebackground="#ccddff", state=NORMAL)
                                quit_game_message.configure(text="quit", activebackground="#ccddff", state=NORMAL)
                        else:
                            # repeat correct guess
                            correct_guess_container.configure(bg=WCBG)
                            display_user_message.configure(text=(f"[ {user_guess} ]"))
                            get_letter_guess.delete(0, END)
    
    def play_again():
        """reconfigure/reset neccessary widgets/variables"""
        
        # globals
        global correct_letters
        global correct_guess
        global incorrect_guess
        global countries
        global country_name
        global correct_guess_list
        global numbers_guessed
        global increment_guess

        correct_letters = ""
        correct_guess = ""
        incorrect_guess = ""
        increment_guess = 0
        numbers_guessed = 0
        
        # select country
        shuffle(countries)
        country_name = choice(countries)
        
        # reconfigure widgets
        get_letter_guess.configure(state=NORMAL)
        stats_button.configure(bg=current_ac_2)
        letter_guess_button.configure(text="", bg=current_ac_2, state=NORMAL, relief=RLF_2, command=letter_entered)
        correct_guess_container.configure(text="")
        incorrect_guess_container.configure(text="")
        display_user_message.configure(text="", fg=current_fg, bg=current_bg)
        play_again_message.configure(text="", bg=current_ac_2, state=DISABLED)
        quit_game_message.configure(text="", bg=current_ac_2, state=DISABLED)
        get_letter_guess.delete(0, END)

        # initialize correct guess list
        correct_guess_list = []
        for number in range(len(country_name)):
            correct_guess_list += "-"
        
        # initialize correct letters
        for item in correct_guess_list:
            correct_letters += item
        
        # insert punctuation
        insert_punctuation(country_name)

        display_current_completion.configure(text=(f"{correct_letters}"), fg=current_fg, bg=current_ac)
    
    def size_toggle(width, height, get_font, font_size_2):
        """resize main window"""
        
        # globals
        global font
        global window_width
        global window_height
        global font_size
        
        font_size = get_font
        FONT=("Monospace", font_size)
        window_width = width
        window_height = height
        MAIN_WINDOW.geometry(f"{window_width}x{window_height}")
        
        x_pos = window_width / 2
        y_pos = window_height / 8

        display_region.configure(font=FONT)
        
        display_current_completion.configure(font=FONT)
        
        get_letter_guess.configure(font=FONT)
        letter_guess_button.configure(font=FONT)

        display_user_message.configure(font=FONT)
        
        display_correct_guess.configure(font=("Monospace", font_size_2))
        display_incorrect_guess.configure(font=("Monospace", font_size_2))
        correct_guess_container.configure(font=FONT)
        incorrect_guess_container.configure(font=FONT)
        show_streak.configure(font=("Monospace", font_size))

        play_again_message.configure(font=FONT)
        quit_game_message.configure(font=FONT)
        
        display_region.place(x=0, y=0, width=x_pos * 2, height=y_pos)
        
        display_current_completion.place(x=0, y=y_pos, width=x_pos * 2, height=y_pos * 2)
        
        stats_button.place(x=0, y=y_pos * 3, width=window_width / 3, height=y_pos)
        get_letter_guess.place(x=window_width / 3, y=y_pos * 3, width=window_width / 3, height=y_pos)
        letter_guess_button.place(x=(window_width / 3) * 2, y=y_pos * 3, width=window_width / 3, height=y_pos)

        display_user_message.place(x=0, y=y_pos * 4, width=x_pos * 2, height=y_pos)
        
        display_correct_guess.place(x=0, y=y_pos * 5, width=x_pos, height=y_pos)
        display_incorrect_guess.place(x=x_pos, y=y_pos * 5, width=x_pos, height=y_pos)
        correct_guess_container.place(x=0, y=y_pos * 6, width=x_pos, height=y_pos)
        incorrect_guess_container.place(x=x_pos, y=y_pos * 6, width=x_pos, height=y_pos)

        play_again_message.place(x=0, y=y_pos * 7, width=(window_width / 3), height=y_pos)
        show_streak.place(x=window_width / 3, y=y_pos * 7, width=(window_width / 3), height=y_pos)
        quit_game_message.place(x=(window_width / 3) * 2, y=y_pos * 7, width=(window_width / 3), height=y_pos) 
        
        MAIN_WINDOW.update()
    
    # size toggles
    def toggle_size_a():
        size_toggle(400, 400, 14, 20)
    
    def toggle_size_b():
        size_toggle(600, 400, 14, 20)
    
    def toggle_size_c():
        size_toggle(700, 700, 20, 32)       
    
    def toggle_size_d():
        size_toggle(1200, 700, 20, 38)    

    def set_fg_colour(colour):
        """sets foreground accent colour"""
        
        # globals
        global current_fg

        FG = colour
        current_fg = FG

        display_region.configure(fg=FG)
        get_letter_guess.configure(fg=FG)
        letter_guess_button.configure(fg=FG)
        display_current_completion.configure(fg=FG)
        display_correct_guess.configure(fg=FG)
        correct_guess_container.configure(fg=FG)
        display_incorrect_guess.configure(fg=FG)
        incorrect_guess_container.configure(fg=FG)
        display_user_message.configure(fg=FG)
        play_again_message.configure(fg=FG)
        quit_game_message.configure(fg=FG)
        guide_frame.configure(fg=FG)
        stats_frame.configure(fg=FG)
        stats_highest_streak.configure(fg=FG)
        stats_current_percentage.configure(fg=FG)
        stats_correct_out_of.configure(fg=FG)
        stats_incorrect_out_of.configure(fg=FG)
        stats_window_close.configure(fg=FG)
        show_streak.configure(fg=FG)
        stats_letters_correct.configure(fg=FG)
        stats_letters_incorrect.configure(fg=FG)
        guide_window_close.configure(fg=FG)

    def set_bg_colour(colour):
        """sets background colour"""
        
        # globals
        global current_bg

        BG = colour
        current_bg = BG
        
        display_region.configure(bg=BG)
        get_letter_guess.configure(bg=BG)
        letter_guess_button.configure(bg=BG)
        display_current_completion.configure(bg=BG)
        display_correct_guess.configure(bg=BG)
        correct_guess_container.configure(bg=BG)
        display_incorrect_guess.configure(bg=BG)
        incorrect_guess_container.configure(bg=BG)
        display_user_message.configure(bg=BG)
        play_again_message.configure(bg=BG)
        quit_game_message.configure(bg=BG)
        guide_frame.configure(bg=BG)
        stats_frame.configure(bg=BG)
        stats_window_close.configure(bg=BG)
        guide_window_close.configure(bg=BG)
    
    def set_accent_colour(colour):
        """sets primary accent colour"""
        
        # globals
        global current_ac

        AC = colour
        current_ac = AC

        get_letter_guess.configure(bg=AC)
        display_current_completion.configure(bg=AC)
        correct_guess_container.configure(bg=AC)
        incorrect_guess_container.configure(bg=AC)
        show_streak.configure(bg=AC)
        stats_highest_streak.configure(bg=AC)
        stats_current_percentage.configure(bg=AC)
        stats_correct_out_of.configure(bg=AC)
        stats_incorrect_out_of.configure(bg=AC)
        stats_letters_correct.configure(bg=AC)
        stats_letters_incorrect.configure(bg=AC)

    def set_accent_colour_b(colour):
        """sets secondary accent colour"""
        
        # globals
        global current_ac_2

        AC_2 = colour
        current_ac_2 = AC_2

        stats_button.configure(bg=AC_2)
        letter_guess_button.configure(bg=AC_2)
        play_again_message.configure(bg=AC_2)
        quit_game_message.configure(bg=AC_2)

    def colour_get(fg, bg, ac, ac_2):
        """set foreground/background and primary/secondary accent colours"""

        # globals
        global current_fg
        global current_bg
        global current_ac

        current_fg = fg
        current_bg = bg
        current_ac = ac
        current_ac_2 = ac_2

        set_fg_colour(fg)
        set_bg_colour(bg)
        set_accent_colour(ac)
        set_accent_colour_b(ac_2)

    def select_colour_samba():
        colour_get("#ffffff", "#ff5555", "#ff4444", "#ff6666")

    def select_colour_dune():
        colour_get("#000000", "#ffffbb", "#ffffcc", "#ffffdd")

    def select_colour_mint():
        colour_get("#000000", "#ddffcc", "#eeffdd", "#eeffee")

    def select_colour_cobalt():
        colour_get("#ffffff", "#5555ee", "#4444ff", "#4455ff")

    def select_colour_black():
        colour_get("#ffffff", "#000000", "#000000", "#000000")

    def select_colour_cream():
        colour_get("#000000", "#eeeeee", "#ffffee", "#ffffff")

    def select_colour_default():
        colour_get("#000000", "#ffeedd", "#fffedd", "#fffeee")
    
    def exit_cmd():
        sys.exit()

    # widgets
    display_region = Label(text="All Regions", font=FONT, fg=FG, bg=BG, bd=4, relief=RLF_2, justify=CENTER)
    
    stats_button = Button(text="",font=FONT, fg=FG, bg=AC_2, activebackground="#ccddff", bd=BD, relief=RLF_2,
            command=stats_show)

    get_letter_guess = Entry(font=FONT, fg=FG, bg=AC, bd=BD, relief=SUNKEN, justify=CENTER)
    letter_guess_button = Button(text="",font=FONT, fg=FG, bg=AC_2, activebackground="#ccddff", bd=BD, relief=RLF_2,
            command=letter_entered)
    
    display_correct_guess = Label(text="+", font=("Monospace", 20), fg=FG, bg=BG, bd=BD, relief=RLF_3)
    correct_guess_container = Label(font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=SUNKEN)
    
    display_current_completion = Label(text=(f"{correct_letters}"), font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=RLF_2)
    display_incorrect_guess = Label(text=f"-", font=("Monospace", 20), fg=FG, bg=BG, bd=BD, relief=RLF_3)
    incorrect_guess_container = Label(font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=SUNKEN)
    
    display_user_message = Label(text="", font=FONT, fg=FG, bg=BG, bd=2, relief=RLF_2)
    
    play_again_message = Button(font=FONT, fg=FG, bg=AC_2, bd=BD, relief=RLF_2, state=DISABLED, disabledforeground=FG,
            command=play_again)
    
    show_streak = Label(text=(f"Streak: {current_streak}"), font=("Monospace", 10), fg=FG, bg=AC, bd=BD - 2, relief=RLF_2)
    quit_game_message = Button(font=FONT, fg=FG, bg=AC_2, bd=BD, relief=RLF_2, state=DISABLED, disabledforeground=BG,
            command=exit_cmd)
    
    guide_frame = LabelFrame(MAIN_WINDOW, text="Guide", font=FONT, fg=FG, bg=BG, bd=BD - 2, relief=RIDGE)
    guide_text = "Objective:\nAttemp to guess country name. \nProgress window lights up green once all letters have been guessed correctly. \nCountry name is displayed in red after five incorrect guesses. \n\n"
    guide_text_2 = "Buttons:\nLeft Button: Show Stats\nRight Button: Enter\n\nHotkeys:\nCtrl + S: Shuffle Countries \nCtrl + A: Shuffle Regions \nReturn: Enter \nCtrl + T: Show Stats \nCtrl + Alt + T: Close Stats \nCtlr + H: Show Guide \nCtrl + Alt + H: Close Guide \nCtrl + Q: Exit"
    guide_window = Message(guide_frame, text=(f"{guide_text}{guide_text_2}"), width=window_width - 20, font=("Monospace", 10), fg=FG, bg="#dddddd", bd=BD - 2, relief=RLF_3, justify=CENTER)
    guide_window_close = Button(guide_frame, text=(f"Close"), font=("Monospace", 10), fg=FG, bg=BG, bd=BD, relief=RLF_2, activebackground="#ccddff", 
            command=close_guide_show)

    stats_frame = LabelFrame(MAIN_WINDOW, text="Stats", font=FONT, fg=FG, bg=BG, bd=BD - 2, relief=GROOVE)
    stats_highest_streak = Label(stats_frame, text=(f"Highest\nStreak\n\n{current_streak}"),font=("Monospace", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_current_percentage = Label(stats_frame, text=(f"Win\nPercentage\n\n{current_percentage:.0f} %"), font=("Monospace", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_correct_out_of = Label(stats_frame, text=(f"Wins\n\n{correct_out_of} / {games_played}"), font=("Monospace", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_incorrect_out_of = Label(stats_frame, text=(f"Losses\n\n{incorrect_out_of} / {games_played}"), font=("Monospace", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_letters_correct = Label(stats_frame, text=(f"Correct\nLetters\n\n{letters_correct}"), font=("Monospace", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_letters_incorrect = Label(stats_frame, text=(f"Incorrect\nLetters\n\n{letters_incorrect}"), font=("Monospace", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_window_close = Button(stats_frame, text=(f"Close"), font=("Monospace", 10), fg=FG, bg=BG, bd=BD, relief=RLF_2, activebackground="#ccddff", command=close_stats_show)

    # place widgets
    x_pos = window_width / 2
    y_pos = window_height / 8

    display_region.place(x=0, y=0, width=x_pos * 2, height=y_pos)
    
    display_current_completion.place(x=0, y=y_pos, width=x_pos * 2, height=y_pos * 2)
    
    stats_button.place(x=0, y=y_pos * 3, width=window_width / 3, height=y_pos)
    get_letter_guess.place(x=window_width / 3, y=y_pos * 3, width=window_width / 3, height=y_pos)
    letter_guess_button.place(x=(window_width / 3) * 2, y=y_pos * 3, width=window_width / 3, height=y_pos)

    display_user_message.place(x=0, y=y_pos * 4, width=x_pos * 2, height=y_pos)
    
    display_correct_guess.place(x=0, y=y_pos * 5, width=x_pos, height=y_pos)
    display_incorrect_guess.place(x=x_pos, y=y_pos * 5, width=x_pos, height=y_pos)
    correct_guess_container.place(x=0, y=y_pos * 6, width=x_pos, height=y_pos)
    incorrect_guess_container.place(x=x_pos, y=y_pos * 6, width=x_pos, height=y_pos)

    play_again_message.place(x=0, y=y_pos * 7, width=(window_width / 3), height=y_pos)
    show_streak.place(x=(window_width / 3), y=y_pos * 7, width=(window_width / 3), height=y_pos)
    quit_game_message.place(x=(window_width / 3) * 2, y=y_pos * 7, width=(window_width / 3), height=y_pos) 
    
    guide_frame.place(x=0, y=0, width=x_pos * 2, height=y_pos * 8)
    guide_frame.lower()
    guide_window.place(x=0, y=0, width=x_pos * 2, height=y_pos * 7)
    guide_window_close.place(x=0, y=(y_pos * 7) - 20, width=x_pos * 2, height=y_pos)

    stats_frame.place(x=0, y=0, width=x_pos * 2, height=y_pos * 8)
    stats_frame.lower()
    
    stats_highest_streak.place(x=0, y=0, width=x_pos, height=window_height / 4)
    stats_current_percentage.place(x=x_pos, y=0, width=x_pos, height=window_height / 4)
    
    stats_correct_out_of.place(x=0, y=window_height / 4, width=x_pos, height=window_height / 4)
    stats_incorrect_out_of.place(x=x_pos, y=window_height / 4, width=x_pos, height=window_height / 4)
    
    stats_letters_correct.place(x=0, y=(window_height / 4) * 2, width=x_pos, height=window_height / 4)
    stats_letters_incorrect.place(x=x_pos, y=(window_height / 4) * 2, width=x_pos, height=window_height / 4)
    
    stats_window_close.place(x=0, y=(window_height / 4) * 3, width=x_pos * 2, height=(window_height / 4) - 20)

    # set menu
    top_menu = Menu(MAIN_WINDOW)
    settings_menu = Menu(top_menu)
    
    # scale menu
    window_scale_menu = Menu(settings_menu)
    window_scale_menu.add_command(label="400x400  (default)", command=toggle_size_a)
    window_scale_menu.add_command(label="600x400", command=toggle_size_b)
    window_scale_menu.add_command(label="700x700", command=toggle_size_c)
    window_scale_menu.add_command(label="1200x700", command=toggle_size_d)
    settings_menu.add_cascade(label="Window Scale", menu=window_scale_menu)
    
    # shuffle menu
    shuffle_menu = Menu(settings_menu)
    shuffle_menu.add_command(label="Shuffle Country", command=play_again, accelerator="Ctrl+S")
    shuffle_menu.add_command(label="Shuffle Region", command=shuffle_region_all, accelerator="Ctrl+A")
    settings_menu.add_cascade(label="Shuffle", menu=shuffle_menu)
    
    # select region menu
    select_region_menu = Menu(settings_menu)
    select_region_menu.add_command(label="All Regions", command=select_region_all)
    select_region_menu.add_separator()
    region_europe_menu = Menu(select_region_menu)
    region_europe_menu.add_command(label="Europe", command=select_region_europe)
    region_europe_menu.add_separator()
    region_europe_menu.add_command(label="Northern Europe", command=select_country_northern_europe)
    region_europe_menu.add_command(label="Southern Europe", command=select_country_southern_europe)
    region_europe_menu.add_command(label="Eastern Europe", command=select_country_eastern_europe)
    region_europe_menu.add_command(label="Western Europe", command=select_country_western_europe)
    select_region_menu.add_cascade(label="Europe", menu=region_europe_menu)
    region_america_menu = Menu(select_region_menu)
    region_america_menu.add_command(label="America", command=select_region_america)
    region_america_menu.add_separator()
    region_america_menu.add_command(label="Caribbean", command=select_country_caribbean)
    region_america_menu.add_command(label="North America", command=select_country_north_america)
    region_america_menu.add_command(label="South America", command=select_country_south_america)
    region_america_menu.add_command(label="Central America", command=select_country_central_america)
    region_america_menu.add_command(label="Latin America", command=select_country_latin_america)
    select_region_menu.add_cascade(label="America", menu=region_america_menu)
    region_asia_menu = Menu(select_region_menu)
    region_asia_menu.add_command(label="Asia", command=select_region_asia)
    region_asia_menu.add_separator()
    region_asia_menu.add_command(label="Central Asia",command=select_country_central_asia)
    region_asia_menu.add_command(label="Southern Asia", command=select_country_southern_asia)
    region_asia_menu.add_command(label="Southeastern Asia", command=select_country_southeastern_asia)
    region_asia_menu.add_command(label="Middle East Asia", command=select_country_middle_east_asia)
    region_asia_menu.add_command(label="Eastern Asia", command=select_country_eastern_asia)
    region_asia_menu.add_command(label="Western Asia", command=select_country_western_asia)
    select_region_menu.add_cascade(label="Asia", menu=region_asia_menu)
    region_africa_menu = Menu(select_region_menu)
    region_africa_menu.add_command(label="Africa", command=select_region_africa)
    region_africa_menu.add_separator()
    region_africa_menu.add_command(label="Central Africa", command=select_country_central_africa)
    region_africa_menu.add_command(label="Northern Africa", command=select_country_northern_africa)
    region_africa_menu.add_command(label="Southern Africa", command=select_country_southern_africa)
    region_africa_menu.add_command(label="Eastern Africa", command=select_country_eastern_africa)
    region_africa_menu.add_command(label="Western Africa", command=select_country_western_africa)
    select_region_menu.add_cascade(label="Africa", menu=region_africa_menu)
    region_oceania_menu = Menu(select_region_menu)
    region_oceania_menu.add_command(label="Oceania", command=select_region_oceania)
    region_oceania_menu.add_separator()
    region_oceania_menu.add_command(label="Melanesia", command=select_country_melanesia)
    region_oceania_menu.add_command(label="Micronesia", command=select_country_micronesia)
    region_oceania_menu.add_command(label="Polynesia", command=select_country_polynesia)
    select_region_menu.add_cascade(label="Oceania", menu=region_oceania_menu)
    settings_menu.add_cascade(label="Region", menu=select_region_menu)
    
    # colourscheme menu
    colourscheme_menu = Menu(settings_menu)
    colourscheme_menu.add_command(label="Samba", command=select_colour_samba)
    colourscheme_menu.add_command(label="Dune", command=select_colour_dune)
    colourscheme_menu.add_command(label="Mint", command=select_colour_mint)
    colourscheme_menu.add_command(label="Cobalt", command=select_colour_cobalt)
    colourscheme_menu.add_command(label="Black", command=select_colour_black)
    colourscheme_menu.add_command(label="Cream", command=select_colour_cream)
    colourscheme_menu.add_separator()
    colourscheme_menu.add_command(label="Default", command=select_colour_default)
    settings_menu.add_cascade(label="Colorscheme", menu=colourscheme_menu)
    settings_menu.add_separator()
    settings_menu.add_command(label="Exit", command=exit_cmd, accelerator="Ctrl+Q")
    top_menu.add_cascade(label="Settings", menu=settings_menu)
    
    # about menu
    about_menu = Menu(top_menu)
    about_menu.add_command(label="Guide", command=guide_show, accelerator="Ctrl+H")
    about_menu.add_command(label="Stats", command=stats_show, accelerator="Alt+S")
    top_menu.add_cascade(label="About", menu=about_menu)
    
    MAIN_WINDOW.config(menu=top_menu)

    # keybindings
    def callback_play_again(event):
        play_again()

    def callback_exit(event):
        exit_cmd()

    def callback_letter_guess(event):
        letter_guess_button.invoke()
    
    def callback_shuffle_region(event):
        shuffle_region_all()

    def callback_open_guide(event):
        guide_show()
    
    def callback_close_guide(event):
        close_guide_show()
    
    def callback_open_stats(event):
        stats_show()

    def callback_close_stats(event):
        close_stats_show()

    MAIN_WINDOW.bind("<Control-KeyPress-s>", callback_play_again)
    MAIN_WINDOW.bind("<Control-KeyPress-q>", callback_exit)
    MAIN_WINDOW.bind("<Return>", callback_letter_guess)
    MAIN_WINDOW.bind("<Control-KeyPress-a>", callback_shuffle_region)
    MAIN_WINDOW.bind("<Control-KeyPress-h>", callback_open_guide)
    MAIN_WINDOW.bind("<Control-Alt-KeyPress-h>", callback_close_guide)
    MAIN_WINDOW.bind("<Control-KeyPress-t>", callback_open_stats)
    MAIN_WINDOW.bind("<Control-Alt-KeyPress-t>", callback_close_stats)

    # mainloop
    MAIN_WINDOW.mainloop()


if __name__ == '__main__':
    main()
