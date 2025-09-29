const input = document.getElementById("commandInput");
const output = document.getElementById("output");

const commands = {
  help: "Available commands: help, about, clear, run",
  about: "This is a simulated terminal built with HTML/CSS/JS.",
  run: "Running final project... ✅",
  clear: "clear"
};

input.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    const cmd = input.value.trim();
    processCommand(cmd);
    input.value = "";
  }
});

function processCommand(cmd) {
  if (cmd === "") return;

  appendOutput(`user@site:~$ ${cmd}`);

  if (commands[cmd]) {
    if (cmd === "clear") {
      output.innerHTML = "";
    } else {
      appendOutput(commands[cmd]);
    }
  } else {
    appendOutput(`Command not found: ${cmd}`);
  }
}

function appendOutput(text) {
  output.innerHTML += text + "\n";
}
