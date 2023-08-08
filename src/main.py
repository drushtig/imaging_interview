__author__      = "Drushti Gulhane"
__version__ = "1.0.1"
__maintainer__ = "Drushti Gulhane"
__email__ = "drushtimgulhane@gmail.com"
__status__ = "Dev"


import yaml
from utils import process_images

def main():
    """Main function to process images."""
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    source_folder = config['source_folder']
    destination_folder = config['destination_folder']
    threshold = config['threshold']

    process_images(source_folder, destination_folder, threshold)

if __name__ == "__main__":
    main()

