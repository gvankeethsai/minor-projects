from pathlib import Path
def show_files_folders():
    path = Path('')
    ls = list(path.rglob('*'))
    for index , item in enumerate(ls):
        print(f"{index+1} : {item}")

    
def create_file():
    file_name = input("Enter the name of the file : ")
    path = Path(file_name)
    if path.exists():
        print("File already exists")
    else:
        path.touch()
        print(f"File {file_name} created")
    choice1 = input("would you like to write into your file? (y/n)")    
    if choice1.lower() == "y":
       write_Into_file(file_name) 
    else:
        print("Okay , I think you are")
def write_Into_file(file_name):
    content = input("Enter the content : ")
    with open(file_name, 'a') as f:
        f.write(content)
    print(f"Content written into {file_name}")

def update_file():
    file_name = input("Enter the name of the file : ")
    path = Path(file_name)
    print("Enter 1 to overwrite into an existing file")
    print("Enter 2 to append into an existing file")
    print("Enter 3 to create a new file and write into it")
    print("Enter 4 to rename a file")
    enter = int(input("Enter your choice : "))
    if enter == 1:
        with open(file_name , "w") as f:
            content = input("Enter the content : ")
            f.write(content)
            print("content overwritten")
    elif enter == 2:
        with open(file_name , "a") as f:
            content = input("Enter the content : ")
            f.write(content)
            print("content appended")
    elif enter == 3:
        file_name = input("Enter the name of the file : ")
        with open(file_name , "w") as f:
            content = input("Enter the content : ")
            f.write(content)
            print("content written into a new file")
            
    elif enter ==4:
        new_name = input("Enter the new name of the file : ")
        Path(file_name).rename(new_name)   
        print("File renamed Successfully ")     
    else:
        print("Invalid choice")
def read_file():
    file_name = input("Enter the name of the file : ")
    path = Path(file_name)
    if path.exists() and path.is_file():
       with open(file_name , "r") as f:
          content = f.read()
          print(content)
    else:
        print("File does not exist")
def delete_file():
    file_name = input("Enter the name of the file : ")
    path = Path(file_name)
    if path.exists() and path.is_file():
        path.unlink()
        print(f"File {file_name} deleted")
    else:
        print("File does not exist")
def main():

    print("Enter 1 for creating a File")
    print("Enter 2 for reading a File")
    print("Enter 3 for updating(renaming) a File")
    print("Enter 4 for deleting a File")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_file()
    elif choice == 2:
        read_file()
    elif choice == 3:
        update_file()
    elif choice == 4:
        delete_file()
    else:
        print("Invalid choice")

main()
