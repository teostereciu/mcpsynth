# Task: Build a CLI Tool for the Spoonacular Food API

## What You're Building

A command-line interface (CLI) tool that covers Spoonacular food and recipe API functionality, suitable for use by an autonomous agent completing real-world tasks.

## What You Have

- **API documentation** in `docs/` — 7 markdown files covering the Spoonacular API endpoints.
- **Environment variables** for authentication:
  - `SPOONACULAR_API_KEY` — API key
- **Base URL:** `https://api.spoonacular.com`
- **Auth:** `apiKey` query parameter appended to every request.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Recipe search (by query, by ingredients, by nutrients, complex search)
- Recipe information (details, ingredients, nutrition, instructions, similar)
- Ingredient search and information
- Meal plan generation (daily, weekly)
- Wine pairing
- Autocomplete (recipe and ingredient search)

## Technical Requirements

- **No generic passthrough commands**: do not expose a generic `query` or `request` command. Every command must correspond to a specific, named operation.

## Deliverables

- `spoonacular_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
