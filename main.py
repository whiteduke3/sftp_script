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
        print("\n")
        for dir in dirs:
            if dir.strip() == "enterprise-cloud" and PROJECT_ROOT.strip() == "": # Searching only up to enterprise cloud to shorten search time
                PROJECT_ROOT = os.path.join(root, dir) + "\\Virtual Appliance\\opt\\grizzly"
                LIB_FOLDER_PATH = PROJECT_ROOT + "\\lib\\"
                DATABASE_FOLDER_PATH = PROJECT_ROOT + "\\database\\"
                WWW_FOLDER_PATH = PROJECT_ROOT + "\\www\\"
                #TODO: separate folder paths may not be necessary, just project root, can add specific paths when copying to remote
                '''
                print ("Root: " + PROJECT_ROOT + "\n")
                print ("Lib: " + LIB_FOLDER_PATH + "\n")
                print ("DB: " + DATABASE_FOLDER_PATH + "\n")
                print ("www: " + WWW_FOLDER_PATH + "\n")
                '''
                break

def replace_remote_with_local(sftp, localroot, remoteroot):
    pass


def rm(sftp, path):
    files = sftp.listdir(path)
    for f in files:
        filepath = path + "/" + f
        try:
            sftp.remove(filepath)
        except IOError:
            rm(sftp, filepath)

    sftp.rmdir(path)

def upload_dir(sftp, localpath, remotepath):
    for fso in os.listdir(localpath):
        if os.path.isdir(localpath + fso):
            upload_dir(sftp, localpath+fso, remotepath+fso)
        else:
            sftp.put(localpath=localpath, remotepath=remotepath+fso)

def upload_to_remote():
    global PROJECT_ROOT, LIB_FOLDER_PATH, DATABASE_FOLDER_PATH, WWW_FOLDER_PATH
    with pysftp.Connection(HOST, username=USER, password=PASS) as sftp:
        print("Uploading files to remote...")
        #removes dir at remote if it exists
        if sftp.exists("/opt/grizzly/lib/"):
            rm(sftp, "/opt/grizzly/lib")
        sftp.mkdir("/opt/grizzly/lib/")
        for fso in os.listdir(LIB_FOLDER_PATH):
            local_path = LIB_FOLDER_PATH + fso
            remote_path = "/opt/grizzly/lib/" + fso
            #print(fso)
            #print(local_path)
            #print(remote_path + "\n")
            if os.path.isfile(local_path):
                sftp.put(localpath=local_path, remotepath=remote_path)
            elif os.path.isdir(local_path):
                #sftp.put_d(localpath=local_path, remotepath="/opt/grizzly/lib/")
                #upload_dir(sftp, local_path, remote_path)
                pass
            '''
            code above works but it doesn't copy directories, 
            need to implement upload_dir function to upload directory and it's contents recursively
            '''



if __name__ == "__main__":
    find_grizzly_files()
    upload_to_remote()
