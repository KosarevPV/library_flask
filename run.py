import os


os.chdir("library_flask")
print("+Текущая директория изменилась на folder:", os.getcwd())
os.system("pip install virtualenv")
os.system("virtualenv venvLIB")
print("+Созадана переменная среда venvLIB")

