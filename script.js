const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");
menuBtn.addEventListener("click", () => sidebar.classList.toggle("open"));
document.querySelectorAll(".nav-link").forEach(link => {
  link.addEventListener("click", () => {
    document.querySelectorAll(".nav-link").forEach(item => item.classList.remove("active"));
    link.classList.add("active");
    sidebar.classList.remove("open");
  });
});

const form = document.getElementById("commandForm");
const input = document.getElementById("command");
const output = document.getElementById("terminalText");
const responses = {
  help: "Commandes disponibles : help, whoami, status, missions, clear",
  whoami: "RAMZI — étudiant, gamer et créateur. Accès personnel autorisé.",
  status: "SYSTÈME EN LIGNE // RAMZI.exe v2.0.77",
  missions: "Project: Revenge // RAMZI.exe // JAPAN.exe",
  clear: ""
};
form.addEventListener("submit", event => {
  event.preventDefault();
  const command = input.value.trim().toLowerCase();
  if (!command) return;
  const line = document.createElement("p");
  line.textContent = "> " + command;
  output.appendChild(line);
  const reply = document.createElement("p");
  reply.textContent = responses[command] ?? "Commande inconnue. Tape help pour voir les commandes.";
  if (command === "clear") output.innerHTML = "";
  else output.appendChild(reply);
  input.value = "";
  output.scrollTop = output.scrollHeight;
});
