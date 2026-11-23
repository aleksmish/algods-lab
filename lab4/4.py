def is_palindrome(s: str) -> bool:
    s = "".join(char.lower() for char in s if char.isalnum())
    def check(sub: str) -> bool:
        if len(sub) <= 1:
            return True
        if sub[0] != sub[-1]:
            return False
        return check(sub[1:-1])

    return check(s)

s = input("Введите строку ")
print(is_palindrome(s))
