
def parse_env_config(env_string: str):
    """
    Parses environment variables string into a configuration dictionary.
    """
    config = {}

    lines = env_string.splitlines()
    for line in lines:
        line = line.strip()

        # Ignore empty lines and comments
        if not line or line.startswith("#"):
            continue

        # Split into KEY and VALUE
        if "=" not in line:
            continue  # skip invalid lines

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        # Type conversion
        val_lower = value.lower()
        if val_lower == "true":
            value = True
        elif val_lower == "false":
            value = False
        elif value.isdigit():
            value = int(value)
        else:
            try:
                value = int(value)
            except ValueError:
                pass  # keep as string

        config[key] = value

    return config



if __name__ == "__main__":
    sample_env = """
# Database Configuration
DATABASE_URL=postgresql://user:pass@localhost:5432/appdb
DATABASE_POOL_SIZE=10

# Application Settings  
APP_NAME="E-Commerce API"
DEBUG=false
PORT=3000
WORKERS=4

# Feature Flags
ENABLE_LOGGING=true
ENABLE_CACHE="false"
CACHE_TTL=3600

# Empty line above should be ignored
REDIS_URL=redis://localhost:6379/0
"""
    
    config = parse_env_config(sample_env)
    print("Parsed Configuration:")
    for key, value in config.items():
        print(f"  {key}: {value} ({type(value).__name__})") 