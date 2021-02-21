#   Question 6
#   Complete the body of the format_name function. This function receives the first_name #   and last_name parameters and then returns a properly formatted string.

#   Specifically:

#   If both the last_name and the first_name parameters are supplied, the function should #   return like so:

#   print(format_name("Ella", "Fitzgerald"))
#   Name: Fitzgerald, Ella

#   print(format_name("Adele", ""))
#   Name: Adele

#   print(format_name("", "Einstein"))
#   Name: Einstein

#   print(format_name("", ""))
#   

def format_name(first_name, last_name):
	# code goes here
	if first_name != '' and last_name != '':
		return("Name: " + last_name + ", " + first_name)
	elif first_name != '' or last_name != '':
		return("Name: " + last_name + first_name)
	else:
		return ''

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string