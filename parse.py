import re

f = open('raw.txt', 'r')
fo = open('links.txt', 'w')
for line in f:
  s = re.findall('{"identifier": "(.*)"}', line)
  fo.writelines(s)
  fo.write("\n")
f.close()
fo.close()