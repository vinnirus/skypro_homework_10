class Candidate:

    def __init__(self, pk, name: str, picture: str, position: str, gender: str, age: int, skills: list[str]):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = set(skills.lower().strip().split(", "))

    def __repr__(self):
        print(f'{type(self)} -> {self.name} | {self.position}')

    def get_skills_to_str(self):
        return ', '.join(self.skills)
