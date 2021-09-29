"""
script.py
runs the script mode
Russell Lee
"""
import site_generator
from dataclasses import dataclass

# FileParameters helps organize how to export the files
@dataclass
class FileParameters:
    mode: str
    settings: list
    title: str
    text: str
    number: str
    multi: list
    titles: list


def file_builder():
    """
    builds a file by collecting all the names needed
    :return: a list of the names of the files
    """
    repeater = True
    files = []
    while repeater is True:
        files.append(input('What is the file name? '))
        more = input("Do you want to add another file? [yes] ")
        if more == 'yes' or more == '':
            pass
        else:
            repeater = False
    return files


def file_writer(file):
    """
    writes the file and sends all the lines as a string
    :param file: the file name
    :return: the entire file as a string
    """
    doc = open(file)
    generator = []
    final = ''
    for line in doc:
        generator += line.strip().split('\n')
    for i in generator:
        final += i + '\n'
    return final


def title_finder(files):
    """
    returns the title of files
    :param files: the list of the files
    :return: the titles of the files in list form
    """
    thing = []
    for i in files:
        holder = open(i)
        for line in holder:
            thing += line.strip().split('\n')
            break
    return thing


def script_main(background, font_color, font_header, font_type):
    """
    main function of the script mode
    :param background: the background for the file
    :param font_color: the text color
    :param font_header: the color of the header
    :param font_type: the type of font used
    :return:
    """
    files = file_builder()
    for i in range(0, len(files)):
        final = file_writer(files[i])
        titles = title_finder(files)
        site_generator.generator_main(FileParameters(
            'script',
            [background, font_color, font_header, font_type],
            '',
            final,
            str(i),
            files,
            titles
            ))
