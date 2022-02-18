# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from pdb import find_function
player1 = ('Ruud Gullit')
Player2 = ('Marco van Basten')
str(player1)
str(Player2)
goal_0 = 32
goal_1 = 54
str(goal_0)
str(goal_1)
scorers = player1 + ' ' + str(goal_0) + ',' + ' ' + Player2 + ' ' + str(goal_1)
report = f'{player1} scored in the {goal_0}nd minute\n{Player2} scored in the {goal_1}th minute'
player = 'Frank Rijkaard'
first_name = player[player.find(''):5]
last_name_len = len(player[-8: ])
name_short = player[0:1] + '.' + ' '+ player[6: ]
chant = ((player[0:5]+'! ')*4)+'Frank!'
good_chant = (len(chant) != 33)
