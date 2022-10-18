import itertools, time, string, random

nap = lambda x: time.sleep(x)

s_baseCharset = string.ascii_letters+string.digits+"`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"

def BruteForcer(password: str, charset: str):
    f_start = time.time()
    i_attempts = 0
    for i in range(1, 27):
        for letter in itertools.product(charset, repeat=i):
            attempts += 1
            guess = ''.join(letter)
            print(guess)
            if guess == password:
                f_end = time.time()
                f_timeDif = f_end - f_start
                return (i_attempts, f_timeDif)

def GenTestPass(length: int):
    return ''.join(random.choice(s_baseCharset) for _ in range(length))

def main():
    global s_password
    choice = input("Generate Or Enter Password (g/e) >\n- % ")
    if choice in ("g","e"):
        if choice == 'g':
            passwordLength = int(input("Enter Password Length >\n- % "))
            s_password = GenTestPass(passwordLength)
            print("Generated Password Is : %s. Starting..." % s_password)
            nap(3)
        elif choice == 'e':
            s_password = str(input("Enter Password To Attempt >\n- % "))
            print("Your Password Is : %s. Starting..." % s_password)
            nap(3)
    else:
        print("Invalid Choice... Try Again")
        main()
    tries, timeAmount = BruteForcer(s_password, s_baseCharset)
    print("Cracked Password %s in %s tries and %s seconds!" % (s_password, tries, timeAmount))

if __name__ == "__main__":
    main()