import os

def display_environment_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")

print("Environment Variables:")
display_environment_variables()
