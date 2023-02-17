import ctypes  # An included library with Python install.


def MBox(buttonStyles: int, title: str, text: str, style: int):
    return ctypes.windll.user32.MessageBoxW(buttonStyles, text, title, style)

# Button styles:
# 0 : OK
# 1 : OK | Cancel
# 2 : Abort | Retry | Ignore
# 3 : Yes | No | Cancel
# 4 : Yes | No
# 5 : Retry | No
# 6 : Cancel | Try Again | Continue

# To also change icon, add these values to previous number
# 16 Stop-sign icon
# 32 Question-mark icon
# 48 Exclamation-point icon
# 64 Information-sign icon consisting of an 'i' in a circle
