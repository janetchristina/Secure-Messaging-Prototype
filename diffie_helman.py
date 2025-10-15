from signatures import generate_keys, sign_message, verify_signature
import secrets

def diffie_hellman_key_exchange():
    p = 23  
    g = 5   
    a = secrets.randbelow(p)
    b = secrets.randbelow(p)

    A = pow(g, a, p)
    B = pow(g, b, p)

    shared_secret_alice = pow(B, a, p)
    shared_secret_bob = pow(A, b, p)

    return p, g, A, B, shared_secret_alice, shared_secret_bob

if __name__ == "__main__":
    print("===== Task 2: Diffie–Hellman Key Exchange =====")

    # Generate RSA keys for signing (reuse Task 1)
    alice_private, alice_public = generate_keys()
    bob_private, bob_public = generate_keys()

    p, g, A, B, shared_a, shared_b = diffie_hellman_key_exchange()

    print(f"Public values: p={p}, g={g}")
    print(f"Alice sends A = {A}")
    print(f"Bob sends B = {B}")

    # Sign and verify exchanged values
    sig_A = sign_message(alice_private, str(A).encode())
    sig_B = sign_message(bob_private, str(B).encode())

    print("Bob verifies Alice’s A:", verify_signature(alice_public, str(A).encode(), sig_A))
    print("Alice verifies Bob’s B:", verify_signature(bob_public, str(B).encode(), sig_B))

    print("Alice’s computed shared secret:", shared_a)
    print("Bob’s computed shared secret:", shared_b)

    if shared_a == shared_b:
        print("✅ Shared secret matches!")
    else:
        print("❌ Shared secret mismatch!")
