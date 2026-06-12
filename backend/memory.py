conversation_history = []

def save_message(role, message):
    conversation_history.append(
        {
            "role": role,
            "content": message,
        }
    )

def get_history():
    return conversation_history

def clear_history():
    conversation_history.clear()