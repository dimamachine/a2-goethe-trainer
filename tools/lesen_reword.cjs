// Reword: replace individual sentences (and optionally title/subtitle) IN PLACE.
// Sentence count and order never change, so paragraphs and question hints stay valid.
// Data: tools/lesen_reword_data.cjs =
//   { T1: { <idx>: { title?, subtitle?, s: { <sentIdx>: "new text", ... } } }, T3: {...} }
// Run from project root: node tools/lesen_reword.cjs
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
const DATA = require('./lesen_reword_data.cjs');
const MAP = { T1: 'LESEN_T1_SETS', T3: 'LESEN_T3_SETS' };

let touched = 0;
for (const [poolKey, byIdx] of Object.entries(DATA)) {
  const pool = POOLS[MAP[poolKey]];
  for (const [idx, spec] of Object.entries(byIdx)) {
    const set = pool[Number(idx)];
    if (spec.title) set.title = spec.title;
    if (spec.subtitle) set.subtitle = spec.subtitle;
    for (const [si, text] of Object.entries(spec.s || {})) {
      if (Number(si) >= set.sentences.length) throw new Error(`T? ${idx}: sentence ${si} out of range`);
      set.sentences[Number(si)] = text;
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
console.log('reworded sets:', touched);
