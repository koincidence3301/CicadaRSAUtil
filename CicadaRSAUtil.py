'''
P.S Number = 10412790658919985359827898739594318956404425106955675643739226952372682423852959081739834390370374475764863415203423499357108713631, which can be considered N as it factorises into two primes
'''

import math, argparse, base64, pathlib

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
        exit()

def ImportKeys():
    with open("pspublic.pem", "r") as f:
        lines = f.readlines()
        lines2 = lines[2:-1]
        
        base64str = ""
        for l in lines2:
            base64str += l.replace("\n", "")
        
        public_key = base64.b64decode(bytes(base64str, "utf-8"))    
    f.close()
    
    with open("psprivate.pem", "r") as f:
        lines = f.readlines()
        lines2 = lines[2:-1]
        
        base64str = ""
        for l in lines2:
            base64str += l.replace("\n", "")
        
        private_key = base64.b64decode(bytes(base64str, "utf-8"))
    f.close()

    return public_key, private_key


RunesToIndex = {      
    "ᚠ":    0,
    "ᚢ":    1,
    "ᚦ":    2,
    "ᚩ":    3,
    "ᚱ":    4,
    "ᚳ":    5,
    "ᚷ":    6,
    "ᚹ":    7,
    "ᚻ":    8,
    "ᚾ":    9,
    "ᛁ":    10,
    "ᛄ":    11,
    "ᛇ":    12,
    "ᛈ":    13,
    "ᛉ":    14,
    "ᛋ":    15,
    "ᛏ":    16,
    "ᛒ":    17,
    "ᛖ":    18,
    "ᛗ":    19,
    "ᛚ":    20,
    "ᛝ":    21,
    "ᛟ":    22,
    "ᛞ":    23,
    "ᚪ":    24,
    "ᚫ":    25,
    "ᚣ":    26,
    "ᛡ":    27,
    "ᛠ":    28
}

RunesToGP = {      
    "ᚠ":    2,
    "ᚢ":    3,
    "ᚦ":    5,
    "ᚩ":    7,
    "ᚱ":    11,
    "ᚳ":    13,
    "ᚷ":    17,
    "ᚹ":    19,
    "ᚻ":    23,
    "ᚾ":    29,
    "ᛁ":    31,
    "ᛄ":    37,
    "ᛇ":    41,
    "ᛈ":    43,
    "ᛉ":    47,
    "ᛋ":    53,
    "ᛏ":    59,
    "ᛒ":    61,
    "ᛖ":    67,
    "ᛗ":    71,
    "ᛚ":    73,
    "ᛝ":    79,
    "ᛟ":    83,
    "ᛞ":    89,
    "ᚪ":    97,
    "ᚫ":    101,
    "ᚣ":    103,
    "ᛡ":    107,
    "ᛠ":    109
}

RuneToText = {
    "ᚠ":    "F",
    "ᚢ":    "U",
    "ᚦ":    "TH",
    "ᚩ":    "O",
    "ᚱ":    "R",
    "ᚳ":    "C",
    "ᚷ":    "G",
    "ᚹ":    "W",
    "ᚻ":    "H",
    "ᚾ":    "N",
    "ᛁ":    "I",
    "ᛄ":    "J",
    "ᛇ":    "EO",
    "ᛈ":    "P",
    "ᛉ":    "X",
    "ᛋ":    "S",
    "ᛏ":    "T",
    "ᛒ":    "B",
    "ᛖ":    "E",
    "ᛗ":    "M",
    "ᛚ":    "L",
    "ᛝ":    "ING",
    "ᛟ":    "OE",
    "ᛞ":    "D",
    "ᚪ":    "A",
    "ᚫ":    "AE",
    "ᚣ":    "Y",
    "ᛡ":    "IA",
    "ᛠ":    "EA"
}

# Reversing RunesToTabulaIndex
IndexToRunes = {v: k for k, v in RunesToIndex.items()}

# Reversing RunesToGP
GPToRunes = {v: k for k, v in RunesToGP.items()}

TextToRune = {v: k for k, v in RuneToText.items()}

gematriaprimus = (
    (" ", " ", 0),
    (u"ᚠ", "f", 2),
    (u"ᚢ", "v", 3),
    (u"ᚢ", "u", 3),
    (u"ᚦ", "T", 5),  # th
    (u"ᚩ", "o", 7),
    (u"ᚱ", "r", 11),
    (u"ᚳ", "k", 13),
    (u"ᚳ", "c", 13),
    (u"ᚷ", "g", 17),
    (u"ᚹ", "w", 19),
    (u"ᚻ", "h", 23),
    (u"ᚾ", "n", 29),
    (u"ᛁ", "i", 31),
    (u"ᛄ", "j", 37),
    (u"ᛇ", "E", 41),  # eo
    (u"ᛈ", "p", 43),
    (u"ᛉ", "x", 47),
    (u"ᛋ", "z", 53),
    (u"ᛋ", "s", 53),
    (u"ᛏ", "t", 59),
    (u"ᛒ", "b", 61),
    (u"ᛖ", "e", 67),
    (u"ᛗ", "m", 71),
    (u"ᛚ", "l", 73),
    (u"ᛝ", "G", 79),  # ing
    (u"ᛝ", "G", 79),  # ng
    (u"ᛟ", "O", 83),  # oe
    (u"ᛞ", "d", 89),
    (u"ᚪ", "a", 97),
    (u"ᚫ", "A", 101),  # ae
    (u"ᚣ", "y", 103),
    (u"ᛡ", "I", 107),  # ia
    (u"ᛡ", "I", 107),  # io
    (u"ᛠ", "X", 109),  # ea
)

