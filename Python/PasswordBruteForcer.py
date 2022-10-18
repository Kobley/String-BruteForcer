import itertools, time, string, random
from BruteForcer.brute import BruteUtil

nap = lambda x: time.sleep(x)

s_baseCharset = string.ascii_letters+string.digits+"`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"

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
    
    BruteUtil(password=s_password, charset=s_baseCharset, verbose=True).Attempt()

if __name__ == "__main__":
    main()