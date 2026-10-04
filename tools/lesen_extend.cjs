// Extender: append NEW sentences to Teil-1 articles / Teil-3 emails to reach
// exam length, WITHOUT disturbing existing sentence indices (so question
// hints stay valid). New sentences go to the end of sentences[]; for Teil 1 a
// new paragraph group with the appended indices is added to paragraphs[].
// Author content in ./lesen_extend_data.cjs, then: node tools/lesen_extend.cjs
const fs = require('fs');
const path = require('path');
const FILE = path.join(__dirname, '..', 'assets', 'data', 'lesen-tests.js');

global.window = {};
require(FILE);
const POOLS = {
  LESEN_T1_SETS: global.window.LESEN_T1_SETS,
  LESEN_T2_SETS: global.window.LESEN_T2_SETS,
  LESEN_T3_SETS: global.window.LESEN_T3_SETS,
  LESEN_T4_SETS: global.window.LESEN_T4_SETS,
};

// { T1: { <idx>: ["neuer Satz", ...] }, T3: { <idx>: [...] } }
const DATA = require('./lesen_extend_data.cjs');
const MAP = { T1: 'LESEN_T1_SETS', T3: 'LESEN_T3_SETS' };

let touched = 0;
for (const [poolKey, byIdx] of Object.entries(DATA)) {
  const pool = POOLS[MAP[poolKey]];
  for (const [idx, newSents] of Object.entries(byIdx)) {
    if (!newSents || !newSents.length) continue;
    const set = pool[Number(idx)];
    const start = set.sentences.length;
    set.sentences.push(...newSents);
    if (Array.isArray(set.paragraphs)) {
      // chunk appended sentences into paragraphs of ~5 for readability
      for (let k = 0; k < newSents.length; k += 5) {
        const group = [];
        for (let m = k; m < Math.min(k + 5, newSents.length); m++) group.push(start + m);
        set.paragraphs.push(group);
      }
    }
    touched++;
  }
}

const raw = fs.readFileSync(FILE, 'utf8');
const header = raw.slice(0, raw.indexOf('window.'));
let out = header;
for (const [name, arr] of Object.entries(POOLS)) {
  out += `window.${name} = ${JSON.stringify(arr, null, 2)};\n\n`;
}
fs.writeFileSync(FILE, out);
console.log('extended sets:', touched);
