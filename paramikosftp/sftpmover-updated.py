#!/usr/bin/env python3
## Moving files with SFTP

## import standard library imports
import os
## import Paramiko so we can talk SSH
import paramiko
## allow user to pass input at prompt
import argparse

def sftpmover(dir2move, sftpsessionobj):
  ## iterate across the files within directory
  for x in os.listdir(dir2move): # iterate on directory contents
    if not os.path.isdir(dir2move+x): # filter everything
                                      # that is NOT a directory
      sftpsessionobj.put(dir2move+x, "/tmp/"+x) # move file to target location

def main():
  ## where to connect to
  t = paramiko.Transport("10.10.2.3", 22) ## IP and port

  ## how to connect (see other labs on using id_rsa private / public keypairs)
  t.connect(username="bender", password="alta3")

  ## Make an SFTP connection object
  sftp = paramiko.SFTPClient.from_transport(t)

  sftpmover(args.moveme, sftp)

  ## close the connection
  sftp.close() # close the SFTP connection
  
  t.close() # close SSH connection

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("moveme", help="Directory containing files you wish to move.", type=str)
  args = parser.parse_args()
  main()

