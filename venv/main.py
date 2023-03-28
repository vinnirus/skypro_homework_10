from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill


PATH_TO_JSON_FILE = 'candidates.json'

if __name__ == '__main__':

    app = Flask(__name__)

    @app.route("/")
    def get_candidates():
        candidates = get_all()
        page_output: str = '<pre>'

        for candidate in candidates:
            page_output += f'\nИмя кандидата - {candidate.name}\nПозиция кандидата - {candidate.position}\nНавыки кандидата - {candidate.get_skills_to_str()}\n\n'

        page_output += '</pre>'

        return page_output


    @app.route("/candidates/<int:id_candidate>")
    def get_candidate(id_candidate):
        candidate = get_by_pk(id_candidate)
        page_output: str = f'<img src="{candidate.picture}">\n\n'
        page_output += f'<pre>\nИмя кандидата - {candidate.name}\nПозиция кандидата - {candidate.position}\nНавыки кандидата - {candidate.get_skills_to_str()}\n</pre>'

        return page_output


    @app.route("/skills/<skill>")
    def get_candidates_by_skill(skill):
        candidates = get_by_skill(skill)

        page_output: str = '<pre>'

        for candidate in candidates:
            page_output += f'\nИмя кандидата - {candidate.name}\nПозиция кандидата - {candidate.position}\nНавыки кандидата - {candidate.get_skills_to_str()}\n\n'

        page_output += '</pre>'
        return page_output

    app.run()
