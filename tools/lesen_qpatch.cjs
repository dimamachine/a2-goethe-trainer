// Q-patcher: replace ONLY q and opts of individual questions (Satzergänzung
// conversion). correct/hint/de/ru stay untouched. Aborts if opts length != 3.
// Data: tools/lesen_qpatch_data.cjs =
//   { T1: { <setIdx>: { <qIdx>: { q: "...", opts: ["...","...","..."] } } }, T3: {...} }
// Run from project root: node tools/lesen_qpatch.cjs
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
const DATA = require('./lesen_qpatch_data.cjs');
const MAP = { T1: 'LESEN_T1_SETS', T3: 'LESEN_T3_SETS' };

let items = 0;
for (const [poolKey, bySet] of Object.entries(DATA)) {
  const pool = POOLS[MAP[poolKey]];
  for (const [setIdx, byQ] of Object.entries(bySet)) {
    const set = pool[Number(setIdx)];
    for (const [qIdx, repl] of Object.entries(byQ)) {
      const q = set.questions[Number(qIdx)];
      if (!q) throw new Error(`${poolKey}[${setIdx}] q${qIdx} missing`);
      if (!Array.isArray(repl.opts) || repl.opts.length !== 3) throw new Error(`${poolKey}[${setIdx}] q${qIdx} opts != 3`);
      q.q = repl.q;
      q.opts = repl.opts;
      items++;
    }
  }
}

const raw = fs.readFileSync(FILE, 'utf8');
const header = raw.slice(0, raw.indexOf('window.'));
let out = header;
for (const [name, arr] of Object.entries(POOLS)) {
  out += `window.${name} = ${JSON.stringify(arr, null, 2)};\n\n`;
}
fs.writeFileSync(FILE, out);
console.log('converted items:', items);
