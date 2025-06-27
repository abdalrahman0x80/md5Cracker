import hashlib
import argparse

class Argument:
    def __init__(self):
        argument = argparse.ArgumentParser(description="Fast MD5 hash cracker")
        argument.add_argument("--wordlist", "-w", required=True, help="Custom wordlist like (wordlist.txt)")
        argument.add_argument("--hash", "-H", required=True, help="Target MD5 hash to crack")
        self.parser = argument.parse_args()

    def Parser(self):
        return self.parser


class HashCrack:
    def crack(self, wordlist, target_hash):
        try:
            with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
                for keyword in file:
                    keyword = keyword.strip()  # remove newlines
                    encrypt = hashlib.md5(keyword.encode()).hexdigest()
                    if encrypt == target_hash.lower():
                        print(f"[+] Hash cracked: {encrypt}")
                        print(f"[+] Plaintext: {keyword}")
                        return
                print("[-] Hash not found in the wordlist.")
        except FileNotFoundError:
            print(f"[-] File not found: {wordlist}")

# Main logic
if __name__ == "__main__":
    argumentParser = Argument().Parser()
    hash_crack = HashCrack()
    hash_crack.crack(argumentParser.wordlist, argumentParser.hash)
