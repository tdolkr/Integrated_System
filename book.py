import xml.etree.ElementTree as ET

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

add_new = input("Do you want to add a new book? (yes/no): ").strip().lower()

if add_new == "yes":
    new_title = input("Enter book title: ")
    new_author = input("Enter author name: ")
    new_genre = input("Enter genre: ")
    new_description = input("Enter description: ")

    new_book = ET.Element("book")
    ET.SubElement(new_book, "title").text = new_title
    ET.SubElement(new_book, "author").text = new_author
    ET.SubElement(new_book, "genre").text = new_genre
    ET.SubElement(new_book, "description").text = new_description

    root.append(new_book)
    print(f'\nNew book titled "{new_title}" has been added.\n')

tree.write('book.xml')

print("Updated book list:")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    description = book.find('description').text

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Description: {description}")
    print('-' * 40)
