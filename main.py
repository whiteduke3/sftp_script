'''
MAIN FILE
'''
from ftplib import FTP
import pysftp
import os
import sys

HOST = "dinoce-ghoul2"
USER = "root"
PASS = "Nux2017."

root_dir = 'C:\\'

def copy_local_files():
    for i, (folder, subfolders, files) in enumerate(os.walk(root_dir)):
        if(i<=1):
            print(folder)
        else:
            break

def upload_to_remote():
    with pysftp.Connection(HOST, username=USER, password=PASS) as sftp:
        print(sftp.pwd)


if __name__ == "__main__":
    copy_local_files()
    #upload_to_remote()