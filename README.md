# CourseAligned
Local React + Flask research prototype. All included questions, historical conventions, and cached scores are synthetic. Cached comparisons illustrate behavior and are not measured accuracy results. No submissions are persisted.

## Run
From this directory:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/app.py
```
In another terminal:
```sh
npm install
npm run dev
```
Open http://127.0.0.1:5173. Load a prepared example and compare graders without credentials. For custom answers, copy backend/.env.example to backend/.env and supply an OpenAI API key. Both graders send the answer to that provider. Never enter sensitive student information in this demo.

`GET /api/questions` returns fixtures. `POST /api/compare` accepts `{questionId, response}`. Live grader failures appear independently. Alignment notes are authored fixtures; automatic optimization and held-out evaluation are future work.

Validation: `npm run build`; backend tests: `python -m unittest discover -s backend`.
