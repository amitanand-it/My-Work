import re
pattern = r'<[\w]*?>'

#2
#<html><head><title>HTML Parser - I</title></head>
#<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

for _ in range(int(input())):
    for line in input():
        for tag in re.finditer(pattern, line):
            print(tag)