message = input("> ")
message = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "🙁"
}
output = ''
for str in message:
    output += emojis.get(str, str) + ' '
print(output)