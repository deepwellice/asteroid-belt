"""
Both methods below cannot work on Windows. Not sure Mac.
"""

import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        print('No color.')
        return False

has_colours = has_colours(sys.stdout)

def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

printout("[debug]   ", GREEN)
print("in green")
printout("[warning] ", YELLOW)
print("in yellow")
printout("[error]   ", RED)
print("in red")

colours = {
'none' : "",
'default' : "\033[.0m",
'bold' : "\033[.1m",
'underline' : "\033[.4m",
'blink' : "\033[.5m",
'reverse' : "\033[.7m",
'concealed' : "\033[.8m",

'black' : "\033[.30m",
'red' : "\033[.31m",
'green' : "\033[.32m",
'yellow' : "\033[.33m",
'blue' : "\033[.34m",
'magenta' : "\033[.35m",
'cyan' : "\033[.36m",
'white' : "\033[.37m",

'on_black' : "\033[.40m",
'on_red' : "\033[.41m",
'on_green' : "\033[.42m",
'on_yellow' : "\033[.43m",
'on_blue' : "\033[.44m",
'on_magenta' : "\033[.45m",
'on_cyan' : "\033[46m",
'on_white' : "\033[47m",

'beep' : "\007",

# non-standard attributes, supported by some terminals
'dark' : "\033[.2m",
'italic' : "\033[3m",
'rapidblink' : "\033[6m",
'strikethrough': "\033[9m",
}

print colours['red'], 'this is red', colours['blue'], 'blue', colours['on_green'], 'and with a green background', colours['default'] 
