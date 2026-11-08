const fs=require('fs'); const L=require('./lib'); const c1=require('./content1'); const c2=require('./content2');
const toc=fs.existsSync('toc.json')?JSON.parse(fs.readFileSync('toc.json')):{};
L.build({front:c1.front,body:[...c1.body,...c2.body]},toc,process.argv[2]||'out.docx',c1.cover).then(()=>{fs.writeFileSync('headings.json',JSON.stringify(L.reg.filter(r=>r.toc)));console.log('built',L.reg.length)});
