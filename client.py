"""
Autonomous Agent Shannon Entropy & Information Theory Estimator Skill
Pure Python Standard Library implementation.
"""
import math
from typing import List, Dict, Any

class InformationTheoryEstimator:
    """
    Shannon Entropy, Mutual Information, and Divergence Estimator.
    """
    @staticmethod
    def entropy(probs: List[float]) -> float:
        total = sum(probs)
        if total <= 0:
            return 0.0
        h = 0.0
        for p in probs:
            p_norm = p / total
            if p_norm > 1e-12:
                h -= p_norm * math.log2(p_norm)
        return round(h, 6)

    @staticmethod
    def kl_divergence(p: List[float], q: List[float]) -> float:
        sum_p = sum(p)
        sum_q = sum(q)
        kl = 0.0
        for pi, qi in zip(p, q):
            p_norm = pi / sum_p
            q_norm = qi / sum_q
            if p_norm > 1e-12:
                if q_norm <= 1e-12:
                    return float("inf")
                kl += p_norm * math.log2(p_norm / q_norm)
        return round(kl, 6)

    @staticmethod
    def jensen_shannon_divergence(p: List[float], q: List[float]) -> float:
        sum_p = sum(p)
        sum_q = sum(q)
        p_norm = [x / sum_p for x in p]
        q_norm = [x / sum_q for x in q]
        m = [(pi + qi) / 2.0 for pi, qi in zip(p_norm, q_norm)]
        jsd = 0.5 * InformationTheoryEstimator.kl_divergence(p_norm, m) + 0.5 * InformationTheoryEstimator.kl_divergence(q_norm, m)
        return round(jsd, 6)

    @staticmethod
    def mutual_information(joint_matrix: List[List[float]]) -> float:
        total = sum(sum(row) for row in joint_matrix)
        if total <= 0:
            return 0.0
        n_x = len(joint_matrix)
        n_y = len(joint_matrix[0])
        norm_mat = [[joint_matrix[x][y] / total for y in range(n_y)] for x in range(n_x)]

        p_x = [sum(norm_mat[x][y] for y in range(n_y)) for x in range(n_x)]
        p_y = [sum(norm_mat[x][y] for x in range(n_x)) for y in range(n_y)]

        mi = 0.0
        for x in range(n_x):
            for y in range(n_y):
                pxy = norm_mat[x][y]
                if pxy > 1e-12:
                    denom = p_x[x] * p_y[y]
                    if denom > 1e-12:
                        mi += pxy * math.log2(pxy / denom)
        return round(mi, 6)
