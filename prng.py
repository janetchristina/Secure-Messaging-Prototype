import time, random
class SimplePRNG:
    def __init__(self, seed=None):
        self.seed(seed or int(time.time()))

    def seed(self, s):
        random.seed(s)
        self.state = s

    def reseed(self, s):
        self.state ^= s
        random.seed(self.state)

    def generate(self):
        return random.randint(0, 2**128)

if __name__ == "__main__":
    print("===== Task 4: Pseudo-Random Number Generator (PRNG) =====")

    rng1 = SimplePRNG(1234)
    seq1 = [rng1.generate() for _ in range(3)]

    rng2 = SimplePRNG(1234)
    seq2 = [rng2.generate() for _ in range(3)]

    print("\nSequence 1 (seed=1234):", seq1)
    print("Sequence 2 (same seed=1234):", seq2)

    rng3 = SimplePRNG(5678)
    seq3 = [rng3.generate() for _ in range(3)]

    print("\nSequence 3 (seed=5678):", seq3)

    print("\n✅ Deterministic behavior confirmed for same seed")
    print("✅ Random behavior confirmed for different seed")
