import json
from helper import file_check, random_recipient

class WaitList:
    def __init__(self, name="temp"):
        self.name = name
        if name != "temp":
            if file_check(f"{name}_waitlist"):
                with open(f"{name}_waitlist.json", 'r') as Json_waitlist:
                    data = json.load(Json_waitlist)
                    self.W = data['Waitlist']
                    self.size = len(self.W)
            else:
                self.W = []
                self.size = 0
        else:
            self.W = []
            self.size = 0
        return

    def save(self):
        if self.name == "temp":
            return "Temp waitlists unable to be saved"
        with open(f"{self.name}_waitlist.json", 'w+') as Json_waitlist:
            data = {"Waitlist": self.W}
            json.dump(data, Json_waitlist)
        return f"{self.name}_waitlist.json has been saved"

    def clear(self):
        self.W = []
        self.size = 0
        with open(f"{self.name}_waitlist.json", 'w') as Json_waitlist:
            data = {"Waitlist": []}
            json.dump(data, Json_waitlist)
        return

    def add_recipient(self, recipient):
        self.W.append(recipient)

    def pass_day(self, days=1, mode="default"):
        to_die = []
        for Recipient in range(self.size):
            if self.W[Recipient]["Time Til Death"] > days:
                self.W[Recipient]["Time Til Death"] -= days
            else:
                if mode == "default":
                    print(f"{self.W[Recipient]} has Died")
                to_die.append(Recipient)
        for i in range(len(to_die) - 1, -1, -1):
            self.remove_recipient(to_die[i])
        return len(to_die)

    def print_list(self):
        return {"Waitlist": self.W, "Size": self.size, "Name": self.name}