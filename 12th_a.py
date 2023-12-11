class PhoneBook:
    def __init__(self):
        self.entries = []

    def add_friend(self, name, mobile_number):
        entry = (name, mobile_number)
        if entry not in self.entries:
            self.entries.append(entry)
            self.entries.sort()

    def search_friend(self, name):
        left, right = 0, len(self.entries) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.entries[mid][0] == name:
                return self.entries[mid][1]
            elif self.entries[mid][0] < name:
                left = mid + 1
            else:
                right = mid - 1

        return None

    def display_friends(self):
        for name, mobile_number in self.entries:
            print(f"{name}: {mobile_number}")

if __name__ == "__main__":
    phone_book = PhoneBook()
    
    while True:
        print("\nOptions:")
        print("1. Add a friend")
        print("2. Search for a friend")
        print("3. Display all friends")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter friend's name: ")
            mobile_number = input("Enter friend's mobile number: ")
            phone_book.add_friend(name, mobile_number)
            print("Friend added to the phone book.")
        
        elif choice == "2":
            name = input("Enter friend's name to search: ")
            mobile_number = phone_book.search_friend(name)
            if mobile_number:
                print(f"Mobile Number: {mobile_number}")
            else:
                print(f"{name} not found in the phone book.")
        
        elif choice == "3":
            phone_book.display_friends()
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
