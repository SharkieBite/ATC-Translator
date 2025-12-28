import os

llc = "0"
llb = "0"
phonetic_alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

airport_codes = {
    "GCLP": "Gran Canaria",
    "EGKK": "Gatwick",
    "LEMH": "Menorca",
    "LYTV": "Tivat",
    "EGHI": "Southhampton",
    "EFKT": "Kittila",
    "GVBA": "Boa Vista",
}


def pilot():
    global llb
    global flight_name
    global flight_number
    global location
    if llb == "0":
      flight_name = input("Enter airline name: ")
      os.system('clear')
      flight_number = input("Enter flight number: ")
      os.system('clear')
      location = input("Enter Location: ")
    airport_name = airport_codes.get(location, "Unknown Airport")
    os.system('clear')
    type = input("1 - Landing, 2 - Takeoff, 3 - Lineup & Wait, 4 - Taxi, 5 - Startup & Pushback: ")
    goback = ""
    if type in ["1", "2", "3", "4"]:
        os.system('clear')
        rw = input("Enter runway number: ")
        if type == "1":
            os.system('clear')
            print("[" + str(flight_name), str(flight_number) + "] Requesting Landing at",
                  airport_name + ", Runway " + str(rw))
            goback = input("")
        if type == "2":
            os.system('clear')
            print("[" + str(flight_name), str(flight_number) + "] Requesting Takeoff at",
                  airport_name + ", Runway " + str(rw))
            goback = input("")
        if type == "3":
            os.system('clear')
            print("[" + str(flight_name), str(flight_number) + "] Requesting Line up & wait at",
                  airport_name + ", Runway " + str(rw))
            goback = input("")
        if type == "4":
            os.system('clear')
            type_taxi = input("1 - Taxi to gate, 2 - Taxi to runway: ")
            os.system('clear')
            code = input("Enter path: ")
            if type_taxi == "1":
                os.system('clear')
                print("[" + str(flight_name), str(flight_number) + "] Requesting taxi to gate",
                      str(rw) + " via " + ", ".join(phonetic_alphabet.get(code, "Invalid code") for code in code.split()))
                goback = input("")
            if type_taxi == "2":
                os.system('clear')
                print("[" + str(flight_name), str(flight_number) + "] Requesting taxi to runway",
                      str(rw) + " via " + ", ".join(phonetic_alphabet.get(code, "Invalid code") for code in code.split()))
                goback = input("")
    if type == "5":
      os. system('clear')
      print("[" + str(flight_name), str(flight_number) + "] Requesting startup & Pushback", airport_name)
      goback = input("")
      if goback == "":
        os. system('clear')
        direction()


def atc():
    global flight_location_atc
    flight_name_atc = input("Enter airline name: ")
    os.system('clear')
    flight_number_atc = input("Enter flight number: ")
    os.system('clear')
    if llc == "0":
      flight_location_atc = input("Enter Location: ")
    airport_name_atc = airport_codes.get(flight_location_atc, "Unknown Airport")
    os.system('clear')
    type_atc = input("1 - Landing, 2 - Takeoff, 3 - Lineup & Wait, 4 - Taxi, 5 - Startup & Pushback: ")
    goback = ""
    if type_atc in ["1", "2", "3", "4"]:
        os.system('clear')
        rw = input("Enter runway number: ")
        if type_atc == "1":
            os.system('clear')
            print("[" + str(flight_name_atc), str(flight_number_atc) + "] Clear to Land at",
                  airport_name_atc + ", Runway " + str(rw))
            goback = input("")
        if type_atc == "2":
            os.system('clear')
            print("[" + str(flight_name_atc), str(flight_number_atc) + "] Clear to Takeoff at",
                  airport_name_atc + ", Runway " + str(rw))
            goback = input("")
        if type_atc == "3":
            os.system('clear')
            print("[" + str(flight_name_atc), str(flight_number_atc) + "] Line up & wait at",
                  airport_name_atc + ", Runway " + str(rw))
            goback = input("")
        if type_atc == "4":
            os.system('clear')
            type_atc_taxi = input("1 - Taxi to gate, 2 - Taxi to runway: ")
            os.system('clear')
            code = input("Enter path: ")
            if type_atc_taxi == "1":
                os.system('clear')
                print("[" + str(flight_name_atc), str(flight_number_atc) + "] Taxi to gate via " + ", ".join(phonetic_alphabet.get(code, "Invalid code") for code in code.split()),
                      airport_name_atc)
                goback = input("")
            if type_atc_taxi == "2":
                os.system('clear')
                print("[" + str(flight_name_atc), str(flight_number_atc) + "] Taxi to runway",
                      str(rw) + " via " + ", ".join(phonetic_alphabet.get(code, "Invalid code") for code in code.split()),
                      airport_name_atc)
                goback = input("")
    if type_atc == "5":
      os. system('clear')
      print("[" + str(flight_name_atc), str(flight_number_atc) + "] Approved for Startup & Pushback", airport_name_atc)
      goback = input("")
      if goback == "":
        os. system('clear')
        direction()


def direction():
    print("Welcome to FAA Tower Request System")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    choice = input("1 - ATC, 2 - Pilot, 3 - Register : ")
    os.system('clear')
    if choice == "1":
        atc()
    if choice == "2":
        pilot()
    if choice == "3":
      global llc
      global flight_location_atc
      llc = "1"
      flight_location_atc = input("Enter Location: ")
      os.system('clear')
      direction()
    if choice == "4":
      global llb
      global flight_name
      global flight_number
      global location
      llb = "1"

      flight_name = input("Enter airline name: ")
      os.system('clear')
      flight_number = input("Enter flight number: ")
      os.system('clear')
      location = input("Enter Location: ")
      os.system('clear')
      direction()
      


direction()


