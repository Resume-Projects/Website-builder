"""
wizard.py
wizard mode for html_builder
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


def loop_inputs(text):
    """
    creates the file format for the site generator
    :param text: the format for the generator
    :return: the format to be converted
    """
    inputs = True
    while inputs is True:
        text += "!new_paragraph\n"
        text += "!title " + input('Title of your paragraph: ') + '\n'
        text += input("Content of your paragraph (single line) ") + '\n'
        ask_img = input("Do you want to add images? [yes] ")
        if ask_img == 'yes' or ask_img == '':
            ask_loop = True
            while ask_loop is True:
                text += '!image ' + input('Image file name: ') + '\n'
                ask_img = input('Do you want to add another image? [yes] ')
                if ask_img != 'yes' and ask_img != "":
                    ask_loop = False
        # text += '\n'
        repeat = input('Do you want to add another paragraph to your website? [yes] ')
        if repeat == 'yes' or repeat == '':
            pass
        else:
            return text


def wizard_main(background, font_color, header_color, font_type):
    """
    main function for wizard mode
    :param background: the background for the file
    :param font_color: the text color
    :param header_color: the color of the header
    :param font_type: the type of font used
    :return:
    """
    text = ''
    title = input("Enter a title for your web page: ") + " \n"
    text += title
    outline = loop_inputs(text)
    site_generator.generator_main(
        FileParameters('wizard', [background, font_color, header_color, font_type], title, outline, '0', [], []))
