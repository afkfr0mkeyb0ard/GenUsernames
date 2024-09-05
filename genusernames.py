import sys

with open('french_firstnames.txt', 'r') as file:
    french_firstnames = [line.strip() for line in file]

with open('french_lastnames.txt', 'r') as file:
    french_lastnames = [line.strip() for line in file]

with open('english_firstnames.txt', 'r') as file:
    english_firstnames = [line.strip() for line in file]

with open('english_lastnames.txt', 'r') as file:
    english_lastnames = [line.strip() for line in file]

with open('spanish_firstnames.txt', 'r') as file:
    spanish_firstnames = [line.strip() for line in file]

with open('spanish_lastnames.txt', 'r') as file:
    spanish_lastnames = [line.strip() for line in file]

# Returns the formated usernames
#form = 1: {firstname}{lastname}
#form = 2: {f}{lastname}
#form = 3: {firstname}.{lastname}
#form = 4: {f}.{lastname}
def format_user(firstname,lastname,form):
	if form == 1:
		result = firstname + lastname
		return(result.lower())
	elif form == 2:
		result = firstname[0] + lastname
		return(result.lower())
	elif form == 3:
		result = firstname + "." + lastname
		return(result.lower())
	elif form == 4:
		result = firstname[0] + "." + lastname
		return(result.lower())

def get_usernames(lang="all",form=3):
	result = []
	if lang == "fr":
		for lastname in french_lastnames:
			for firstname in french_firstnames:
				result.append(format_user(firstname=firstname,lastname=lastname,form=form))
	elif lang == "en":
		for lastname in english_lastnames:
			for firstname in english_firstnames:
				result.append(format_user(firstname=firstname,lastname=lastname,form=form))
	elif lang == "es":
		for lastname in spanish_lastnames:
			for firstname in spanish_firstnames:
				result.append(format_user(firstname=firstname,lastname=lastname,form=form))
	elif lang == "all":
		firstnames_all = french_firstnames + english_firstnames + spanish_firstnames
		firstnames_all = list(dict.fromkeys(firstnames_all))
		lastnames_all = french_lastnames + english_lastnames + spanish_lastnames
		lastnames_all = list(dict.fromkeys(lastnames_all))
		for lastname in lastnames_all:
			for firstname in firstnames_all:
				result.append(format_user(firstname=firstname,lastname=lastname,form=form))
	return result

if '-h' in sys.argv :
	print('Usage: python3 genusernames.py [-f1/f2/f3/f4] [-es/fr/en]')
	print('-en       Use English dictionary only')
	print('-fr       Use French dictionary only')
	print('-es       Use Spanish dictionary only')
	print('-f1       Output format: {firstname}{lastname}')
	print('-f2       Output format: {f}{lastname}')
	print('-f3       Output format: {firstname}.{lastname}')
	print('-f4       Output format: {f}.{lastname}')
	print('-h        Display help')
	sys.exit()

if "-f1" in sys.argv:
	form = 1
elif "-f2" in sys.argv:
	form = 2
elif "-f3" in sys.argv:
	form = 3
elif "-f4" in sys.argv:
	form = 4
else:
	form = 3

if "-es" in sys.argv:
	lang = "es"
elif "-fr" in sys.argv:
	lang = "fr"
elif "-en" in sys.argv:
	lang = "en"
else:
	lang = "all"

print("Using format" + str(form) + " and language " + lang)
print("")

result = get_usernames(lang,form)
result.sort()
result = list(dict.fromkeys(result))
for username in result:
	print(username)