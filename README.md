# nexus-verify-api

Identity verification engine for demographic matching.

## What it does
Compares a submitted name and date of birth against a reference
record and returns MATCH, PARTIAL, or NO_MATCH with a confidence score.

## How it works
Uses Levenshtein distance for fuzzy name matching and strict
equality for date of birth. Designed for African name variations.

## Run the tests
python3 tests.py
