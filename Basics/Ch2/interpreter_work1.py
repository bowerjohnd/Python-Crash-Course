print("-" * 50)

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("-" * 50)

fav_language = "python "
print("|" + fav_language + "|")
print("|" + fav_language.rstrip() + "|")
print("|" + fav_language + "|")
fav_language = fav_language.rstrip()
print("|" + fav_language + "|")

print("-" * 50)

fav_language = " python "
print("|" + fav_language + "|")
print("|" + fav_language.rstrip() + "|")
print("|" + fav_language.lstrip() + "|")
print("|" + fav_language.strip() + "|")

print("-" * 50)

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
