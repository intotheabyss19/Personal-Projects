# Disclaimer: This code was made for personal use and the owner of this code i.e. intotheabyss19 will not be responsible for any harm caused by usage of this code

import hashlib, hmac
from getpass import getpass

try:
    from argon2.low_level import hash_secret_raw, Type as Argon2Type
except ImportError:
    hash_secret_raw = None

CHARSETS = {
    "a-z": "abcdefghijklmnopqrstuvwxyz",
    "A-Z": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "0-9": "0123456789",
    "special": "@#%&*!?-=+<>$"
}

BIAS_PROFILES = {
    "1": "a-z>0-9>A-Z>special",
    "2": "a-z>A-Z>0-9>special",
    "3": "A-Z>a-z>0-9>special",
    "4": "a-z>special>A-Z>0-9",
}

def hash_data(method, root, context):
    combined = (root + ":" + context).encode()
    root_b = root.encode()

    match method:
        case "sha256":
            return hashlib.sha256(combined).digest()
        case "sha512":
            return hashlib.sha512(combined).digest()
        case "blake2b":
            return hashlib.blake2b(combined).digest()
        case "sha3_256":
            return hashlib.sha3_256(combined).digest()
        case "sha3_512":
            return hashlib.sha3_512(combined).digest()
        case "shift_add_3":
            return shift_ascii_algorithm(root, context, 3)
        case "shift_sub_2":
            return shift_ascii_algorithm(root, context, -2)
        case "xor_with_5":
            return xor_ascii_algorithm(root, context, 5)
        case "rot13":
            return rot13_ascii_algorithm(root, context)
        case "multiply_mod_256_7":
            return multiply_mod_ascii_algorithm(root, context, 7)

        case "bcrypt (pbkdf2)":
            return hashlib.pbkdf2_hmac("sha256", root_b, context.encode(), 100_000)
        case "hmac_sha256":
            return hmac.new(root_b, context.encode(), hashlib.sha256).digest()
        case "hmac_sha512":
            return hmac.new(root_b, context.encode(), hashlib.sha512).digest()
        case "argon2" if hash_secret_raw:
            return hash_secret_raw(root_b, context.encode(), time_cost=2, memory_cost=512,
                                   parallelism=2, hash_len=32, type=Argon2Type.I)
        case "scrypt":
            return hashlib.scrypt(root_b, salt=context.encode(), n=16384, r=8, p=1, dklen=32)
        case _:
            raise ValueError("Unsupported or unavailable method")

def shift_ascii_algorithm(root, context, shift_val):
    data = (root + context).encode()
    shifted = bytes((b + shift_val) % 256 for b in data)
    return shifted[:32].ljust(32, b'\0')

def xor_ascii_algorithm(root, context, xor_val):
    data = (root + context).encode()
    xored = bytes(b ^ xor_val for b in data)
    return xored[:32].ljust(32, b'\0')

def rot13_ascii_algorithm(root, context):
    data = (root + context).encode()
    def rot13_char(c):
        if 65 <= c <= 90:
            return (c - 65 + 13) % 26 + 65
        elif 97 <= c <= 122:
            return (c - 97 + 13) % 26 + 97
        else:
            return c
    rot13ed = bytes(rot13_char(b) for b in data)
    return rot13ed[:32].ljust(32, b'\0')

def multiply_mod_ascii_algorithm(root, context, mul_val):
    data = (root + context).encode()
    multiplied = bytes((b * mul_val) % 256 for b in data)
    return multiplied[:32].ljust(32, b'\0')

ALGORITHMS = [
    "shift_add_3", "shift_sub_2", "xor_with_5", "rot13", "multiply_mod_256_7", "argon2", "bcrypt (pbkdf2)", "scrypt", "sha256", "sha512",
]

