#!/usr/bin/env python3
"""
Linux File System Manager
A comprehensive tool to create and manage file systems in Linux
"""

import os
import sys
import shutil
import subprocess
import stat
from pathlib import Path
from datetime import datetime
import json

class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

class FileSystemManager:
    """Main class for managing file systems"""
    
    def __init__(self, base_path="./filesystem_test"):
        self.base_path = Path(base_path)
        self.current_path = self.base_path
        
    def print_banner(self):
        """Display program banner"""
        banner = f"""{Colors.BOLD}{Colors.CYAN}
╔════════════════════════════════════════════╗
║                                            ║
║     🗂️  LINUX FILE SYSTEM MANAGER 🗂️     ║
║                                            ║
║     Create & Manage File Systems          ║
║                                            ║
╚════════════════════════════════════════════╝
{Colors.RESET}"""
        print(banner)
    
    def create_filesystem(self):
        """Create a new file system structure"""
        print(f"\n{Colors.CYAN}Creating new file system at: {self.base_path}{Colors.RESET}")
        
        try:
            # Create base directory
            self.base_path.mkdir(parents=True, exist_ok=True)
            
            # Create standard Linux directory structure
            directories = [
                "bin",      # Binaries
                "etc",      # Configuration files
                "home",     # User home directories
                "var/log",  # Log files
                "tmp",      # Temporary files
                "usr/local/bin",  # User binaries
                "opt",      # Optional software
                "proc",     # Process information
                "dev",      # Device files
                "mnt",      # Mount points
            ]
            
            for directory in directories:
                dir_path = self.base_path / directory
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"{Colors.GREEN}✓ Created: {directory}{Colors.RESET}")
            
            # Create some sample files
            self.create_sample_files()
            
            print(f"\n{Colors.GREEN}✓ File system created successfully!{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error creating file system: {e}{Colors.RESET}")
            return False
    
    def create_sample_files(self):
        """Create sample files in the file system"""
        # Create a sample configuration file
        config_file = self.base_path / "etc" / "config.conf"
        config_file.write_text("# Configuration File\nversion=1.0\nstatus=active\n")
        
        # Create a sample log file
        log_file = self.base_path / "var" / "log" / "system.log"
        log_file.write_text(f"[{datetime.now()}] System initialized\n")
        
        # Create a sample script
        script_file = self.base_path / "bin" / "hello.sh"
        script_file.write_text("#!/bin/bash\necho 'Hello, World!'\n")
        script_file.chmod(0o755)  # Make executable
        
        # Create a README
        readme = self.base_path / "README.md"
        readme.write_text("# File System\nThis is a sample Linux file system structure.\n")
    
    def create_file(self, filename, content=""):
        """Create a new file"""
        try:
            file_path = self.current_path / filename
            
            if file_path.exists():
                overwrite = input(f"{Colors.YELLOW}File exists. Overwrite? (y/n): {Colors.RESET}")
                if overwrite.lower() != 'y':
                    print(f"{Colors.YELLOW}Operation cancelled.{Colors.RESET}")
                    return False
            
            file_path.write_text(content)
            print(f"{Colors.GREEN}✓ File created: {filename}{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error creating file: {e}{Colors.RESET}")
            return False
    
    def create_directory(self, dirname):
        """Create a new directory"""
        try:
            dir_path = self.current_path / dirname
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"{Colors.GREEN}✓ Directory created: {dirname}{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error creating directory: {e}{Colors.RESET}")
            return False
    
    def list_contents(self, path=None, detailed=False):
        """List directory contents"""
        target_path = Path(path) if path else self.current_path
        
        try:
            if not target_path.exists():
                print(f"{Colors.RED}✗ Path does not exist: {target_path}{Colors.RESET}")
                return
            
            print(f"\n{Colors.CYAN}Contents of: {target_path}{Colors.RESET}")
            print("=" * 70)
            
            if detailed:
                # Detailed listing (like ls -l)
                print(f"{'Permissions':<12} {'Size':<10} {'Modified':<20} {'Name':<20}")
                print("-" * 70)
                
                items = sorted(target_path.iterdir())
                for item in items:
                    stats = item.stat()
                    perms = stat.filemode(stats.st_mode)
                    size = stats.st_size
                    mtime = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
                    
                    if item.is_dir():
                        name = f"{Colors.BLUE}{item.name}/{Colors.RESET}"
                    else:
                        name = item.name
                    
                    print(f"{perms:<12} {size:<10} {mtime:<20} {name}")
            else:
                # Simple listing
                items = sorted(target_path.iterdir())
                for item in items:
                    if item.is_dir():
                        print(f"{Colors.BLUE}📁 {item.name}/{Colors.RESET}")
                    else:
                        print(f"📄 {item.name}")
            
            print()
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error listing contents: {e}{Colors.RESET}")
    
    def change_directory(self, path):
        """Change current directory"""
        try:
            if path == "..":
                new_path = self.current_path.parent
            elif path == "~" or path == "/":
                new_path = self.base_path
            else:
                new_path = self.current_path / path
            
            if new_path.exists() and new_path.is_dir():
                self.current_path = new_path
                print(f"{Colors.GREEN}✓ Changed to: {self.current_path}{Colors.RESET}")
                return True
            else:
                print(f"{Colors.RED}✗ Directory does not exist: {path}{Colors.RESET}")
                return False
                
        except Exception as e:
            print(f"{Colors.RED}✗ Error changing directory: {e}{Colors.RESET}")
            return False
    
    def copy_file(self, source, destination):
        """Copy a file or directory"""
        try:
            src_path = self.current_path / source
            dest_path = self.current_path / destination
            
            if not src_path.exists():
                print(f"{Colors.RED}✗ Source does not exist: {source}{Colors.RESET}")
                return False
            
            if src_path.is_dir():
                shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dest_path)
            
            print(f"{Colors.GREEN}✓ Copied: {source} → {destination}{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error copying: {e}{Colors.RESET}")
            return False
    
    def move_file(self, source, destination):
        """Move/rename a file or directory"""
        try:
            src_path = self.current_path / source
            dest_path = self.current_path / destination
            
            if not src_path.exists():
                print(f"{Colors.RED}✗ Source does not exist: {source}{Colors.RESET}")
                return False
            
            shutil.move(str(src_path), str(dest_path))
            print(f"{Colors.GREEN}✓ Moved: {source} → {destination}{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error moving: {e}{Colors.RESET}")
            return False
    
    def delete_file(self, path):
        """Delete a file or directory"""
        try:
            target_path = self.current_path / path
            
            if not target_path.exists():
                print(f"{Colors.RED}✗ Path does not exist: {path}{Colors.RESET}")
                return False
            
            confirm = input(f"{Colors.YELLOW}Delete '{path}'? (y/n): {Colors.RESET}")
            if confirm.lower() != 'y':
                print(f"{Colors.YELLOW}Operation cancelled.{Colors.RESET}")
                return False
            
            if target_path.is_dir():
                shutil.rmtree(target_path)
            else:
                target_path.unlink()
            
            print(f"{Colors.GREEN}✓ Deleted: {path}{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error deleting: {e}{Colors.RESET}")
            return False
    
    def search_files(self, pattern):
        """Search for files matching a pattern"""
        try:
            print(f"\n{Colors.CYAN}Searching for: {pattern}{Colors.RESET}")
            print("=" * 70)
            
            matches = list(self.current_path.rglob(pattern))
            
            if not matches:
                print(f"{Colors.YELLOW}No matches found.{Colors.RESET}")
                return
            
            for match in matches:
                relative_path = match.relative_to(self.current_path)
                if match.is_dir():
                    print(f"{Colors.BLUE}📁 {relative_path}/{Colors.RESET}")
                else:
                    print(f"📄 {relative_path}")
            
            print(f"\n{Colors.GREEN}Found {len(matches)} match(es){Colors.RESET}\n")
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error searching: {e}{Colors.RESET}")
    
    def get_file_info(self, filename):
        """Get detailed information about a file"""
        try:
            file_path = self.current_path / filename
            
            if not file_path.exists():
                print(f"{Colors.RED}✗ File does not exist: {filename}{Colors.RESET}")
                return
            
            stats = file_path.stat()
            
            print(f"\n{Colors.CYAN}File Information: {filename}{Colors.RESET}")
            print("=" * 70)
            print(f"Path:        {file_path}")
            print(f"Type:        {'Directory' if file_path.is_dir() else 'File'}")
            print(f"Size:        {stats.st_size} bytes")
            print(f"Permissions: {stat.filemode(stats.st_mode)}")
            print(f"Owner UID:   {stats.st_uid}")
            print(f"Group GID:   {stats.st_gid}")
            print(f"Created:     {datetime.fromtimestamp(stats.st_ctime)}")
            print(f"Modified:    {datetime.fromtimestamp(stats.st_mtime)}")
            print(f"Accessed:    {datetime.fromtimestamp(stats.st_atime)}")
            print()
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error getting file info: {e}{Colors.RESET}")
    
    def change_permissions(self, filename, mode):
        """Change file permissions (chmod)"""
        try:
            file_path = self.current_path / filename
            
            if not file_path.exists():
                print(f"{Colors.RED}✗ File does not exist: {filename}{Colors.RESET}")
                return False
            
            # Convert octal string to integer
            mode_int = int(mode, 8)
            file_path.chmod(mode_int)
            
            print(f"{Colors.GREEN}✓ Changed permissions: {filename} → {mode}{Colors.RESET}")
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error changing permissions: {e}{Colors.RESET}")
            return False
    
    def tree_view(self, path=None, prefix="", max_depth=3, current_depth=0):
        """Display directory tree structure"""
        if current_depth >= max_depth:
            return
        
        target_path = Path(path) if path else self.current_path
        
        try:
            items = sorted(target_path.iterdir())
            
            for i, item in enumerate(items):
                is_last = i == len(items) - 1
                connector = "└── " if is_last else "├── "
                
                if item.is_dir():
                    print(f"{prefix}{connector}{Colors.BLUE}{item.name}/{Colors.RESET}")
                    
                    extension = "    " if is_last else "│   "
                    self.tree_view(item, prefix + extension, max_depth, current_depth + 1)
                else:
                    print(f"{prefix}{connector}{item.name}")
                    
        except PermissionError:
            print(f"{prefix}[Permission Denied]")
        except Exception as e:
            print(f"{Colors.RED}Error: {e}{Colors.RESET}")
    
    def get_disk_usage(self):
        """Get disk usage statistics"""
        try:
            total_size = 0
            file_count = 0
            dir_count = 0
            
            for item in self.base_path.rglob('*'):
                if item.is_file():
                    total_size += item.stat().st_size
                    file_count += 1
                elif item.is_dir():
                    dir_count += 1
            
            print(f"\n{Colors.CYAN}Disk Usage Statistics{Colors.RESET}")
            print("=" * 70)
            print(f"Base Path:    {self.base_path}")
            print(f"Directories:  {dir_count}")
            print(f"Files:        {file_count}")
            print(f"Total Size:   {total_size} bytes ({total_size / 1024:.2f} KB)")
            print()
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error calculating disk usage: {e}{Colors.RESET}")

