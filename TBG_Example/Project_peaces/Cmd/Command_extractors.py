
from TBG.CMD import Cmd

""""
Here I have created the Cmd objects required to play the game,
I also added the synonyms using the regex pattern format.

Some patterns won't have <arg1> value for them and that's because 
they are linked to function that don't require an argument
"""

# Creating extractor for 'eat' related words
eat = Cmd('eat')
# > creating synonyms for the Cmd object
eat1 = r"([E,e]at)(\s*)(?P<arg1>[\w\s\']*)"
eat2 = r"([C,c]onsume)(\s*)(?P<arg1>[\w\s\']*)"

eat.command_list = [eat1, eat2]
# =================================================

# Creating extractor for 'ex-help' related words
ex_help = Cmd('ex_help')
# > creating synonyms for the Cmd object
ex_help1 = r"([A,a]ssistance)(\s*)"
ex_help2 = r"([E,x][\s]*help)(\s*)"

ex_help.command_list = [ex_help1, ex_help2]
# =================================================

# Creating extractor for 'battle_help' related words
battle_help = Cmd('battle_help')
# > creating synonyms for the Cmd object
battle_help1 = r"([a,A]ssistance)(\s*)"
battle_help2 = r"([B,b]attle[\s]*help)(\s*)"

battle_help.command_list = [battle_help1, battle_help2]
# =================================================

# Creating extractor for 'goto' related words
goto = Cmd('goto')
# > creating synonyms for the Cmd object
goto1 = r"([E,e]nter)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
goto2 = r"([v,V]isit)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
goto3 = r"([G,g]o[\s]*to)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

goto.command_list = [goto1, goto2, goto3]
# =================================================

# Creating extractor for 'look_around' related words
look_around = Cmd('look_around')
# > creating synonyms for the Cmd object
look_around1 = r"([G,g]aze)(\s*)"
look_around2 = r"([l,L]ook[\s]*around)(\s*)"

look_around.command_list = [look_around1, look_around2]
# =================================================

# Creating extractor for 'examine_item' related words
examine_item = Cmd('examine_item')
# > creating synonyms for the Cmd object
examine_item1 = r"([E,e]xamine)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
examine_item2 = r"([L,l]ook[\s]*at)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

examine_item.command_list = [examine_item1, examine_item2]
# =================================================

# Creating extractor for 'throw' related words
throw = Cmd('throw')
# > creating synonyms for the Cmd object
throw1 = r"([D,d]ispose)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
throw2 = r"([T,t]hrow[\s]*away)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

throw.command_list = [throw1, throw2]
# =================================================

# Creating extractor for 'talk' related words
talk = Cmd('talk')
# > creating synonyms for the Cmd object
talk1 = r"([C,c]onverse)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
talk2 = r"([A,a]pproach)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
talk3 = r"([T,t]alk[\s]*to)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

talk.command_list = [talk1, talk2, talk3]
# =================================================

# Creating extractor for 'take_item' related words
take_item = Cmd('take_item')
# > creating synonyms for the Cmd object
take_item1 = r"([S,s]teal)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
take_item2 = r"([T,t]ake)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

take_item.command_list = [take_item1, take_item2]
# =================================================

# Creating extractor for 'search_inv' related words
search_inv = Cmd('search_inv')
# > creating synonyms for the Cmd object
search_inv1 = r"([S,s]earch[\s]*inventory)(\s*)"
search_inv2 = r"([M,m]y[\s]*stuff)(\s*)"

search_inv.command_list = [search_inv1, search_inv2]
# =================================================

# Creating extractor for 'stats' related words
stats = Cmd('stats')
# > creating synonyms for the Cmd object
stats1 = r"([S,s]tatistics)(\s*)"
stats2 = r"([A,a]bilities)(\s*)"

stats.command_list = [stats1, stats2]
# =================================================

# Creating extractor for 'my_story' related words
my_story = Cmd('my_story')
# > creating synonyms for the Cmd object
my_story1 = r"([B,b]ack[\s]*story)(\s*)"
my_story2 = r"([M,m]y[\s]*story)(\s*)"

my_story.command_list = [my_story1, my_story2]
# =================================================

# Creating extractor for 'show_move' related words
show_move = Cmd('show_move')
# > creating synonyms for the Cmd object
show_move1 = r"([M,m]y[\s]*move)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
show_move2 = r"([S,s]kill)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

show_move.command_list = [show_move1, show_move2]
# =================================================

# Creating extractor for 'learn' related words
learn = Cmd('learn')
# > creating synonyms for the Cmd object
learn1 = r"([S,s]tudy)(\s*)(?P<arg1>[\w\s\']+)(\s*)"
learn2 = r"([L,l]earn)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

learn.command_list = [learn1, learn2]
# =================================================

