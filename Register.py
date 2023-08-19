#!/usr/bin/python 

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>5.
"""

from os import system 
from functions import create_user, read_user
from functions import update_user, delete_user
from functions import software_info  

system("clear")
print("""
====================================
|    Simple Registration System    | 
====================================
|        1 - Create user           |
====================================
|        2 - Read user             |
====================================
|        3 - Update user           |
==================================== 
|        4 - Delete user           |
==================================== 
|        5 - Software Info         |
====================================

""")

option = int(input("[*] Choose option: "))
if option == 1:
    create_user()
elif(option == 2):
    read_user()
elif(option == 3):
    update_user()
elif(option == 4):
    delete_user()
elif(option == 5):
    software_info()
else: 
    print("[-] Option not defined.\n")


