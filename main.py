import os
diary_folder = os.path.join(os.getcwd,"diary")
os.makedirs(diary_folder,exist_ok = True)
while True:
    print('''Welcome to Personal Diary!
1. Write a new entry
2. Read an entry
3. Add something to existing entry
4. Delete an entry          
5. Exit''')


    try:
        x = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number 1-5.")
        continue
    