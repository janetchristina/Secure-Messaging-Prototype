# Secure-Messaging-Prototype
This project involves implementing a two-party protocol between Alice and Bob in a way that the communication between them provides confidentiality and integrity using the cryptographic techniques.

Five tasks were implemented in total.

1. Digital Signature - 'signatures.py'
Alice and Bob each generate RSA key pairs. Messages exchanged in Diffie–Hellman are signed and verified to prevent MITM attacks. Functions used are generate_keys(), sign_message(), verify_signature()

2. Diffie-Hellman Key Exchange - 'diffie_helman.py'
Both parties compute the shared secret. Signatures ensure the authenticity of exchanged values. This is implemented using the function diffie_hellman_key_exchange()

3. Key Derivation Function - 'kdf.py'
Using the function derive_key(), the shared secret is iteratively hashed to derive a strong session key. 

4. Pseudo-Random Number Generators (PRNGs) - 'prng.py'
A simple seeded PRNG generates random IV/nonce values for symmetric encryption. This was achieved by using SimplePRNG class with seed(), reseed(), generate()

5. Secure Message Exchange - 'encryption.py'
AES (CBC mode) provides confidentiality.  
HMAC-SHA256 ensures message integrity.  
Bob verifies the MAC before decryption.
Functions implemented are sym_enc(), sym_dec(), compute_hmac(), authenticated_encrypt(), authenticated_decrypt()


Technologies Used
Python 3.10

Libraries
cryptography
hashlib
secrets
random / time

Installation and setup

1. Clone the repository
git clone https://github.com/<your-username>/SecureMessagingProject.git

2. Install dependencies
pip install cryptography
 
3. Run
To run the files, open two split terminals in VS Code, one for Alice and one for Bob, and run the command 'python filename.py'




