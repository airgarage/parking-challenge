"""Configuration settings for the dynamic pricing system"""

# API Configuration
WALK_SCORE_API_KEY = "YOUR_API_KEY"

# Time Multiplier Configuration
TIME_MULTIPLIERS = {
    "BUSINESS_HOURS": 1.5,  # 9AM - 5PM
    "EVENING_HOURS": 2.0,   # 5PM - 11PM
    "OFF_HOURS": 1.0       # 11PM - 9AM
}

# Walk Score Multiplier Configuration
WALK_SCORE_MULTIPLIER = {
    "MIN": 0.8,
    "MAX": 2.0
}