latsimple = (
    ("T", "th"),
    ("E", "eo"),
    ("G", "ing"),
    ("G", "ng"),
    ("O", "oe"),
    ("A", "ae"),
    ("I", "io"),
    ("I", "ia"),
    ("X", "ea"),
)

def gem_map(x, src, dest):
    m = {p[src]: p[dest] for p in gematriaprimus}
    return [m[c] if c in m else c for c in x]

def lat_to_sim(x):
    x = x.replace("q", "cw")
    for sim in latsimple:
        x = x.replace(sim[1], sim[0])
    return x

def lat_to_run(x):
    x = x.lower().replace("qu", "q")
    return "".join(gem_map(lat_to_sim(x), 1, 0))

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

        public_key = f"{e}:{n}"
        private_key = f"{d}:{n}"

        print("Public key:  " + str(public_key))
        print("Private key:  " + str(private_key))

        ExportKeypair(public_key, private_key)

    def encryptps(self):
        pubfile = pathlib.Path("./pspublic.pem")
        privfile = pathlib.Path("./psprivate.pem")

        if not pubfile.is_file():
            print("Keys not found, generate them")
            exit()

        if not privfile.is_file():
            print("Keys not found, generate them")
            exit()

        choice = input("(L)atin or (r)unic:\n> ")
        if choice.upper() != "L" and choice.upper() != "R":
            print("Invalid choice..")
            exit()
        ct = input("Please input cipher text:\n> ")
        if choice.upper() == "L":
            runic = lat_to_run(ct)
            base = []
            base2 = []
            for rune in runic.replace(" ", ""):
                base.append(RunesToGP[rune])
                base2.append(RunesToIndex[rune])
            
        elif choice.upper() == "R":
            base = []
            base2 = []
            for rune in ct.replace(" ", ""):
                base.append(RunesToGP[rune])
                base2.append(RunesToIndex[rune])

        public, private = ImportKeys()
        epublic = public.decode()
        eprivate = private.decode()
        
        pub = epublic.split(":")
        priv = eprivate.split(":")
        """
        public_key = f"{e}:{n}"
        private_key = f"{d}:{n}"
        formula : cyphertext = message^e mod n
        """
        nbase1 = []
        nbase2 = []

        for i in base:
            nbase1.append(((i^int(pub[0]))%int(pub[1]))%29)
        
        for i in base2:
            nbase2.append(((i^int(pub[0]))%int(pub[1]))%29)

        nbase1str = ""
        for res in nbase1:
            nbase1str += IndexToRunes[res]

        nbase2str = ""
        for res2 in nbase2:
            nbase2str += IndexToRunes[res2]

        #this is done because i am lazy, very lazy
        nbase1str2 = ""
        for char in nbase1str:
            nbase1str2 += RuneToText[char] + " "

        nbase2str2 = ""
        for char2 in nbase2str:
            nbase2str2 += RuneToText[char2] + " "

        print("GP to Index RSA encrypt:  " + nbase1str2)
        print("Index to Index RSA encrypt:  " + nbase2str2)
        
    def decryptps(self):
        pubfile = pathlib.Path("./pspublic.pem")
        privfile = pathlib.Path("./psprivate.pem")

        if not pubfile.is_file():
            print("Keys not found, generate them")
            exit()

        if not privfile.is_file():
            print("Keys not found, generate them")
            exit()

        choice = input("(L)atin or (r)unic:\n> ")
        if choice.upper() != "L" and choice.upper() != "R":
            print("Invalid choice..")
            exit()
        ct = input("Please input cipher text:\n> ")
        if choice.upper() == "L":
            runic = lat_to_run(ct)
            base = []
            base2 = []
            for rune in runic.replace(" ", ""):
                base.append(RunesToGP[rune])
                base2.append(RunesToIndex[rune])
            
        elif choice.upper() == "R":
            base = []
            base2 = []
            for rune in ct.replace(" ", ""):
                base.append(RunesToGP[rune])
                base2.append(RunesToIndex[rune])

        public, private = ImportKeys()
        epublic = public.decode()
        eprivate = private.decode()
        
        pub = epublic.split(":")
        priv = eprivate.split(":")
        """
        public_key = f"{e}:{n}"
        private_key = f"{d}:{n}"
        formula : plaintext = cyphertext^d mod n
        """
        nbase1 = []
        nbase2 = []

        for i in base:
            nbase1.append(((i^int(priv[0]))%int(priv[1]))%29)
        
        for i in base2:
            nbase2.append(((i^int(priv[0]))%int(priv[1]))%29)

        nbase1str = ""
        for res in nbase1:
            nbase1str += IndexToRunes[res]

        nbase2str = ""
        for res2 in nbase2:
            nbase2str += IndexToRunes[res2]

        #this is done because i am lazy, very lazy
        nbase1str2 = ""
        for char in nbase1str:
            nbase1str2 += RuneToText[char] + " "

        nbase2str2 = ""
        for char2 in nbase2str:
            nbase2str2 += RuneToText[char2] + " "

        print("GP to Index RSA decrypt:  " + nbase1str2)
        print("Index to Index RSA decrypt:  " + nbase2str2)

if __name__ == "__main__":
    handler = Handler()
    handler.handle()