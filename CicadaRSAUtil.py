'''
P.S Number = 10412790658919985359827898739594318956404425106955675643739226952372682423852959081739834390370374475764863415203423499357108713631, which can be considered N as it factorises into two primes
'''

import math, argparse, base64

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ExportKeypair(public_key, private_key):
        '''
        VERY SIMPLE way of storing keys, please never do this in other circumstances.  I am too lazy to do this differently
        '''
        private_key_start = "-----BEGIN RSA PRIVATE KEY-----"
        private_key_end = "-----END RSA PRIVATE KEY-----"
        private_key_b64 = base64.b64encode(bytes(str(private_key), "utf-8"))
        private_key_file = ""
        private_key_file += private_key_start + "\n\n"
        count = 0
        for char in private_key_b64.decode():
            private_key_file += char
            count += 1
            if count == 64:
                private_key_file += "\n"
                count = 0
            
        private_key_file += "\n" + private_key_end

        public_key_start = "-----BEGIN RSA PUBLIC KEY-----"
        public_key_end = "-----END RSA PUBLIC KEY-----"
        public_key_b64 = base64.b64encode(bytes(str(public_key), "utf-8"))
        public_key_file = ""
        public_key_file += public_key_start + "\n\n"
        count = 0
        for char in public_key_b64.decode():
            public_key_file += char
            count += 1
            if count == 64:
                public_key_file += "\n"
                count = 0
        public_key_file += "\n" + public_key_end

        with open("psprivate.pem", "w+") as f:
            f.write(private_key_file)
        f.close()

        with open("pspublic.pem", "w+") as f:
            f.write(public_key_file)
        f.close()

        print("Generation and exporting to pem-like key done")

class Handler:
    def handle(self):
        """Interpret the first command line argument, and redirect."""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "action",
            choices=["generateps", "encryptps", "decryptps", "pgpverify", "pgpdecrypt"],
            help="cicada rsa util",
        ) # MORE UTIL SUCH AS PS MESSAGE ENCRYPT/DECRYPT AND PGP WILL BE ADDED LATER
        parser.add_argument("other", nargs="*")
        args = parser.parse_args()

        action = getattr(self, args.action)
        action()

    def generateps(self):
        '''
        Simple RSA keypair generation based on the PS message
        '''
        p = 99554414790940424414351515490472769096534141749790794321708050837
        q = 104593961812606247801193807142122161186583731774511103180935025763

        n = p*q

        phi = (p-1)*(q-1)

        e = 65537

        g = gcd(e, phi)

        if g == 1:
            print("Coprime!")
        else:
            print("Not coprime")
            exit()

        d = pow(e, -1, phi)

        public_key = (e, n)
        private_key = (d, n)

        print("Public key:  " + str(public_key))
        print("Private key:  " + str(public_key))

        ExportKeypair(public_key, private_key)

if __name__ == "__main__":
    handler = Handler()
    handler.handle()