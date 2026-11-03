const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:2});
for(const f of process.argv.slice(2)){const s=require('fs').readFileSync(f,'utf8');await p.setContent('<body style="margin:0">'+s+'</body>');await (await p.$('svg')).screenshot({path:f.replace('.svg','.png')});}
await b.close();})();
