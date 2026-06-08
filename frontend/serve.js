const http = require("http");
const fs   = require("fs");
const path = require("path");

const PORT = 5500;
const API = process.env.API;
const DIR  = __dirname;

const MIME = {
  ".html": "text/html",
  ".css":  "text/css",
  ".js":   "application/javascript",
};

http.createServer((req, res) => {
  // Strip query string
  let urlPath = req.url.split("?")[0];

  // Try exact file first
  let filePath = path.join(DIR, urlPath);

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath);
    res.writeHead(200, { "Content-Type": MIME[ext] || "text/plain" });
    fs.createReadStream(filePath).pipe(res);
    return;
  }

  // Try appending .html
  if (fs.existsSync(filePath + ".html")) {
    res.writeHead(200, { "Content-Type": "text/html" });
    fs.createReadStream(filePath + ".html").pipe(res);
    return;
  }

  // Everything else → 404.html (this is where shortcodes land)
  res.writeHead(200, { "Content-Type": "text/html" });
  fs.createReadStream(path.join(DIR, "404.html")).pipe(res);

}).listen(PORT, () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});