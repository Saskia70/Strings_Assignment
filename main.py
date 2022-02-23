# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
Player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player1 + ' ' + str(goal_0) + ', ' + Player2 + ' ' + str(goal_1)
report = f'{player1} scored in the {goal_0}nd minute\n{Player2} scored in the {goal_1}th minute'

player = 'Frank Rijkaard'
first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:]
last_name_len = len(last_name)
name_short = ((first_name[:1]) + '. ' + (last_name))
chant = ((first_name+'! ')*4)+ (first_name + '!')
good_chant = (chant[-1:] != ' ')
