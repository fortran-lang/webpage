from pathlib2 import Path

a =""
a = a.split()
def replacetext(search_text, replace_text,file_name):
  
    # Opening the file using the Path function
    file = Path(file_name)
  
    # Reading and storing the content of the file in
    # a data variable
    data = file.read_text()
  
    # Replacing the text using the replace function
    data = data.replace(search_text, replace_text)
  
    # Writing the replaced data
    # in the text file
    file.write_text(data)
  
    # Return "Text replaced" string
    return "Text replaced"

for i in a:
    replacetext("```{play-code-block} fortran","```{play-code-block} fortran",i)