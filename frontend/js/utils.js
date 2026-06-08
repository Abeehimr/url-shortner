const API = "http://localhost:8000/shrtn";
const FRONTEND_API = "http://localhost:5500";
function setActiveNav() {
  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav a").forEach(a => {
    const href = a.getAttribute("href").split("/").pop();
    a.classList.toggle("active", href === path);
  });
}

function showAlert(el, msg, type = "success") {
  el.textContent = msg;
  el.className = `alert alert-${type} visible`;
}

function hideAlert(el) {
  el.className = "alert";
}

function showResult(el) {
  el.classList.add("visible");
}

function hideResult(el) {
  el.classList.remove("visible");
}

async function copyToClipboard(text, btn) {
  try {
    await navigator.clipboard.writeText(text);
    btn.textContent = "Copied!";
    btn.classList.add("copied");
    setTimeout(() => {
      btn.textContent = "Copy";
      btn.classList.remove("copied");
    }, 2000);
  } catch {
    btn.textContent = "Failed";
  }
}

document.addEventListener("DOMContentLoaded", setActiveNav);