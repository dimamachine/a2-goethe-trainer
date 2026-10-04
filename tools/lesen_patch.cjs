// Patcher: rewrite Lesen question sets to the harder "exam" standard.
// Author new content as plain JS in OVERRIDES; this merges into the existing
// pools and regenerates assets/data/lesen-tests.js (header preserved).
// Run from project root:  node tools/lesen_patch.cjs
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

// ---- OVERRIDES ----------------------------------------------------------
// Shape: { LESEN_T1_SETS: { <index>: { questions:[...] } }, ... }
// Only the listed fields on each set are replaced (shallow merge per set).
const OVERRIDES = require('./' + (process.argv[2] || 'lesen_overrides.cjs'));
// -------------------------------------------------------------------------

let patched = 0;
for (const [pool, byIdx] of Object.entries(OVERRIDES)) {
  for (const [idx, fields] of Object.entries(byIdx)) {
    Object.assign(POOLS[pool][Number(idx)], fields);
    patched++;
  }
}

// preserve original leading comment block (everything before first "window.")
const raw = fs.readFileSync(FILE, 'utf8');
const header = raw.slice(0, raw.indexOf('window.'));
let out = header;
for (const [name, arr] of Object.entries(POOLS)) {
  out += `window.${name} = ${JSON.stringify(arr, null, 2)};\n\n`;
}
fs.writeFileSync(FILE, out);
console.log('patched sets:', patched);
