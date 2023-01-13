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
PASS = "Nux2017." # Define password before using script (PASS is empty for Git security purposes for now (arguments will be implemented))

PROJECT_ROOT = ""


LIB_FOLDER_PATH = ""
DATABASE_FOLDER_PATH = ""
WWW_FOLDER_PATH = ""


ROOT_DIRECTORY = 'C:\\Users'
HOME_DIRECTORY = os.path.expanduser( '~' )

'''
#ignores known_hosts file check - to be tested
cnOpts = pysftp.CnOpts()
cnOpts.hostkeys = None
'''



def find_grizzly_files():
    global PROJECT_ROOT, LIB_FOLDER_PATH, DATABASE_FOLDER_PATH, WWW_FOLDER_PATH
    sys.stdout.write("Searching local project files...\n")
    for root, dirs, files in os.walk(HOME_DIRECTORY): # Assumes project is somewhere in the home directory (needs improvement)
        for dir in dirs:
            if dir.strip() == "enterprise-cloud" and PROJECT_ROOT.strip() == "": # Searching only up to enterprise cloud to shorten search time
                PROJECT_ROOT = os.path.join(root, dir) + "\\Virtual Appliance\\opt\\grizzly"
                LIB_FOLDER_PATH = PROJECT_ROOT + "\\lib\\"
                DATABASE_FOLDER_PATH = PROJECT_ROOT + "\\database"
                WWW_FOLDER_PATH = PROJECT_ROOT + "\\www"
                #TODO: separate folder paths may not be necessary, just project root, can add specific paths when copying to remote
                '''
                print ("Root: " + PROJECT_ROOT + "\n")
                print ("Lib: " + LIB_FOLDER_PATH + "\n")
                print ("DB: " + DATABASE_FOLDER_PATH + "\n")
                print ("www: " + WWW_FOLDER_PATH + "\n")
                '''
                print ("Lib: " + LIB_FOLDER_PATH + "\n")
                break

def replace_remote_with_local(sftp, localroot, remoteroot):
    pass


def upload_to_remote():
    global PROJECT_ROOT, LIB_FOLDER_PATH, DATABASE_FOLDER_PATH, WWW_FOLDER_PATH
    with pysftp.Connection(HOST, username=USER, password=PASS) as sftp:
        '''
        if sftp.exists("/opt/grizzly/lib"):
            sys.stdout.write("Deleting all lib files...\n")
            sftp.execute("rm -rf /opt/grizzly/lib")
        '''
        # TODO: upload folder from local to remote with put_d (if possible, else file by file)
        print("Uploading files to remote...")
        #sftp.put_d(LIB_FOLDER_PATH, "/opt/grizzly/")
        if not sftp.exists("/opt/grizzly/lib"):
            sftp.mkdir("/opt/grizzly/lib/")
        for file in os.listdir(LIB_FOLDER_PATH):
            local_file = LIB_FOLDER_PATH + file
            remote_file = "/opt/grizzly/lib/" + file
            print(file)
            print(local_file)
            print(remote_file + "\n")
            if(sftp.exists("/opt/grizzly/lib/" + file)):
                sftp.remove("/opt/grizzly/lib/" + file)
            sftp.put(localpath=local_file, remotepath=remote_file)
            #upper code works but it doesn't copy fips folders (because they are folders)
            #sftp.put_r(LIB_FOLDER_PATH + , "/opt/grizzly/lib/")


if __name__ == "__main__":
    find_grizzly_files()
    upload_to_remote()