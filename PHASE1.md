# PyGravity — Phase 1: Basic IDE

## Objective

Build the first working version of PyGravity: a local browser-based code editor that opens a selected project directory and lets the user browse, edit, create, rename, and delete project files.

Phase 1 does **not** include OpenRouter, AI agents, terminal execution, or live preview. The goal is to establish a reliable IDE foundation first.

---

## Phase 1 Architecture

```text
Browser
   │
   │ HTTP
   ▼
FastAPI Server
   │
   ▼
Workspace Manager
   │
   ▼
Current Project Directory
```

---

## Step 1 — Create the Python Backend

Create the basic FastAPI application.

Target structure:

```text
PyGravity/
├── backend/
│   ├── __init__.py
│   └── main.py
├── frontend/
└── requirements.txt
```

Tasks:

- Install FastAPI.
- Install Uvicorn.
- Create the FastAPI application.
- Add a basic health/status endpoint.
- Serve the frontend from the Python server.

Expected result:

```bash
python3 -m backend.main
```

Then open:

```text
http://127.0.0.1:8000
```

---

## Step 2 — Build the Basic Web Interface

Create the initial IDE layout using normal HTML, CSS, and JavaScript.

Layout:

```text
┌──────────────────────────────────────────────────────────────┐
│ PyGravity                                      Project       │
├────────────┬───────────────────────────────────┬─────────────┤
│ Explorer   │ Editor                            │ AI          │
│            │                                   │             │
│ Files      │                                   │ Coming      │
│            │                                   │ Soon        │
├────────────┴───────────────────────────────────┴─────────────┤
│ Status Bar                                                   │
└──────────────────────────────────────────────────────────────┘
```

Tasks:

- Create the main layout.
- Add Explorer panel.
- Add Editor panel.
- Add right-side AI placeholder.
- Add top toolbar.
- Add status bar.
- Make the layout responsive.
- Use a dark IDE-style theme.

---

## Step 3 — Add the Workspace System

PyGravity must work with the directory from which it is launched.

Example:

```bash
cd ~/projects/my-website
pygravity
```

The workspace becomes:

```text
~/projects/my-website/
```

Tasks:

- Determine the current working directory.
- Store it as the active workspace.
- Do not copy project source files.
- Reject filesystem paths outside the workspace.
- Handle symbolic links carefully.
- Exclude `.git` and `.pygravity` from normal file browsing where appropriate.

Security rule:

```text
Requested path
      ↓
Normalize path
      ↓
Check it is inside workspace
      ↓
Allow / Reject
```

---

## Step 4 — Build the File Explorer API

Create backend endpoints for browsing the workspace.

Initial API:

```text
GET /api/workspace
GET /api/files
GET /api/file?path=...
POST /api/file
POST /api/folder
PUT /api/file
PUT /api/rename
DELETE /api/file
```

The API should return structured JSON.

Example:

```json
{
  "name": "src",
  "type": "directory",
  "children": []
}
```

Tasks:

- List directories.
- List files.
- Read files.
- Create files.
- Create folders.
- Rename files/folders.
- Delete files/folders.
- Validate all paths.
- Return useful errors.

---

## Step 5 — Connect Explorer to the Frontend

The browser Explorer should use the filesystem API.

Tasks:

- Load the workspace tree.
- Expand/collapse folders.
- Open files by clicking them.
- Show file icons based on file type.
- Add context-menu actions later if needed.
- Refresh the tree after filesystem changes.

Example:

```text
📁 my-website
├── 📁 src
│   ├── 📄 App.jsx
│   ├── 📄 main.jsx
│   └── 📁 components
├── 📄 index.html
├── 📄 package.json
└── 📄 vite.config.js
```

---

## Step 6 — Integrate Monaco Editor

Use Monaco Editor as the main code editor.

Required capabilities:

- Line numbers.
- Syntax highlighting.
- Multiple tabs.
- File switching.
- Unsaved-change indicator.
- Basic autocomplete.
- Keyboard shortcuts.
- Language detection.

Languages to support first:

```text
HTML
CSS
JavaScript
TypeScript
JSON
JSX
TSX
Python
Markdown
```

