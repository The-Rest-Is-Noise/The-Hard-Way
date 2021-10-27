from sys import argv

script, filename = argv

filetxt = open(filename)

print(filetxt.read())

filetxt.close()
