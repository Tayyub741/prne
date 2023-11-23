#Import the pexpect library
import pexpect

#Define variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

#Create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)
result = session.expect (['Username:', pexpect.TIMEOUT])


#Session expects a username, enter details
session.sendline(username)
result = session.expect (['Password:', pexpect.TIMEOUT])

#Session expects a username, enter details
session.sendline(password)
result= session.expect(['#', pexpect.TIMEOUT])

#Dislay a message if successful
print('------------------------------------------------------')
print('')
print('----Success! connecting to: ', ip_address)
print('----            Username:   ', ip_address)
print('----            Password:   ', ip_address)
print('')
print('------------------------------------------------------')

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

  

#Terminate telnet to device and close session
session.sendline('quit')
session.close
