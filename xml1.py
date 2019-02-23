import xml.etree.ElementTree as ET

data='''
<person>
    <name>Ankit</name>
    <phone type="intl">
       +91 8709774667
     </phone>
     <email hide="kumarankit3450@gmail.com"/>
</person>'''

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
