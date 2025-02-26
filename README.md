# IndoTool

A node-based mindmap visualization tool for knowledge management and collaboration.

## Description

IndoTool is a Python/Qt desktop application that allows users to visualize artifacts, conversations, and notes in an interactive node-based mindmap. It processes various input formats (file system, markdown, JSON, XML, YAML) and provides an intuitive interface for navigating complex information spaces.

## Installation

```bash
# Clone the repository
git clone https://github.com/PrimeDeviation/IndoTool.git
cd IndoTool

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```python
# Launch the application
python main.py

# Or import as a module in your own project
from indotool import MindMap

# Create a new mind map from various sources
mindmap = MindMap()
mindmap.add_from_directory("path/to/files")
mindmap.add_from_markdown("path/to/notes.md")
mindmap.add_from_json("path/to/data.json")
```

## Features

- Interactive node-based visualization of knowledge graphs
- Support for multiple input formats (filesystem, MD, JSON, XML, YAML)
- Seamless integration with external tools and chat conversations
- Efficient navigation and exploration of complex information spaces
- Comprehensive functional testing suite
- Cross-platform support via Python and Qt

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.