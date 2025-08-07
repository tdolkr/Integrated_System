import xml.etree.ElementTree as ET

# Parse the XML
tree = ET.parse('book.xml')
root = tree.getroot()

print("Books:")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    description = book.find('description').text

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Description: {description}")
    print('-' * 40)

target_title = input("Enter the title of the book you want to delete: ")

found = False
for book in root.findall('book'):
    title = book.find('title').text
    if title.lower() == target_title.lower():  
        root.remove(book)
        found = True
        print(f'\nBook titled "{title}" has been deleted.\n')
        break

if not found:
    print(f'\nBook titled "{target_title}" not found.\n')

tree.write('book.xml')

print("Remaining books:")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    description = book.find('description').text

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Description: {description}")
    print('-' * 40)
