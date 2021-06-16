#!/usr/bin/env python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

## suppress warnings generated by Paramiko
## at time of writing, paramiko is generating deprecation warnings
import warnings

## python3 -m pip install paramiko
import paramiko

## describe the types of warnings to ignore
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"},\
            {"un": "fry", "ip": "10.10.2.4"}]

    # harvest private key for all three servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    try:
        ## loop across credz
        for cred in credz:
            ## create a session object with SSHClient
            sshsession = paramiko.SSHClient()

            ## add host key policy
            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # display our connections
            print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))
            # make a connection
            sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

            sftpsession = sshsession.open_sftp()

            # move file, and also rename extension to kola
            sftpsession.put("slurm.cola", "/home/" + cred.get("un") + "/slurm.kola")
        
            # display the current working directory of remote system
            working_dir = sftpsession.listdir()

            print("Files in the remote home directory:")
            for onefile in working_dir:
                # check the FIRST character of the string
                # filter out IF it begins with a "."
                if "." not in onefile[0]:
                    print(onefile)


        ## close SFTP and SSH connection
        sftpsession.close()
        sshsession.close()            
    except:                        
        ## close SFTP and SSH connection due to error
        print("Error with connections")
        print("Closing connections...")
        sftpsession.close()
        sshsession.close()
        print("Connections closed.")

    print("\nLooping with Python and Paramiko!")
    
main()