def display_menu():
    """Display main menu"""
    menu = f"""
{Colors.BOLD}{Colors.CYAN}═══════════════ MENU ═══════════════{Colors.RESET}
{Colors.GREEN}File Operations:{Colors.RESET}
  1.  Create File System
  2.  Create File
  3.  Create Directory
  4.  List Contents (simple)
  5.  List Contents (detailed)
  6.  Change Directory
  7.  Copy File/Directory
  8.  Move/Rename File
  9.  Delete File/Directory
  10. Search Files

{Colors.GREEN}Information:{Colors.RESET}
  11. File Information
  12. Tree View
  13. Disk Usage
  14. Change Permissions

{Colors.GREEN}Navigation:{Colors.RESET}
  15. Print Current Directory
  16. Go to Base Directory

{Colors.RED}Other:{Colors.RESET}
  17. Exit

{Colors.CYAN}════════════════════════════════════{Colors.RESET}
"""
    print(menu)

def main():
    """Main program loop"""
    manager = FileSystemManager()
    manager.print_banner()
    
    print(f"\n{Colors.YELLOW}Welcome to Linux File System Manager!{Colors.RESET}")
    print(f"Base directory: {manager.base_path}")
    
    while True:
        display_menu()
        print(f"{Colors.CYAN}Current directory: {manager.current_path}{Colors.RESET}")
        choice = input(f"\n{Colors.YELLOW}Enter your choice (1-17): {Colors.RESET}").strip()
        
        if choice == "1":
            manager.create_filesystem()
        
        elif choice == "2":
            filename = input("Enter filename: ")
            content = input("Enter content (or press Enter for empty): ")
            manager.create_file(filename, content)
        
        elif choice == "3":
            dirname = input("Enter directory name: ")
            manager.create_directory(dirname)
        
        elif choice == "4":
            manager.list_contents()
        
        elif choice == "5":
            manager.list_contents(detailed=True)
        
        elif choice == "6":
            path = input("Enter path (.. for parent, ~ for base): ")
            manager.change_directory(path)
        
        elif choice == "7":
            source = input("Enter source path: ")
            destination = input("Enter destination path: ")
            manager.copy_file(source, destination)
        
        elif choice == "8":
            source = input("Enter source path: ")
            destination = input("Enter destination path: ")
            manager.move_file(source, destination)
        
        elif choice == "9":
            path = input("Enter path to delete: ")
            manager.delete_file(path)
        
        elif choice == "10":
            pattern = input("Enter search pattern (e.g., *.txt): ")
            manager.search_files(pattern)
        
        elif choice == "11":
            filename = input("Enter filename: ")
            manager.get_file_info(filename)
        
        elif choice == "12":
            print(f"\n{Colors.CYAN}Directory Tree:{Colors.RESET}")
            print("=" * 70)
            print(f"{Colors.BLUE}{manager.current_path.name}/{Colors.RESET}")
            manager.tree_view()
            print()
        
        elif choice == "13":
            manager.get_disk_usage()
        
        elif choice == "14":
            filename = input("Enter filename: ")
            mode = input("Enter permissions (e.g., 755): ")
            manager.change_permissions(filename, mode)
        
        elif choice == "15":
            print(f"\n{Colors.CYAN}Current directory: {manager.current_path}{Colors.RESET}\n")
        
        elif choice == "16":
            manager.current_path = manager.base_path
            print(f"{Colors.GREEN}✓ Moved to base directory{Colors.RESET}")
        
        elif choice == "17":
            print(f"\n{Colors.CYAN}Thank you for using File System Manager!{Colors.RESET}")
            print(f"{Colors.GREEN}Goodbye! 👋{Colors.RESET}\n")
            break
        
        else:
            print(f"{Colors.RED}Invalid choice! Please try again.{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
        os.system('clear' if os.name == 'posix' else 'cls')
        manager.print_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
        print(f"{Colors.GREEN}Goodbye! 👋{Colors.RESET}\n")
        sys.exit(0)
