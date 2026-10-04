// Spread the answer keys of the Lesen MC pools (T1, T2, T3).
// They were heavily skewed to option "b" (e.g. T1: 441× b vs 48× a / 11× c, and
// 57/100 sets had all-identical keys). For each MC question we reorder `opts` so
// the SAME correct option text lands at a varied position and update `correct`.
// `hint` (a text index) and `de`/`ru` (explanations referencing the correct
// TEXT) are unaffected. T4 (letter matching) is left as-is.
//
// Re-serializes assets/data/lesen-tests.js. Source of truth = that file.
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const FILE = path.join(ROOT, 'assets', 'data', 'lesen-tests.js');

global.window = {};
require(FILE);
const w = global.window;

function balancedPattern(seed, n) {
  // length-n array over {0,1,2}; for n>=3 contains all three, else >=2 distinct
  let s = seed >>> 0;
  const rnd = () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; };
  for (let guard = 0; guard < 500; guard++) {
    const p = Array.from({ length: n }, () => Math.floor(rnd() * 3));
    const distinct = new Set(p).size;
    const counts = [0, 1, 2].map(k => p.filter(x => x === k).length);
    if (n >= 3 ? (distinct === 3 && Math.max(...counts) <= 2) : distinct >= 2) return p;
  }
  return Array.from({ length: n }, (_, i) => i % 3);
}

function moveCorrect(opts, correct, target) {
  const correctText = opts[correct];
  const rest = opts.filter((_, j) => j !== correct);
  const out = new Array(opts.length).fill(null);
  out[target] = correctText;
  let fi = 0;
  for (let k = 0; k < out.length; k++) if (out[k] === null) out[k] = rest[fi++];
  return out;
}

let fixedQ = 0, fixedSets = 0;
[['T1', w.LESEN_T1_SETS, 1], ['T2', w.LESEN_T2_SETS, 2], ['T3', w.LESEN_T3_SETS, 3]].forEach(([, arr, teilNo]) => {
  arr.forEach((set, si) => {
    const qs = set.questions || [];
    if (!qs.length) return;
    const usable = qs.filter(q => Array.isArray(q.opts) && q.opts.length === 3 && typeof q.correct === 'number');
    if (!usable.length) return;
    const pattern = balancedPattern(teilNo * 100003 + si * 31 + 7, usable.length);
    let i = 0, changed = false;
    qs.forEach(q => {
      if (!(Array.isArray(q.opts) && q.opts.length === 3 && typeof q.correct === 'number')) return;
      const target = pattern[i++];
      if (target !== q.correct) {
        q.opts = moveCorrect(q.opts, q.correct, target);
        q.correct = target;
        fixedQ++; changed = true;
      }
    });
    if (changed) fixedSets++;
  });
});

const header =
  '// Auto-generated migration: Lesen test pools extracted from lesen.html.\n' +
  '// Loaded via <script src> (works under file://; .json+fetch() would be CORS-blocked).\n' +
  '// Answer keys spread across a/b/c by tools/_fix_lesen_keys.js (content-preserving).\n\n';

const out = header +
  ['T1', 'T2', 'T3', 'T4'].map(n =>
    `window.LESEN_${n}_SETS = ${JSON.stringify(w[`LESEN_${n}_SETS`], null, 2)};\n`
  ).join('\n');

fs.writeFileSync(FILE, out, 'utf-8');
console.log(`Reordered ${fixedQ} questions across ${fixedSets} sets. Wrote ${FILE.replace(ROOT + '/', '')}.`);
