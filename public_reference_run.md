# Public Reference Run - Tier 1 Audit Tool v9

**Date:** 2025-01-15
**Auditor:** Ahmad Sabawoon Rasoli (Bad Homburg, Germany)
**Tool version:** audit_tier1_tool_v9

## Purpose

This is a public demonstration of the Tier 1 screening tool on a
synthetic HealthTech file that contains five known defects. The goal
is to show what the tool detects and what it does not detect, so that
potential clients can evaluate its accuracy for themselves.

## Test file

The file `patient_data.py` is a synthetic example, not real client
code. It intentionally includes:

1. An unchecked pickle model load (NC-B1)
2. A scaler fitted on the full dataset (NC-B3)
3. An f-string SQL query (NC-B4)
4. A hardcoded database password (NC-B5)
5. A hardcoded API token (NC-B5)

## Expected result

Five defects should be flagged, and one check (NC-B6, semantic layer
version) should return PASS because the file has no semantic layer
definition.

## Actual result

```json
{
  "file": "patient_data.py",
  "results": {
    "NC-B1": "FAIL",
    "NC-B3": "FAIL",
    "NC-B4": "FAIL",
    "NC-B5": "FAIL",
    "NC-B6": "PASS"
  },
  "overall": "FAIL",
  "reasons": [
    "NC-B1: pickle.load without safeguard",
    "NC-B3: Data leakage pattern 'fit_transform' at line 26",
    "NC-B4: Potential SQL injection via f-string at line 18",
    "NC-B5: Hardcoded credential 'DB_PASSWORD' at line 5",
    "NC-B5: Hardcoded credential 'API_TOKEN' at line 6"
  ]
}
