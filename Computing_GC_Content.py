file = open('gene_data.txt', 'r')
Str_data = (file.readlines())
#Str_data = '-'.join(Str_data)
#Str_data = Str_data.trim()
#
processed_str = ''
for itr in Str_data:
    processed_str += str(itr).strip('\n')

string_list = processed_str.split('>')
string_list = string_list[1:]

gene_dictionary = {}

for itr in string_list:
    key = itr[0:13]
    value = itr[13:]
    gene_dictionary[key] = value

#print(gene_dictionary)

max_percent = 0.0
key = ''

for itr in gene_dictionary:
    count_CG =  gene_dictionary[itr].count('C') + gene_dictionary[itr].count('G')
    length = len(gene_dictionary[itr])
    percentage = count_CG * 100 / length
    if percentage > max_percent:
        key = itr
        max_percent = percentage

print(F'{key} \n{max_percent}')


