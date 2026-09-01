# PyGravity — Development Plan

PyGravity is a local, browser-based AI coding IDE inspired by modern AI coding environments. It is designed primarily for web development and runs inside Termux → proot-distro → Ubuntu.

## Goal

Build a local AI-powered web IDE for:

- HTML
- CSS
- JavaScript
- TypeScript
- React
- Node.js
- Angular
- Vite
- Other web-development projects

The IDE uses a Python backend, a browser-based editor, OpenRouter for AI, and the selected local project directory as the workspace.

## Core Principle

When PyGravity is launched inside a project directory:

```bash
cd ~/projects/myapp
pygravity
```

PyGravity works directly with:

```text
~/projects/myapp/
```

Source files are not copied to another project database or hidden workspace.

Optional PyGravity-specific metadata can be stored inside:

```text
myapp/
└── .pygravity/
    ├── settings.json
    ├── state.json
    └── chats/
```

## Target Architecture

```text
Termux
  │
  └── proot-distro Ubuntu
        │
        └── PyGravity
              │
              ├── Python backend
              ├── Web IDE
              ├── OpenRouter AI
              ├── Local filesystem
              └── Terminal
                       │
                       ├── node
                       ├── npm
                       ├── npx
                       ├── python
                       └── other tools
```

## Main Interface

```text
┌───────────────────────────────────────────────────────────────┐
│ ⚡ PyGravity        my-website              ▶ Run       ⚙    │
├────────────┬──────────────────────────────┬───────────────────┤
│ EXPLORER   │ EDITOR                       │ AI AGENT          │
│            │                              │                   │
│ 📁 src     │ App.jsx                      │ 🤖 PyGravity AI   │
│ ├ App.jsx  │                              │                   │
│ ├ main.jsx │ 1  import React from 'react' │ Create a navbar  │
│ └ ...      │ 2                            │ for my app        │
│ 📄 package │ 3  function App() {          │                   │
│            │ 4    return (...)            │ [Send]            │
│ + New File │                              │                   │
├────────────┴──────────────────────────────┴───────────────────┤
│ TERMINAL                                                      │
│ $ npm run dev                                                 │
└───────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Backend

- Python
- FastAPI
- WebSockets
- PTY for interactive terminal sessions

### Frontend

- HTML
- CSS
- JavaScript
- Monaco Editor

### AI

- OpenRouter API
- Configurable model selection
- Streaming responses
- Project-aware context

### Storage

- Local filesystem for source code
- JSON and/or SQLite for PyGravity metadata and history

### Development Tools

- Node.js
- npm
- npx
- Git
- Python
- Framework-specific CLI tools

## Development Phases

### Phase 1 — Basic IDE

- Python server
- Web UI
- File explorer
- Create files/folders
- Delete files/folders
- Rename files/folders
- Save files
- Editor tabs
- Monaco Editor
- Search

### Phase 2 — Local Filesystem

Create a secure filesystem API:

```text
GET  /api/files
GET  /api/file
POST /api/file
PUT  /api/file
DELETE /api/file
POST /api/folder
```

The backend must restrict filesystem access to the selected workspace.

### Phase 3 — Integrated Terminal

Implement a WebSocket-based terminal using a PTY.

Example commands:

```bash
npm install
npm run dev
npx vite
node server.js
python app.py
```

Terminal output should stream live into the browser.

### Phase 4 — Project Detection

Automatically detect project types.

#### React/Vite

Detect files such as:

```text
package.json
vite.config.*
src/
```

#### Angular

```text
angular.json
package.json
```

#### Node.js

```text
package.json
server.js
```

#### Static Website

```text
index.html
style.css
script.js
```

### Phase 5 — Live Preview

Support local development servers such as:

```text
http://localhost:5173
```

Provide an integrated browser preview using an iframe where appropriate.

### Phase 6 — OpenRouter Integration

Add an AI assistant capable of:

- Code generation
- Code explanation
- Debugging
- Refactoring
- Code review
- Project analysis
- Error explanation

The API key must never be hardcoded into the repository.

### Phase 7 — AI Agent

Implement controlled project tools:

```text
list_files()
read_file()
search_files()
create_file()
edit_file()
delete_file()
rename_file()
run_command()
get_terminal_output()
```

The AI must not receive unrestricted access to the host filesystem.

### Phase 8 — Change Preview

Before applying significant AI modifications, show the user a diff:

```text
AI wants to modify:

src/App.jsx
src/App.css

+ 24 lines
- 8 lines

[Reject]    [Apply]
```

### Phase 9 — Git Integration

Add source-control functionality:

- Git status
- Git diff
- Add files
- Commit
- Branches
- Checkout
- Log

### Phase 10 — IDE Polish

Add:

- Dark/light themes
- Command palette
- Ctrl+P file search
- Ctrl+Shift+P commands
- Split editor
- Multiple terminal tabs
- Preview tabs
- Resizable panels
- Notifications
- Settings
- Keyboard shortcuts

## AI Agent Workflow

```text
User
 ↓
AI
 ↓
Select tool
 ↓
Python validates request
 ↓
Tool executes
 ↓
Result returned to AI
 ↓
AI continues
 ↓
User reviews changes
```

Example:

```text
User: Fix my React application.

AI:
1. list_files()
2. read_file("src/App.jsx")
3. read_file("src/main.jsx")
4. run_command("npm run build")
5. inspect error
6. edit_file("src/App.jsx")
7. run_command("npm run build")
8. report success
```

## Proot-distro Compatibility

PyGravity is specifically intended to run in:

```text
Termux
   ↓
proot-distro
   ↓
Ubuntu
   ↓
Python
   ↓
PyGravity
   ↓
Browser
```

The core system should use ordinary user-space technologies that work reliably under proot: Python, HTTP/WebSockets, filesystem APIs, PTYs, and user-space processes.

## Recommended Build Order

```text
Foundation
  1. Python server
  2. Web UI
  3. File explorer
  4. Monaco editor
  5. Terminal
  6. Live preview

AI
  7. OpenRouter
  8. AI chat
  9. File tools
 10. AI agent
 11. Diff/apply system
 12. Git integration
```

## MVP

The first usable milestone is:

1. Open a local project directory.
2. Browse its files.
3. Edit files with Monaco.
4. Save changes directly to the project.
5. Open an integrated terminal.
6. Run `npm run dev`.
7. View the running website in a preview.

After this foundation works reliably, implement the OpenRouter AI agent.

## Security Principles

- Never hardcode API keys.
- Restrict AI filesystem operations to the selected workspace.
- Validate paths to prevent traversal outside the workspace.
- Require user confirmation for destructive or risky operations.
- Show diffs before major AI-generated file changes.
- Do not execute arbitrary AI-generated commands without an appropriate permission mechanism.
- The application is intended for development and authorized testing only.
