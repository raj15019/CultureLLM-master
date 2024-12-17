from google.colab import userdata

def print_secret(secret_name):
    """
    Prints the value of a secret from environment variables.

    
    Args:
        secret_name (str): The name of the secret to print.
    """

    try:
        secret_value = userdata.get('OPEN_AI_KEY')
        print(f"Secret '{secret_name}': {secret_value}")
    except KeyError:
        print(f"Secret '{secret_name}' not found in environment variables.")

# Example usage:
print_secret("OPEN_AI_KEY")

