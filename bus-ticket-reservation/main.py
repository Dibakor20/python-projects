class User:
    def __init__(self,name,password):
        self.name = name
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




company = GreenLine()
company.install()

b = BusCounter()
b.reservation()
b.showBusInfo()
