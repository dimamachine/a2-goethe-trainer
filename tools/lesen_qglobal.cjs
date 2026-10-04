// Global-item patcher: replaces the ENTIRE question at index 4 of T1 sets
// with a whole-text item ("Der Text informiert über ..."). Unlike lesen_qpatch,
// this intentionally rewrites correct/hint/de/ru too.
// Data: tools/lesen_qglobal_data.cjs =
//   { <setIdx>: { q, opts:[3], correct:0..2, de, ru } }   (hint is forced to 0)
// Run from project root: node tools/lesen_qglobal.cjs
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
const DATA = require('./lesen_qglobal_data.cjs');

let items = 0;
for (const [setIdx, repl] of Object.entries(DATA)) {
  const set = POOLS.LESEN_T1_SETS[Number(setIdx)];
  if (!set) throw new Error(`T1[${setIdx}] missing`);
  const q = set.questions[4];
  if (!q) throw new Error(`T1[${setIdx}] q4 missing`);
  if (!Array.isArray(repl.opts) || repl.opts.length !== 3) throw new Error(`T1[${setIdx}] opts != 3`);
  if (![0, 1, 2].includes(repl.correct)) throw new Error(`T1[${setIdx}] bad correct`);
  if (!repl.de || !repl.ru) throw new Error(`T1[${setIdx}] missing de/ru`);
  set.questions[4] = { q: repl.q, opts: repl.opts, correct: repl.correct, hint: 0, de: repl.de, ru: repl.ru };
  items++;
}

const raw = fs.readFileSync(FILE, 'utf8');
const header = raw.slice(0, raw.indexOf('window.'));
let out = header;
for (const [name, arr] of Object.entries(POOLS)) {
  out += `window.${name} = ${JSON.stringify(arr, null, 2)};\n\n`;
}
fs.writeFileSync(FILE, out);
console.log('global items set:', items);
