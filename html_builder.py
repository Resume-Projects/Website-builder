"""
html_builder.py
builds an html file
Russell Lee
"""
import turtle
import wizard
import script


def main_mode():
    """
    Chooses a mode for the website
    :return: the mode for the site
    """
    prompt = ''
    site_chooser = False
    while site_chooser is False:
        prompt = input('What mode do you want the website to be built in? (wizard/script)  ')
        if prompt == 'wizard' or prompt == 'script':
            site_chooser = True
    return prompt


def color_get(title, prompt, color_preset):
    """
    Chooses a color for the specific thing
    :param title: the prompt thing
    :param prompt: title but with lowercase letters
    :param color_preset: list of colors
    :return:
    """
    correct = False
    output = ''
    while correct is False:
        print(title)
        bg_color = input('What do you want the ' + prompt + ' to be? (color/format"#XXXXXX) ')
        output = ''
        for ch in bg_color:
            if ch is '#':
                output = bg_color
                break
            elif ord(ch) < 96:
                to_num = ord(ch) + (97 - 65)
                output += chr(to_num)
            else:
                output += ch
        for i in color_preset:
            if i == output:
                return output
            else:
                pass
    print(output)
    return output


def font_name():
    """
    Chooses a font and returns it
    :return:
    """
    print('Choose a font')
    font = input('Do you want to see the fonts? [yes]')
    fonts = ['Arial', 'Comic Sans MS', 'Lucida Grande', 'Tahoma', 'Verdana', 'Helvetica', 'Times New Roman']
    if font is 'yes' or font is '':
        turtle.setup(400, 400)
        turtle.up()
        turtle.hideturtle()
        position = 100
        for i in fonts:
            turtle.goto(-100, position)
            turtle.write(i, True, align="left", font=(i, 14, "normal"))
            position -= 20
        input('Displaying fonts. Press enter to close.')
    print('Choose a font by the number')
    numb = 0
    for i in fonts:
        print(str(numb) + ":", i + ", size 14")
        numb += 1
    value = int(input('>>'))
    wrong_input = True
    while wrong_input is True:
        if 0 <= value < 7:
            break
        else:
            value = int(input('>>'))
    return fonts[value]


def main():
    """

    :return:
    """
    color_list = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
                  'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen',
                  'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat',
                  'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ', 'antiquewhite',
                  'royalblue', 'yellow', 'indigo ', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray',
                  'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise',
                  'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise',
                  'coral', 'forestgreen', 'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum',
                  'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon',
                  'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray',
                  'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown',
                  'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod',
                  'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine',
                  'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple',
                  'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon',
                  'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue',
                  'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown',
                  'thistle', 'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow',
                  'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod',
                  'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}

    mode = main_mode()
    bg = color_get('Background color', 'background color', color_list)
    font_type = font_name()
    font_color = color_get('Font color', 'font color', color_list)
    header_color = color_get('Header color', 'header color', color_list)

    # debug parameters
    # mode = 'script'
    # bg = 'blue'
    # font_type = 'Arial'
    # font_color = 'gray'
    # header_color = 'black'

    if mode == "wizard":
        wizard.wizard_main(bg, font_color, header_color, font_type)
    else:
        script.script_main(bg, font_color, header_color, font_type)


if __name__ == "__main__":
    main()
