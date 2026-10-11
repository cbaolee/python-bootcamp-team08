def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa) ->list[str]:
    
    message = []
    
    if credits < 120:
        missing_credits = 120 - credits
        message.append(f"need {missing_credits} more credits")    
    if gpa < 2.0:
        message.append("GPA below 2.0")
    
    return message
        