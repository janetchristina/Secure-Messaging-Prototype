import hashlib

def derive_key(shared_secret: int, iterations: int = 10000):
    key = str(shared_secret).encode()
    for _ in range(iterations):
        key = hashlib.sha256(key).digest()
    return key

if __name__ == "__main__":
    print("===== Task 3: Key Derivation Function (KDF) =====")
    
    shared_secret = 2
    iterations = 10000
    
    # Derive key
    derived_key = derive_key(shared_secret, iterations)
    
    # Show results
    print("Shared Secret:", shared_secret)
    print("Iterations:", iterations)
    print("Derived Key (hex):", derived_key.hex())
