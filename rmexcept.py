#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

def main():
    # Parse arguments - files to keep
    keep_files = set(sys.argv[1:])

    if not keep_files:
        print("Usage: rmexcept file1 file2 file3 ...")
        print("Deletes everything in current directory except specified files")
        sys.exit(1)

    cwd = Path.cwd()
    to_delete = []

    # Find everything to delete
    for item in cwd.iterdir():
        if item.name not in keep_files:
            to_delete.append(item)

    if not to_delete:
        print("Nothing to delete (all files/dirs are protected)")
        return

    # Show what will be deleted
    print(f"Will delete {len(to_delete)} items:")
    for item in to_delete:
        item_type = "DIR" if item.is_dir() else "FILE"
        print(f"  [{item_type}] {item.name}")

    # Confirm
    response = input("\nProceed? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled")
        return

    # Delete
    for item in to_delete:
        try:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
            print(f"Deleted: {item.name}")
        except Exception as e:
            print(f"Error deleting {item.name}: {e}")

if __name__ == '__main__':
    main()
