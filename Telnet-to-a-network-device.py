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

   #Write into a file the running config
   outfile = open('config_1.txt', 'w')
   outfile.write(config_info)

   #Output the running config
   #print('This is the: ',config_info)

   #Display message that the user has successfully saved the config, if it works.
   print('-------------------------------------------------------------------------')
   print('')
   print('--- You have saved the running config succesfully!')
   print('')
   print('-------------------------------------------------------------------------')

   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('FAILED TO SAVE CONFIG, CONFIG NOT FOUND:')
       exit()

   #Display message that the user has successfully chnaged the hostname, if it works.
   print('-------------------------------------------------------------------------')
   print('')
   print('--- You have saved the running-config succesfully!: ')
   print('')
   print('-------------------------------------------------------------------------')

   #Enter the congiure terminal
   session.sendline("conf t")
   result= session.expect(['#'])

   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('FAILED TO ENTER CONFIGURE TERMINAL , INVALID INPUT:')
       exit()

   #Display message that the user has successfully entered the host terminal, if it works.
   print('-------------------------------------------------------------------------')
   print('')
   print('--- You have sucessfully entered the configure terminal: ')
   print('')
   print('-------------------------------------------------------------------------')


   #Enable secret for accessing enable.

   session.sendline("username prne secret cisco123!")
   result= session.expect(['#'])
   print('Successfully enabled secret')


   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('FAILED TO password , INVALID INPUT:')
       exit()

   #Display message that the user has successfully changed the password, if it works.
   print('-------------------------------------------------------------------------')
   print('')
   print('--- You have sucessfully changed the password: ')
   print('')
   print('-------------------------------------------------------------------------')

   # Enter line con 0
   session.sendline("line con 0")
   result= session.expect(['#'])

   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('FAILED TO enter line con 0 , INVALID INPUT:')
       exit()

   #Display message that the user has successfully entered line con 0, if it works.
   print('-------------------------------------------------------------------------')
   print('')
   print('Successfully entered line con 0')  
   print('')
   print('-------------------------------------------------------------------------')

   # Enter Exec timeout
   session.sendline("exec-timeout 10 5")
   result= session.expect(['#'])

   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('FAILED TO CHANGE EXEC TIMEOUT , INVALID INPUT:')
       exit()

   #Display message that the user has successfully added Exec timeout, if it works.
   print('')
   print('-------------------------------------------------------------------------')
   print('')
   print('-------------------------------------------------------------------------')
   print('Successfully added Exec timeout!')
   print('')
   print('-------------------------------------------------------------------------')
  
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

   #Change the configuration to CONFIG3
   session.sendline("no service password-recovery")
   result= session.expect(['#'])

   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('FAILED TO CHANGE NO PASSWORD RECOVERY , INVALID INPUT:')
       exit()

   #Display message that the user has successfully changed config, if it works.
   print('-------------------------------------------------------------------------')
   print('')
   print('Successfully added no password recovery')  
   print('')
   print('-------------------------------------------------------------------------')

   #The session needs the password now
   session.sendline(password)
   result= session.expect(['#', pexpect.TIMEOUT])

   #Check for any errors if any are discovered show a warning message and exit.
   if result != 0:
       print('SESSION LOGIN FAILED PASSWORD DOES NOT MATCH USERNAME:', password)
       exit()

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
