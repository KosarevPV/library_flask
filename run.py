import os


os.system("cd library_flask")
os.system("pip install virtualenv")
os.system("virtualenv venvLIB")
os.system(r"venvLIB\Scripts\activate")
os.system("python -m pip install -r requirements.txt")
os.system("python app.py")
