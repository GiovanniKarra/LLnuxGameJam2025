
def get_username():
	with open("username.txt", "r") as f:
		username = f.read()
	return username