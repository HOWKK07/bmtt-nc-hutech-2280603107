import hashlib

def calculate_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_hash = input("nhập dữ liệu: ")
sha256_hash = calculate_sha256(data_hash)

print("giá trị hash sha-256:", sha256_hash)
