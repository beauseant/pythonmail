import configparser
from lib import sendMail

if __name__ == "__main__":

	try:
		config = configparser.ConfigParser()
		config.read('mail.conf')
		username = config.get('mail', 'user')
		pwd = config.get ('mail','passwd')
		server = config.get ('mail','server')


		sm = sendMail.sender ( username=username, host=server, pwd = pwd)

		subject = 'mensaje de prueba'
		body = 'hola patata'
		from_addr = 'fulanito'
		to_addr_list = ['mail1', 'mail2']

		errors = sm.sent (subject=subject, body=body, from_addr=from_addr, to_addr_list = to_addr_list,cc_addr_list=[])

		if problems:
			print ('Sending mail problems, %s' % errors)

	except Exception as E:
		print ('Error: %s' % E)
		exit()

