from bs4 import BeautifulSoup as BS
import datetime
with open('index.html') as fp:
    soup = BS(fp, features="html.parser")
now = datetime.datetime.now()
rules = '''
The Technology Club | notblind development team
HOW TO USE NotBlindWriter(R)
When prompted with 'Write here>', write down the text of your article.
After pressing 'return', you will be asked for the 'command>' prompt.
Enter 'exit' to exit the article.
Enter 'image' to insert an image.
Enter 'newline' to go to the next line.

NOTE: THIS SOFTWARE IS STILL IN BETA!!!
'''
print(rules)
head = input('Enter title>')
original_tag = soup.body
new_tag = soup.new_tag("div", id="blogpost")
original_tag.append(new_tag)
h = soup.new_tag('h1')
h.string = head
new_tag.append(h)
date = soup.new_tag('p')
date.string = now.strftime("%Y-%m-%d %H:%M")
new_tag.append(date)
while True:
    inp = input('Write here>')
    if inp != '':
        par = soup.new_tag('p')
        new_tag.append(par)
        par.string = inp
    else:
        pass
    command = input('command>')
    if command == 'exit':
        break
    elif command == 'newline':
        pass
    elif command == 'image':
        src = input('imgsrc>')
        image = soup.new_tag('img', src=src, height="30%", width="30%")
        new_tag.append(image)
    else:
        print('Invalid command! Moving to newline!!')
hr=soup.new_tag('hr')
new_tag.append(hr)
with open('index.html','w') as outf:
    outf.write((soup.prettify()))
    input('Your changes have been published! Press return to exit.')
