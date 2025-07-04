import sqlite3

conn=sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)
''')

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
            print('*'*50,'\n',row,'\n')

def update_video(id,name,time):

    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?" 
                   ,(name,time,id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id=?",(id,))
    conn.commit()
def main():
    while True:

        print("\n Youtube Manager | Choose 1 option ")
        print("1. List all the youtube vidoes")
        print("2. Add a youtube vidoe")
        print("3. Update a youtube vidoes")
        print("4. Delete a the youtube vidoes")
        print("5. Exit app")

        
        choice=input("Enter Your choice=")
        
        if choice == '1':
            list_videos()

        elif choice == '2':
            name=input("Enter video Name=")
            time=input("Enter video Time=")
            add_video(name,time)

        elif choice == '3':
            id=input("Enter video id:")
            name=input("Enter video Name=")
            time=input("Enter video Name=")
            update_video(id,name,time)

        elif choice == '4':
            list_videos()
            id=input("Enter video id:") 
            delete_video(id)
        
        elif choice == '5':
            break
        
        else:
            print('***INVALID CHOICE***')
    conn.close()

if __name__ == "__main__":
    main()