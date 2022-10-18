import itertools, time, sys

class BruteUtil:
    start = time.time()
    end = time.time()
    cracked = False

    def __init__(self, password: str, charset: str, verbose: bool):
        # Validate Password
        if not isinstance(password, str):
            raise TypeError("Password Must Be A String.")

        self.password = password

        # Validate Charset
        if not isinstance(charset, str):
            raise TypeError("Charset Must Be A String.")

        self.charset = charset

        # Validate Verbose
        if not isinstance(verbose, bool):
            raise TypeError("Verbose Must Be A Boolean.")

        self.verbose = verbose

    def Attempt(self):
        self.start = time.time()
        attempts = 0
        for i in range(1, 27):
            for letter in itertools.product(self.charset, repeat=i):
                attempts += 1
                guess = ''.join(letter)
                if self.verbose:
                    print(guess)
                if guess == self.password:
                    self.end = time.time()
                    timeDif = self.end - self.start
                    print("Cracked Password %s in %s tries and %s seconds!" % (self.password, attempts, timeDif))
                    self.cracked = True
                    self._exit()

    def _exit(self):
        sys.exit()