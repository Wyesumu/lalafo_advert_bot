import os


def load_env_file():
    if os.path.isfile(".env"):
        with open(".env") as f:
            while line := f.readline():
                if "=" in line and not line[0] in "#; ":
                    name, value = line.split("=", 1)
                    os.environ.update({name: value.strip("\n")})
