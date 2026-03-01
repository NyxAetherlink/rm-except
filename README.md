# rm-except

A simple Python utility to delete everything in your current directory except specified files.

## Why?

Ever wanted to nuke a directory but keep just a few files? This tool makes it dead simple:

```bash
rmexcept keep_this.txt important_folder config.yml
```

Done. Everything else is gone.

## Installation

### Option 1: Add to PATH (Recommended)

```bash
# Copy to ~/.local/bin
cp rmexcept.py ~/.local/bin/rmexcept

# Add to your PATH in ~/.config/fish/config.fish (or your shell)
set -gx PATH ~/.local/bin $PATH
```

Then use it anywhere:
```bash
rmexcept file1 file2
```

### Option 2: Use as Alias

```bash
alias rmexcept='/path/to/rmexcept.py'
```

## Usage

```bash
rmexcept file1 file2 file3
```

Just list the files/directories to keep. The script will:
1. Show you what will be deleted
2. Ask for confirmation
3. Delete everything else in the current directory

### Example

```
$ rmexcept important.txt data/

Will delete 3 items:
  [FILE] temp.log
  [DIR] cache
  [FILE] .backup

Proceed? (y/n): y
Deleted: temp.log
Deleted: cache
Deleted: .backup
```

## Safety

The script always shows you what's getting deleted and asks for confirmation before proceeding. It's safe—just double-check the list before pressing `y`.

## Requirements

- Python 3.6+
- Unix-like system (Linux, macOS, BSD)

## License

GPL-3.0
