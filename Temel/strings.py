# substring
message = "Hello World"
print(message[2:7])
newMessage = message[10:11]
print(newMessage)

# len
print(len(message))
newMessage2 = message[len(message)-1:len(message)]
print(newMessage2)

# lower upper
print(message.upper())
print(message.lower())

# replace
print(message.replace("o", "ö"))

# split strip
info = "Murat Aşık 20 Ankara".strip()
print(info.split())

# input
name = input("What's your name?")
number1 = input("number 1 = ?")
number2 = input("number 2 = ?")
print(int(number1) + int(number2))
