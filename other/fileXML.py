from xml.etree import ElementTree

tree = ElementTree.parse('example1.xml')
root = tree.getroot()
# print(root)
# print(root.tag, root.attrib)
# for child in root:
#     print(child.tag, child.attrib)
for element in root.iter('name'):
    print(element)  # не могу перебрать элементы name1,name2,name3
tree.write('example1_new.xml')
