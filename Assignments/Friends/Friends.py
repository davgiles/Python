#  File: Friends.py
#  Description: This program utilizes linked lists to implement the
#      "friend" functionality of a Facebook-like application
#  Student"s Name: David Giles
#  Student"s UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 07/12/17
#  Date Last Modified: 07/15/17

class Node(object):

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # returns data
    def getData(self):
        return self.data

    # returns name attribute of data
    def getName(self):
        return self.data.name

    # returns friends attribute of data
    def getFriends(self):
        return self.data.friends

    # returns next
    def getNext(self):
        return self.next

    # overwrites initial data
    def setData(self, newData):
        self.data = newData.name

    # changes next
    def setNext(self, newNext):
        self.next = newNext


class LinkedList(object):

    def __init__(self):
        self.head = None

    def __str__(self):
        s = ''
        current = self.head
        item = 1

        while current != None:
            if item % 10 == 0:
                s += (str(current.getData()) + '\n')
            else:
                s += (str(current.getData()) + ' ')
            current = current.getNext()
            item += 1

        return s

    # Add an item to the beginning of the list
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # Return True if the item is in the list, False otherwise.
    def find(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getName() == item.name:  # modified to search for object's name
                found = True
            else:
                current = current.getNext()

        return found

    # Delete item from list if found, return True. Otherwise, return False.
    def delete(self, item):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return True
        else:
            return False

    # Return True if a list is empty, or False otherwise
    def isEmpty(self):
        return self.head == None

    # Searches for item in list, if found return item. Otherwise, return None
    def get(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getName() == item.name:  # modified to search for object's name
                found = True
            else:
                current = current.getNext()

        if found:
            return current.getData()
        else:
            return None


class User(object):

    def __init__(self, name):
        self.name = name
        self.friends = LinkedList()

    def __str__(self):
        return self.name

    def addFriend(self, person):
        self.friends.add(person)

    def removeFriend(self, person):
        self.friends.delete(person)

    def showFriends(self):
        return "[ " + str(self.friends) + "]"

    def isFriend(self, person):
        return self.friends.find(person)


def main():

    userList = LinkedList()

    in_file = open("./FriendData.txt", "r")

    for line in in_file:
        line = line.strip()
        print("--> " + line)
        line = line.split()  # splits the words in line into list

        if line[0] == "Person":
            name = line[1]
            user = User(name)

            # if user is found in users list, don't
            if userList.find(user):
                print("\tError: User " + name + " already exists.")
            else:
                userList.add(user)
                print("\t" + name + " now has an account.")

        if line[0] == "Friend":
            name1, name2 = line[1], line[2]
            user1, user2 = User(name1), User(name2)

            if name1 == name2:
                print("\tA person cannot friend him/herself.\n")
                continue

            if userList.find(user1) and userList.find(user2):
                user1 = userList.get(user1)
                user2 = userList.get(user2)

                if user1.isFriend(user2):
                    print("\tError: " + name1 + " and " + name2 + " are already friends.")
                else:
                    user1.addFriend(user2)
                    user2.addFriend(user1)
                    print("\t" + name1 + " and " + name2 + " are now friends.")
            elif not userList.find(user1) and userList.find(user2):
                print("\tError: User " + name1 + " does not exist.")
            elif userList.find(user1) and not userList.find(user2):
                print("\tError: User " + name2 + " does not exist.")
            else:
                print("\tError: User " + name1 + " does not exist.")
                print("\tError: User " + name2 + " does not exist.")

        if line[0] == "Unfriend":
            name1, name2 = line[1], line[2]
            user1, user2 = User(name1), User(name2)

            if name1 == name2:
                print("\tA person cannot unfriend him/herself.\n")
                continue

            if userList.find(user1) and userList.find(user2):
                user1 = userList.get(user1)
                user2 = userList.get(user2)

                if user1.isFriend(user2):
                    user1.removeFriend(user2)
                    user2.removeFriend(user1)
                    print("\t" + name1 + " and " + name2 + " are no longer friends.")
                else:
                    print("\tError: " + name1 + " and " + name2 + " aren't friends, so you can't unfriend them.")
            elif not userList.find(user1) and userList.find(user2):
                print("\tError: User " + name1 + " does not exist.")
            elif userList.find(user1) and not userList.find(user2):
                print("\tError: User " + name2 + " does not exist.")
            else:
                print("\tError: User " + name1 + " does not exist.")
                print("\tError: User " + name2 + " does not exist.")

        if line[0] == "List":
            name = line[1]
            user = User(name)

            if userList.find(user):
                user = userList.get(user)

                if user.friends.isEmpty():
                    print("\t" + name + " has no friends.")
                else:
                    print("\t" + user.showFriends())
            else:
                print("\tError: User " + name + " does not exist.")

        if line[0] == "Query":
            name1, name2 = line[1], line[2]
            user1, user2 = User(name1), User(name2)

            if name1 == name2:
                print("\tA person cannot query him/herself.\n")
                continue

            if userList.find(user1) and userList.find(user2):
                user1 = userList.get(user1)
                user2 = userList.get(user2)

                if user1.isFriend(user2):
                    print("\t" + name1 + " and " + name2 + " are friends.")
                else:
                    print("\t" + name1 + " and " + name2 + " are not friends.")
            elif not userList.find(user1) and userList.find(user2):
                print("\tError: User " + name1 + " does not exist.")
            elif userList.find(user1) and not userList.find(user2):
                print("\tError: User " + name2 + " does not exist.")
            else:
                print("\tError: User " + name1 + " does not exist.")
                print("\tError: User " + name2 + " does not exist.")

        if line[0] == "Exit":
            print("\tExiting...")
            break

        print()

main()
