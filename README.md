# JOBSEEKER FAST API SKELETON GUIDELINES

## HOW TO INSTALL

- Clone: 
  ```bash
  git clone git@github.com:devjobseekercompany/skeleton-fast-api
- Request ```.env.dev``` and ```resources``` to other programmers
- Create venv:
  ```bash
  python -m venv ./.venv
- Activate venv:
  ```bash
  .venv/Scripts/activate.ps1
- Install requirement packages:
  ```bash
  pip install -r requirements.txt
- Run:
  ```bash
  uvicorn main:app -reload

### Additional
- Install formatter for VSCode (to format clean code, sorting import packages on module):
  ```bash
  pip install -r requirements-dev.txt
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

## ROLES

- Improve readibility python code with PEP8
- Database (column, table (plural)): Snack Case -> user_id
- Request and Response using Camel Case [example](https://github.com/devjobseekercompany/skeleton-fast-api/blob/master/data/responses/holiday_response.py)
- Commit and Branch: [Semantic Commit](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
  tickets: ```(Job Posting) Requisition List```
  branch: namaku/type/scope, example: ```omi/feat/job-posting```
  commit: ```feat(Job Posting): add requisition list```

## Pattern Description
- Use Scope to SELECT only, CREATE UPDATE DELETE on Repository
- CONTROLLER contains route mapping, request and response formatting (DTO) 
- SERVICE contains bussiness flow
- REPOSITORY contains model flow
- Always using try catch on controllers