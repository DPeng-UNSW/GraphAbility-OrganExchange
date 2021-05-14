#Flow Chart

#Scenario 1 - Live Donor Person Added
#1 Add Pair to Graph
#2 Calculate Weightings of each Node to the Starting Node
#3 Check for Matches
#3a If no matches leave pair in Graph
#3b If an acceptable cycle is made all nodes exit and the organisation of the process begins

#Scenario 2 - Deceased Donor or Altruistic Donor
#1 Make a pair with people from the Waiting List
#Repeat Scenario 1
import json
from Graph import Graph
from WaitList import WaitList
from helper import random_donor, random_recipient, create_pair, probability_success_pair
import random


if __name__ == '__main__':
    name = input("Enter the name of the Network you are working on: ")
    G = Graph(name)
    W = WaitList(name)
    print("type '?' to see a list of commands")
    c = input("Enter Command: ")
    while c != 'q':
        if c == 'g':
            G.print_graph()
        elif c == 'p':
            G.print_pairs()
        elif c == 'w':
            pass
            #W.print_waitlist()
        elif c == 'n':
            G.print_size()
        elif c == 's':
            print(G.save())
            print(W.save())
        elif c == 'a':
            G.add_pair(create_pair(random_donor(), random_recipient()))
        elif c == 'c':
            G.clear()
            print(f"{G.name}.json has been cleared")
        elif c == 'd':
            days = input("Which days would you like to pass? ")
            G.pass_day(int(days))
        elif c == 'r':
            Pair = input("Which pair would you like to remove? ")
            G.remove_pair(int(Pair))
        elif c == 'sim':
            TG = Graph()
            total_days = int(input("Total days to run simulation?: "))
            new_pair_add = int(input("%chance each day for a new pair? "))
            dead = 0
            saved = 0
            count = 0
            for i in range(total_days):
                rand = random.randint(0, 99)
                if rand < new_pair_add:
                    saved += TG.add_pair(create_pair(random_donor(), random_recipient()), "sim")
                    count += 1
                dead += TG.pass_day(1, "sim")
            print(f"    Total Pairs: {count}")
            print(f"    Total Dead: {dead}")
            print(f"    Total Saved: {saved}")
            print(f"    Still on List: {TG.size}")
        elif c == '?':
            print("g : print_graph")
            print("a : add_pair")
            print("q : exit")
            print("p : print_pairs")
            print("n : print_size")
            print("d : pass_day")
            print("r : remove_pair")
            print("c : clear_graph")
            print("s : save_graph")
            print("sim: run simulation")
        c = input("Enter Command: ")
    print("Exiting: code 0")
