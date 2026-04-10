# Logseq API MCP Server

**Model Context Protocol server for Logseq API integration with dynamic tool discovery**

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-compatible-green)](https://modelcontextprotocol.io/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![UV](https://img.shields.io/badge/package%20manager-uv-orange)](https://docs.astral.sh/uv/)
[![Tests](https://github.com/gustavo-meilus/logseq-api-mcp/workflows/Test%20Suite/badge.svg)](https://github.com/gustavo-meilus/logseq-api-mcp/actions/workflows/test.yml)
[![Quality](https://github.com/gustavo-meilus/logseq-api-mcp/workflows/Code%20Quality%20%26%20Security/badge.svg)](https://github.com/gustavo-meilus/logseq-api-mcp/actions/workflows/quality.yml)
[![PR Validation](https://github.com/gustavo-meilus/logseq-api-mcp/workflows/Pull%20Request%20Validation/badge.svg)](https://github.com/gustavo-meilus/logseq-api-mcp/actions/workflows/pr-validation.yml)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Available Tools](#available-tools)
- [Tool Details & Examples](#tool-details--examples)
- [Usage Examples](#usage-examples)
- [Development](#development)
- [Adding New Tools](#adding-new-tools)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Logseq API MCP Server provides seamless integration between [Model Context Protocol](https://modelcontextprotocol.io/) clients and [Logseq](https://logseq.com/) knowledge bases. This server enables AI assistants and other MCP clients to interact with your Logseq notes, extract educational content, analyze knowledge relationships, and work with structured information through a comprehensive set of specialized tools.

**🚀 Key Innovation**: Features a **dynamic tool discovery system** that automatically detects, imports, and registers any new tools added to the `src/tools/` directory - **zero configuration required**!

Perfect for:

- 📚 **Educational Content Management** - Extract and organize flashcards and study materials
- 🎓 **Learning Systems** - Build AI-powered study assistants and spaced repetition tools
- 🔍 **Knowledge Base Analysis** - Discover relationships and patterns in your notes
- 📊 **Content Discovery** - Navigate complex knowledge graphs with AI assistance
- 🧠 **Academic Research** - Analyze course materials and learning resources

## Features

### 🛠️ Core Tools (10 Available)

#### Read Operations

1. **`get_all_pages`** - Complete page listing with metadata
2. **`get_page_blocks`** - Hierarchical block structure analysis
3. **`get_page_links`** - Page relationship and reference discovery
4. **`get_block_content`** - Detailed block content with children
5. **`get_all_page_content`** - Comprehensive page content extraction
6. **`get_linked_flashcards`** - Advanced flashcard collection and analysis

#### Write Operations

7. **`append_block_in_page`** - Append blocks to pages with positioning options
8. **`create_page`** - Create new pages with properties and format
9. **`update_block`** - Update existing block content and properties directly (no UI focus required)
10. **`insert_block`** - Insert blocks as children or siblings of existing blocks
11. **`remove_block`** - Remove a block permanently by UUID

### 🔄 Dynamic Tool Discovery

- **Auto-Discovery** - Automatically finds and imports tools from `src/tools/`
- **Zero Configuration** - No manual imports or registrations needed
- **Instant Integration** - New tools are immediately available
- **CI Validation** - Automated testing ensures all tools work correctly

### 🎯 Optimized for AI/LLM Consumption

- **Clean Structured Output** - Emoji-enhanced, hierarchical formatting
- **Educational Content Focus** - Specialized flashcard and learning material extraction
- **Comprehensive Metadata** - Block IDs, UUIDs, timestamps, properties, and relationships
- **Smart Content Organization** - Automatic categorization and summary generation
- **Language Agnostic** - Works with any Logseq knowledge base language

## Installation

### Prerequisites

- **Python 3.11+** - Modern Python with async/await support
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package manager and project management
- **Running Logseq instance** with API enabled
- **Logseq API token** for authentication

### Quick Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/gustavo-meilus/logseq-api-mcp.git
   cd logseq-api-mcp
   ```

2. **Install with uv**

   ```bash
   uv sync
   ```

3. **Configure environment**

   ```bash
   cp .env.template .env
   # Edit .env with your Logseq API details
   ```

4. **Start the server**
   ```bash
   uv run mcp run src/server.py
   ```

## Configuration

Create a `.env` file in the project root:

```env
# Logseq API Configuration
LOGSEQ_API_ENDPOINT=http://127.0.0.1:12315/api
LOGSEQ_API_TOKEN=your_api_token_here
```

### Getting Your Logseq API Token

1. Open Logseq application
2. Go to **Settings → Features → Developer mode**
3. Enable **"HTTP APIs server"**
4. Copy the displayed API token
5. Note the API endpoint (default: `http://127.0.0.1:12315/api`)
6. Activate the API

## Available Tools

| Tool                    | Description                             | Output                               | Best For                       |
| ----------------------- | --------------------------------------- | ------------------------------------ | ------------------------------ |
| `get_all_pages`         | Lists all pages with essential metadata | 568 pages (135 journal, 433 regular) | Navigation, page discovery     |
| `get_page_blocks`       | Hierarchical block tree structure       | Multi-level tree with IDs, UUIDs     | Structure analysis, navigation |
| `get_page_links`        | Pages linking to target page            | Reference analysis with metadata     | Relationship discovery         |
| `get_block_content`     | Detailed block info with children       | Block content + immediate children   | Deep content analysis          |
| `get_all_page_content`  | Complete page content + references      | Full content with linked sources     | Comprehensive content review   |
| `get_linked_flashcards` | Flashcards from page + linked pages     | 20 flashcards across 2 pages         | Study material extraction      |
| `append_block_in_page`  | Append blocks to pages with positioning | Success confirmation with details    | Content creation, organization |
| `create_page`           | Create new pages with properties        | Page creation confirmation           | Page management, structure     |
| `update_block`          | Update block content/properties headlessly | Update confirmation with changes  | Content modification, updates  |
| `insert_block`          | Insert blocks as children or siblings   | Insert confirmation with new UUID    | Nested content, hierarchy      |
| `remove_block`          | Remove a block permanently by UUID      | Removal confirmation                 | Cleanup, delete outdated content |

## Tool Details & Examples

### 🗂️ `get_all_pages`

**Purpose:** Get a clean listing of all pages in your knowledge base

**Output Format:**

```
📊 LOGSEQ PAGES LISTING
📈 Total pages: 568
📅 Journal pages: 135
📄 Regular pages: 433

📄 REGULAR PAGES:
📄 Domain Driven Design (DDD) I | ID: 3460 | UUID: 682cfd19-7df6-46e0-a6f3-c09eca3b2530
📄 MBA Engenharia de Software | ID: 170 | UUID: 682fa28c-a3cc-47f2-ae65-7b7db57e1d67
```

**Use Cases:**

- Knowledge base exploration
- Page inventory and organization
- Finding specific pages by name or metadata

---

### 🌳 `get_page_blocks`

**Purpose:** Get hierarchical block structure of any page

**Example Input:** `"Domain Driven Design (DDD) I"`

**Output Features:**

- Tree structure with indentation levels
- Block IDs, UUIDs, and parent-child relationships
- Property extraction and metadata
- Multi-level hierarchy support (up to 8+ levels)

**Sample Output:**

```
🌳 PAGE BLOCKS TREE STRUCTURE
📄 Page: Domain Driven Design (DDD) I (ID: 3460)
📊 Total blocks: 1

📋 tipo:: #aula curso:: [[MBA Engenharia de Software]]
   📊 ID:3544 | UUID:682cfd19-2826-46b7-8222-0821b11abc60 | Level:1
   👇 Children: 7

  H1 # Flashcards [heading: 1]
     📊 ID:3552 | UUID:682cfd19-4c9c-40dd-8cb1-c2625315b8ae | Level:2
     👇 Children: 10
```

---

### 🔗 `get_page_links`

**Purpose:** Find all pages that link to a target page

**Example Result for "Domain Driven Design (DDD) I":**

```
🔗 PAGE LINKS ANALYSIS
📄 Target Page: Domain Driven Design (DDD) I
📊 Found 1 pages linking to this page

📄 1. Domain Driven Design (DDD) II
   🔑 ID: 3588 | UUID: 682cfd19-3a24-4636-a5d5-c62ea57d352e
   📊 References: 1 | Journal: No
   ⚙️ Properties: relacionado: Domain Driven Design (DDD) I
```

**Applications:**

- Discover related content and cross-references
- Build knowledge maps and relationship graphs
- Find course sequences and learning paths

---

### 🔍 `get_block_content`

**Purpose:** Get detailed information about a specific block and its immediate children

**Example Input:** UUID `682cfd19-3c3f-427c-a0be-c5a3a197ea20`

**Output:**

```
🔍 MAIN BLOCK
📌 Block ID: 3465
🔑 UUID: 682cfd19-3c3f-427c-a0be-c5a3a197ea20

📝 CONTENT:
💡 Flashcard
Por que o DDD prioriza a colaboração entre desenvolvedores e especialistas do domínio? #card
+ [ ] Porque os especialistas do domínio são responsáveis apenas por aprovar a infraestrutura tecnológica.
+ [ ] Para garantir que o software seja construído com base no conhecimento profundo do domínio, reduzindo ambiguidades e erros.

👶 IMMEDIATE CHILDREN:
🔸 CHILD 1:
Resposta Correta: Para garantir que o software seja construído com base no conhecimento profundo do domínio, reduzindo ambiguidades e erros.
```

---

### 📖 `get_all_page_content`

**Purpose:** Extract comprehensive content from a page including properties, blocks, and linked references

**Key Features:**

- Complete hierarchical content structure
- Property extraction and formatting
- Flashcard identification and extraction
- Linked references analysis
- Educational content optimization

**Example Summary:**

```
📖 Domain Driven Design (DDD) I
📊 1 blocks | 1 linked sources

📄 COMPREHENSIVE CONTENT:
📄 Page Properties [3544]
   📋 curso: MBA Engenharia de Software | tipo: aula | professor: Guilherme Bezerra de Lima

🎯 # Flashcards [3552]
   💡 Flashcard [3465]
      ❓ Q: Por que o DDD prioriza a colaboração entre desenvolvedores e especialistas do domínio?
```

---

### ✏️ `append_block_in_page`

**Purpose:** Append new blocks to any page with precise positioning control

**Key Features:**

- **Positioning Options** - Insert before specific blocks, as siblings, or at page end
- **Page-level Blocks** - Support for page-level block creation
- **Content Flexibility** - Support for any text content including markdown
- **Immediate Feedback** - Detailed confirmation with positioning information

**Example Usage:**

```python
# Basic block append
await append_block_in_page("My Page", "New content here")

# Positioned before specific block
await append_block_in_page("My Page", "Important note", before="block-uuid-123")

# As sibling of another block
await append_block_in_page("My Page", "Related content", sibling="block-uuid-456")

# Page-level block
await append_block_in_page("My Page", "Page property", is_page_block=True)
```

**Output Example:**

```
✅ **BLOCK APPENDED SUCCESSFULLY**
📄 Page: My Page
📝 Content: New content here
📍 Positioned: At the end of the page
🔗 **NEXT STEPS:**
• Check your Logseq graph to see the new block
• Use get_page_blocks to verify the block was added
• Use get_block_content to get details of the new block
```

---

### 📄 `create_page`

**Purpose:** Create new pages with custom properties and formatting

**Key Features:**

- **Property Support** - Add custom properties and metadata
- **Format Options** - Support for markdown and org formats
- **Journal Detection** - Automatic journal page recognition
- **Comprehensive Metadata** - Full page entity information

**Example Usage:**

```python
# Basic page creation
await create_page("New Page")

# With properties
properties = {"status": "active", "priority": "high"}
await create_page("Project Page", properties=properties)

# With format specification
await create_page("Org Page", format="org")

# Complete page with all options
await create_page("Complete Page", properties=properties, format="markdown")
```

**Output Example:**

```
✅ **PAGE CREATED SUCCESSFULLY**
📄 Page: New Page
⚙️ Properties set: 2 items
📝 Format: markdown
🔗 **NEXT STEPS:**
• Check your Logseq graph to see the new page
• Use get_all_pages to verify the page was created
• Use get_page_blocks to start adding content
```

---

### ✏️ `update_block`

**Purpose:** Update a block's content and properties directly via the Logseq data layer — no UI focus required

**Key Features:**

- **Headless Updates** - Uses `logseq.Editor.updateBlock`; works without the Logseq window in focus
- **Content Editing** - Replace block content with new Markdown
- **Property Management** - Optionally set block properties alongside the content update

**Example Usage:**

```python
# Update content only
await update_block("block-uuid-123", content="Updated content")

# Update content and properties
properties = {"status": "completed", "priority": "high"}
await update_block("block-uuid-123", content="Updated content", properties=properties)
```

**Output Example:**

```
✅ **BLOCK UPDATED SUCCESSFULLY**
🔗 Block UUID: block-uuid-123
📝 **UPDATED CONTENT:**
Updated content
⚙️ **UPDATED PROPERTIES:**
• status: completed
• priority: high
🔗 **NEXT STEPS:**
• Use get_block_content to verify the changes
• Use get_page_blocks to see the block in context
```

---

### 🗑️ `remove_block`

**Purpose:** Permanently remove a block from the Logseq graph by UUID

**Key Features:**

- **Headless Deletion** - Uses `logseq.Editor.removeBlock`; works without the Logseq window in focus
- **Irreversible** - Deletes the block and any child blocks from the data layer

**Example Usage:**

```python
await remove_block("block-uuid-123")
```

**Output Example:**

```
✅ **BLOCK REMOVED SUCCESSFULLY**
🗑️ Block UUID: block-uuid-123

🔗 **NEXT STEPS:**
• Use get_page_blocks to confirm the block is gone
• Use get_all_pages to review the affected page
```

---

### 📦 `insert_block`

**Purpose:** Insert a new block as a child (indented) or sibling of any existing block, enabling nested hierarchical structures

**Key Features:**

- **Child Blocks** - Insert indented blocks under any parent (default behavior)
- **Sibling Blocks** - Insert at the same level as the reference block
- **Position Control** - Insert before or after the reference block
- **Property Support** - Set block properties on creation

**Example Usage:**

```python
# Insert as child (indented under parent block)
await insert_block("parent-block-uuid", "Indented content")

# Insert as sibling (same level)
await insert_block("block-uuid", "Same level content", sibling=True)

# Insert before the reference block as sibling
await insert_block("block-uuid", "Before content", sibling=True, before=True)

# Insert as first child of a block
await insert_block("parent-uuid", "First child", before=True)

# Insert with properties
await insert_block("parent-uuid", "Tagged content", properties={"status": "active"})
```

**Output Example:**

```
✅ **BLOCK INSERTED SUCCESSFULLY**
🔑 New block UUID: 682cfd19-xxxx-xxxx-xxxx-xxxxxxxxxxxx
🆔 New block ID: 3600
📝 Content: Indented content
📍 Inserted as last child of: parent-block-uuid
🔗 **NEXT STEPS:**
• Use insert_block with this UUID to add children under it
• Use get_block_content to verify the new block
• Use get_page_blocks to see the updated hierarchy
```

---

### 🧠 `get_linked_flashcards`

**Purpose:** Comprehensive flashcard extraction from target page and all linked pages

**Real Example Results for "Domain Driven Design (DDD) I":**

```
🎯 LINKED FLASHCARDS ANALYSIS
📄 Target Page: Domain Driven Design (DDD) I
🔗 Searched 2 pages (target + 1 linked)
💡 Found 20 flashcards total

📚 Domain Driven Design (DDD) I (10 flashcards)
📚 Domain Driven Design (DDD) II (10 flashcards)

📊 SUMMARY:
• Total flashcards: 20
• Total answer blocks: 0
• Pages with flashcards: 2
• Average answers per flashcard: 0.0
```

**Advanced Features:**

- Multi-choice question support
- Answer block extraction and linking
- Cross-page flashcard discovery
- Educational metadata preservation
- Learning system integration ready

## Usage Examples

Add to your Claude Desktop MCP settings (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "logseq-api": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/logseq-api-mcp",
        "python",
        "src/server.py"
      ],
      "env": {
        "LOGSEQ_API_ENDPOINT": "http://127.0.0.1:12315/api",
        "LOGSEQ_API_TOKEN": "your_token_here"
      }
    }
  }
}
```

**Note:** Replace `/path/to/logseq-api-mcp` with the actual path to your cloned repository.

## Development

### Project Structure

```
logseq-api-mcp/
├── .github/
│   ├── workflows/             # GitHub Actions CI/CD
│   │   ├── test.yml           # Main test suite
│   │   ├── pr-validation.yml  # PR validation
│   │   ├── comprehensive-test.yml # Extended testing
│   │   └── quality.yml        # Code quality & security
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── pull_request_template.md # PR template
├── src/
│   ├── server.py              # MCP server implementation
│   ├── registry.py            # Dynamic tool discovery & registration
│   └── tools/                 # Tool implementations (auto-discovered)
│       ├── __init__.py        # Dynamic tool importer
│       ├── get_all_pages.py   # Page listing tool
│       ├── get_page_blocks.py # Block structure tool
│       ├── get_page_links.py  # Page links tool
│       ├── get_block_content.py # Block detail tool
│       ├── get_all_page_content.py # Complete content tool
│       ├── get_linked_flashcards.py # Flashcard extraction tool
│       ├── append_block_in_page.py # Block creation tool
│       ├── create_page.py     # Page creation tool
│       ├── update_block.py    # Block update tool (headless)
│       ├── insert_block.py    # Block insertion tool (child/sibling)
│       └── remove_block.py    # Block removal tool
├── tests/
│   ├── conftest.py            # Shared test fixtures
│   ├── test_append_block_in_page.py # Block creation tests
│   ├── test_create_page.py    # Page creation tests
│   ├── test_update_block.py   # Block update tests
│   ├── test_remove_block.py   # Block removal tests
│   ├── test_get_tools.py      # Read operation tests
│   ├── test_mcp_server.py     # Server validation tests
│   ├── test_runner.py         # Test runner utility
│   └── TEST_SUMMARY.md        # Test documentation
├── pyproject.toml             # UV project configuration
├── .env.template              # Environment template
└── README.md                  # This file
```

### Development Setup

```bash
# Install with development dependencies
uv sync --dev

# Format code (auto-fixes issues)
uv run ruff check --fix && uv run ruff format

# Test server with MCP inspector
uv run mcp dev src/server.py

# Run server directly
uv run mcp run src/server.py
```

## Adding New Tools

Thanks to the **dynamic discovery system**, adding new tools is incredibly simple:

### 1. Create Your Tool File

Create `src/tools/your_new_tool.py`:

```python
def your_new_tool(param: str) -> dict:
    """
    Your tool description here.

    Args:
        param: Description of parameter

    Returns:
        Dict with tool results
    """
    return {
        "result": f"Processed: {param}",
        "status": "success"
    }
```

### 2. That's It! 🎉

The system automatically:

- ✅ **Discovers** your tool file
- ✅ **Imports** the function
- ✅ **Registers** it with the MCP server
- ✅ **Validates** it in CI tests

### Tool Requirements

- **File location**: Must be in `src/tools/` directory
- **Function visibility**: Don't start function names with `_`
- **File naming**: Don't start filenames with `_`
- **Documentation**: Include docstring with description
- **Type hints**: Use for better IDE support

### Dynamic Discovery Process

```
New Tool File → Auto-Scan → Import → Registration → Validation
```

1. **Auto-Scan**: `src/tools/__init__.py` scans directory for `.py` files
2. **Import**: Dynamically imports all public functions
3. **Registration**: `src/registry.py` auto-registers with MCP server
4. **Validation**: Tests automatically verify tool presence

## Testing

### Automated Testing

The project includes comprehensive automated testing with **68 test cases** covering all functionality:

```bash
# Run the full test suite
uv run pytest tests/ --cov=src/tools --cov-report=html

# Run specific tool tests
uv run python tests/test_runner.py --tool append_block_in_page
uv run python tests/test_runner.py --tool create_page
uv run python tests/test_runner.py --tool update_block

# Run server validation
uv run python tests/test_mcp_server.py
```

**Test Coverage:**

- ✅ **68 Test Cases** - Comprehensive coverage of all 10 tools
- ✅ **Server Health** - Ensures MCP server starts correctly
- ✅ **Tool Discovery** - Validates automatic tool detection
- ✅ **Dynamic Registration** - Confirms all tools are registered
- ✅ **Write Operations** - Tests for append, create, and edit tools
- ✅ **Read Operations** - Tests for all get\_\* tools
- ✅ **Error Handling** - HTTP errors, network issues, edge cases
- ✅ **CI Integration** - Runs automatically on all commits
- ✅ **Coverage Reporting** - 80% minimum coverage requirement

### Manual Testing

```bash
# Test with MCP Inspector (interactive)
uv run mcp dev src/server.py

# Direct server testing
uv run mcp run src/server.py
```

### Test Output Example

```
🔍 Testing MCP Server Health and Tools...
🔧 Discovered tools (auto-discovery): ['append_block_in_page', 'create_page', 'get_all_page_content', 'get_all_pages', 'get_block_content', 'get_linked_flashcards', 'get_page_blocks', 'get_page_links', 'insert_block', 'remove_block', 'update_block']

🏥 Testing server health...
✅ Server started and responded successfully
✅ Dynamic tool discovery working correctly

🎉 MCP Server test completed successfully!
   📊 Tools auto-discovered: 10
   🏥 Server health: OK
   🔄 Dynamic discovery: OK
```

## CI/CD Pipeline

The project includes a comprehensive CI/CD pipeline with automated testing, code quality checks, and security scanning.

### 🚀 **Automated Workflows**

#### **Pull Request Validation**

- ✅ **Test Coverage** - 80% minimum coverage requirement
- ✅ **Code Quality** - Ruff linting and MyPy type checking
- ✅ **Security Scanning** - Bandit security analysis
- ✅ **Tool Discovery** - Automated tool validation
- ✅ **MCP Server Testing** - Server startup and functionality tests

#### **Main Test Suite**

- ✅ **Multi-Python Testing** - Python 3.11, 3.12, and 3.13
- ✅ **Cross-Platform** - Ubuntu, Windows, and macOS
- ✅ **Performance Testing** - Memory usage and test duration
- ✅ **Integration Testing** - Real MCP server with tools

#### **Code Quality & Security**

- ✅ **Daily Security Scans** - Automated vulnerability detection
- ✅ **Dependency Checking** - Safety and license validation
- ✅ **Code Standards** - Automated formatting and linting
- ✅ **Secret Detection** - Hardcoded credential scanning

### 📊 **Quality Gates**

All workflows must pass for:

- ✅ Code to be merged to main
- ✅ Releases to be published
- ✅ PRs to be approved

### 🔧 **Local Testing**

Run the same checks locally:

```bash
# Install dependencies
uv sync --dev

# Run tests with coverage
uv run pytest tests/ --cov=src/tools --cov-report=html

# Run linting
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/

# Run type checking
uv run mypy src/ --ignore-missing-imports

# Run security scan
uv run bandit -r src/

# Run dependency check
uv run safety check
```

### 📈 **Coverage Requirements**

- **Minimum Coverage:** 80% for PR validation
- **Target Coverage:** 85% for comprehensive testing
- **Coverage Tools:** pytest-cov with HTML and XML reports

### 🛡️ **Security Features**

- **Bandit** - Python security linter
- **Safety** - Dependency vulnerability scanner
- **Secret Detection** - Hardcoded credential detection
- **License Check** - Dependency license validation

## Contributing

We follow **GitHub Flow** for all contributions. See [CONTRIBUTING.md](CONTRIBUTING.md) for complete details.

### Quick Start

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/add-search-tool
   ```
3. **Create your tool** (just add the file - automatic integration!)
   ```bash
   # Create src/tools/search_tool.py with your function
   ```
4. **Format and test**
   ```bash
   uv run ruff check --fix && uv run ruff format
   uv run python tests/test_mcp_server.py
   ```
5. **Commit and push**
   ```bash
   git commit -m "feat: add search tool for content discovery"
   git push origin feature/add-search-tool
   ```
6. **Open a Pull Request**

### Development Benefits

- **Zero Configuration** - No manual imports or registrations
- **Instant Feedback** - Tools work immediately after creation
- **Automated Validation** - CI tests verify everything works
- **Clean Architecture** - Dynamic system keeps code organized
- **Comprehensive Testing** - 68 test cases with 80% coverage
- **Quality Assurance** - Automated linting, type checking, and security
- **CI/CD Pipeline** - Automated testing on every PR and push

### Code Quality Standards

- **Python 3.11+** with modern async/await patterns
- **PEP 8** compliance via Ruff formatting
- **Type hints** for better IDE support
- **Error handling** with comprehensive exception management
- **Environment variables** for configuration
- **Modular design** with dynamic tool loading

## Documentation & Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Logseq API Documentation](https://logseq.github.io/plugins/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [UV Package Manager](https://docs.astral.sh/uv/)
- [Testing Documentation](tests/README.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/) for the excellent protocol specification
- [Logseq](https://logseq.com/) for the powerful knowledge management platform
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) for the robust development framework
- [UV](https://docs.astral.sh/uv/) for modern Python package management

---

**Made for the Logseq and MCP communities**
