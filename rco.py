""" THIS WORKS
def runcmd(self):
	data = input(str(os.getcwd() + ">"))
	
	while data != 'q':
		if data[:2] == 'cd':
			if os.path.isdir(data[3:]):
				os.chdir(data[3:])
			else:
				print(f"Error: {data[3:]} is invalid path...")
		# checking that command is not 'cd' prevents the 'cd'
		# from running through our Popen and throwing an error			
		if data[:2] != 'cd' and len(data) > 0:
			cmd = Popen(data, shell=True,
						stdout=PIPE,
						stderr=PIPE,
						stdin=PIPE)
			output_bytes = cmd.stdout.read() + cmd.stderr.read()
			output_str = output_bytes.decode('utf-8')
			print(output_str)				 
			
		data = input(os.getcwd() + '>')
"""

""" OLD TESTING PURPOSES
if cmd[:2] == 'cd':
	if len(cmd) <= 2:
		os.chdir("C:\\")
	else:
		os.chdir(cmd[3:])
	# Popen('cd', cwd=str(cmd[:3]))
if len(cmd) > 0:
	data = Popen(cmd[:], shell=True, stdout=PIPE, stderr=PIPE)
	output_bytes = data.stdout.read() + data.stderr.read()
	# BELOW SORTA FIXES ERRORS ON DIRECTORY CHANGE
	# AND IS MORE SECURE THAN shell=True 
	# data = Popen(['cmd', '/c', cmd[:]], stdout = PIPE, stderr = PIPE)			
	# output_bytes = data.stdout.read()	# removed + data.stderr.read() due to error
										# on directory changes
	output_str = str(output_bytes, 'utf-8')
	print(output_str)
"""	
