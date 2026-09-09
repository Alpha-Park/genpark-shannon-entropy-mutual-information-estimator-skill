"""Example usage for Shannon Entropy & Information Theory Estimator Skill."""
from client import InformationTheoryEstimator

def main():
    print("Executing Information Theory Estimator...")
    # Fair coin entropy = 1.0 bit
    p = [0.5, 0.5]
    h = InformationTheoryEstimator.entropy(p)
    print("Entropy of fair coin:", h)
    assert h == 1.0, f"Expected 1.0, got {h}"

    # KL Divergence
    q = [0.8, 0.2]
    kl = InformationTheoryEstimator.kl_divergence(p, q)
    print("KL Divergence:", kl)
    assert kl > 0

    # Mutual Information of perfectly correlated binary variables
    joint = [[0.5, 0.0], [0.0, 0.5]]
    mi = InformationTheoryEstimator.mutual_information(joint)
    print("Mutual Information:", mi)
    assert mi == 1.0, f"Expected 1.0, got {mi}"
    print("Information Theory Estimator verified successfully!")

if __name__ == "__main__":
    main()
