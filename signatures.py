from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, _serialization
def generate_keys():
    private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public = private.public_key()
    return private, public

def sign_message(private_key, message: bytes):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message: bytes, signature: bytes):
    try:
        public_key.verify(
            signature, message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

if __name__ == "__main__":
    print("===== Digital Signature Demonstration =====")

    alice_private, alice_public = generate_keys()
    bob_private, bob_public = generate_keys()

    message = b"Hello from Alice!"

    # Alice signs a message
    signature = sign_message(alice_private, message)
    print("Original Message:", message)
    print("Alice's Signature (truncated):", signature.hex()[:64], "...")

    # Bob verifies Alice's signature
    valid = verify_signature(alice_public, message, signature)
    print("Bob verifying Alice's signature →", valid)

    # Test with wrong public key (should fail)
    invalid = verify_signature(bob_public, message, signature)
    print("Bob verifying with wrong key →", invalid)
