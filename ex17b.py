from sys import argv
from os.path import exists

script, from_file, to_file = argv; in_data = (open(from_file).read()); open(to_file, 'w').write(in_data)

#print(f"Copying from {from_file} to {to_file}")

#in_file = open (from_file)
#in_data = (in_file.read())
#in_data = (open(from_file).read())


#print(f"The input file is {len(in_data)} bytes long. " + f"The output file exists? {exists(to_file)}")
#print(f"Does the output file exist? {exists(to_file)}")
#print(f"Ready, hit the RETURN key to comtinue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')

#out_file.write(in_data)

#open(to_file, 'w').write(in_data)


#print("Alright, all done.")
# out_file.close()
#in_file.close()
