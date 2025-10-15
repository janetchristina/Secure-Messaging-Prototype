from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
import secrets

def sym_enc(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    pad_len = 16 - len(plaintext) % 16
    plaintext += bytes([pad_len]) * pad_len
    return encryptor.update(plaintext) + encryptor.finalize()

def sym_dec(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    pad_len = plaintext[-1]
    return plaintext[:-pad_len]

# --- HMAC and Authenticated Encryption ---
def compute_hmac(key, data):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(data)
    return h.finalize()

def authenticated_encrypt(key, plaintext):
    iv = secrets.token_bytes(16)
    ciphertext = sym_enc(key, iv, plaintext)
    mac = compute_hmac(key, ciphertext)
    return iv, ciphertext, mac

def authenticated_decrypt(key, iv, ciphertext, mac):
    expected_mac = compute_hmac(key, ciphertext)
    if mac != expected_mac:
        raise ValueError("❌ HMAC verification failed — message tampered!")
    return sym_dec(key, iv, ciphertext)

if __name__ == "__main__":
    print("===== Task 5: Secure Message Exchange (Encrypt-then-MAC) =====")
    # Sample 32-byte AES key (from KDF)
    key = secrets.token_bytes(32)
    message = b"Hello Alice! Secure message test."

    iv, ciphertext, mac = authenticated_encrypt(key, message)

    print("Plaintext:", message)
    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())
    print("HMAC:", mac.hex())

    try:
        decrypted = authenticated_decrypt(key, iv, ciphertext, mac)
        print("✅ Decrypted message:", decrypted)
    except ValueError as e:
        print(e)
