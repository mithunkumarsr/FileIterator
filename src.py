import webbrowser

append = ""
with open('C:\\Users\\rmithun\\Desktop\\Hori.txt') as input_file:
    for i, line in enumerate(input_file):
        webbrowser.open(line+append)
