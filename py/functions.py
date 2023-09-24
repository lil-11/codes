#using functions
def greetings(name):
    print(f"Hello {name}!")
    print("Welcome") #for best practice, skip two lines after the function
    
    
print("Start")
greetings("John")
greetings("Mary")

'''
message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
'''