# Creating extractor for 'enhance' related words
enhance = Cmd('enhance')
# > creating synonyms for the Cmd object
enhance1 = r"([e,E]nhance[\s]*with)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
enhance2 = r"([T,t]rain)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

enhance.command_list = [enhance1, enhance2]
# =================================================

# Creating extractor for 'equip' related words
equip = Cmd('equip')
# > creating synonyms for the Cmd object
equip1 = r"([W,w]ear)(\s*)(?P<arg1>[\w\s\'\s]*)(\s*)"
equip2 = r"([p,P]ut[\s]*on)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

equip.command_list = [equip1, equip2]
# =================================================

# Creating extractor for 'attack' related words
attack = Cmd('attack')
# > creating synonyms for the Cmd object
attack1 = r"([A,a]ttack[\s]*with)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
attack2 = r"([U,u]se)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

attack.command_list = [attack1, attack2]
# =================================================

# Creating extractor for 'proceed' related words
proceed = Cmd('proceed')
# > creating synonyms for the Cmd object
proceed1 = r"([p,P]roceed)(\s*)(?P<arg1>[\w\s\']*)(\s*)"
proceed2 = r"([C,c]ontinue)(\s*)(?P<arg1>[\w\s\']*)(\s*)"

proceed.command_list = [proceed1, proceed2]
# =================================================

# loading all the extractors into a list
Cmd_instances = [goto, attack, equip, enhance, learn, show_move, my_story, stats, search_inv, take_item, talk, throw,
                 examine_item, look_around, ex_help, battle_help, eat, proceed]



# Help text explaining the function of each synonymy
explorer_help_text = """
>> How to play?

On playing the game you will see this 'Command: ' here you will
input what you want to do next. There are multiple options to pick from
based on your needs of exploration.

Command types:

1.  Command: gaze/look around 
>   This command is used to display the items, people, exits available a Room.
eg. Command: look around

2.  Command: enter/visit Name_of_Room
>   This command is used to change the player's location/Room.
    Input the command followed by the name of the Room
eg. Command: enter Johnny's_House

3.  Command: steal/take Name_of_item
>   This command is used to take items from a Room.
    Input the command followed by the name of the item
eg. Command: take Phone

4.  Command: dispose/throw away Name_of_item
>   This command is used to throw away items from your inventory.
    Input the command followed by the name of the item
eg. Command: throw away Phone

5.  Command: examine/look at Name_of_item
>   This command is used to display the attribute of an item from your inventory.
    Input the command followed by the name of the item.
eg. Command: examine Phone 

6.  Command: search inventory/my stuff
> This command is used to display the names of items that are in your inventory.
eg. Command: search inventory

7.  Command: statistics/abilities
>   This command is used to display the attribute of the player.
eg Command: abilities

8.  Command: back story/my story
>   This command is used to display the players back story.
eg Command: back story

9.  Command: study/learn Name_of_item
>   This command is used to give player a new set of fighting moves
    Input the command followed by the name of the item
eg. Command: study Dragon_scroll

10. Command: enhance with/train Name_of_item
>   This command is used to increase damage of player's fighting move set, provided
    that they are of the same style.
    Input the command followed by the name of the item
eg. Command: train Dumbbell

11. Command: my move/skill Name_of_fighting_move
>   This command is used to display the attribute of a player's fighting move.
    Input the command followed by the name of the fight move
eg. Command: skill Dragon_kick

12. Command: wear/put on Name_of_armor
>   This command is allows the player to equip armor.
    Input the command followed by the name of the armor
eg. Command: wear T-shirt

13. Command: converse/approach Name_of_NPC
>   This command is used for talking to NPCs in the game
    Input the command followed by the name of NPC
eg. Command: approach Mummy

14. Command: eat/consume Name_of_item
>   This command is used to eat food from the game. 
    Input the command followed by the name of the item
eg. Command: eat Pizza
    
15. Command: proceed/continue
>   This command will end the game loop inorder to proceed.
eg. Command: proceed

"""

battle_help_text = """
>> How to play?

On playing the game you will see this 'Command: ' here you will
input what you want to do next. There are multiple options to pick from
based on your needs of battle.

Command types:

1.  Command: attack with/use Name_of_fighting_move
>   This command allows the user to used their fight move against an enemy.
    Input the command followed by the name of the fight move
eg. Command: attack with Dragon_kick

2. Command: eat/consume Name_of_item
>   This command is used to eat food from the game. 
    Input the command followed by the name of the item
eg. Command: eat Pizza

3.  Command: statistics/abilities
>   This command is used to display the attribute of the player.
eg Command: abilities

4. Command: my move/skill Name_of_fighting_move
>   This command is used to display the attribute of a player's fighting move.
    Input the command followed by the name of the fight move
eg. Command: skill Dragon_kick
    
"""


if __name__ == '__main__':
    test = "go to pu's sy"
    print(goto.breaker(test).groupdict())
