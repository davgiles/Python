#  File: htmlChecker.py
#  Description: Checks an html file for matching start and end tags
#  Student's Name: David Giles
#  Student's UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 06/28/17
#  Date Last Modified: 06/28/17

EXCEPTIONS = ['br', 'hr', 'meta']
VALID_TAGS = []

class Stack(object):
    def __init__(self):
        self.items = [ ]

    def isEmpty (self):
        return self.items == [ ]

    def push (self, item):
        self.items.append (item)

    def pop (self):
        return self.items.pop ()

    def peek (self):
        return self.items[-1]

    def size (self):
        return len(self.items)

    def __str__(self):
        string = '['
        for i in range(len(self.items)):
            if i == len(self.items)-1:
                string += (self.items[i])
            else:
                string += (self.items[i]+', ')
        string += ']'
        return string

# extracts the tags from a string and returns a list of tags
def getTag(text):

    tagList = []
    tagIsOpen = False
    tag = ''

    for char in text:

        if char == '<':
            tagIsOpen = True
        if char == '>' or char == ' ':
            tagIsOpen = False
            if len(tag) > 0:
                tagList.append(tag)
                tag = ''

        if tagIsOpen and char != '<':
            tag += char

    return tagList

def main():

    in_file = open('./htmlfile.txt', 'r')

    text = in_file.read()

    tagList = getTag(text)
    print('tagList = [', end='')
    print(*tagList, sep=', ', end='')
    print(']\n')

    s = Stack()  # stack to use for storing 'start' tags

    for tag in tagList:
        if tag not in VALID_TAGS:
            VALID_TAGS.append(tag)
            print('New tag '+tag+' found and added to list of valid tags.')
        if tag in EXCEPTIONS:
            print('Tag '+tag+' does not need to match: stack is still '+str(s))
            continue

        # if closing tag, check for matching start tag in stack
        if tag.startswith('/'):
            if tag[1:] == s.peek():
                s.pop()
                print('Tag '+tag+' matches top of stack: stack is now '+str(s))
                continue
            else:
                print('\nError: tag is '+tag+' but top of stack is '+str(s.peek()))
                return

        s.push(tag)
        print('Tag '+tag+' pushed: stack is now '+str(s))

    if s.isEmpty():
        print('\nProcessing complete. No mismatches found.')
    else:
        print('\nProcessing complete. Unmatched tags remain on stack: '+str(s))

    print('\nVALID_TAGS = [', end='')
    print(*VALID_TAGS, sep=', ', end='')
    print(']')
    print('EXCEPTIONS = [', end='')
    print(*EXCEPTIONS, sep=', ', end='')
    print(']')

main()
