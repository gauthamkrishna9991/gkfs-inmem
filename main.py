from gkfs import File, Directory
root = Directory('/',None)
pwd = root
print("""
GK_FS File System
    Prototype 2019_001
    An in-memory quasi-filesystem plus shell written in Python 3
    Author: Goutham Krishna K V <gauthamkrishna9991@live.com>
    This tool comes with NO WARRANTIES, implied or otherwise and is protected by GNU Public Licence ver. 3.0
    For licence, read COPYING
        """)
while True:
    prompt = input("["+pwd.getPath() + "]$ ")
    keys = prompt.split(' ')
    command = keys[0]
    if command == 'exit' or command == 'quit' or command == 'quit':
        break
    elif command == 'ls'  or command == 'dir':
        print(pwd.getContents())
    elif command == 'cd':
        isFound = False
        if keys[1] == '/':
            pwd = root
            isFound = True
        elif keys[1] == '..':
            if not pwd.parentDir is None:
                pwd = pwd.parentDir
            isFound = True
        for content in pwd.contents:
            if keys[1] == content.fileName and content.isDir():
                pwd = content
                isFound = True
                break
        if not isFound:
            print("Directory " + keys[1] + " not found")
    elif command == 'mkdir':
        Directory(keys[1], pwd)
    elif command == 'touch':
        File(keys[1], pwd)
    elif command == 'pwd':
        print(pwd.getPath())
    elif command == 'into':
        isFound = False
        for content in pwd.contents:
            if keys[1] == content.fileName and not content.isDir():
                content.setContents("".join(keys[2:]))
                isFound = True
        if not isFound:
            print('File not found. Try again')
    elif command == 'cat':
        isFound = False
        for content in pwd.contents:
            if keys[1] == content.fileName and not content.isDir():
                print(content.readContents())
                isFound = True
        if not isFound:
            print("File not found, try again")
