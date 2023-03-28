import json
from candidate import Candidate


def load_candidates() -> list[Candidate]:

    with open('candidates.json', 'r', encoding='utf-8') as candidates_json_file:
        applicants = json.load(candidates_json_file)

    candidates: Candidate = []

    for applicant in applicants:
        candidate = Candidate(applicant["pk"], applicant["name"], applicant["picture"], applicant["position"], applicant["gender"], applicant["age"], applicant["skills"])
        candidates.append(candidate)

    return candidates


def get_all() -> list[Candidate]:
    return load_candidates()


def get_by_pk(pk: int) -> Candidate:
    candidates: list[Candidate] = load_candidates()
    for candidate in candidates:
        if candidate.pk == pk:
            return candidate


def get_by_skill(skill_name) -> list[Candidate]:
    candidates: list[Candidate] = load_candidates()
    candidates_with_skill: list[Candidate] = []

    for each in candidates:
        if skill_name in each.skills:
            candidates_with_skill.append(each)

    return candidates_with_skill
