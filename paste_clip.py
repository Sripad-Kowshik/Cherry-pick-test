import pyperclip

try:
    pyperclip.copy("Hello from the other side!")
    print("Text copied to clipboard.")
except pyperclip.PyperclipException as e:
    print(e)
