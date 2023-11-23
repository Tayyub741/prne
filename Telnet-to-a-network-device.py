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

#Terminate telnet to device and close session
session.sendline('quit')
session.close
