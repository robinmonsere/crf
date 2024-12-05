import os
import random
import shutil
import argparse
import sys

def move_random_files(src_folder, dest_folder, count=10):
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get the name of the current executable or script
    main_exe = os.path.basename(sys.executable if getattr(sys, 'frozen', False) else __file__)

    # List files, excluding the main executable or script
    files = [
        f for f in os.listdir(src_folder)
        if os.path.isfile(os.path.join(src_folder, f)) and f != main_exe
    ]

    if len(files) < count:
        print(f"Not enough files to copy. Found only {len(files)} files.")
        count = len(files)

    random_files = random.sample(files, count)

    for file in random_files:
        src_path = os.path.join(src_folder, file)
        dest_path = os.path.join(dest_folder, file)
        shutil.copy2(src_path, dest_path)
        print(f"Copied: {file}")

if __name__ == "__main__":
    # Get the folder where the script or .exe is located
    exe_folder = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    default_src_folder = exe_folder
    default_dest_folder = os.path.join(exe_folder, 'random_images')

    parser = argparse.ArgumentParser(description="Copy random files from one folder to another.")
    parser.add_argument(
        "src_folder",
        nargs="?",
        default=default_src_folder,
        help=f"Path to the source folder (default: current folder where the script/exe is located)"
    )
    parser.add_argument(
        "dest_folder",
        nargs="?",
        default=default_dest_folder,
        help=f"Path to the destination folder (default: 'random_images' in the script/exe folder)"
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=10,
        help="Number of files to copy (default is 10)"
    )

    args = parser.parse_args()
    move_random_files(args.src_folder, args.dest_folder, args.count)
