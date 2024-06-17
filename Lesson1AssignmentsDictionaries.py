# Lesson 1: Assignments | Dictionaries
# ________________________________________
# 1. Real-World Python Dictionary Applications
# Objective: The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.
# 
# Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.
# Problem Statement: Given the initial menu:
# restaurant_menu = {
#     "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
#     "Main Course": {"Steak": 15.99, "Salmon": 13.99},
#     "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
# }
# •	Add a new category called "Beverages" with at least two items.
# •	Update the price of "Steak" to 17.99.
# •	Remove "Bruschetta" from "Starters".
# Initial menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# 1. Add a new category called "Beverages" with two items Coffee and Tea
restaurant_menu["Beverages"] = {"Coffee": 4.99, "Tea": 4.49}

# 2. Update the price of "Steak" to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# 3. Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# Print the updated menu
print(restaurant_menu)

# _______________________________________
# 2. Python Programming Challenges for Customer Service Data Handling
# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
# Problem Statement: Develop a program that:
# •	Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# •	Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
# (Bonus) filter by status

# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:
# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

# Function to open a new service ticket
def open_ticket(tickets):
    ticket_id = "Ticket" + str(len(tickets) + 1).zfill(4)
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
    print("Ticket", ticket_id, "opened successfully.")

# Function to update the status of an existing ticket to "closed"
def close_ticket(tickets):
    ticket_id = input("Enter ticket ID to close: ")
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = "closed"
        print("Ticket", ticket_id, "closed successfully.")
    else:
        print("Ticket not found.")

# Function to display all tickets
def display_tickets(tickets):
    print("All tickets:")
    for ticket_id, ticket_info in tickets.items():
        print("Ticket ID:", ticket_id)
        print("Customer:", ticket_info["Customer"])
        print("Issue:", ticket_info["Issue"])
        print("Status:", ticket_info["Status"])
        print()

# Function to filter tickets by status
def filter_tickets_by_status(tickets, status):
    print("Tickets with status", status + ":")
    for ticket_id, ticket_info in tickets.items():
        if ticket_info["Status"] == status:
            print("Ticket ID:", ticket_id)
            print("Customer:", ticket_info["Customer"])
            print("Issue:", ticket_info["Issue"])
            print()

# Main function
def main():
    # Initialize with sample tickets
    service_tickets = {
        "Ticket0001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
        "Ticket0002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }
    
    while True:
        print("\n1. Open a new service ticket")
        print("2. Update the status of an existing ticket to 'closed'")
        print("3. Display all tickets")
        print("4. Filter tickets by status")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            open_ticket(service_tickets)
        elif choice == "2":
            close_ticket(service_tickets)
        elif choice == "3":
            display_tickets(service_tickets)
        elif choice == "4":
            status = input("Enter status to filter by (open/closed): ")
            filter_tickets_by_status(service_tickets, status)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
