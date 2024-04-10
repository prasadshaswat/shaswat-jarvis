class File:
    def __init__(self):
        self.filename = input("Enter filename:")
    
    def create_file(self):
        try:
            with open(self.filename, "w") as f:
                pass
            print("File created successfully.")
        except FileNotFoundError:
            print("File not found!")
    
    def write_file(self):
        try:
            with open(self.filename, "a") as f:
                data = input("Enter data:")
                f.write(data)
                print("Data written successfully.")
        except FileNotFoundError:
            print("File not found!")
    
    def read_file(self):
        try:
            with open(self.filename, "r") as f:
                lines = 0
                words = 0
                characters = 0
                vowels_count = 0  # Initialize vowels count
                consonants_count = 0  # Initialize consonants count
                vowels = "aeiou"
                consonants = "bcdfghjklmnpqrstvwxyz"
                for line in f:
                    lines += 1
                    words += len(line.split())
                    characters += len(line)
                    for char in line:
                        if char.lower() in vowels:
                            vowels_count += 1
                        elif char.lower() in consonants:
                            consonants_count += 1
                
                print("No of lines:", lines)
                print("No of words:", words)
                print("No of characters:", characters)
                print("No of vowels:", vowels_count)
                print("No of consonants:", consonants_count)
        except FileNotFoundError:
            print("File not found!")


if __name__ == "__main__":
    f = File()
    while True:
        print("1. Create file")
        print("2. Write file")
        print("3. Read file")
        print("4. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            f.create_file()
        elif choice == 2:
            f.write_file()
        elif choice == 3:
            f.read_file()
        elif choice == 4:
            break
        else:
            print("Invalid choice!")
