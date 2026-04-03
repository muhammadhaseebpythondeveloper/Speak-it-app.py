import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Speak It", page_icon="🔊", layout="centered")

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body { background:#0f172a; color:white; font-family:sans-serif; padding:10px; }
textarea { width:100%; height:120px; }
button { padding:10px; margin:5px; background:#14b8a6; border:none; color:white; border-radius:8px; }
select, input { width:100%; margin:5px 0; }
</style>
</head>
<body>
<h3>Speak It – Paste text → listen instantly</h3>
<p><b>How to use:</b> Type text → press Play</p>

<textarea id="text" placeholder="Enter your text..."></textarea>
<p id="meta">0 characters</p>

<select id="lang">
<option value="en-US">English US</option>
<option value="en-GB">English UK</option>
<option value="ur-PK">Urdu</option>
<option value="ar-SA">Arabic</option>
<option value="hi-IN">Hindi</option>
</select>

<select id="voice"></select>

<label>Rate</label>
<input type="range" id="rate" min="0.5" max="2" step="0.1" value="1">

<label>Pitch</label>
<input type="range" id="pitch" min="0.5" max="2" step="0.1" value="1">

<label>Volume</label>
<input type="range" id="volume" min="0" max="1" step="0.1" value="1">

<br>

<button onclick="speak()">Play</button>
<button onclick="pause()">Pause</button>
<button onclick="resume()">Resume</button>
<button onclick="stop()">Stop</button>
<button onclick="clearText()">Clear</button>

<p id="status">Status: Stopped</p>

<script>
const synth = window.speechSynthesis;
let voices = [];

function loadVoices(){
  voices = synth.getVoices();
  const voiceSelect = document.getElementById("voice");
  voiceSelect.innerHTML = "";
  voices.forEach(v=>{
    let opt = document.createElement("option");
    opt.value = v.name;
    opt.textContent = v.name + " (" + v.lang + ")";
    voiceSelect.appendChild(opt);
  });
}

speechSynthesis.onvoiceschanged = loadVoices;
loadVoices();

function speak(){
  let text = document.getElementById("text").value;
  let u = new SpeechSynthesisUtterance(text);

  let vName = document.getElementById("voice").value;
  let v = voices.find(v=>v.name===vName);
  if(v) u.voice = v;

  u.rate = document.getElementById("rate").value;
  u.pitch = document.getElementById("pitch").value;
  u.volume = document.getElementById("volume").value;

  u.onstart = ()=>status("Speaking...");
  u.onend = ()=>status("Stopped");

  synth.cancel();
  synth.speak(u);
}

function pause(){ synth.pause(); status("Paused"); }
function resume(){ synth.resume(); status("Speaking..."); }
function stop(){ synth.cancel(); status("Stopped"); }

function clearText(){
  document.getElementById("text").value="";
  updateMeta();
}

function status(t){
  document.getElementById("status").innerText="Status: "+t;
}

function updateMeta(){
  let t=document.getElementById("text").value;
  document.getElementById("meta").innerText = t.length + " characters";
}

document.getElementById("text").addEventListener("input", updateMeta);
</script>

<p><b>FAQ:</b><br>No, your text is not stored. Everything runs in your browser.</p>

</body>
</html>
"""

components.html(HTML, height=800, scrolling=True)
