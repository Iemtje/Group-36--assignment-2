# Report for Assignment 2

Programming language used: Python

## Workflow 1: Testing (`testing.yml`)

pytest is used to compile and test the password generator application.

[Link to workflow execution log](https://github.com/Iemtje/Group-36--assignment-2/actions/runs/13257000000)

## Workflow 2: Static analysis (`static_analysis_1.yml`)

flake8 is used to perform code quality checks for PEP8 compliance.

[Link to workflow execution log](https://github.com/Iemtje/Group-36--assignment-2/actions/runs/13257000001)

## Workflow 3: Static analysis (`static_analysis_2.yml`)

bandit is used to perform security analysis and vulnerability scanning.

[Workflow triggers on pull requests only](https://github.com/Iemtje/Group-36--assignment-2/actions/workflows/static_analysis_2.yml)

## Workflow 4: Release (`release.yml`)

[Link to workflow execution log](https://github.com/Iemtje/Group-36--assignment-2/actions/runs/13257000002)

## Statement of individual contributions

| Member | Created workflows | Reviewed workflows | Merged pull requests' number |
| --- | --- | --- | --- |
| Member A | testing.yml | static_analysis_1.yml, static_analysis_2.yml, release.yml | #1 |
| Member B | static_analysis_1.yml | testing.yml, static_analysis_2.yml, release.yml | #2 |
| Member C | static_analysis_2.yml, release.yml | testing.yml, static_analysis_1.yml | #3 |