---

## Step 7 — Open and Edit Files

When a file is selected:

```text
Explorer
   ↓
GET /api/file
   ↓
Monaco Editor
```

Tasks:

- Load file content.
- Detect language.
- Display content in Monaco.
- Track modifications.
- Show unsaved state.
- Save with Ctrl+S.
- Save through the backend API.

Expected workflow:

```text
Open App.jsx
      ↓
Edit code
      ↓
Ctrl+S
      ↓
PUT /api/file
      ↓
Saved to project directory
```

---

## Step 8 — File Management UI

Add basic project-management actions.

Required actions:

```text
New File
New Folder
Rename
Delete
Save
Refresh
```

Example:

```text
Right click src/

+ New File
+ New Folder
  Rename
  Delete
  Refresh
```

Destructive operations should require confirmation.

---

## Step 9 — Editor Tabs

Implement a VS Code-style tab system.

Example:

```text
┌────────────┬─────────────┬─────────────┐
│ App.jsx  × │ main.jsx  × │ index.html × │
└────────────┴─────────────┴─────────────┘
```

Tasks:

- Open file in a tab.
- Switch tabs.
- Close tabs.
- Preserve unsaved state.
- Warn before closing an unsaved file.
- Prevent duplicate tabs for the same file.

---

## Step 10 — Search

Add project/file search.

Phase 1 search can include:

- Search filenames.
- Search file contents.
- Case-sensitive toggle.
- Basic result navigation.

Example:

```text
Search: useState

src/App.jsx:12
src/components/Form.jsx:8
src/components/Header.jsx:4
```

---

## Step 11 — Error Handling

The IDE should not crash because a file operation fails.

Handle:

- File not found.
- Permission denied.
- Invalid path.
- Unsupported/binary file.
- File changed externally.
- Failed save.
- Malformed API request.

Display errors inside the UI rather than only in the server console.

---

## Step 12 — Phase 1 Testing

Test the IDE with different project types.

### Static website

```text
index.html
style.css
script.js
```

### React/Vite

```text
package.json
index.html
src/
```

### Node.js

```text
package.json
server.js
```

### Angular

```text
angular.json
package.json
src/
```

### Python

```text
app.py
requirements.txt
```

Test:

- Opening a project.
- Browsing nested folders.
- Opening files.
- Editing files.
- Saving files.
- Creating files.
- Creating folders.
- Renaming.
- Deleting.
- Searching.
- Opening multiple tabs.
- Reloading the browser.
- Handling invalid paths.

---

## Phase 1 Completion Criteria

Phase 1 is complete when all of the following work reliably:

- [ ] PyGravity starts from a local project directory.
- [ ] Browser UI loads successfully.
- [ ] Workspace is detected automatically.
- [ ] File explorer displays the project.
- [ ] Folders can be expanded/collapsed.
- [ ] Files can be opened.
- [ ] Monaco Editor works.
- [ ] HTML/CSS/JS/TS/JSX/TSX/JSON/Python syntax highlighting works.
- [ ] Files can be edited.
- [ ] Ctrl+S saves directly to the project.
- [ ] New files can be created.
- [ ] New folders can be created.
- [ ] Files/folders can be renamed.
- [ ] Files/folders can be deleted with confirmation.
- [ ] Multiple editor tabs work.
- [ ] Basic search works.
- [ ] Workspace path traversal is blocked.
- [ ] Errors are shown cleanly.
- [ ] The IDE works inside Termux → proot-distro → Ubuntu.

---

## What Comes After Phase 1

Do not implement these during Phase 1:

- OpenRouter
- AI chat
- AI agent
- AI file editing
- Integrated terminal
- npm execution
- Live preview
- Git UI

They belong to later phases.

The next major phase after the editor foundation is **Phase 2 — Local Filesystem and Workspace API hardening**, followed by the integrated terminal and live preview. OpenRouter should be added after the basic IDE is stable.

## Target Result

At the end of Phase 1:

```bash
cd ~/projects/my-react-app
pygravity
```

opens a browser IDE where the user can browse and edit the actual React project directly from the current directory.
