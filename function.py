import os
def one():
	
	infile = open("password.txt", 'r') # open file for appending
	outfile = open("pass2.txt","a") # open file for appending

	for line in infile.readlines():
  	    outfile.write(line.strip("\n")+",day Mon 00 00:00:00 year\n")

	infile.close()
	outfile.close()
	os.remove("password.txt");
	os.rename("pass2.txt", "password.txt");#Wed Sep 17 16:16:25 2014

 

