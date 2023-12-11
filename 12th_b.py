class PhoneBook:
    def __init(self):
        self.entries = []

    def add_friend(self, name, mobile_number):
        entry = (name, mobile_number)
        if entry not in self.entries:
            self.entries.append(entry)
            self.entries.sort()

    def search_friend(self, name):
        def fibonacci_search(arr, x):
            m, k, n = 0, 0, 1

            while m < len(arr):
                m = k + n
                n = k
                k = m

            offset = -1

            while m > 1:
                i = min(offset + k, len(arr) - 1)
                if arr[i][0] < name:
                    m, n, k = m - n, n, m - n
                    offset = i

                elif arr[i][0] > name:
                    m, n, k = n, k - n, m - n

                else:
                    return arr[i][1]

            if n and arr[offset + 1][0] == name:
                return arr[offset + 1][1]
            return None

        return fibonacci_search(self.entries, name)

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
