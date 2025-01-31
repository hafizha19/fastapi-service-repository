# FAST API WITH SERVICE REPOSITORY PATTERN

## HOW TO INSTALL

- Clone:
  ```bash
  git clone git@github.com:hafizha19/fastapi-service-repository
  ```
- Request `.env.dev` and `resources` to other programmers
- Create venv:
  ```bash
  python -m venv ./.venv
  ```
- Activate venv:
  ```bash
  .venv/Scripts/activate.ps1
  ```
  for macOS:
  ```bash
  source .venv/bin/activate
  ```
- Install requirement packages:
  ```bash
  pip install -r requirements.txt
  ```
- Run:
  ```bash
  uvicorn main:app -reload
  ```
- :sparkles: **_Code with joy and let the algorithms dance!_** :sparkles:

### Additional

- Install formatter for VSCode (to format clean code, sorting import packages on module):
  ```bash
  pip install -r requirements-dev.txt
  ```
- Add json on .vscode/settings.json

```
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "ruff.organizeImports": false,
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        }
    }
}
```

- Change remote origin if create new project:
  ```bash
  git remote set-url origin git@github.com:devjobseekercompany/blahblah.git
  ```

## ROLES

- Improve readibility python code with PEP8
- Database (column, table (plural)): Snack Case -> user_id
- Request and Response using Camel Case [example](https://github.com/hafizha19/fastapi-service-repository/blob/master/data/responses/holiday_response.py)
- Commit and Branch: [Semantic Commit](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
  tickets: `(Job Posting) Requisition List`
  branch: namaku/type/scope, example: `omi/feat/job-posting`
  commit: `feat(Job Posting): add requisition list`

## Pattern Description

- CONTROLLER contains route mapping, request and response formatting (DTO)
- SERVICE contains business/logic flow
- REPOSITORY contains database query flow
- Always using try catch on controllers
