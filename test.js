let users = JSON.parse(localStorage.getItem('bakura_social')||'[]');
let vids = JSON.parse(localStorage.getItem('bakura_vids')||'[]');
let cur = JSON.parse(localStorage.getItem('bakura_cur')||'null');
let boosts = JSON.parse(localStorage.getItem('boosts')||'[]');
function go(id){document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));document.getElementById(id).classList.add('active'); if(id==='p-admin')renderAdmin();}
function setAuth(t,el){document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));el.classList.add('active');document.querySelectorAll('.form').forEach(f=>f.classList.remove('active'));document.getElementById(t==='reg'?'f-reg':'f-log').classList.add('active');}
function tog(id,el){let i=document.getElementById(id); i.type=i.type==='password'?'text':'password';}
function openM(id){document.getElementById(id).classList.add('active'); if(id==='profileM')loadProfile();}
function closeM(id){document.getElementById(id).classList.remove('active');}
if(cur){ go('p-main'); setTimeout(renderFeed,200); }

document.getElementById('f-reg').addEventListener('submit',e=>{
 e.preventDefault();
 let name=document.getElementById('rName').value;
 let gender=document.getElementById('rGender').value;
 let p1=document.getElementById('rP1').value,p2=document.getElementById('rP2').value;
 if(p1!==p2)return alert('Passwords not match'); if(!gender)return alert('Select Gender');
 let phone=document.getElementById('ccR').value+document.getElementById('rPhone').value;
 if(users.find(u=>u.phone===phone))return alert('Exists');
 let u={name, gender, phone, pass:p1, id:phone, created:Date.now(),last:Date.now(),blue:false};
 users.push(u); localStorage.setItem('bakura_social',JSON.stringify(users)); localStorage.setItem('bakura_cur',JSON.stringify(u)); location.reload();
});
document.getElementById('f-log').addEventListener('submit',e=>{
 e.preventDefault(); let phone=document.getElementById('ccL').value+document.getElementById('lId').value; let id=document.getElementById('lId').value; let p=document.getElementById('lPass').value;
 let f=users.find(u=>(u.phone===phone||u.id===id)&&u.pass===p); if(!f)return alert('Wrong');
 f.last=Date.now(); localStorage.setItem('bakura_social',JSON.stringify(users)); localStorage.setItem('bakura_cur',JSON.stringify(f)); go('p-main'); renderFeed();
});
function newVid(inp){ let file=inp.files[0]; if(!file)return; let url=URL.createObjectURL(file); vids.unshift({id:Date.now(),url,owner:cur.phone,name:cur.name,title:cur.name+' video',likes:0,verified:false}); localStorage.setItem('bakura_vids',JSON.stringify(vids)); renderFeed();}
function renderFeed(){ let f=document.getElementById('feed'); f.innerHTML=''; let show=vids.filter(v=>v.verified||v.owner===cur.phone); if(!show.length){f.innerHTML='<div style="padding:70px;text-align:center;color:#555">No videos<br>Tap + to upload</div>';return;} show.forEach(v=>{ f.innerHTML+=`<div class="tik"><video src="${v.url}" loop playsinline autoplay muted onclick="this.paused?this.play():this.pause()"></video><div class="tik-info"><b>${v.name||v.owner} ${users.find(u=>u.phone===v.owner)?.blue?'✓':''}</b><p style="color:#aaa">${v.title}</p></div><div class="tik-acts"><div onclick="like(${v.id})">❤️<br><small>${v.likes}</small></div></div></div>`;});}
function like(id){ let v=vids.find(x=>x.id===id); v.likes++; localStorage.setItem('bakura_vids',JSON.stringify(vids)); renderFeed();}
function loadProfile(){ document.getElementById('pName').innerText=cur.name; document.getElementById('pGender').innerText=cur.gender; document.getElementById('pPhone').innerText=cur.phone; document.getElementById('pBlue').innerText=cur.blue?'BLUE VERIFIED ✓':'Free Account';}
function logout(){ localStorage.removeItem('bakura_cur'); location.reload();}
function doBoost(){ let txn=document.getElementById('txn').value.trim(); let err=document.getElementById('boostErr'); if(txn.length<10){err.innerText='Fake ID! Min 10 chars';return;} if(boosts.find(b=>b.txn===txn)){err.innerText='ID already used!';return;} boosts.push({user:cur.phone,txn,time:new Date().toLocaleString(),status:'pending'}); localStorage.setItem('boosts',JSON.stringify(boosts)); closeM('boostM'); alert('Proof sent - Admin will verify in Palmpay app');}
function aliClick(){ let p=prompt('Enter Security Key for ALI REMOTE'); if(p==='.ALI39096617@Kali linux.'){go('p-admin');} else alert('Wrong key!');}
function renderAdmin(){ let div=document.getElementById('adminContent'); div.innerHTML=`<h4>Pending Videos</h4>`+vids.filter(v=>!v.verified).map(v=>`<div style="background:#111;border:1px solid #222;border-radius:12px;padding:10px;margin:8px 0"><video src="${v.url}" style="width:100%"></video><p>${v.name} - ${v.owner}</p><button onclick="verify(${v.id})">Verify</button> <button onclick="delV(${v.id})">Delete</button></div>`).join('')+`<h4>Users</h4>`+users.map(u=>`<div style="padding:6px 0;border-bottom:1px solid #222;font-size:12px"><b>${u.name}</b> (${u.gender}) - ${u.phone} - ${u.blue?'BLUE ✓':'FREE'} <button onclick="makeBlue('${u.phone}')">Blue</button> <button onclick="block('${u.phone}')">Block</button></div>`).join('')+`<h4>Boosts</h4>`+boosts.map((b,i)=>`<div style="font-size:12px">${b.user} - ${b.txn} - ${b.status} <button onclick="approveBoost(${i})">Approve</button> <button onclick="rejectBoost(${i})">Reject</button></div>`).join('');}
function verify(id){ let v=vids.find(x=>x.id===id); v.verified=true; v.trending=true; localStorage.setItem('bakura_vids',JSON.stringify(vids)); renderAdmin(); renderFeed();}
function delV(id){ vids=vids.filter(x=>x.id!==id); localStorage.setItem('bakura_vids',JSON.stringify(vids)); renderAdmin();}
function approveBoost(i){ let b=boosts[i]; b.status='approved'; let u=users.find(x=>x.phone===b.user); if(u)u.blue=true; localStorage.setItem('bakura_social',JSON.stringify(users)); localStorage.setItem('boosts',JSON.stringify(boosts)); renderAdmin(); alert('Blue given');}
function rejectBoost(i){ boosts[i].status='REJECTED FAKE'; localStorage.setItem('boosts',JSON.stringify(boosts)); renderAdmin();}
function block(p){ users=users.filter(u=>u.phone!==p); localStorage.setItem('bakura_social',JSON.stringify(users)); renderAdmin();}
function makeBlue(p){ let u=users.find(x=>x.phone===p); if(u){u.blue=true; localStorage.setItem('bakura_social',JSON.stringify(users)); if(cur.phone===p){cur.blue=true; localStorage.setItem('bakura_cur',JSON.stringify(cur));} renderAdmin();}}