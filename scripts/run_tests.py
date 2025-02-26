#!/usr/bin/env python3
"""
Test runner script that provides feedback on each commit.
This script runs tests and generates a summary report.
"""
import os
import sys
import time
import subprocess
from datetime import datetime

# Create scripts directory if it doesn't exist
if not os.path.exists('scripts'):
    os.makedirs('scripts')

# Create feedback directory if it doesn't exist
if not os.path.exists('feedback'):
    os.makedirs('feedback')

# Constants
FEEDBACK_FILE = 'feedback/commit_feedback.txt'
LOG_FILE = 'feedback/test_history.log'

def run_command(command):
    """Run a shell command and return stdout, stderr and return code."""
    process = subprocess.Popen(
        command, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        shell=True, 
        text=True
    )
    stdout, stderr = process.communicate()
    return stdout, stderr, process.returncode

def get_git_info():
    """Get current git commit information."""
    commit_hash, _, _ = run_command('git rev-parse HEAD')
    commit_msg, _, _ = run_command('git log -1 --pretty=%B')
    
    return {
        'hash': commit_hash.strip(),
        'message': commit_msg.strip()
    }

def run_tests():
    """Run pytest and collect results."""
    start_time = time.time()
    stdout, stderr, return_code = run_command('pytest -v')
    end_time = time.time()
    
    return {
        'output': stdout,
        'errors': stderr,
        'success': return_code == 0,
        'duration': end_time - start_time
    }

def get_coverage():
    """Run coverage report and collect results."""
    stdout, stderr, return_code = run_command('pytest --cov=indotool --cov-report=term-missing')
    
    if return_code != 0:
        return "Coverage analysis failed"
    
    # Extract coverage percentage from output
    for line in stdout.splitlines():
        if 'TOTAL' in line:
            return line.strip()
    
    return "Coverage data not found"

def write_feedback(git_info, test_results, coverage):
    """Write feedback to the feedback file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(FEEDBACK_FILE, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write(f"COMMIT FEEDBACK - {timestamp}\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Commit: {git_info['hash']}\n")
        f.write(f"Message: {git_info['message']}\n\n")
        
        f.write("-" * 80 + "\n")
        f.write("TEST RESULTS\n")
        f.write("-" * 80 + "\n")
        
        if test_results['success']:
            f.write("✅ All tests passed!\n")
        else:
            f.write("❌ Tests failed!\n")
        
        f.write(f"Duration: {test_results['duration']:.2f} seconds\n\n")
        
        f.write("COVERAGE\n")
        f.write("-" * 80 + "\n")
        f.write(f"{coverage}\n\n")
        
        f.write("DETAILS\n")
        f.write("-" * 80 + "\n")
        f.write(test_results['output'])
        
        if test_results['errors']:
            f.write("\nERRORS\n")
            f.write("-" * 80 + "\n")
            f.write(test_results['errors'])
    
    # Also append a summary to the log file
    with open(LOG_FILE, 'a') as f:
        status = "PASS" if test_results['success'] else "FAIL"
        f.write(f"{timestamp} | {git_info['hash'][:8]} | {status} | {git_info['message'].splitlines()[0][:50]}\n")
    
    # Print a summary to the console
    print(f"\nCommit feedback generated in {FEEDBACK_FILE}")
    print(f"Status: {'PASS' if test_results['success'] else 'FAIL'}")

def main():
    """Main function."""
    # Create necessary directories
    os.makedirs('feedback', exist_ok=True)
    
    # Get git information
    git_info = get_git_info()
    
    # Skip if we're in an empty repository or no tests exist yet
    if not git_info['hash'] or not os.path.exists('tests'):
        print("Skipping tests: empty repository or no tests directory")
        return 0
    
    # Run tests
    test_results = run_tests()
    
    # Get coverage
    coverage = get_coverage()
    
    # Write feedback
    write_feedback(git_info, test_results, coverage)
    
    # Return appropriate exit code
    return 0 if test_results['success'] else 1

if __name__ == "__main__":
    sys.exit(main())