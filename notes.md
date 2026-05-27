1. Levenshtein algorithm is the preferred one because it solves the problem of having to use strict equality for data such as names.It measures how similiar the entries are instead. For example, Bello Muhammed == Bello Mohammed would fail the strict test while using levenshtein, the entries can be compared to see if it is merely an error of spelling etc. This prevents a situation where a lot of false negatives are recorded.

2.DOB uses strict matching because DOBs are strict numerical identifiers.A difference in digit arrangement could refer to an entrely new person. Using fuzzy matching could merge a lot of identities and increase fraud risk.

3.The numbers for MATCH,PARTIAL and NO MATCH are just heuristics based on real world data collection and they require validation.
