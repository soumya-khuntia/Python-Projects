import os

def Create_file(filename):
    try:
        with open(filename, 'w') as w:
            value = input("Enter the text you want to write in file: ")
            w.write(value)
            w.close()
        print(f"Text written in {filename} successfully!")

    except Exception:
        print("Somethig goes wrong!")

def read_file(filename):
    try:
        with open(filename, 'r') as r:
            text = r.read()
            print(text)
            r.close()
    
    except FileNotFoundError:
        print(f"{filename} not found!")

    except Exception:
        print("Something goes wrong!")


def update_file(filename):  #Needs to look
    try:
        with open(filename, 'a') as u:
            value = input("Enter the text you want to add: ")
            u.write(" " + value)
            u.close()
        print(f"{filename} updated successfully!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception:
        print("Something goes wrong!")

def show_all_files():
    files = os.listdir()
    for file in files:
        print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception:
        print("Something goes wrong!")

def main():
    while True:
        print("\nFilemanagement App", end="\n\n")
        print("1. Create File", end= "\t")
        print("2. Read File", end= "\t")
        print("3. Update File", end= "\t")
        print("4. Display all File", end= "\t")
        print("5. Delete File", end= "\t")
        print("6. Exit", end="\n\n")

        choice = input("Enter your choice(1-6): ")
        if choice=='1':
            file = input("Enter the filename you want to create(ex: sample.txt): ")
            Create_file(file)
        elif choice=='2':
            file = input("Enter the filename you want to read(ex: sample.txt): ")
            read_file(file)
        elif choice=='3':
            file = input("Enter the filename you want to update(ex: sample.txt): ")
            update_file(file)
        elif choice=='4':
            show_all_files()
        elif choice=='5':
            file = input("Enter the filename you want to delete(ex: sample.txt): ")
            delete_file(file)
        elif choice=='6':
            print("Quiting The App......")
            break
        else:
            print("Invalid input!")

if __name__=="__main__":
    main()