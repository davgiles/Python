# File: Bowling.py
# Description: Calculates bowling scores frame by frame
# Student's Name: David Giles
# Student's UT EID: DGG524
# Course Name: CS 313E
# Unique Number: 86940
#
# Date Created: 06/06/17
# Date Last Modified: 06/09/17

# converts gutter balls, spares, and strikes into ints
def bowls_to_ints(line):

    bowls = []  # create new list for ints

    for i in range(len(line)):
        if line[i] == '-':
            bowls.append(0)
            line[i] = 0
        elif line[i] == 'X':
            bowls.append(10)
        elif line[i] == '/':
            bowls.append(10 - int(line[i-1]))
        else:
            bowls.append(int(line[i]))

    return bowls

# calculates score of each frame of bowls
def score_game(bowls, line):

    score = 0           # keeps track of total score
    frames = []         # holds score of each frame
    idx = 0             # index
    scored_line = ''    # string for score inputs

    while idx < len(bowls):
        # last frame of bowls (special case)
        if (len(frames) == 9):
            if (bowls[idx] == 10):  # strike
                scored_line += ('|X '+str(line[idx+1])+' '+str(line[idx+2])+'|')
                score += bowls[idx]
                score += bowls[idx+1]
                score += bowls[idx+2]
                frames.append(score)
                idx += 3
            elif (bowls[idx] + bowls[idx+1] == 10):  # spare
                scored_line += ('|'+str(line[idx])+' '+str(line[idx+1])+' '+str(line[idx+2])+'|')
                score += bowls[idx]
                score += bowls[idx+1]
                score += bowls[idx+2]
                frames.append(score)
                idx += 3
            else:  # open
                scored_line += ('|'+str(line[idx])+' '+str(line[idx+1])+'  |')
                score += bowls[idx]
                score += bowls[idx+1]
                frames.append(score)
                idx += 3                
        # rest of the frames
        else:
            if (bowls[idx] == 10):  # strike
                scored_line += ('|X  ')
                score += bowls[idx]
                score += bowls[idx+1]
                score += bowls[idx+2]
                frames.append(score)
                idx += 1
            elif (bowls[idx] + bowls[idx+1] == 10):  # spare
                scored_line += ('|'+str(line[idx])+' '+str(line[idx+1]))
                score += bowls[idx]
                score += bowls[idx+1]
                score += bowls[idx+2]
                frames.append(score)
                idx += 2
            else:  # open
                scored_line += ('|'+str(line[idx])+' '+str(line[idx+1]))
                score += bowls[idx]
                score += bowls[idx+1]
                frames.append(score)
                idx += 2

    return frames, scored_line

# prints the scoresheet
def print_game(frames, scored_line):
    
    print('  1   2   3   4   5   6   7   8   9    10  ')
    print('+---+---+---+---+---+---+---+---+---+-----+')
    print(scored_line)
    for i in range(len(frames)):
        if (i == len(frames) - 1): # last frame
            print('|{:>5}|'.format(frames[i]))
        else:
            print('|{:>3}'.format(frames[i]),end='')
    print('+---+---+---+---+---+---+---+---+---+-----+\n')
        
        
def main():

    in_file = open('./scores.txt', 'r')

    for line in in_file:
        line = line.strip()
        line = line.split()

        bowls = bowls_to_ints(line)
        frames, scored_line = score_game(bowls, line)
        print_game(frames, scored_line)
        
main()
