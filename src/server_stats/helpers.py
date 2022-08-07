import uuid


# REVIEW: Methods that are abstract of context should be collected into a helpers script
def generate_id() -> str:
    """
    Generates a UUID string for unique client IDs
    :return: String representation of UUID object
    """
    return str(uuid.uuid4())
