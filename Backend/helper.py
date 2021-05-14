import random

def file_check(file_name):
    try:
        open(f"{file_name}.json", "r")
        return True
    except IOError:
        return False

def probability_success_pair(Pair1, Pair2):
    P = round(random.random(), 1)
    if Pair1 == Pair2:
        return 0
    return P if P >= 0.9 else 0

def random_bloodtype():

    Bracket = random.randint(0, 1000)
    if Bracket <= 6:
        return "AB-"
    elif Bracket > 6 and Bracket <= 6 + 15:
        return "B-"
    elif Bracket > 6 + 15 and Bracket <= 6 + 15 + 34:
        return "AB+"
    elif Bracket > 6 + 15 + 34 and Bracket <= 6 + 15 + 34 + 63:
        return "A-"
    elif Bracket > 6 + 15 + 34 + 63 and Bracket <= 6 + 15 + 34 + 63 + 66:
        return "O+"
    elif Bracket > 6 + 15 + 34 + 63 + 66 and Bracket <= 6 + 15 + 34 + 63 + 66 + 85:
        return "B+"
    elif Bracket > 6 + 15 + 34 + 63 + 66 + 85 and Bracket <= 6 + 15 + 34 + 63 + 66 + 85 + 357:
        return "A+"
    else:
        return "O-"

def random_donor():
    data = {}
    data.update({"Name": "Dave"})
    if random.randint(0, 5538) < 2052:
        data.update({"Gender": "M"})
    else:
        data.update({"Gender": "F"})
    
    Bracket = random.randint(0, 5538)
    if Bracket <= 1627:
        data.update({"Age": random.randint(18, 34)})
    elif Bracket > 1627 and Bracket <= 1627 + 2258:
        data.update({"Age": random.randint(35, 49)})
    elif Bracket > 1627 + 2258 and Bracket <= 1627 + 2258 + 1492:
        data.update({"Age": random.randint(50, 64)})
    else:
        data.update({"Age": random.randint(65, 90)})
    
    data.update({"Time Til Death": random.randint(30, 730)})
    data.update({"Blood Type": random_bloodtype()})


    return data

def random_recipient():
    data = {}
    data.update({"Name": "Dave"})
    if random.randint(0, 1) == 0:
        data.update({"Gender": "M"})
    else:
        data.update({"Gender": "F"})
    
    Bracket = random.randint(0, 5535)
    if Bracket <= 63:
        data.update({"Age": random.randint(1, 5)})
    elif Bracket > 63 and Bracket <= 63 + 52:
        data.update({"Age": random.randint(6, 10)})
    elif Bracket > 63 + 52 and Bracket <= 63 + 52 + 127:
        data.update({"Age": random.randint(11, 17)})
    elif Bracket > 63 + 52 + 127 and Bracket <= 63 + 52 + 127 + 1035:
        data.update({"Age": random.randint(18, 34)})
    elif Bracket > 63 + 52 + 127 + 1035 and Bracket <= 63 + 52 + 127 + 1035 + 1590:
        data.update({"Age": random.randint(35, 49)})
    elif Bracket > 63 + 52 + 127 + 1035 + 1590 and Bracket <= 63 + 52 + 127 + 1035 + 1590 + 1913:
        data.update({"Age": random.randint(50, 64)})
    else:
        data.update({"Age": random.randint(65, 90)})

    data.update({"Blood Type": random_bloodtype()})

    return data

def create_pair(data_Donor, data_Recipient):
    Donor = data_Donor
    Recipient = data_Recipient
    return (Donor, Recipient)
