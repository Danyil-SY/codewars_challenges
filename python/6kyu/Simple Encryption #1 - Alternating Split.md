# Simple Encryption #1 - Alternating Split

---

Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

```
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
```
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.

---

### Solution

```py
def decrypt(encrypted_text, n):
    if n <= 0 or not encrypted_text:
        return encrypted_text
    
    ans = list(encrypted_text)
    length = len(ans)
    
    for _ in range(n):
        j = 0
        for i in range(1, length, 2):
            ans[i] = encrypted_text[j]
            j += 1
        
        for i in range(0, length, 2):
            ans[i] = encrypted_text[j]
            j += 1

        encrypted_text = ''.join(ans)
            
    return ''.join(ans) 

def encrypt(text, n):
    if n <= 0 or not text:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[0::2]
    
    return text

```
