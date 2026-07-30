def title_simplifier(title: str):
    """
        Simplifies in job_title into proper categorical manner
    """
    title_lower = title.lower()
    
    if "data scientist" in title_lower:
        return "data scientist"
    elif "data engineer" in title_lower:
        return "data engineer"
    elif "analyst" in title_lower:
        return "analyst"
    elif "machine learning" in title_lower:
        return "mle"
    elif "manager" in title_lower:
        return "manager"
    elif "director" in title_lower:
        return "director"
    else:
        return "na"


def seniority(title):
    """
        Identifies the seniority level from the job title
    """
    title_lower = title.lower()
    if "sr" in title_lower or "senior" in title_lower or "lead" in title_lower or "principal" in title_lower: 
        return "senior"
    elif "junior" in title_lower or "jr" in title_lower:
        return "junior"
    else: 
        return "na"