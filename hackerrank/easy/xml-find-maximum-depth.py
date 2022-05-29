
# Ref: https://diveintopython3.net/xml.html

import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth

    if level == maxdepth:
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)
        
                
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)



"""





max_depth = 1

def traverse(node):
    global max_depth
    for child in node:
        print(child, len(child))
        if len(child) > 0:
            traverse(child)
            max_depth += 1

xml = '''
<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>
'''
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
traverse(root)
print(max_depth)

"""

"""
You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as .

Input Format

The first line contains , the number of lines in the XML document.
The next  lines follow containing the XML document.

Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Sample Output

1
Explanation

Here, the root is a feed tag, which has depth of .
The tags title, subtitle, link and updated all have a depth of .

Thus, the maximum depth is .
"""