def generate_password(root, context, method, length, bias_order):
    digest = hash_data(method, root, context)
    sets = [x.strip() for x in bias_order.split(">")]
    proportions = {
        0: (length * 0.5, 0.7),
        1: (1, 4),
        2: (1, 3),
        3: (1, 2)
    }
    index = 0
    password_chars = []
    remaining = length
    for i, cat in enumerate(sets):
        if cat not in CHARSETS:
            continue
        charset = CHARSETS[cat]
        if i in proportions:
            low, high = proportions[i]
            count = int(low + (digest[index] % (int(high)-int(low)+1)))
        else:
            count = remaining
        count = min(count, remaining)
        remaining -= count
        for j in range(count):
            char = charset[digest[index+j] % len(charset)]
            password_chars.append(char)
        index += count
    if remaining > 0:
        charset = CHARSETS[sets[0]]
        for i in range(remaining):
            password_chars.append(charset[digest[index+i] % len(charset)])
    return "".join(password_chars[:length])

if __name__ == "__main__":
    print("~~~ Deterministic Password Generator with custom algorithms ~~~")
    root_password = getpass("Enter root password (hidden): ")
    context = input("Enter site/context string: ")
    pepper = getpass("Enter optional pepper (press Enter to skip): ")
    if pepper:
        context = context + "|" + pepper
    print("Available algorithms:")
    for i, alg in enumerate(ALGORITHMS, 1):
        print(f"{i}. {alg}")
    choice = int(input("Choose algorithm: "))
    method = ALGORITHMS[choice - 1]

    length = int(input("Enter password length (8-12): "))
    print("Available bias profiles:")
    for k, v in BIAS_PROFILES.items():
        print(f"{k}: {v}")
    bias_choice = input("Choose bias profile (default is 1): ").strip()
    if bias_choice == "":
        bias_choice = "1"
    bias_order = BIAS_PROFILES.get(bias_choice, BIAS_PROFILES["1"])

    password = generate_password(root_password, context, method, length, bias_order)
    print("\nOriginal Generated Password:", password)

    yn = input("Make password more typable and readable? (y/n): ").lower()
    if yn == 'y':
        from string import ascii_lowercase, ascii_uppercase, digits
        lowers = sorted([c for c in password if c in ascii_lowercase])
        uppers = sorted([c for c in password if c in ascii_uppercase])
        nums = sorted([c for c in password if c in digits])
        specials = [c for c in password if c not in lowers + uppers + nums]
        password = "".join(lowers + nums + uppers + specials)
        print("Reordered for readability:", password)

        QWERTY_LAYOUT = {
            **{ch: (0, idx) for idx, ch in enumerate("qwertyuiop")},
            **{ch: (1, idx) for idx, ch in enumerate("asdfghjkl")},
            **{ch: (2, idx) for idx, ch in enumerate("zxcvbnm")},
        }

        def expand_layout(layout):
            new_layout = {}
            for k, v in layout.items():
                new_layout[k] = v
                new_layout[k.upper()] = v
            return new_layout

        QWERTY_LAYOUT = expand_layout(QWERTY_LAYOUT)

        def key_distance(a, b, layout):
            if a not in layout or b not in layout:
                return 3.0
            r1, c1 = layout[a]
            r2, c2 = layout[b]
            return abs(r1 - r2) + abs(c1 - c2)

        def total_typing_distance(password, layout):
            dist = 0.0
            for i in range(len(password) - 1):
                dist += key_distance(password[i], password[i+1], layout)
            return dist

        def optimize_password_typing(password, layout, max_iters=1000):
            arr = list(password)
            n = len(arr)
            current_dist = total_typing_distance(arr, layout)
            improved = True
            iteration = 0
            while improved and iteration < max_iters:
                improved = False
                iteration += 1
                for i in range(n):
                    for j in range(i+1, n):
                        arr[i], arr[j] = arr[j], arr[i]
                        new_dist = total_typing_distance(arr, layout)
                        if new_dist < current_dist:
                            current_dist = new_dist
                            improved = True
                        else:
                            arr[i], arr[j] = arr[j], arr[i]
                if not improved:
                    break
            return "".join(arr)

        password = optimize_password_typing(password, QWERTY_LAYOUT)
        print("Optimized Password:", password)
    else:
        print("Final Password:", password)
