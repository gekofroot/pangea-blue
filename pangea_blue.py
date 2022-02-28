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
from random import choice, shuffle, randint
from os import sys
from time import sleep
from tkinter import *
from countries import *
from variables import *
from country_facts import *

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
    global perfect_game
    global highest_streak
    global current_streak
    global current_percentage
    global current_loss_percentage
    global correct_total
    global incorrect_total
    global correct_out_of
    global incorrect_out_of
    global letters_correct
    global letters_incorrect
    global current_country
    global index_count
    global shown_hint
    global highest_score
    global points

    MAIN_WINDOW = Tk()
    MAIN_WINDOW.geometry(f"{window_width}x{window_height}")
    MAIN_WINDOW.title("Pangea Blue")
    
    # retrieve high scores
    with open("highest_streak.txt", "r") as high_streak:
        hs_txt = high_streak.read()
        if hs_txt == 0:
            highest_streak = 0
            high_streak.close()
        else:
            highest_streak = int(hs_txt)
            high_streak.close()
    
    # retrieve high points
    with open("high_score.txt", "r") as high_score:
        hp_txt = high_score.read()
        if hp_txt == 0:
            highest_score = 0
            high_score.close()
        else:
            highest_score = int(hp_txt)
            high_score.close()
    
    countries = []

    # select random country
    for group in regions:
        for country in group:
            countries.append(country)
    shuffle(countries)    
    country_name = choice(countries)

    # show initial hint
    def show_first_hint():
        count = 0
        for country in country_names:
            if country_name == country_names[count]:
                if len(country_facts[count]) > 0:
                    if len(country_facts[count]) == 1:
                        info = country_facts[count][index_count]
                        show_hint.configure(text=info)
                    elif len(country_facts[count]) > 1:
                        index_count = randint(0, len(country_facts[count]) - 1)
                        info = country_facts[count][index_count]
                        show_hint.configure(text=info)
                else:
                    show_hint.configure(text="no available data at this time...")
            count += 1
    
    # initialize list
    correct_guess_list = []
    for number in range(len(country_name)):
        correct_guess_list += "-"
    
    # fill correct letters
    for item in correct_guess_list:
        correct_letters += item
    
    #functions
    # get next hint
    def get_next_hint():
        
        global index_count
        count = 0
        
        for country in country_names:
            if country_name == country_names[count]:
                if len(country_facts[count]) > 0:
                    if index_count == len(country_facts[count]) - 1:
                        index_count = 0
                    else:
                        index_count += 1
                    info = country_facts[count][index_count]
                    show_hint.configure(text=info)
                else:
                    show_hint.configure(text="no available data at this time...")
            count += 1
    
    # get previous hint
    # mod
    def get_prev_hint():
        
        global index_count
        count = 0

        for country in country_names:
            if country_name == country_names[count]:
                if len(country_facts[count]) > 0:
                    if index_count == 0:
                        index_count = len(country_facts[count]) - 1
                    else:
                        index_count - 1
                        index_count -= 1
                    info = country_facts[count][index_count]
                    show_hint.configure(text=info)
                else:
                    show_hint.configure(text="no available data at this time...")
            count += 1
    
    # get random hint
    def get_random_hint(): 
        
        global index_count
        global shown_hint
        count = 0
        
        for country in country_names:
            if country_name == country_names[count]:
                if len(country_facts[count]) > 0:
                    if len(shown_hint) == len(country_facts[count]):
                        del shown_hint[:-1]
                    index_count = randint(0, len(country_facts[count]) -1)
                    info = country_facts[count][index_count]
                    if info in shown_hint:
                        while info in shown_hint:
                            index_count = randint(0, len(country_facts[count]) -1)
                            info = country_facts[count][index_count]
                    
                    shown_hint.append(info)
                    show_hint.configure(text=info)
                else:
                    show_hint.configure(text="no available data at this time...")
            count += 1

    def guide_show():
        """open user guide"""

        guide_frame.lift()
        stats_frame.lower()
        hint_frame.lower()

    def close_guide_show():
        """close user guide"""
        
        guide_frame.lower()
        hint_frame.lift()
    
    def stats_show():
        """show stats window"""
        
        stats_frame.lift()
        guide_frame.lower()
        hint_frame.lower()
    
    def close_stats_show():
        """close stats window"""

        stats_frame.lower()
        hint_frame.lift()
    
    def hint_show():
        """open user guide"""
        
        hint_frame.lift()
        guide_frame.lower()
        stats_frame.lower()

    def close_hint_show():
        """close user guide"""
        
        hint_frame.lower()
    
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
        """inserts punctuation where needed"""
        
        global correct_letters
        global numbers_guessed
        global correct_guess_list

        init_count = 0
        punctuation_type = [" ", "-", "\'", "."]
        for letter in name:
            count = 0
            for item in range(len(punctuation_type)):
                if punctuation_type[count] == letter:
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
        global perfect_game
        global lucky_win
        global highest_streak
        global current_streak
        global current_percentage
        global current_loss_percentage
        global correct_total
        global incorrect_total
        global correct_out_of
        global incorrect_out_of
        global letters_correct
        global letters_incorrect
        global highest_score
        global points

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
                current_loss_percentage = (incorrect_total / games_played) * 100
            else:
                current_percentage = 0
                current_loss_percentage = 0
            stats_highest_streak.configure(text=(f"Streak\n\n{highest_streak}"))
            stats_current_percentage.configure(text=(f"Win\nPercentage\n\n{current_percentage:.2f}"))
            stats_current_loss_percentage.configure(text=(f"Loss\nPercentage\n\n{current_loss_percentage:.2f}"))
            get_letter_guess.configure(disabledbackground=current_ac, state=DISABLED)
            letter_guess_button.configure(text="Play Again", command=play_again)
            sleep(1)
            display_user_message.configure(text=(f"{country_name}"), fg="#000000", bg="#ffbb99")
        else:
            # ensure valid input
            if user_guess.strip() in invalid_characters:
                display_user_message.configure(text=(f"[  {user_guess}  ]\nentry must be a letter"), font=10, fg="#ff0000", bg="#ffffff")
                get_letter_guess.delete(0, END)
            else:
                user_guess = user_guess.strip()

                # ensure one character per entry
                if len(user_guess) > 1:
                    display_user_message.configure(text=(f"[  {user_guess}  ]\nonly one character allowed per entry"), font=10, fg="#ff0000", bg="#ffffff")
                    get_letter_guess.delete(0, END)
                elif len(user_guess) == 1:
                    display_user_message.configure(text="", font=("Helvetica", font_size), fg=current_fg, bg=current_bg)
                    
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
                                
                                # set bonus
                                if current_streak > 10:
                                    points += 25
                                else:
                                    points += 20
                            
                                # no incorrect guesses
                                if numbers_guessed == len(country_name) and len(incorrect_guess) == 0:
                                    perfect_game += 1
                                    stats_perfect_game.configure(text=(f"Perfect\nGames\n\n{perfect_game}"))
                                    if current_streak > 10:
                                        points += 15
                                    else:
                                        points += 10
                                
                                if len(incorrect_guess) == 4:
                                    lucky_win += 1
                                    stats_lucky_win.configure(text=(f"Lucky\nWins\n\n{lucky_win}"))
                                    points += 2

                                # update highest streak
                                if current_streak > highest_streak:
                                    highest_streak = current_streak
                                    with open("highest_streak.txt", "w") as high_streak:
                                        print(f"{highest_streak}", file=high_streak)
                                        high_streak.close()
                                
                                # update high score
                                if points > highest_score:
                                    highest_score = points
                                    with open("high_score.txt", "w") as high_score:
                                        print(f"{highest_score}", file=high_score)
                                        high_score.close()
                                
                                correct_total += 1
                                current_percentage = (correct_total / games_played) * 100
                                current_loss_percentage = (incorrect_total / games_played) * 100
                                display_points.configure(text=(f"{points}"))
                                show_streak.configure(text=(f"Streak: {current_streak}"))
                                stats_highest_streak.configure(text=(f"Highest\nStreak\n\n{highest_streak}"))
                                stats_high_score.configure(text=(f"High\nScore\n\n{highest_score}"))
                                stats_correct_out_of.configure(text=(f"Wins\n\n{correct_total} / {games_played}"))
                                stats_incorrect_out_of.configure(text=(f"Losses \n\n{incorrect_total} / {games_played}"))
                                stats_current_percentage.configure(text=(f"Win\nPercentage\n\n{current_percentage:.2f} %"))
                                stats_current_loss_percentage.configure(text=(f"Loss\nPercentage\n\n{current_loss_percentage:.2f} %"))
                                get_letter_guess.configure(disabledbackground=current_ac, state=DISABLED)
                                letter_guess_button.configure(text="Play Again", command=play_again)
                                display_user_message.configure(text="")
                                display_current_completion.configure(activeforeground="#ffffff", fg="#000000", bg=WCBG)
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
                                
                                # update highest streak
                                if current_streak > highest_streak:
                                    highest_streak = current_streak
                                    with open("high_score.txt", "w") as high_streak:
                                        print(f"{highest_streak}", file=high_streak)
                                        hs_txt.close()
                                
                                # update points
                                if points > highest_score:
                                    highest_score = points
                                    with open("high_score.txt", "w") as high_score:
                                        print(f"{highest_score}", file=high_score)
                                        hs_txt.close()
                                points -= 10
                                current_streak = 0
                                incorrect_total += 1
                                current_percentage = (correct_total / games_played) * 100
                                current_loss_percentage = (incorrect_total / games_played) * 100
                                display_points.configure(text=(f"{points}"))
                                show_streak.configure(text=(f"Streak: {current_streak}"))
                                stats_highest_streak.configure(text=(f"Highest\nStreak\n\n{highest_streak}"))
                                stats_high_score.configure(text=(f"High\nScore\n\n{highest_score}"))
                                stats_correct_out_of.configure(text=(f"Wins\n\n{correct_total} / {games_played}"))
                                stats_incorrect_out_of.configure(text=(f"Losses\n\n{incorrect_total} / {games_played}"))
                                stats_current_percentage.configure(text=(f"Win\nPercentage\n\n{current_percentage:.2f} %"))
                                stats_current_loss_percentage.configure(text=(f"Loss\nPercentage\n\n{current_loss_percentage:.2f} %"))
                                get_letter_guess.configure(disabledbackground=current_ac, state=DISABLED)
                                letter_guess_button.configure(text="Play Again", command=play_again)
                                sleep(1)
                                display_user_message.configure(text=(f"{country_name}"), fg="#000000", bg="#ffbb99")
                        else:
                            # repeat correct guess
                            correct_guess_container.configure(bg=WCBG)
                            display_user_message.configure(text=(f"[ {user_guess} ]"))
                            get_letter_guess.delete(0, END)
    
    # reconfigure/reset neccessary widgets/variables"""
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
        global index_count

        correct_letters = ""
        correct_guess = ""
        incorrect_guess = ""
        increment_guess = 0
        numbers_guessed = 0
        index_count = 0

        # select country
        shuffle(countries)
        country_name = choice(countries)

        # reconfigure widgets
        get_letter_guess.configure(state=NORMAL)
        stats_button.configure(bg=current_ac_2)
        letter_guess_button.configure(text="Enter", bg=current_ac_2, command=letter_entered)
        correct_guess_container.configure(text="")
        incorrect_guess_container.configure(text="")
        display_user_message.configure(text="", fg=current_fg, bg=current_bg)
        show_hint.configure(text="")
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
        
        count = 0
        for country in country_names:
            if country_name == country_names[count]:
                if len(country_facts[count]) > 0:
                    if len(country_facts[count]) == 1:
                        info = country_facts[count][index_count]
                        show_hint.configure(text=info)
                    elif len(country_facts[count]) > 1:
                        index_count = randint(0, len(country_facts[count]) - 1)
                        info = country_facts[count][index_count]
                        show_hint.configure(text=info)
                    info = country_facts[count][index_count]
                    show_hint.configure(text=info)
                else:
                    show_hint.configure(text="no available data at this time...")
            count += 1
    
    def size_toggle(width, height, get_font, font_size_2):
        """resize main window"""
        
        # globals
        global font
        global window_width
        global window_height
        global font_size
        
        font_size = get_font
        FONT=("Helvetica", font_size)
        window_width = width
        window_height = height
        MAIN_WINDOW.geometry(f"{window_width}x{window_height}")
        
        # main window
        x_pos = window_width / 2
        y_pos = window_height / 8

        # widgets b
        guide_window.configure(width=window_width - 40)
        prev_hint_button.configure(text="Prev.")
        next_hint_button.configure(text="Next")
        random_hint_button.configure(text="Rand.")

        display_region.configure(font=FONT)
        
        display_current_completion.configure(font=FONT)
        
        get_letter_guess.configure(font=FONT)
        letter_guess_button.configure(font=FONT)

        display_user_message.configure(font=FONT)
        
        display_correct_guess.configure(font=("Helvetica", font_size_2))
        display_incorrect_guess.configure(font=("Helvetica", font_size_2))
        correct_guess_container.configure(font=FONT)
        incorrect_guess_container.configure(font=FONT)
        show_streak.configure(font=("Helvetica", font_size))

        display_points.configure(font=FONT)
        bottom_right_label.configure(font=FONT)
        
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

        display_points.place(x=0, y=y_pos * 7, width=(window_width / 3), height=y_pos)
        show_streak.place(x=window_width / 3, y=y_pos * 7, width=(window_width / 3), height=y_pos)
        bottom_right_label.place(x=(window_width / 3) * 2, y=y_pos * 7, width=(window_width / 3), height=y_pos) 
        
        # window b
        hint_frame.place(x=0, y=0, width=400, height=y_pos * 8)
        hint_frame.lower()
        show_hint.place(x=0, y=0, width=400, height=window_height- 90)
        prev_hint_button.place(x=0, y=window_height - 90, width=400 / 4, height=70)
        next_hint_button.place(x=(0) + (400 / 4), y=window_height - 90, width=400 / 4, height=70)
        random_hint_button.place(x=(0) + (400 / 4) * 2, y=window_height - 90, width=400 / 4, height=70)
        close_hint_button.place(x=(0) + (400 / 4) * 3, y=window_height - 90, width=400 / 4, height=70)

        guide_frame.place(x=0, y=0, width=400, height=y_pos * 8)
        guide_frame.lower()
        guide_window.place(x=0, y=0, width=400, height=y_pos * 7)
        guide_window_close.place(x=0, y=(y_pos * 7) - 20, width=400, height=y_pos)
        
        stats_frame.place(x=0, y=0, width=x_pos * 2, height=y_pos * 8)
        stats_frame.lower()
        
        stats_highest_streak.place(x=0, y=0, width=400 / 2, height=window_height / 6)
        stats_high_score.place(x=400 / 2, y=0, width=400 / 2, height=window_height / 6)
        
        stats_current_percentage.place(x=0, y=window_height / 6, width=400 / 2, height=window_height / 6)
        stats_current_loss_percentage.place(x=400 / 2, y=window_height / 6, width=400 / 2, height=window_height / 6)

        stats_perfect_game.place(x=0, y=(window_height / 6) * 2, width=400 / 2, height=window_height / 6)
        stats_lucky_win.place(x=400 / 2, y=(window_height / 6) * 2, width=400 / 2, height=window_height / 6)
        
        stats_correct_out_of.place(x=0, y=(window_height / 6) * 3, width=400 / 2, height=window_height / 6)
        stats_incorrect_out_of.place(x=400 / 2, y=(window_height / 6) * 3, width=400 / 2, height=window_height / 6)
        
        stats_letters_correct.place(x=0, y=(window_height / 6) * 4, width=400 / 2, height=window_height / 6)
        stats_letters_incorrect.place(x=400 / 2, y=(window_height / 6) * 4, width=400 / 2, height=window_height / 6)
        
        stats_window_close.place(x=0, y=(window_height / 6) * 5, width=400, height=(window_height / 6) - 20)
        
        MAIN_WINDOW.update()
    
    def size_toggle_b(width, height, get_font, font_size_2):
        """resize main window"""
        
        # globals
        global font
        global window_width
        global window_height
        global font_size
        
        font_size = get_font
        FONT=("Helvetica", font_size)
        window_width = width
        window_height = height
        MAIN_WINDOW.geometry(f"{window_width}x{window_height}")
        
        guide_window.configure(width=window_width - 20)
        ## place widgets
        #main_window
        x_pos = 700 / 2
        y_pos = window_height / 8

        display_region.place(x=0, y=0, width=x_pos * 2, height=y_pos)
        
        display_current_completion.place(x=0, y=y_pos, width=x_pos * 2, height=y_pos * 2)
        
        stats_button.place(x=0, y=y_pos * 3, width=700 / 3, height=y_pos)
        get_letter_guess.place(x=700 / 3, y=y_pos * 3, width=700 / 3, height=y_pos)
        letter_guess_button.place(x=(700 / 3) * 2, y=y_pos * 3, width=700 / 3, height=y_pos)

        display_user_message.place(x=0, y=y_pos * 4, width=x_pos * 2, height=y_pos)
        
        display_correct_guess.place(x=0, y=y_pos * 5, width=x_pos, height=y_pos)
        display_incorrect_guess.place(x=x_pos, y=y_pos * 5, width=x_pos, height=y_pos)
        correct_guess_container.place(x=0, y=y_pos * 6, width=x_pos, height=y_pos)
        incorrect_guess_container.place(x=x_pos, y=y_pos * 6, width=x_pos, height=y_pos)

        display_points.place(x=0, y=y_pos * 7, width=(700 / 3), height=y_pos)
        show_streak.place(x=(700 / 3), y=y_pos * 7, width=(700 / 3), height=y_pos)
        bottom_right_label.place(x=(700 / 3) * 2, y=y_pos * 7, width=(700 / 3), height=y_pos) 
        
        # window b
        hint_frame.place(x=700, y=0, width=500, height=y_pos * 8)
        show_hint.place(x=0, y=0, width=500, height=window_height - 90)
        prev_hint_button.place(x=0, y=window_height - 90, width=500 / 3, height=70)
        next_hint_button.place(x=(0) + (500 / 3), y=window_height - 90, width=500 / 3, height=70)
        random_hint_button.place(x=(0) + (500 / 3) * 2, y=window_height - 90, width=500 / 3, height=70)
        prev_hint_button.configure(text="Previous")
        next_hint_button.configure(text="Next")
        random_hint_button.configure(text="Random")
        
        #temp fix #2500
        close_hint_button.place(x=(0) + (2500 / 3) * 3, y=window_height - 90, width=500 / 3, height=70)

        guide_frame.place(x=700, y=0, width=500, height=y_pos * 8)
        guide_frame.lower()
        guide_window.place(x=0, y=0, width=500, height=y_pos * 7)
        guide_window_close.place(x=0, y=(y_pos * 7) - 20, width=500, height=y_pos)
        
        stats_frame.place(x=700, y=0, width=x_pos * 2, height=y_pos * 8)
        stats_frame.lower()
        
        stats_highest_streak.place(x=0, y=0, width=500 / 2, height=window_height / 6)
        stats_high_score.place(x=500 / 2, y=0, width=500 / 2, height=window_height / 6)
        
        stats_current_percentage.place(x=0, y=window_height / 6, width=500 / 2, height=window_height / 6)
        stats_current_loss_percentage.place(x=500 / 2, y=window_height / 6, width=500 / 2, height=window_height / 6)
        
        stats_perfect_game.place(x=0, y=(window_height / 6) * 2, width=500 / 2, height=window_height / 6)
        stats_lucky_win.place(x=500 / 2, y=(window_height / 6) * 2, width=500 / 2, height=window_height / 6)
        
        stats_correct_out_of.place(x=0, y=(window_height / 6) * 3, width=500 / 2, height=window_height / 6)
        stats_incorrect_out_of.place(x=500 / 2, y=(window_height / 6) * 3, width=500 / 2, height=window_height / 6)
        
        stats_letters_correct.place(x=0, y=(window_height / 6) * 4, width=500 / 2, height=window_height / 6)
        stats_letters_incorrect.place(x=500 / 2, y=(window_height / 6) * 4, width=500 / 2, height=window_height / 6)
        
        stats_window_close.place(x=0, y=(window_height / 6) * 5, width=500, height=(window_height / 6) - 20)
        

        MAIN_WINDOW.update()
    

    # size toggles
    def toggle_size_a():
        size_toggle(400, 400, 14, 20)
    
    def toggle_size_b():
        size_toggle_b(1200, 600, 14, 20)

    def set_fg_colour(colour):
        """sets foreground colour"""
        
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
        display_points.configure(fg=FG)
        bottom_right_label.configure(fg=FG)
        guide_frame.configure(fg=FG)
        stats_frame.configure(fg=FG)
        stats_highest_streak.configure(fg=FG)
        stats_high_score.configure(fg=FG)
        stats_current_percentage.configure(fg=FG)
        stats_current_loss_percentage.configure(fg=FG)
        stats_perfect_game.configure(fg=FG)
        stats_lucky_win.configure(fg=FG)
        stats_correct_out_of.configure(fg=FG)
        stats_incorrect_out_of.configure(fg=FG)
        stats_window_close.configure(fg=FG)
        show_streak.configure(fg=FG)
        stats_letters_correct.configure(fg=FG)
        stats_letters_incorrect.configure(fg=FG)
        guide_window_close.configure(fg=FG)
        stats_button.configure(fg=FG)
        show_hint.configure(fg=FG)
        prev_hint_button.configure(fg=FG)
        random_hint_button.configure(fg=FG)
        next_hint_button.configure(fg=FG)
        close_hint_button.configure(fg=FG)
    
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
        display_points.configure(bg=BG)
        bottom_right_label.configure(bg=BG)
        guide_frame.configure(bg=BG)
        stats_frame.configure(bg=BG)
        stats_window_close.configure(bg=BG)
        guide_window_close.configure(bg=BG)
        show_hint.configure(bg=BG)
        prev_hint_button.configure(bg=BG)
        random_hint_button.configure(bg=BG)
        next_hint_button.configure(bg=BG)
        close_hint_button.configure(bg=BG)
    
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
        stats_high_score.configure(bg=AC)
        stats_current_percentage.configure(bg=AC)
        stats_current_loss_percentage.configure(bg=AC)
        stats_perfect_game.configure(bg=AC)
        stats_lucky_win.configure(bg=AC)
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
        display_points.configure(bg=AC_2)
        bottom_right_label.configure(bg=AC_2)
    
    def set_active_bg_colour(colour):
        """sets active background colour"""

        #globals
        global current_actvbg

        ACTVBG = colour
        current_actvbg

        stats_button.configure(activebackground=ACTVBG)
        letter_guess_button.configure(activebackground=ACTVBG)
        bottom_right_label.configure(activebackground=ACTVBG)
        guide_window_close.configure(activebackground=ACTVBG)
        stats_window_close.configure(activebackground=ACTVBG)
        prev_hint_button.configure(activebackground=ACTVBG)
        next_hint_button.configure(activebackground=ACTVBG)
        random_hint_button.configure(activebackground=ACTVBG)
        close_hint_button.configure(activebackground=ACTVBG)

    def colour_get(fg, bg, ac, ac_2, actvbg):
        """set foreground/background and primary/secondary accent colours"""

        # globals
        global current_fg
        global current_bg
        global current_ac
        global current_actvbg

        current_fg = fg
        current_bg = bg
        current_ac = ac
        current_ac_2 = ac_2
        current_actvbg = actvbg

        set_fg_colour(fg)
        set_bg_colour(bg)
        set_accent_colour(ac)
        set_accent_colour_b(ac_2)
        set_active_bg_colour(actvbg)

        with open("colourscheme.txt", "w") as f:
            current_colourscheme_bg = bg[1:]
            current_colourscheme_actv = actvbg[1:]
            print(f"{current_colourscheme_bg}\n{current_colourscheme_actv}", file=f)
            f.close()
    
    # samba
    def select_colour_samba():
        colour_get("#ffffff", "#140000", "#140000", "#140000", "#ffcccc")
    
    def select_colour_samba_sunda():
        colour_get("#ffffff", "#140000", "#140000", "#140000", "#6a604d")
    
    def select_colour_samba_snow():
        colour_get("#ffffff", "#140000", "#140000", "#140000", "#ffffff")
    
    def select_colour_samba_cara():
        colour_get("#ffffff", "#140000", "#140000", "#140000", "#a58c79")
    
    def select_colour_dune():
        colour_get("#000000", "#ffffbb", "#ffffcc", "#ffffdd", "#ffee77")

    # mint
    def select_colour_mint():
        colour_get("#000000", "#ddffcc", "#eeffdd", "#eeffee", "#99ff99")

    # cobalt
    def select_colour_cobalt():
        colour_get("#ffffff", "#000007", "#000007", "#000007", "#dddddd")
    
    def select_colour_cobalt_snow():
        colour_get("#ffffff", "#000007", "#000007", "#000007", "#ffffff")
    
    def select_colour_cobalt_cara():
        colour_get("#ffffff", "#000007", "#000007", "#000007", "#a58c79")

    def select_colour_cobalt_lynx():
        colour_get("#ffffff", "#000007", "#000007", "#000007", "#767a7d")

    # black
    def select_colour_black():
        colour_get("#ffffff", "#000000", "#000000", "#000000", "#dddddd")
    
    def select_colour_black_corsac():
        colour_get("#ffffff", "#000000", "#000000", "#000000", "#8d6c44")
    
    def select_colour_black_fennec():
        colour_get("#ffffff", "#000000", "#000000", "#000000", "#bd9d85")

    def select_colour_black_lynx():
        colour_get("#ffffff", "#000000", "#000000", "#000000", "#767a7d")
    
    # pearl
    def select_colour_pearl():
        colour_get("#000000", "#eeeeee", "#dddddd", "#eeeeee", "#ffaa99")
    
    def select_colour_pearl_corsac():
        colour_get("#000000", "#eeeeee", "#dddddd", "#eeeeee", "#8d6c44")
    
    def select_colour_pearl_fennec():
        colour_get("#000000", "#eeeeee", "#dddddd", "#eeeeee", "#bd9d85")

    def select_colour_pearl_lynx():
        colour_get("#000000", "#eeeeee", "#dddddd", "#eeeeee", "#767a7d")
    

    def exit_cmd():
        """save current high score and exit"""

        global highest_streak
        global highest_score

        # update highest streak / update high score
        if current_streak > highest_streak:
            highest_streak = current_streak
            with open("highest_streak.txt", "w") as hs_txt:
                print(f"{highest_streak}", file=hs_txt)
                hs_txt.close()
        
        # update points
        if points > highest_score:
            highest_score = points
            with open("high_score.txt", "w") as hs_txt:
                print(f"{highest_score}", file=hs_txt)
                hs_txt.close()
        sys.exit()

    # widgets a
    display_region = Label(text="All Regions", font=FONT, fg=FG, bg=BG)
    
    stats_button = Button(text="Stats",font=FONT, fg=FG, bg=AC_2, activebackground=ACTVBG, bd=BD, relief=RLF_2,
            command=stats_show)

    get_letter_guess = Entry(font=FONT, fg=FG, bg=AC, bd=BD, relief=SUNKEN, justify=CENTER)
    letter_guess_button = Button(text="Enter",font=FONT, fg=FG, bg=AC_2, activebackground=ACTVBG, bd=BD, relief=RLF_2,
            command=letter_entered)
    
    display_correct_guess = Label(text="+", font=("Helvetica", 20), fg=FG, bg=BG, bd=BD, relief=RLF_3)
    correct_guess_container = Label(font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=SUNKEN)
    
    display_current_completion = Label(text=(f"{correct_letters}"), font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=RLF_2)
    display_incorrect_guess = Label(text=f"-", font=("Helvetica", 20), fg=FG, bg=BG, bd=BD, relief=RLF_3)
    incorrect_guess_container = Label(font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=SUNKEN)
    
    display_user_message = Label(text="", font=FONT, fg=FG, bg=BG)
    
    display_points = Label(text=(f"{points}"), font=FONT, fg=FG, bg=AC_2, bd=BD, relief=RLF_2, disabledforeground=FG)
    
    show_streak = Label(text=(f"Streak: {current_streak}"), font=FONT, fg=FG, bg=AC, bd=BD - 2, relief=RLF_2)
    bottom_right_label = Label(font=FONT, fg=FG, bg=AC_2, bd=BD, relief=RLF_2, activebackground=ACTVBG)
    
    guide_frame = LabelFrame(MAIN_WINDOW, text="Guide", font=FONT, fg=FG, bg=BG, bd=BD - 2, relief=RIDGE)
    guide_text = open("guide.txt", "r")
    guide_window = Message(guide_frame, text=(f"{guide_text.read()}"), width=window_width - 20, font=("Helvetica", 10), fg="#000000", bg="#dddddd", bd=BD - 2, relief=RLF_3, justify=CENTER)
    guide_window_close = Button(guide_frame, text=(f"Close"), font=FONT, fg=FG, bg=BG, bd=BD, relief=RLF_2, activebackground=ACTVBG, 
            command=close_guide_show)

    stats_frame = LabelFrame(MAIN_WINDOW, text="Stats", font=FONT, fg=FG, bg=BG, bd=BD - 2, relief=GROOVE)
    
    stats_highest_streak = Label(stats_frame, text=(f"Highest\nStreak\n\n{highest_streak}"),font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_high_score = Label(stats_frame, text=(f"High\nScore\n\n{highest_score}"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_perfect_game = Label(stats_frame, text=(f"Perfect\nGames\n\n{perfect_game}"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_lucky_win = Label(stats_frame, text=(f"Lucky\nWins\n\n{lucky_win}"),font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_current_percentage = Label(stats_frame, text=(f"Win\nPercentage\n\n{current_percentage:.0f} %"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_current_loss_percentage = Label(stats_frame, text=(f"Loss\nPercentage\n\n{current_loss_percentage:.0f} %"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_correct_out_of = Label(stats_frame, text=(f"Wins\n\n{correct_out_of} / {games_played}"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_incorrect_out_of = Label(stats_frame, text=(f"Losses\n\n{incorrect_out_of} / {games_played}"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_letters_correct = Label(stats_frame, text=(f"Correct\nLetters\n\n{letters_correct}"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_letters_incorrect = Label(stats_frame, text=(f"Incorrect\nLetters\n\n{letters_incorrect}"), font=("Helvetica", 10), fg=FG, bg=AC, bd=BD, relief=RLF_2)
    stats_window_close = Button(stats_frame, text=(f"Close"), font=FONT, fg=FG, bg=BG, bd=BD, relief=RLF_2, activebackground=ACTVBG, command=close_stats_show)

    # widgets b
    hint_frame = LabelFrame(MAIN_WINDOW, text="Hint", font=FONT, fg=FG, bg=BG, bd=BD - 2, relief=GROOVE)
    show_hint = Label(hint_frame, font=FONT, fg=FG, bg=BG, padx=100, wraplength=300)
    show_first_hint()
    prev_hint_button = Button(hint_frame, text="Previous", font=FONT, fg=FG, bg=AC, bd=BD, relief=RLF_2, activebackground=ACTVBG,
            command=get_prev_hint)
    next_hint_button = Button(hint_frame, text="Next", font=FONT, fg=FG, bg=AC, bd=BD, relief=RLF_2, activebackground=ACTVBG,
            command=get_next_hint)
    random_hint_button = Button(hint_frame, text="Random", font=FONT, fg=FG, bg=AC, bd=BD, relief=RLF_2, activebackground=ACTVBG,
            command=get_random_hint)
    close_hint_button = Button(hint_frame, text="Close", font=FONT, fg=FG, bg=AC, bd=BD, relief=RLF_2, activebackground=ACTVBG,
            command=close_hint_show)

    # place widgets
    #main_window
    x_pos = 700 / 2
    y_pos = window_height / 8

    display_region.place(x=0, y=0, width=x_pos * 2, height=y_pos)
    
    display_current_completion.place(x=0, y=y_pos, width=x_pos * 2, height=y_pos * 2)
    
    stats_button.place(x=0, y=y_pos * 3, width=700 / 3, height=y_pos)
    get_letter_guess.place(x=700 / 3, y=y_pos * 3, width=700 / 3, height=y_pos)
    letter_guess_button.place(x=(700 / 3) * 2, y=y_pos * 3, width=700 / 3, height=y_pos)

    display_user_message.place(x=0, y=y_pos * 4, width=x_pos * 2, height=y_pos)
    
    display_correct_guess.place(x=0, y=y_pos * 5, width=x_pos, height=y_pos)
    display_incorrect_guess.place(x=x_pos, y=y_pos * 5, width=x_pos, height=y_pos)
    correct_guess_container.place(x=0, y=y_pos * 6, width=x_pos, height=y_pos)
    incorrect_guess_container.place(x=x_pos, y=y_pos * 6, width=x_pos, height=y_pos)

    display_points.place(x=0, y=y_pos * 7, width=(700 / 3), height=y_pos)
    show_streak.place(x=(700 / 3), y=y_pos * 7, width=(700 / 3), height=y_pos)
    bottom_right_label.place(x=(700 / 3) * 2, y=y_pos * 7, width=(700 / 3), height=y_pos) 
    
    # window b
    hint_frame.place(x=700, y=0, width=500, height=y_pos * 8)
    show_hint.place(x=0, y=0, width=500, height=window_height - 90)
    prev_hint_button.place(x=0, y=window_height - 90, width=500 / 3, height=70)
    next_hint_button.place(x=(0) + (500 / 3), y=window_height - 90, width=500 / 3, height=70)
    random_hint_button.place(x=(0) + (500 / 3) * 2, y=window_height - 90, width=500 / 3, height=70)
    
    # place guide
    guide_frame.place(x=700, y=0, width=500, height=y_pos * 8)
    guide_frame.lower()
    guide_window.place(x=0, y=0, width=500, height=y_pos * 7)
    guide_window_close.place(x=0, y=(y_pos * 7) - 20, width=500, height=y_pos)
    
    # place stats
    stats_frame.place(x=700, y=0, width=x_pos * 2, height=y_pos * 8)
    stats_frame.lower()
    
    stats_highest_streak.place(x=0, y=0, width=500 / 2, height=window_height / 6)
    stats_high_score.place(x=500 / 2, y=0, width=500 / 2, height=window_height / 6)

    stats_current_percentage.place(x=0, y=window_height / 6, width=500 / 2, height=window_height / 6)
    stats_current_loss_percentage.place(x=500 / 2, y=window_height / 6, width=500 / 2, height=window_height / 6) 
    
    stats_perfect_game.place(x=0, y=(window_height / 6) * 2, width=500 / 2, height=window_height / 6)
    stats_lucky_win.place(x=500 / 2, y=(window_height / 6) * 2, width=500 / 2, height=window_height / 6)
    
    stats_correct_out_of.place(x=0, y=(window_height / 6) * 3, width=500 / 2, height=window_height / 6)
    stats_incorrect_out_of.place(x=500 / 2, y=(window_height / 6) * 3, width=500 / 2, height=window_height / 6)
    
    stats_letters_correct.place(x=0, y=(window_height / 6) * 4, width=500 / 2, height=window_height / 6)
    stats_letters_incorrect.place(x=500 / 2, y=(window_height / 6) * 4, width=500 / 2, height=window_height / 6)

    stats_window_close.place(x=0, y=(window_height / 6) * 5, width=500, height=(window_height / 6) - 20)

    # retrieve colourscheme
    with open("colourscheme.txt", "r") as f:
        saved_colourscheme = f.read()
        saved_colourscheme_bg = saved_colourscheme[:6]
        saved_colourscheme_actvbg = saved_colourscheme[6:]
        
        # samba
        if saved_colourscheme_bg.strip() == "140000" and saved_colourscheme_actvbg.strip() == "ffcccc":
            select_colour_samba()
        elif saved_colourscheme_bg.strip() == "140000" and saved_colourscheme_actvbg.strip() == "6a604d":
            select_colour_samba_sunda()
        elif saved_colourscheme_bg.strip() == "140000" and saved_colourscheme_actvbg.strip() == "ffffff":
            select_colour_samba_snow()
        elif saved_colourscheme_bg.strip() == "140000" and saved_colourscheme_actvbg.strip() == "a58c79":
            select_colour_samba_cara()
        
        # dune
        elif saved_colourscheme_bg.strip() == "ffffbb" and saved_colourscheme_actvbg.strip() == "ffee77":
            select_colour_dune()
        
        # mint
        elif saved_colourscheme_bg.strip() == "ddffcc" and saved_colourscheme_actvbg.strip() == "99ff99":
            select_colour_mint()
        
        # cobalt
        elif saved_colourscheme_bg.strip() == "000007" and saved_colourscheme_actvbg.strip() == "dddddd":
            select_colour_cobalt()
        elif saved_colourscheme_bg.strip() == "000007" and saved_colourscheme_actvbg.strip() == "ffffff":
            select_colour_cobalt_snow()
        elif saved_colourscheme_bg.strip() == "000007" and saved_colourscheme_actvbg.strip() == "a58c79":
            select_colour_cobalt_cara()
        elif saved_colourscheme_bg.strip() == "000007" and saved_colourscheme_actvbg.strip() == "767a7d":
            select_colour_cobalt_lynx()
        
        # black
        elif saved_colourscheme_bg.strip() == "000000" and saved_colourscheme_actvbg.strip() == "dddddd":
            select_colour_black()
        elif saved_colourscheme_bg.strip() == "000000" and saved_colourscheme_actvbg.strip() == "8d6c44":
            select_colour_black_corsac()
        elif saved_colourscheme_bg.strip() == "000000" and saved_colourscheme_actvbg.strip() == "bd9d85":
            select_colour_black_fennec()
        elif saved_colourscheme_bg.strip() == "000000" and saved_colourscheme_actvbg.strip() == "767a7d":
            select_colour_black_lynx()
        
        # pearl
        elif saved_colourscheme_bg.strip() == "eeeeee" and saved_colourscheme_actvbg.strip() == "ffaa99":
            select_colour_pearl()
        elif saved_colourscheme_bg.strip() == "eeeeee" and saved_colourscheme_actvbg.strip() == "8d6c44":
            select_colour_pearl_corsac()
        elif saved_colourscheme_bg.strip() == "eeeeee" and saved_colourscheme_actvbg.strip() == "bd9d85":
            select_colour_pearl_fennec()
        elif saved_colourscheme_bg.strip() == "eeeeee" and saved_colourscheme_actvbg.strip() == "767a7d":
            select_colour_pearl_lynx()
        
        f.close()
    
    #display_bar
    x_pos = 500
    y_pos = window_height

    # set menu
    top_menu = Menu(MAIN_WINDOW)
    settings_menu = Menu(top_menu)
    
    # scale menu
    window_scale_menu = Menu(settings_menu)
    window_scale_menu.add_command(label="400x400", command=toggle_size_a)
    window_scale_menu.add_command(label="1200x600  (default)", command=toggle_size_b)
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
    colour_samba_menu = Menu(colourscheme_menu)
    colour_samba_menu.add_command(label="Samba", command=select_colour_samba)
    colour_samba_menu.add_command(label="Samba Sunda", command=select_colour_samba_sunda)
    colour_samba_menu.add_command(label="Samba Snow", command=select_colour_samba_snow)
    colour_samba_menu.add_command(label="Samba Cara", command=select_colour_samba_cara)
    colourscheme_menu.add_cascade(label="Samba", menu=colour_samba_menu)
    colourscheme_menu.add_command(label="Dune", command=select_colour_dune)
    colourscheme_menu.add_command(label="Mint", command=select_colour_mint)
    colour_cobalt_menu = Menu(colourscheme_menu)
    colour_cobalt_menu.add_command(label="Cobalt", command=select_colour_cobalt)
    colour_cobalt_menu.add_command(label="Cobalt Snow", command=select_colour_cobalt_snow)
    colour_cobalt_menu.add_command(label="Cobalt Cara", command=select_colour_cobalt_cara)
    colour_cobalt_menu.add_command(label="Cobalt Lynx", command=select_colour_cobalt_lynx)
    colourscheme_menu.add_cascade(label="Cobalt", menu=colour_cobalt_menu)
    colour_black_menu = Menu(colourscheme_menu)
    colour_black_menu.add_command(label="Black", command=select_colour_black)
    colour_black_menu.add_command(label="Black Corsac", command=select_colour_black_corsac)
    colour_black_menu.add_command(label="Black Fennec", command=select_colour_black_fennec)
    colour_black_menu.add_command(label="Black Lynx", command=select_colour_black_lynx)
    colourscheme_menu.add_cascade(label="Black", menu=colour_black_menu)
    colour_pearl_menu = Menu(colourscheme_menu)
    colour_pearl_menu.add_command(label="Pearl", command=select_colour_pearl)
    colour_pearl_menu.add_command(label="Pearl Corsac", command=select_colour_pearl_corsac)
    colour_pearl_menu.add_command(label="Pearl Fennec", command=select_colour_pearl_fennec)
    colour_pearl_menu.add_command(label="Pearl Lynx", command=select_colour_pearl_lynx)
    colourscheme_menu.add_cascade(label="Pearl", menu=colour_pearl_menu)
    settings_menu.add_cascade(label="Colorscheme", menu=colourscheme_menu)
    settings_menu.add_separator()
    settings_menu.add_command(label="Exit", command=exit_cmd, accelerator="Ctrl+Q")
    top_menu.add_cascade(label="Settings", menu=settings_menu)
    
    # about menu
    about_menu = Menu(top_menu)
    about_menu.add_command(label="Guide", command=guide_show, accelerator="Ctrl+H")
    about_menu.add_command(label="Stats", command=stats_show, accelerator="Ctrl+T")
    about_menu.add_command(label="Hints", command=hint_show, accelerator="Ctrl+N")
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
    
    def callback_open_hint(event):
        hint_show()
    
    def callback_close_hint(event):
        close_hint_show()
    
    def callback_previous_hint(event):
        get_prev_hint()
    
    def callback_random_hint(event):
        get_random_hint()
    
    def callback_next_hint(event):
        get_next_hint()

    MAIN_WINDOW.bind("<Control-KeyPress-s>", callback_play_again)
    MAIN_WINDOW.bind("<Control-KeyPress-q>", callback_exit)
    MAIN_WINDOW.bind("<Return>", callback_letter_guess)
    MAIN_WINDOW.bind("<Control-KeyPress-a>", callback_shuffle_region)
    MAIN_WINDOW.bind("<Control-KeyPress-h>", callback_open_guide)
    MAIN_WINDOW.bind("<Control-Alt-KeyPress-h>", callback_close_guide)
    MAIN_WINDOW.bind("<Control-KeyPress-t>", callback_open_stats)
    MAIN_WINDOW.bind("<Control-Alt-KeyPress-t>", callback_close_stats)
    MAIN_WINDOW.bind("<Control-KeyPress-n>", callback_open_hint)
    MAIN_WINDOW.bind("<Control-Alt-KeyPress-n>", callback_close_hint)
    MAIN_WINDOW.bind("<Control-KeyPress-Right>", callback_previous_hint)
    MAIN_WINDOW.bind("<Control-KeyPress-Right>", callback_previous_hint)
    MAIN_WINDOW.bind("<Control-KeyPress-Up>", callback_random_hint)
    MAIN_WINDOW.bind("<Control-KeyPress-Left>", callback_next_hint)

    # mainloop
    MAIN_WINDOW.mainloop()


if __name__ == '__main__':
    main()
