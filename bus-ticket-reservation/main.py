
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,form_des,to_des) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.form_des = form_des
        self.to_des = to_des
        self.seat = ['Empty' for i in range(20)]

class GreenLine:
    total_bus = 5
    total_bus_lst = []

    def install(self):
        bus_no = int(input("Enter bus no: "))

        flag = 1
        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                print('Bus already installed')
                flag = 0
                break                
    
        if flag:
                bus_driver = input('Enter driver name: ')
                bus_arrival = input('Enter arrival time: ')
                bus_departure = input('Enter departure time: ')
                bus_form = input('Enter bus start form: ')
                bus_to = input('Enter bus destination to: ')
                self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_form,bus_to)
                self.total_bus_lst.append(vars(self.new_bus))
                print("\n Bus installed successfully")

class BusCounter(GreenLine):
    user_lst = []
    bus_seat = 20

    def reservation(self):
        bus_no = int(input('Enter Bus number: '))

        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                passenger = input('Enter your name: ')
                seat_no = int(input('Enter your seat no: '))

                if seat_no - 1 > self.bus_seat:
                    print("only 20 seat available")
                
                elif bus['seat'][seat_no -1] != 'Empty':
                    print('Seat already booked')

                else:
                    bus['seat'][seat_no - 1] = passenger

            else:
                print('no bus no available')
                break 

    def showBusInfo(self):
        bus_no = int(input('enter bus no: '))

        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                print('*'*50)
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print(f"Bus No: {bus_no} \t\t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\t Departure: {bus['departure']}")
                print(f"From: {bus['form_des']} \t\t To: {bus['to_des']}")
                print()
                a =1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")

                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()

    def get_User(self):
        return self.user_lst

    def create_account(self):
        name = input('Enter your name: ')
        flag = 0

        for user in self.get_User():
            if user.username == name:
                print('username already exist')
                flag = 1
                break
        if flag == 0:
            password = input("Enter your password: ")
            self.new_user = User(name,password)
            self.user_lst.append(vars(self.new_user))
            print('account created successfully')

    def available_bus(self):
        if len(self.total_bus_lst) == 0:
            print('no bus available')
        else:
            for bus in self.total_bus_lst:
                print('*'*50)
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print(f"Bus No: {bus['coach']} \t\t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\t Departure: {bus['departure']}")
                print(f"From: {bus['form_des']} \t\t To: {bus['to_des']}")
                print()
                a =1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")

                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()
                

while True:
    company = GreenLine()
    b = BusCounter()
    print("1. Create an account\n2. login to your account \n3. EXIT\n")
    user_input = int(input("Enter you choice : "))
    if user_input == 3:
        break
    elif user_input == 1:
        b.create_account()
    elif user_input == 2:
        name = input("Enter your username : ")
        password = input("Enter your password : ")
        flag = 0
        isAdmin = False
        if name == "admin" and password == "123":
            isAdmin = True
        if isAdmin == False:
            for user in b.get_User():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTEM")
                    print("1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. EXIT")
                    a = int(input("Enter Your Choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.available_bus()
                    elif a == 2:
                        b.showBusInfo()
                    elif a == 3:
                        b.reservation()
            else:
                print("No username found")
        else:
            while True:
                print(f"\n {' '*10} HELLO ADMIN Welcome to BUS TICKET BOOKING SYSTEM\n")
                print(
                    "1. Install Bus\n2. Available Buses\n3. Show Bus Info\n4. EXIT")
                a = int(input("Enter Your Choice : "))
                if a == 4:
                    break
                elif a == 1:
                    b.install()
                elif a == 2:
                    b.available_bus()
                elif a == 3:
                    b.showBusInfo()




# company = GreenLine()
# company.install()

b = BusCounter()
# b.reservation()
# b.showBusInfo()
b.install()
b.install()
b.available_bus()
b.create_account()
