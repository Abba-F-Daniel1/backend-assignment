document.addEventListener('DOMContentLoaded', function () {
  const terminal = document.getElementById('terminal');
  const output = document.getElementById('terminal-output');
  const input = document.getElementById('terminal-input');
  const history = [];
  let historyIndex = -1;

  input.addEventListener('keydown', async function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      const command = input.value.trim();

      // Add command to output
      appendOutput(`➜ ${command}`);

      if (command) {
        history.push(command);
        historyIndex = history.length;

        try {
          const response = await fetch('/api/command', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command: command }),
          });

          const data = await response.json();

          if (data.response === 'clear') {
            output.innerHTML = '';
          } else {
            appendOutput(data.response);
          }
        } catch (error) {
          appendOutput('Error: Could not process command', 'error');
        }
      }

      input.value = '';
      terminal.scrollTop = terminal.scrollHeight;
    }
    else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex > 0) {
        historyIndex--;
        input.value = history[historyIndex];
      }
    }
    else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex < history.length - 1) {
        historyIndex++;
        input.value = history[historyIndex];
      } else {
        historyIndex = history.length;
        input.value = '';
      }
    }
  });

  function appendOutput(text, className = '') {
    const line = document.createElement('div');
    line.className = `output-line ${className}`;
    line.textContent = text;
    output.appendChild(line);
  }

  // Focus input when clicking anywhere in terminal
  terminal.addEventListener('click', function () {
    input.focus();
  });
}); 