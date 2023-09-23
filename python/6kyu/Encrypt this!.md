# Encrypt this!

### Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

1. Your message is a string containing space separated words.
2. You need to encrypt each word in the message using the following rules:
   * The first letter must be converted to its ASCII code.
   * The second letter must be switched with the last letter
3. Keepin' it simple: There are no special characters in the input.

### Examples:
```
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```

---

```py
def encrypt_this(text):
    splitted =  text.split(' ')
    encrypted = []
    for x in splitted:
        if len(x) == 1:
            encrypted.append(f'{ord(x[0])}')
        elif len(x) == 2:
            encrypted.append(f'{ord(x[0])}{x[1]}')
        elif len(x) == 3:
            encrypted.append(f'{ord(x[0])}{x[-1]}{x[1]}')
        elif len(x) >= 4:
            encrypted.append(f'{ord(x[0])}{x[-1]}{x[2:-1]}{x[1]}')
    return ' '.join(encrypted)
        
```
