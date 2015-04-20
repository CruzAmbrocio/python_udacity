import urllib
def read_text():
    quotes = open("C:\Users\CRUZ AMBROCIO\Desktop\python_Udacity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profany(contents_of_file)
def check_profany(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true"in output:
        print ("hahahahaahahaha")
    elif "false" in output:
        print("no hay  error")
    else:
        print("hola que hace")

read_text()