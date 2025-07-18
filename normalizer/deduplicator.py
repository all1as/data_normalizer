from typing import List, Dict, Any, Tuple
from fuzzywuzzy import fuzz

def fuzzy_deduplicate(
    records: List[Dict[str, Any]],
    key_weights: Dict[str, float],
    low_threshold: float = 0.4,
    high_threshold: float = 0.8
) -> Tuple[List[Dict[str, Any]], List[Tuple[int, int, float]], List[Tuple[int, int, float]]]:
    unique = []
    duplicates = []
    to_review = []

    for i, rec in enumerate(records):
        classified = False
        for j, uniq in enumerate(unique):
            total_weight = sum(key_weights.values())
            score = 0.0
            for key, weight in key_weights.items():
                v1, v2 = str(rec.get(key, "")), str(uniq.get(key, ""))
                sim = fuzz.token_sort_ratio(v1, v2) / 100.0
                score += sim * weight
            score /= total_weight

            if score >= high_threshold:
                duplicates.append((i, j, score))
                classified = True
                break
            elif score >= low_threshold:
                to_review.append((i, j, score))
                classified = True
                break

        if not classified:
            unique.append(rec)

    return unique, duplicates, to_review
