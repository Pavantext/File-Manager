import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created succesfully!")
    except FileExistsError:
        print(f"File Name {filename} already exists!")
    except Exception as E:
        print("An error occured!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No Files Found!")
    else:
        print("Files in directory1")
        for file in files:
            print(file)

def del_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} Deleted succesfully!")
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print("An error occured!")

def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' : \n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exits")

    except Exception as e:
        print("An Error occured!")

def edit_file(filename):
    try:
        with open("sample.txt", "a") as f:
            content = input("Enter data to add")
            f.write(content + "\n")
            print(f"Content added to {filename} Succesfully!")

    except FileNotFoundError:
        print(f"{filename} does not exits!")

    except Exception as e:
        print("An Error occured!")

def main():
    while True:
        print("FILE MANAGER")
        print("1: Create a File")
        print("2: View all Files")
        print("3: Delete a file")
        print("4: Read a File")
        print("5: Edit a File")
        print("6: Exit")
        
        choice = input("Enter Your Choice(1-6)")

        if choice == "1":
            filename = input("Enter the file-name to create:")
            create_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            filename = input("Enter Filename to delete")
            del_file(filename)
        elif choice == "4":
            filename = input("Enter File name to read")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter File name to edit")
            edit_file(filename)
        elif choice == "6":
            print("Closing...")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()