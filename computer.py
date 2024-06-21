                                                 computer.p
import subprocess
import requests
from colorama import Fore

class Computer():                                                                                                                                def __init__(self, Terminal_Shell=False):
       self.Terminal_Shell = Terminal_Shell
    def Computer_screen(self, computer_struct="*"):
        b = Fore.BLUE
        y = Fore.YELLOW
        r = Fore.RESET
        print("\n")
        print(16 * f"{b} ", 25 * computer_struct + f"{r}")
        for I in range(6):
             print(16 * f"{b} ", computer_struct + "                       " + computer_struct + f"{r}")
        print(16 * f"{b} ", 25 * computer_struct + f"{r}")
        print(16 * " ", f"{b}          /-----\\")
        print(16 * " ", f"         /_______\  {r}")

class settings:
     def fileCW(name):
         print("""
information:
       -exit = for exit of system.
       -ok = for indication the end of reader and of write.
         """)
         file = open(name, "w")
         word = ""
         while(True):
               word = str(input(">>> "))
               if word == "-exit":
                   exit()
               if word == "-ok":
                   exit()
               file.writelines(word + "\n")
         f.close()

     def options():
        g = Fore.GREEN
        y = Fore.YELLOW
        r = Fore.RESET
        print(f"""
      {y}1.{r}{g} (Terminal Shell){r}
      {y}2.{r}{g} (requests){r}
      {y}3.{r}{g} (create and write file){r}                                                                                                       {y}4.{r}{g} (exit of system){r}
      {y}5.{r}{g} (computer struct desing){r}
          """)

        op = int(input(">>> "))
        if op == 1:
           Terminal_Shell.cmd()
        if op == 2:
           url = str(input("url: "))
           print("Do you want to save the content of the request in a file?")
           opt = str(input("[y]yes or [n]no >>: "))
           if opt == "y" or opt == "yes" or opt == "Y" or opt == "YES":
               file_name = str(input("file_name: "))
               HttpRequests.request(url, file_name, save_file=True)
           elif opt == "n" or opt == "N" or opt == "no" or opt == "NO":
               HttpRequests.request(url, file_name, save_file=False)
        if op == 3:
           file_name = str(input("file_name: "))
           settings.fileCW(file_name)
        if op == 4:
           exit()
        if op == 5:
           char_struct = str(input(">>> "))
           c = Computer()
           subprocess.call("clear")
           c.Computer_screen(char_struct)
           settings.options()

class HttpRequests():
      def request(url, name_file, save_file=False):
          response = requests.get(url)
          if save_file:
              HttpRequests.save_file_request(response.text, name_file)
          if not (save_file):
             print(response.body)
      def save_file_request(body, name_file):
          f = open(name_file, "w")
          f.write(body)
          f.close()

class Terminal_Shell():
    def cmd():                                                                                             while(True):
          command = str(input(">>> "))
          if command == "exit":
              exit()
          subprocess.call(command, shell=True)

c = Computer()
c.Computer_screen()
settings.options()
