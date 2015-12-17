from string import maketrans


# load in rdata file and convert to a Python dictionary
rdata = open('lexical_database.csv')
rdata = rdata.readlines()

word_list = rdata[0]
word_list = word_list.split(',')
word_list = [x[1:-1] for x in word_list]
del word_list[0]
word_list[-1] = 'zymurgy'

frequency_list = rdata[1]
frequency_list = frequency_list.split(',')
del frequency_list[0]
frequency_list[-1] = '0.0000000319756700559721'
frequency_list = [float(x) for x in frequency_list]

frequency_table = {}
for i in range(0,len(word_list)):
	frequency_table[word_list[i]] = frequency_list[i]

print frequency_table['honorless']
print frequency_table['boof']
print frequency_table['lawner']

def encrypt(input_string,shift=7):
	trans_domain = 'abcdefghijklmnopqrstuvwxyz'
	trans_range = ''

	for i in range(0,len(trans_domain)):
		trans_range = trans_range + trans_domain[(i+shift)%26]
	trans_function = maketrans(trans_domain,trans_range)

	output_string = input_string.translate(trans_function)

	return output_string

