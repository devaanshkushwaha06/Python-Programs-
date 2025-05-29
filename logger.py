

# Function to write logs to a file
def log_message(message,level="INFO"):
    with open("app.log","a") as log_file:
        log_file.write(f"{level}: {message}\n")

# Logging functions for different levels
def log_info(message):
    log_message(message,"INFO")

def log_warning(message):
    log_message(message,"WARNING")

def log_error(message):
    log_message(message,"ERROR")