import os.path

mod_path = os.path.dirname(__file__)

COMEDIC_FILE_LIST = [
    os.path.join(mod_path, "..", "data", "imdb_comedic_actors.names")
    os.path.join(mod_path, "..", "data", "imdb_comedic_actors_f.names"),
]

def is_comedic_actor(name):
    for comedic_file in COMEDIC_FILE_LIST:
        if is_name_in_file(name, comedic_file):
            return True
    return False

def is_name_in_file(name, filename):
    with open(filename, "r") as f:
        for line in f:
            if name.lower() == line.strip().lower():
                return True
    return False
            