async function loadStatus() {
  try {
    const response = await fetch('/api/status');
    const data = await response.json();
    console.log('PyGravity:', data);
  } catch (error) {
    console.error('Failed to connect to PyGravity backend:', error);
  }
}

loadStatus();
