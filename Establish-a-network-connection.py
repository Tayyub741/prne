# Import required modules/packages/library
import pexpect

# Define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

#---------Create the SSH session---------------------------
session = pexpect.spawn('ssh ' + username + '@' + ip_address,
 encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
 print('--- FAILURE! creating session for: ', ip_address)
 exit()

# Session expecting password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
 print('--- FAILURE! entering password: ', password)
 exit()


#-----------output running  config and save the file locally---------------

  
  #Set the terminal length to 0
    session.sendline('terminal length 0')
    result= session.expect(['#'])

    #Check the running config
    session.sendline("show run brief")
    result= session.expect(['#'])
    config_info = session.before


#Enable System logs to keep track of all actions
    command = 'echo logging on'
    result = subprocess.run(command, shell=True)

     #Check for any errors if any are discovered show a warning message and exit.
    if result != 0:
        print('FAILED TO CHANGE SYSTEM LOGS , INVALID INPUT:')
        exit()

    #Display message that the user has successfully added Exec timeout, if it works.
    print('')
    print('-------------------------------------------------------------------------')
    print('')
    print('-------------------------------------------------------------------------')
    print('Successfully added System logs timeout!')
    print('')
    print('-------------------------------------------------------------------------')


#Display message that the user has successfully logged in, if it works.
    print('-------------------------------------------------------------------------')
    print('')
    print('--- You have logged in succesfully! connecting to:', ip_address)
    print('---                                      Username: ' , username)
    print('---                                      Password: ' , password)
    print('')
    print('-------------------------------------------------------------------------')

    #Set the terminal length to 0
    session.sendline('terminal length 0')
    result= session.expect(['#'])

    #Check the running config
    session.sendline("show startup-config")
    result= session.expect(['#'])
    config_info = session.before

    #Write into a file the running config
    outfile = open('config_2.txt', 'w')
    outfile.write(config_info)


    file_path_1 = "/home/devasc/labs/prne/config_1.txt"

    file_path_2 = "/home/devasc/labs/prne/config_2.txt"

   
    command = f"diff {file_path_1} {file_path_2}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print("Files are identical.")
    else:
        print("Files differ:")
        print(result.stdout)

    #Terminate telnet to device and close the session
    session.sendline('quit')
    session.close()
    exit()    



elif choice == '5':
    print('bye')
    exit()  

#----------------------modify hostname----------------------------------
# Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
 print('--- Failure! entering enable mode')
 exit()
# Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
 print('--- Failure! entering enable mode after sending password')
 exit()


# Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
 print('--- Failure! entering config mode')
 exit()


# Change the hostname to Tayyub
session.sendline('hostname Tayyub')
result = session.expect([r'Tayyub\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
 print('--- Failure! setting hostname')


# Exit config mode
session.sendline('exit')
# Exit enable mode
session.sendline('exit')


# Display a success message if works
print('------------------------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
print('')
print('------------------------------------------------------')
