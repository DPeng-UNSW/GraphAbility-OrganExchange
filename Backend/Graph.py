import json
from helper import file_check, probability_success_pair, create_pair

MAX_CYCLE = 3

class Graph:
    def __init__(self, name="temp"):
        self.name = name
        self.M = []
        if name != "temp":
            if file_check(f"{name}_graph"):
                with open(f"{name}_graph.json", 'r') as Json_Graph:
                    data = json.load(Json_Graph)
                    self.G = data['Graph']
                    self.P = data['Pairs']
                    self.size = len(self.G)
            else:
                self.G = []
                self.P = []
                self.size = 0
        else:
            self.G = []
            self.P = []
            self.size = 0
        return 

    def save(self):
        if self.name == "temp":
            return "Temp graphs unable to be saved"
        with open(f"{self.name}_graph.json", 'w+') as Json_Graph:
            data = {"Graph": self.G, "Pairs": self.P}
            json.dump(data, Json_Graph)
        return f"{self.name}_graph.json has been saved"

    def clear(self):
        self.G = []
        self.P = []
        self.M = []
        self.size = 0
        with open(f"{self.name}_graph.json", 'w') as Json_Graph:
            data = {"Graph": [], "Pairs": []}
            json.dump(data, Json_Graph)
        return {}

    def calculate_graph(self, Graph, Pairs):
        self.G.append([])
        self.size += 1
        for i in range(self.size):
            self.G[i].append(probability_success_pair(Pairs[-1], Pairs[i]))
            if i == self.size - 1:
                break
            self.G[-1].append(probability_success_pair(Pairs[i], Pairs[-1]))
        return

    def cycle_finder(self, origin, current_pair, cycle_so_far, depth):
        if depth < MAX_CYCLE - 1:
            for i in range(self.size):
                if self.G[current_pair][i] != 0 and i == origin:
                    cycle_so_far.append(i)
                    self.M.append(cycle_so_far)
                    return
                elif self.G[current_pair][i] != 0 and i not in cycle_so_far:
                    cycle_so_far.append(i)
                    self.cycle_finder(origin, i, cycle_so_far, depth + 1)
                    return
        elif depth == MAX_CYCLE - 1:
            if self.G[current_pair][origin] != 0:
                cycle_so_far.append(origin)
                self.M.append(cycle_so_far)
                return
        return


    def find_cycles(self):
        for i in range(self.size):
            if self.G[-1][i] != 0:
                cycle_so_far = []
                cycle_so_far.append(self.size -1 )
                cycle_so_far.append(i)
                self.cycle_finder(self.size - 1, i, cycle_so_far, 1)
        return

    def remove_pair(self, PairID):
        self.P.pop(PairID)
        self.G.pop(PairID)
        self.size -= 1
        for i in range(self.size):
            self.G[i].pop(PairID)

    def add_pair(self, Pair):
        self.M = []
        self.P.append(Pair)
        self.calculate_graph(self.G, self.P)
        self.find_cycles()
        max = 0
        if len(self.M) > 0:
            max_match = self.M[0]
        else:
            max_match = None

        for match in self.M:
            sum = 0
            for edge in range(len(match) - 1):
                sum += self.G[match[edge]][match[edge + 1]]
            if sum > max:
                max = sum
                max_match = match
        Transplants_To_Happen = []
        if max_match != None:
            for Pair in range(len(max_match) - 1):
                Transplants_To_Happen.append(self.P[Pair])
            match = sorted(max_match[:-1], key=None, reverse=True)
            for Pair in match:
                self.remove_pair(Pair)
        transplants = len(max_match) - 1 if max_match != None else 0
        return {"Transplants": transplants, "Pairs": Transplants_To_Happen}

    def pass_day(self, days=1, mode="default"):
        to_die = []
        for Pair in range(self.size):
            if self.P[Pair][0]["Time Til Death"] > days:
                self.P[Pair][0]["Time Til Death"] -= days
            else:
                if mode == "default":
                    print(f"{self.P[Pair][0]} has Died from Pair {Pair}")
                to_die.append(Pair)
        for i in range(len(to_die) - 1, -1, -1):
            self.remove_pair(to_die[i])
        return len(to_die)

    def print_graph(self):
        return {"Graph": self.G, "Pairs": self.P, "Size": self.size, "Name": self.name}
         
    def print_pairs(self):
        i = 0
        for pair in self.P:
            print(f"Pair ID: {i}")
            i += 1
            
            age = pair[0]['Age']
            bt = pair[0]['Blood Type']
            gender = pair[0]['Gender']
            print(f"Donor :     [Age: {age} Blood Type: {bt} Gender: {gender}]")
            
            age = pair[1]['Age']
            bt = pair[1]['Blood Type']
            gender = pair[1]['Gender']
            print(f"Recipient:  [Age: {age} Blood Type: {bt} Gender: {gender}]")
            print()

    def print_size(self):
        print(f"Size: {self.size}")


