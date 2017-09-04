#  File: ERsim.py
#  Description: Simulates queues for an ER at a hospital
#  Student"s Name: David Giles
#  Student"s UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 07/03/17
#  Date Last Modified: 07/05/17

class Queue:

    def __init__(self, name):
        self.items = []
        self.name = name

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        temp = list(reversed(self.items))
        return str(temp)

# treats next highest priority patient
def treatNext(critical, serious, fair):

    if critical.isEmpty() == False:
        print("\tTreating \'"+critical.peek()+"\' from Critical queue")
        critical.dequeue()
        return
    elif serious.isEmpty() == False:
        print("\tTreating \'"+serious.peek()+"\' from Serious queue")
        serious.dequeue()
        return
    elif fair.isEmpty() == False:
        print("\tTreating \'"+fair.peek()+"\' from Fair queue")
        fair.dequeue()
        return
    else:
        return

# treats next patient in specified condition
def treatCondition(condition):

    print("\tTreating \'"+condition.peek()+"\' from "+condition.name+" queue")
    condition.dequeue()
    return

# treats all the patients in all the queues
def treatAll(critical, serious, fair):

    for i in range(len(critical.items)):
        print("\tTreating \'"+critical.peek()+"\' from "+critical.name+" queue")
        critical.dequeue()
        printQueues(critical, serious, fair)
    for i in range(len(serious.items)):
        print("\tTreating \'"+serious.peek()+"\' from "+serious.name+" queue")
        serious.dequeue()
        printQueues(critical, serious, fair)
    for i in range(len(fair.items)):
        print("\tTreating \'"+fair.peek()+"\' from "+fair.name+" queue")
        fair.dequeue()
        printQueues(critical, serious, fair)
    return

# prints out current queues for each condition
def printQueues(critical, serious, fair):
    print("\tQueues are:")
    print("\tFair:     " + str(fair))
    print("\tSerious:  " + str(serious))
    print("\tCritical: " + str(critical))
    print()
    return

def main():

    critical = Queue("Critical")
    serious = Queue("Serious")
    fair = Queue("Fair")

    in_file = open("./ERsim.txt", "r")

    for line in in_file:
        line = line.strip()
        command = line.split()

        #  if command begins with add, determine condition and place patient in corresponding queue
        if command[0] == "add":
            condition = command[1]
            name = command[2]
            print("Command: Add patient", name, "to", condition, "queue\n")           
            if condition == "Critical":
                critical.enqueue(name)
            if condition == "Serious":
                serious.enqueue(name)
            if condition == "Fair":
                fair.enqueue(name)
            printQueues(critical, serious, fair)
        #  treat either next patient, next patient in specific queue, or all patients
        elif command[0] == "treat":
            if command[1] == "next":
                print("Command: Treat next patient\n")
                if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                    print("\tNo patients in queues\n")
                else:
                    treatNext(critical, serious, fair)
                    printQueues(critical, serious, fair)
            elif command[1] == "all":
                print("Command: Treat all patients\n")
                treatAll(critical, serious, fair)
                print("\tNo patients in queues\n")
            else:
                condition = command[1]
                print("Command: Treat next patient on", condition, "queue\n")
                if condition == "Critical":
                    if critical.isEmpty():
                        print("\tNo patients in queue\n")
                    else:
                        treatCondition(critical)
                        printQueues(critical, serious, fair)
                if condition == "Serious":
                    if serious.isEmpty():
                        print("\tNo patients in queue\n")
                    else:
                        treatCondition(serious)
                        printQueues(critical, serious, fair)
                if condition == "Fair":
                    if fair.isEmpty():
                        print("\tNo patients in queue\n")
                    else:
                        treatCondition(fair)
                        printQueues(critical, serious, fair)
        #  if command is exit, terminate the program
        elif command[0] == "exit":
            print("Command: Exit")
            return
        else:
            print("Invalid command.")
            continue

main()
