import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()
def main():
    text = input("nhập chuỗi văn bản: ").encode('utf-8')
    hash_text = blake2(text)

    print("chuỗi văn bản đã nhập: ", text.decode('utf-8'))
    print("Blake2 Hash:", hash_text.hex())

if __name__=="__main__":
    main()
