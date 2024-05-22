class ParkingGarage:
    def __init__(self, total_tickets, total_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets and self.parkingSpaces:
            ticket_number = self.tickets.pop(0)
            self.parkingSpaces.pop(0)
            self.currentTicket[ticket_number] = {'paid': False}
            print(f"Ticket {ticket_number} taken. Please park your car.")
        else:
            print("Sorry, no parking spaces available.")

    def payForParking(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket:
            if not self.currentTicket[ticket_number]['paid']:
                payment = input("Please enter the payment amount: ")
                if payment:
                    self.currentTicket[ticket_number]['paid'] = True
                    print("Your ticket has been paid. You have 15 minutes to leave.")
                else:
                    print("Payment was not successful.")
            else:
                print("This ticket has already been paid.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]['paid']:
                print("Thank You, have a nice day!")
                self.parkingSpaces.append(ticket_number)
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
            else:
                payment = input("Your ticket is not paid. Please enter the payment amount: ")
                if payment:
                    self.currentTicket[ticket_number]['paid'] = True
                    print("Thank you, have a nice day!")
                    self.parkingSpaces.append(ticket_number)
                    self.tickets.append(ticket_number)
                    del self.currentTicket[ticket_number]
                else:
                    print("Payment was not successful.")
        else:
            print("Invalid ticket number.")

def main():
    garage = ParkingGarage(total_tickets=5, total_spaces=5)
    
    while True:
        action = input("What would you like to do? (take/pay/leave/quit): ").lower()
        
        if action == 'take':
            garage.takeTicket()
        elif action == 'pay':
            garage.payForParking()
        elif action == 'leave':
            garage.leaveGarage()
        elif action == 'quit':
            print("Thank you for using the parking garage. Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
