# Phase 1 — Project Setup & Basic IDE

## 1. Clone the repository
```bash
git clone https://github.com/vyasanbmathew2008/PyGravity.git
cd PyGravity
```

## 2. Create Python virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Create folders
```bash
mkdir -p backend
mkdir -p frontend/css
mkdir -p frontend/js
mkdir -p frontend/assets
mkdir -p tests
```

## 4. Create files
```bash
touch backend/__init__.py
 touch backend/main.py
 touch frontend/index.html
 touch frontend/css/style.css
 touch frontend/js/app.js
 touch requirements.txt
 touch .gitignore
```

## 5. Install dependencies
Add to `requirements.txt`:

```text
fastapi
uvicorn
```

Then:

```bash
pip install -r requirements.txt
```

## 6. Create the FastAPI server
Create the basic server in:

```text
backend/main.py
```

The server should:

- Start on localhost.
- Serve the frontend.
- Use the current working directory as the workspace.

## 7. Create the basic IDE UI
Build the interface in:

```text
frontend/index.html
frontend/css/style.css
frontend/js/app.js
```

Create:

```text
Top bar
Explorer
Editor
AI panel placeholder
Status bar
```

## 8. Add current-directory workspace
When running:

```bash
cd ~/Projects/myapp
pygravity
```

The workspace must be:

```text
~/Projects/myapp
```

Do not copy the project files elsewhere.

## 9. Create the file explorer backend
Add APIs for:

- List files.
- List folders.
- Read files.
- Create files.
- Create folders.
- Rename files/folders.
- Delete files/folders.

## 10. Connect the Explorer
Display the workspace files and folders in the browser.

## 11. Add Monaco Editor
Integrate Monaco Editor.

Initially support:

```text
HTML
CSS
JavaScript
TypeScript
JSX
TSX
JSON
Python
Markdown
```

## 12. Open and edit files
Clicking a file should:

```text
Explorer → Backend → File → Monaco Editor
```

## 13. Save files
Implement:

```text
Ctrl + S → Backend → Save to project
```

## 14. Add editor tabs
Implement:

- Open tab.
- Switch tab.
- Close tab.
- Unsaved indicator.
- Unsaved-change warning.

## 15. Add file operations
Add UI actions:

```text
New File
New Folder
Rename
Delete
Refresh
```

## 16. Add search
Implement:

- File-name search.
- File-content search.

## 17. Add filesystem security
Only allow operations inside the selected workspace.

Block paths that attempt to access files outside the workspace.

## 18. Test
Test with:

```text
HTML/CSS/JS
React + Vite
Node.js
Angular
TypeScript
```

Check:

- Start server.
- Open project.
- Browse files.
- Open files.
- Edit files.
- Save files.
- Create files/folders.
- Rename.
- Delete.
- Multiple tabs.
- Search.

## 19. Test in proot-distro
Run PyGravity inside:

```text
Termux → proot-distro → Ubuntu
```

Make sure the browser can connect to the local server.

## 20. Commit Phase 1
```bash
git add .
git commit -m "feat: build phase 1 basic IDE"
git push
```

## Phase 1 Result

```bash
cd ~/Projects/my-react-app
pygravity
```

should open a browser-based IDE where the actual project files can be browsed and edited.

Do not add OpenRouter, AI agent, integrated terminal, npm execution, or live preview until Phase 1 is complete.
