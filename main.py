import click
import os
import datetime 
import subprocess 


#setup---------------------------------------------------------------------------------

@click.command() #get info and turn into a hash
def getsysinfo():
	pass

@click.command() #get from and to a time of access
def setuptimeofaccess():
	pass

@click.command()
@click.option('--user',
           	  prompt=True,
              default=lambda: os.environ.get('USER', ''))
@click.option('--password',
              prompt=True,
              default=lambda: HiddenPassword(os.environ.get('PASSWORD', '')),
              hide_input=True)
def setuplogin(user, password):
			print('user: {}'.format(user))
			if isinstance(password, HiddenPassword):
			    password = password.password
			    
			print('password: {}'.format(password))

@click.command()
def setupkeyread():
	pass

@click.command()
def getresetkeys():
	pass

@click.group()
def setup():
	pass

setup.add_command(getsysinfo)
setup.add_command(setuptimeofaccess)
setup.add_command(setuplogin)
setup.add_command(setupkeyread)
setup.add_command(getresetkeys)
#---------------------------------------------------------------------------------------
#login----------------------------------------------------------------------------------
@click.command()
@click.option('--user', prompt=True, default="",help="Enter USER ID")
@click.option('--password',
              prompt=True,
              default=lambda: HiddenPassword(os.environ.get('PASSWORD', '')),
              hide_input=True)
@click.option('--key')#check if true
def sysinfo():
	pass
def time():
	pass

#---------------------------------------------------------------------------------------
#reset----------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------
#



if __name__ == '__main__':
	print("===========4SAKEN=============")
	func = input("4Saken >")
	if func == "setup":
   		setup()
