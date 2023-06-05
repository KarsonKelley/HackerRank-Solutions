message = input("> ")
message = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "🙁"
}
output = ''
for str in message:
    if str == ":)" or str == ":(":
        output += emojis[str] + ' '
    else:
        output += str + ' '
print(output)