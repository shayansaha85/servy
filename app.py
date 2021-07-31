import os

all_files = os.listdir("./")

def isHtml(name_of_file):
    extension = name_of_file.split(".")[-1]
    if extension.lower() == 'html' or extension.lower() == 'htm':
        return True
    else:
        return False
def only_html(list_of_files):
    html_files = []
    for file in list_of_files:
        if isHtml(file):
            html_files.append(file)
    return html_files


port = 3049

html_files = only_html(all_files)
print("Choose your file : ")
print("====================")
t = 1
for file in html_files:
    print(f"{t}. {file}")
    t=t+1

user_choice = int(input("> "))

index_of_file = user_choice - 1
index_html = html_files[index_of_file]

command = f"python -m http.server {port}"

os.system(f"start chrome http://localhost:{port}/{index_html}")
os.system(command)