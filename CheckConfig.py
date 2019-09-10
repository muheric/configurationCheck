import configparser
from configparser import ConfigParser
import codecs
#config1=ConfigParser.ConfigParser()
parser = ConfigParser()
candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
              'simple.ini', 'multisection.ini',]
              #Finding the configuration files, reading the loaded config files
found = parser.read(candidates)
missing = set(candidates) - set(found)
print('Found config files:', sorted(found))
print('Missing config files:', sorted(missing))

#parser.read('simple.ini')

#print parser.get('bug_tracker', 'url')

#opening the file with the correct encoding
from configparser import SafeConfigParser
import codecs
with codecs.open('unicode.ini', 'r', encoding='utf-8') as f:
    parser.read(f)
    password = parser.get('bug_tracker', 'password')

print('Password:', password.encode('utf-8'))
print('Type    :', type(password))
print('repr()  :', repr(password))

#Accessing configuration Settings

from configparser import SafeConfigParser

parser = ConfigParser()
parser.read('multisection.ini')

for section_name in parser.sections():
    print('Section:', section_name)
    print('  Options:', parser.options(section_name))
    for name, value in parser.items(section_name):
        print('  %s = %s' % (name, value))
    print

#Testing weather the values are present
from configparser import SafeConfigParser

parser = ConfigParser()
parser.read('multisection.ini')

for candidate in [ 'wiki', 'bug_tracker', 'dvcs' ]:
    print('%-12s: %s' % (candidate, parser.has_section(candidate)))

#Link to this tutorial is https://pymotw.com/2/ConfigParser/


