"""
site_generator.py
Generates a site
Russell Lee
"""


from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Site:
    Title: Any
    Information: Union[None, 'Content']


@dataclass
class Content:
    Title: str
    Paragraph: str
    Images: Union[None, 'Image']
    Next: Union[None, 'Content']


@dataclass
class Line:
    Value: Any
    Next: [None, 'Line']


@dataclass
class Image:
    Location: str
    Size: Union[None, str]
    Next: Union[None, 'Image']


def fetch_title(title):
    """
    Gets the title for the web page
    :param title: title of web page
    :return: the title template
    """
    doctype = '<!DOCTYPE html>\n\
<html>\n\
<head>\n\
<title>' + title + '\n\
</title>'
    return doctype


def style(bg, fc, hc, fs):
    """
    Builds a style template
    :param bg: background color
    :param fc: font color
    :param hc: header color
    :param fs: font style
    :return: the style template
    """
    css = '<style>\n\
body {background-image: linear-gradient(180deg, ' + bg + ',white);}\n\
\n\
.center {\n\
  display: block;\n\
  margin-left: auto;\n\
  margin-right: auto;\n\
}\n\
h1   {color:' + hc + ';\n\
      font-family: ' + fs + ';\n\
      text-align:center;\n\
      }\n\
\n\
h2   {color:' + hc + ';\n\
      font-family: ' + fs + ';\n\
      text-align: justify;\n\
      }\n\
\n\
p    {color:' + fc + ';\n\
      font-family: ' + fs + ';\n\
      padding: 30px;\n\
      text-align: justify;\n\
      background-color: white;\n\
      box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4);\n\
      font-size: 14px;\n\
      }\n\
\n\
</style>\n'
    return css


def fetch_title_footer(title):
    """
    Gets the "footer' of the document
    :param title: title of the footer
    :return: the footer template
    """
    footer = '</head>\n\
<body>\n\
<h1> ' + title + '\n\
</h1>\n\
<hr/>\n'
    return footer


def url_linker(names, titles):
    """
    if needed, gets all of the urls
    :param names: list of the file names
    :param titles: list of the actual titles
    :return: the framework for the urls
    """
    numb = 0
    name_list = []
    url = ''
    url += '<p align="center">'
    for _ in names:
        name_list.append('new_file' + str(numb) + '.html')
        numb += 1
    numb = 0
    for i in names:
        url += '<a href="' + name_list[numb] + '">' + titles[numb] + '</a>---'
        numb += 1
    url += '\n</p>\n'
    return url


def create_body(text):
    """
    Creates the body of the passage
    :param text: The body of the passage
    :return: the framework for the body
    """
    title = text.Title
    paragraph = text.Paragraph
    body = '<h2>' + title + '\n\
</h2>\n\
<p>' + paragraph + '\n\
</p>\n'
    """
    text img y next n
    text img y next y
    text img n next y
    text img n next n
    """
    if text.Images is not None:
        if text.Next is None:
            return body + str(create_img(text.Images))
        else:
            return body + str(create_img(text.Images)) + create_body(text.Next)
    elif text.Next is not None:
        return body + create_body(text.Next)
    else:
        return body


def create_img(content):
    """
    creates all the images
    :param content: the content needed to make images
    :return: the framework for the image
    """
    location = content.Location
    size = str(content.Size)
    img = '<img src="' + location + '" width= "' + size + '" class="center">\n'
    if content.Next is None:
        return img
    else:
        return img + create_img(content.Next)


"""################## File to linked list functions are below #######################"""


def linked_list(text):
    """
    creates a linked list
    :param text: the entire thing
    :return: Site
    """
    passage = text.split('\n')
    # print(passage)
    title_name = ''
    get_title = True
    while get_title is True:
        if passage[0] != '!new_paragraph':
            title_name += passage[0]
            passage.pop(0)
        else:
            get_title = False
    return Site(title_name, get_content(passage))


def get_content(passage):
    """
    create the paragraphs for the website
    :param passage: Site.Information
    :return:  more content or a none statement
    """
    if not passage:
        return None
    paragraph = ''
    passage.pop(0)
    paragraph_title = passage[0][7:]
    passage.pop(0)
    get_paragraph = True
    while get_paragraph is True:
        if not passage:
            return Content(paragraph_title, paragraph, None, None)
        elif passage[0] == '!new_paragraph':
            return Content(paragraph_title, paragraph, None, get_content(passage))
        elif passage[0][:7] == '!image ':
            image = get_image(passage)
            more = get_content(passage)
            return Content(paragraph_title, paragraph, image, more)
        else:
            paragraph += passage[0] + ' '
            del passage[0]


def get_image(passage):
    """
    fetches an image
    :param passage: the passage
    :return: an image location
    """
    photo = ''
    get_photo = True
    while get_photo is True:
        if not passage or passage[0] == '!new_paragraph':
            return None
        elif passage[0][:7] == '!image ':
            photo += passage[0][7:]
            passage.pop(0)
            photo += ' 100%'
            results = photo.split()
            return Image(results[0], results[1], get_image(passage))
        else:
            photo += passage[0]
            passage.pop(0)


def generator_main(parameters):
    """
    The main function for this file
    :param parameters: Dataclass (see the other python files)
    :return:
    """
    the_site = linked_list(parameters.text)
    title = fetch_title(the_site.Title)
    css_holder = style(parameters.settings[0],
                       parameters.settings[1],
                       parameters.settings[2],
                       parameters.settings[3])
    footer = fetch_title_footer(the_site.Title)
    if len(parameters.multi) < 2 or parameters.mode is "wizard":
        url = ''
    else:
        url = url_linker(parameters.multi, parameters.titles)
    body = create_body(the_site.Information)
    closer = '</body>\n</html>'

    # # debug
    # print(the_site)
    # print(title)
    # print(css_holder)
    # print(footer)
    # print(body)
    # print(closer)

    full_file = title + css_holder + footer + url + body + closer
    num = parameters.number
    file_name = 'new_file' + str(num) + '.html'
    with open(file_name, 'w') as file:
        file.write(full_file)
