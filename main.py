"""
Author: Dino Celikovic
Script for automating transfer of build files to remote HYCU backup controller via SFTP protocol
"""
from ftplib import FTP
import pysftp
import os
import sys

HOST = "dinoce-ghoul2"
USER = "root"
PASS = "" # Define password before using script (PASS is empty for Git security purposes for now (arguments will be implemented))

PROJECT_ROOT = ""


LIB_FOLDER_PATH = ""
DATABASE_FOLDER_PATH = ""
WWW_FOLDER_PATH = ""


ROOT_DIRECTORY = 'C:\\Users'
HOME_DIRECTORY = os.path.expanduser( '~' )


def find_grizzly_files():
    global PROJECT_ROOT, LIB_FOLDER_PATH, DATABASE_FOLDER_PATH, WWW_FOLDER_PATH
    for root, dirs, files in os.walk(HOME_DIRECTORY): # Assumes project is somewhere in the home directory (needs improvement)
        for dir in dirs:
            if dir.strip() == "enterprise-cloud" and PROJECT_ROOT.strip() == "": # Searching only up to enterprise cloud to shorten search time
                PROJECT_ROOT = os.path.join(root, dir) + "\\Virtual Appliance\\opt\\grizzly"
                LIB_FOLDER_PATH = PROJECT_ROOT + "\\lib"
                DATABASE_FOLDER_PATH = PROJECT_ROOT + "\\database"
                WWW_FOLDER_PATH = PROJECT_ROOT + "\\www"
                #TODO: separate folder paths may not be necessary, just project root, can add specific paths when copying to remote
                '''
                print ("Root: " + PROJECT_ROOT + "\n")
                print ("Lib: " + LIB_FOLDER_PATH + "\n")
                print ("DB: " + DATABASE_FOLDER_PATH + "\n")
                print ("www: " + WWW_FOLDER_PATH + "\n")
                '''
                break

def copy_local_to_remote(sftp, localpath, remotepath):
    pass


def upload_to_remote():
    with pysftp.Connection(HOST, username=USER, password=PASS) as sftp:
        sftp.execute("rm -rf /opt/grizzly/lib/*")
        sftp.put()


if __name__ == "__main__":
    print("Found project files")
    find_grizzly_files()
    #upload_to_remote()