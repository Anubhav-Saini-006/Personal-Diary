import os
diary_folder = os.path.join(os.getcwd(),"diary")
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
    

    match(x):
        case 1:
             print("Let's write a new entry ")
             date=input("Enter date in the format ddmmyyyy ")
             if len(date) !=8 or not date.isdigit() or date.endswith('.txt'):
                print("Enter date in correct format \n")
                continue
             filename = os.path.join(diary_folder,date +'.txt')
             with open(filename,'w') as f:
                text=input("Enter the title for the day ")
                f.write("Title: " + text+"\n Date: " + date + "\n --------------------- \n")
                string=input("Enter what happened all the day \n")
                f.write(string)

        case 2:
            items=os.listdir(diary_folder)
            print(items)
            try:
             file=input("Enter date to read file in ddmmyyyy ")
             if len(file) !=8 or not file.isdigit() or file.endswith('.txt'):
                print("Enter date in correct format \n")
                continue
             filename=os.path.join(diary_folder , file +'.txt')
             with open(filename,'r') as f:
                content=f.read()
                print(content)
            except FileNotFoundError:
                print("No such file\n")
                continue