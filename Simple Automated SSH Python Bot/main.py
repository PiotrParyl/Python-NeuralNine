import getpass
from fabric

password = getpass.getpass("Enter pass: ")

config = Config()
conn Connection()

