# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goal_scorer_1 = 'Ruud Gullit'
goal_scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = goal_scorer_1 + ' ' + str(goal_0) + ', ' + goal_scorer_2 + ' ' + str(goal_1)
report = f'{goal_scorer_1} scored in the {goal_0}nd minute\n{goal_scorer_2} scored in the {goal_1}th minute'
player = 'Ronald Koeman'
first_name = player[player.find("Ronald"):player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = player[:1] + '.' + player[player.find(" "):]
chant = (first_name + '! ') * 5 + first_name + '!'
good_chant = chant[-1:] != ' '

print(good_chant)



