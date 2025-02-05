# Dynamic Pricing Implementation (30 minutes)

## Context
Our parking system calculates dynamic prices based on:
- Base price for the location
- Current demand (Walk Score as a proxy)
- Time of day
- Special events nearby

## Task
1. Review and fix the broken code in `dynamic_pricing.py`
2. The script should:
   - Process parking spot data from CSV
   - Fetch Walk Scores via API
   - Calculate dynamic prices
   - Output structured results

## Success Criteria
- All bugs identified and fixed
- Script runs successfully
- Dynamic pricing logic implemented
- Code follows Python best practices
- Proper error handling

## Files Provided
- `dynamic_pricing.py`: Main script (contains bugs)
- `parking_spots.csv`: Sample data
- `config.py`: Configuration settings

## Notes
- Walk Score API key provided during interview
- Focus on code quality and business logic
- Consider edge cases and error handling

## Setup
```bash
git clone https://github.com/airgarage/parking-challenge.git
cd parking-challenge
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
