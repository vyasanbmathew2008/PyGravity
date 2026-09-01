# PyGravity Phase 1

Basic IDE foundation.

## Run

From the `Phase1` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m backend.main
```

Open:

```text
http://127.0.0.1:8000
```

## Structure

```text
Phase1/
├── backend/
│   ├── __init__.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── assets/
├── tests/
├── requirements.txt
└── README.md
```
