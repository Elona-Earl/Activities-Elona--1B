# dictionary
program_language = ['java','C#','C++', 'Phython', 'Perl', "Go lang", 'JavaScript']

# index
print(program_language[-1])

# (keys : Values, keys : Values)
proglang_dictionary = {'mejo mahirap': 'Java', 'ok lang':"C#",'sobrang hirap': "C++",\
                       "ok pa": "Phython", 'pang matanda': "perl", 'bago lang': 'go lang', "pang web dev": 'JavaScript'}

print(proglang_dictionary['bago lang'])

# adding item to a dictionary 
proglang_dictionary['pang noob']= 'html'

print(proglang_dictionary['pang noob'])

print(proglang_dictionary)

proglang_dictionary.pop()