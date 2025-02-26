.PHONY: setup test lint format clean install dev-install

# Setup the development environment
setup:
	pip install -e ".[dev]"
	pre-commit install

# Run tests
test:
	pytest

# Run tests with coverage
coverage:
	pytest --cov=indotool --cov-report=term-missing

# Run linting
lint:
	flake8 indotool tests
	black --check indotool tests
	isort --check-only indotool tests

# Format code
format:
	black indotool tests
	isort indotool tests

# Clean up build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Install the package
install:
	pip install .

# Install in development mode
dev-install:
	pip install -e ".[dev]"

# View feedback
feedback:
	cat feedback/commit_feedback.txt