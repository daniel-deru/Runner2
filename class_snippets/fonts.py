from matplotlib import font_manager

def get_sys_fonts():
    fonts = []
    for x in font_manager.win32InstalledFonts():
        x = x[::-1]
        dot = x.find('.')
        slash = x.find('\\')
        x = x[slash-1:dot:-1]
        fonts += [x]
    fonts.sort()
    return fonts