# Group-36--assignment-2
# Assignment 2 – CI/CD Pipeline for Password Generator

## Project Overview

This repository contains the CI/CD integration for our Password Generator Application, developed in Assignment 1. The password generator is a flexible Python-based tool that allows users to generate highly secure passwords with customizable options, including length, character types (uppercase, lowercase, digits, special characters), and optional exclusion of visually similar characters. It ensures strong security by enforcing character diversity and full randomization.

---

## Workflows

We implemented four GitHub Actions workflows to enable continuous integration and delivery (CI/CD). All workflows are located in `.github/workflows/`.

### 1. `testing.yml`

- **Purpose:** Runs the test suite on each commit to ensure all code changes pass.
- **Trigger:** `on: [push]`
- **Tool:** `pytest`
- **Details:** Installs dependencies from `requirements.txt` and runs tests in the `tests/` directory.
- **Link to GitHub Action:** [Example Run](https://github.com/your-username/your-repo/actions/workflows/testing.yml)

### 2. `static_analysis_1.yml`

- **Purpose:** Performs static code analysis for style and readability.
- **Trigger:** `on: [push]`
- **Tool:** `flake8`
- **Details:** Checks the `src/` folder for PEP8 compliance and code style violations.
- **Link to GitHub Action:** [Example Run](https://github.com/your-username/your-repo/actions/workflows/static_analysis_1.yml)

### 3. `static_analysis_2.yml`

- **Purpose:** Performs sta
