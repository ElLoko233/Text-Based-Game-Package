# Remember to load extractors to each level

# Task
# > Load storyline
# >> With background music

# > load quest
# >> begin explorer loop
# >> Test if objective is  met
# >> print dialog

# repeat
if __name__ == "__main__":

    # =================================

    # Quest1 imports
    from Project_peaces.Quest1.main import Quest1
    from Project_peaces.Quest1.Dialog import Quest1_Dialog

    from Project_peaces import StoryLine
    from TBG.player import Player
    from pyfiglet import figlet_format
    from typewriter.typewriter import typing
    from time import sleep

    try:
        from pygame import mixer, error

        # Initialising the mixer for playing background music
        mixer.init()

    except ImportError:
        pass
    # =================================

    # Creating the player
    Maria = Player('Maria', max_hp=100, defence=100)
    Maria.backstory = """
    Maria is a passionate tribes women, she has studied all the scrolls about her religion.
    She does all of this because her father died in battle of retrieving the dragon egg, and just like 
    all the tribes women she felt proud of what her father was fighting for and thus she developed the interest of
    her people's history.
    """

    # Loading storyline
    Title = figlet_format("                             The Ender Dragon", "digital")
    typing(Title, 0.00001)

    # Testing if player wishes to begin the game
    start = input("Yes/No to start the game: ")

    if start == "yes" or start == "Yes":

        # Playing background music
        main_bg_track = 'Main_bg.mp3'
        try:
            mixer.music.load(main_bg_track)
            mixer.music.play(-1)

        except (TypeError, error):  # If music_dir is equal to "None"
            pass
        # =========================

        # Loading storyline text
        typing(StoryLine.Story_line['Introduction'], 0.045)     #Loading the intro
        typing(StoryLine.Story_line['Paragraph1'], 0.045)   #Loading the first paragraph
        typing(StoryLine.Story_line['Paragraph2'], 0.045)  # Loading the second paragraph
        #   Fade out of background music
        try:
            mixer.music.fadeout(6500)
        except (TypeError, error):
            pass
        # ==============================

        # Loading in the Quest1
        typing(f"{'>>' * 10}Quest 1: The real Truth{'<<' * 10}")
        typing(StoryLine.Quests['Quest1'], 0.045)

        # Starting the quest exploration
        while True:

            Quest1.explore_loop(Maria)

            # Testing if player reached objective
            if Maria.location.name == "Whispering_cave":
                typing(f"{'>>' * 10}Objective reached!!{'<<' * 10}", 0.045)
                break
            else:
                typing("Objective not reached")
                typing(StoryLine.Quests['Quest1'], 0.045)

        # printing  dialog

        # Playing background sounds
        cave_noises = 'Cave_noises.mp3'
        try:
            mixer.music.load(cave_noises)
            mixer.music.play(-1)

        except (TypeError, error):  # If music_dir is equal to "None"
            print('playing cave noises')
        # ===========================

        # Printing Old sage's word
        try:
            times = max([len(Quest1_Dialog['Old Sage']), len(Quest1_Dialog['Maria'])])
            for i in range(9, times):
                typing('Old Sage: ' + Quest1_Dialog['Old Sage'][i], 0.1)

                # Printing Maria's words
                typing('Maria: ' + Quest1_Dialog['Maria'][i], 0.1)
        except IndexError:
            pass

            # Fade out of background music
            try:
                mixer.music.fadeout(1000)
                sleep(1.5)
            except (TypeError, error):
                pass
        # ===============================End of first Quest =====================================


        # Second Quest begins =======================================
        # Starting the quest exploration
        typing(f"{'>>' * 10}Quest 2: If only{'<<' * 10}")
        typing(StoryLine.Quests['Quest2'], 0.045)

        # Loading in new items
        from Project_peaces.Quest2.Quest2_peaces import Dragon_scroll, Doki, Quest2_dialog
        from Project_peaces.Quest1.Rooms.Quest1_locations import Hambonathi

        Hambonathi.items[Dragon_scroll.name] = Dragon_scroll

        while True:

            Quest1.explore_loop(Maria)

            # Testing if player reached objective
            if Maria.location.name == "Whispering_cave" and len(Maria.fight_moves) > 0:
                typing(f"{'>>' * 10}Objective reached!!{'<<' * 10}", 0.045)
                break

            else:
                typing("Objective not reached")
                typing(StoryLine.Quests['Quest2'], 0.045)

        # Print dialog

        for name in Quest2_dialog:
            typing(f'{name[:-1]}: ' + Quest2_dialog[name], 0.035)

        # Begin battle scene
        while True:
            Quest1.battle_loop(player=Maria, enemy=Doki)

            if Doki.hp <= 0:
                typing("You are die")
                continue
            else:
                typing("Ypu won, Thank you for playing")
                break
    else:

        typing("Thank you for your time.", 0.1)
