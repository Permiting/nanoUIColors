#!/usr/bin/env python3
import os

def create_custom_syntax_files(nano_dir):
    # Python syntax
    with open(os.path.join(nano_dir, "python.nanorc"), "w") as f:
        f.write("""## Python syntax highlighting
syntax "python" "\\.py$" "^#!.*python"
# Keywords
color brightcyan "\\<(and|as|assert|break|class|continue|def|del|elif|else|except|exec|finally|for|from|global|if|import|in|is|lambda|not|or|pass|print|raise|return|try|while|with|yield)\\>"
# Built-in functions
color brightblue "\\<(abs|all|any|bool|chr|dict|dir|enumerate|eval|exit|float|hex|int|len|list|map|max|min|open|ord|pow|print|range|raw_input|reduce|reload|repr|round|set|slice|sorted|str|sum|tuple|type|vars|zip)\\>"
# Strings
color brightgreen ""[^"]*"|'[^']*'"
# Comments
color brightred "#.*$"
# Numbers
color magenta "\\<[0-9]+\\>"
# Special variables
color brightyellow "\\<(self|None|True|False)\\>"
""")

    # JavaScript syntax
    with open(os.path.join(nano_dir, "javascript.nanorc"), "w") as f:
        f.write("""## JavaScript syntax highlighting
syntax "javascript" "\\.js$"
# Keywords
color brightcyan "\\<(async|await|break|case|catch|class|const|continue|debugger|default|delete|do|else|export|extends|finally|for|function|if|import|in|instanceof|let|new|of|return|super|switch|this|throw|try|typeof|var|void|while|with|yield)\\>"
# Built-in objects
color brightyellow "\\<(Array|Boolean|Date|Error|Function|JSON|Math|Number|Object|RegExp|String|Promise)\\>"
# Strings
color brightgreen ""[^"]*"|'[^']*'"
# Comments
color brightred "//.*$"
color brightred start="/\\*" end="\\*/"
# Numbers
color magenta "\\<[0-9]+\\>"
# Special values
color brightyellow "\\<(true|false|null|undefined)\\>"
""")

    # HTML syntax
    with open(os.path.join(nano_dir, "html.nanorc"), "w") as f:
        f.write("""## HTML syntax highlighting
syntax "html" "\\.html$" "\\.htm$"
# Tags
color brightmagenta "<[^>]*>"
# Attributes
color brightcyan " [a-z-]+="
# Strings
color brightgreen ""[^"]*""
# Comments
color brightred start="<!--" end="-->"
# DOCTYPE
color brightyellow "<!DOCTYPE.*>"
""")

    # CSS syntax
    with open(os.path.join(nano_dir, "css.nanorc"), "w") as f:
        f.write("""## CSS syntax highlighting
syntax "css" "\\.css$"
# Selectors
color brightmagenta "[A-Za-z0-9#.:*_-]+[ ]*\\{"
# Properties
color brightcyan "[A-Za-z-]+[ ]*:"
# Values
color brightgreen ": *[^;]*;"
# Units
color magenta "\\<(px|em|rem|%|pt|vh|vw)\\>"
# Colors
color brightyellow "#[A-Fa-f0-9]{6}"
# Comments
color brightred start="/\\*" end="\\*/"
""")

def setup_nano_highlighting():
    # Create necessary directories
    home_dir = os.path.expanduser("~")
    nano_dir = os.path.join(home_dir, ".nano")
    
    if not os.path.exists(nano_dir):
        os.makedirs(nano_dir)
    
    # Create custom syntax files
    create_custom_syntax_files(nano_dir)
    
    # Create .nanorc file
    nanorc_path = os.path.join(home_dir, ".nanorc")
    
    with open(nanorc_path, "w") as nanorc:
        # Basic configuration
        nanorc.write("""
# General settings
set const
set autoindent
set tabsize 4
set tabstospaces
set linenumbers
set mouse
set softwrap

# Include custom syntax files
include "~/.nano/python.nanorc"
include "~/.nano/javascript.nanorc"
include "~/.nano/html.nanorc"
include "~/.nano/css.nanorc"
""")

def verify_installation():
    print("Verifying nano syntax highlighting installation...")
    
    if os.path.exists(os.path.expanduser("~/.nanorc")):
        print("✓ Enhanced syntax highlighting configuration created successfully")
        print("✓ Custom highlighting rules implemented for:")
        print("  - Python (*.py)")
        print("  - JavaScript (*.js)")
        print("  - HTML (*.html, *.htm)")
        print("  - CSS (*.css)")
        print("\nFeatures enabled:")
        print("  - Line numbers")
        print("  - Auto-indentation")
        print("  - Mouse support")
        print("  - Soft wrapping")
        print("  - 4-space tabs")
        print("\nTo use: Simply open files with nano, example:")
        print("  nano example.py")
    else:
        print("× Installation failed. Please check permissions and try again.")

if __name__ == "__main__":
    try:
        setup_nano_highlighting()
        verify_installation()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
