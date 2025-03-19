import os
# 1 task
# path=r"C:\Users\Ерс\Desktop"
# all=list(os.listdir(path))
# files=[]
# dir=[]
# for i in all:
#     element_path=os.path.join(path,i)
#     if os.path.isfile(element_path):
#         files.append(i)
#     if os.path.isdir(element_path):
#         dir.append(i)
# print(f"all directories and files: {all}")
# print("********************")
# print(f"only files: {files}")
# print("********************")
# print(f"only directories: {dir}")

# 2 task
# path=r"C:\Users\Ерс\Downloads"
# if os.path.exists(path):
#     print("file exists")
#     if os.access(path,os.R_OK):
#         print("File is readble")
#     else:
#         print("file is not readble")
    
#     if os.access(path, os.W_OK):
#         print("file is writable")
#     else:
#         print("file is not writable")
    
#     if os.access(path, os.X_OK):
#         print("file is executable")
#     else:
#         print("file is not executable")
# else:
#     print("file does not exist")


# 3 task
# path=r"C:\Users\Ерс\Downloads"
# if os.path.exists(path):
#     print("file exists")
#     print(f"name of the file {os.path.basename(path)}")
#     print(f"name of the directory {os.path.dirname(path)}")
# else:
#     print("file does not exist")


# 4 task
# path=r"C:\Users\Ерс\Desktop\w3\abcd.txt"
# f=open(path,'r')
# cnt=0
# for i in f:
#     cnt+=1
# print(cnt)


# 5 task
# path=r"C:\Users\Ерс\Desktop\w3\abcd.txt"
# list=["artur morgan", " john marston", " mika the rat"]
# f=open(path, 'w')
# for i in list:
#     f.write(i)
# print(f.read)

# 6 task
# for i in range(0,26):
#     s=chr(65+i)+".txt"
#     f=open(s,'w')
#     f.write("")
#     f.close()


# 7 task
# path=r"C:\Users\Ерс\Desktop\w3\abcd.txt"
# f=open(path, 'r')
# f1=open('efg.txt','w')
# for i in f:
#     f1.write(i)
# f.close()
# f1.close()
# with open('efg.txt','r') as f1:
#     print(f1.read())


# 8 task
# path=r"C:\Users\Ерс\Desktop\w3\ab.txt"
# if os.path.exists(path):
#     print("this file exists and will be deleted")
#     os.remove(path)
# else:
#     print("this file does not exist")

# for i in range(0,26):
#     s=chr(65+i)+".txt"
#     if os.path.exists(s):
#         print("this file exists and will be deleted")
#         os.remove(s)
#     else:
#         print("this file does not exist")
# code above to delete all files A.txt, B.txt,..., Z.txt