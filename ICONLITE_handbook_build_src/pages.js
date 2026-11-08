const {execSync}=require('child_process'); const fs=require('fs');
const pdf=process.argv[2]; const H=JSON.parse(fs.readFileSync('headings.json'));
const n=+execSync(`pdfinfo ${pdf} | grep Pages`).toString().match(/\d+/)[0];
const norm=s=>s.replace(/\s+/g,' ').trim(); const pg=[];
for(let i=1;i<=n;i++)pg.push(norm(execSync(`pdftotext -f ${i} -l ${i} ${pdf} -`).toString()));
const tocPg=pg.findIndex(t=>t.startsWith('ICONLITE 2026 · ONT Amplicon Sequencing Handbook Contents'))+1; const toc={}; H.forEach(h=>{const k=norm(h.text); let f=0; let first=0;pg.forEach((t,i)=>{if(t.includes(k)){f=i+1;if(!first)first=i+1}}); if(f===tocPg)f=first; toc[h.text]=f?String(f):'';});
fs.writeFileSync('toc.json',JSON.stringify(toc,null,1)); console.log(n,'pages; missing:',Object.entries(toc).filter(([k,v])=>!v).map(e=>e[0]));
