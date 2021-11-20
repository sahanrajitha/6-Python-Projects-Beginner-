import os

def main(): 
    x = 0
    a = 0
    path = input("Input Path : (C:\python\)") + "@"#"E:/notepad ++ projects/6 python projects in freecodecamp video/renamed files/"
    for i in path:
        if i == "\\":
            path = path.replace("\\","/")
        a += 1
    if path[-1] != ("/") :
        path = path.replace("@","/")


    input_name = input("Enter a New Name: ")
    file_extention = input("Input a file extention: (.png) ")

    for filename in os.listdir(path):
        x += 1
        my_dest = input_name + str(x) + file_extention
        my_source = path + filename
       # print(my_source)
        my_dest = path + my_dest
       # print(my_dest)
        os.rename(my_source,my_dest)

    print("\nRenamed Succusfully !!")
    
if __name__ == '__main__':
        main()

