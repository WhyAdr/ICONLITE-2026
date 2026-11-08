const d = require('docx'); const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, HeadingLevel, AlignmentType, LevelFormat, PageBreak, ImageRun, Header, Footer, PageNumber, TabStopType, LeaderType } = d;
const BLUE = '1769AA', YEL = 'EABF45', PALE = 'EAF3FA', INK = '2B2F36', GRAY = '5F6B7A', W = 9026;
const reg = [], numRefs = []; let figN = 0, tabN = 0;

function runs(t, o = {}) { return String(t).split(/(\*\*.+?\*\*|`.+?`)/).filter(x => x).map(x => x.startsWith('**') ? new TextRun({ text: x.slice(2, -2), bold: true, ...o }) : x.startsWith('`') ? new TextRun({ text: x.slice(1, -1), font: 'Courier New', size: (o.size || 21) - 2, ...o }) : new TextRun({ text: x, ...o })); }
const P = (t, o = {}) => new Paragraph({ children: runs(t), spacing: { after: 110 }, ...o });
const head = (lvl, text, toc = true, o = {}) => { reg.push({ level: lvl, text, toc }); return new Paragraph({ heading: [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3][lvl - 1], children: [new TextRun(text)], ...o }); };
const PART = t => head(1, t, true, { pageBreakBefore: true });
const CH = (t, slides) => [head(2, t, true), ...(slides ? [new Paragraph({ children: runs('Slides: ' + slides, { color: GRAY, size: 19, italics: true }), spacing: { after: 120 } })] : [])];
const SEC = (t, toc = false) => head(3, t, toc);
const B = a => a.map(t => new Paragraph({ children: runs(t), numbering: { reference: 'bul', level: 0 }, spacing: { after: 50 } }));
function N(a) { const ref = 'n' + numRefs.length; numRefs.push(ref); return a.map(t => new Paragraph({ children: runs(t), numbering: { reference: ref, level: 0 }, spacing: { after: 60 } })); }
const KIND = { warn: [YEL, 'FFF6D9', 'Checkpoint / warning'], note: [BLUE, PALE, 'Note'], F: ['2A9D8F', 'E8F5F3', 'Foundational'], A: [GRAY, 'F1F3F5', 'Advanced'], src: [GRAY, 'F1F3F5', 'Source status'] };
function CALL(kind, text, title) { const [c, f, lab] = KIND[kind]; return new Paragraph({ children: [new TextRun({ text: (title || lab) + ': ', bold: true, color: INK }), ...runs(text)], shading: { type: ShadingType.CLEAR, fill: f, color: 'auto' }, border: { left: { style: BorderStyle.SINGLE, size: 24, color: c, space: 8 } }, indent: { left: 200, right: 100 }, spacing: { before: 80, after: 140 } }); }
const cap = t => new Paragraph({ children: [new TextRun({ text: t, italics: true, size: 18, color: GRAY })], spacing: { before: 60, after: 160 } });
function T(rows, widths, o = {}) {
  const sum = widths.reduce((a, b) => a + b, 0), ws = widths.map(x => Math.round(x * W / sum)); ws[ws.length - 1] += W - ws.reduce((a, b) => a + b, 0);
  const bd = { style: BorderStyle.SINGLE, size: 4, color: 'D5DEE6' }, borders = { top: bd, bottom: bd, left: bd, right: bd };
  const tr = rows.map((r, i) => new TableRow({ tableHeader: i === 0 && o.hdr !== false, cantSplit: true, children: r.map((c, j) => new TableCell({ width: { size: ws[j], type: WidthType.DXA }, borders, margins: { top: 50, bottom: 50, left: 90, right: 90 }, shading: { type: ShadingType.CLEAR, fill: (i === 0 && o.hdr !== false) ? BLUE : (i % 2 ? 'FFFFFF' : PALE), color: 'auto' }, children: String(c).split('\n').map(l => new Paragraph({ children: runs(l, { size: o.fs || 18, color: (i === 0 && o.hdr !== false) ? 'FFFFFF' : INK, bold: (i === 0 && o.hdr !== false) ? true : undefined }) })) })) }));
  const out = []; if (o.cap) out.push(new Paragraph({ children: [new TextRun({ text: 'Table ' + (++tabN) + '. ' + o.cap, bold: true, size: 19, color: BLUE })], spacing: { before: 120, after: 60 }, keepNext: true }));
  out.push(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: ws, rows: tr })); out.push(new Paragraph({ children: [], spacing: { after: 100 } })); return out;
}
function FIG(file, caption, wIn, hIn) { const buf = fs.readFileSync(file); return [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 100, after: 40 }, keepNext: true, children: [new ImageRun({ type: 'png', data: buf, transformation: { width: wIn * 96, height: hIn * 96 }, altText: { title: 'Figure', description: caption, name: 'fig' } })] }), cap('Figure ' + (++figN) + '. ' + caption)]; }
function PHF(text, caption) { return [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 100, after: 40 }, border: { top: { style: BorderStyle.DASHED, size: 6, color: GRAY, space: 20 }, bottom: { style: BorderStyle.DASHED, size: 6, color: GRAY, space: 20 }, left: { style: BorderStyle.DASHED, size: 6, color: GRAY, space: 8 }, right: { style: BorderStyle.DASHED, size: 6, color: GRAY, space: 8 } }, shading: { type: ShadingType.CLEAR, fill: PALE, color: 'auto' }, children: [new TextRun({ text: '[' + text + ']', italics: true, color: GRAY })] }), cap('Figure ' + (++figN) + '. ' + caption)]; }

function build(parts, toc, outFile, cover) {
  const style = (sz, col, bef, aft, o = {}) => ({ run: { font: 'Arial', size: sz, bold: true, color: col }, paragraph: { spacing: { before: bef, after: aft }, keepNext: true, ...o } });
  const tocP = reg.filter(r => r.toc).map(r => new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: W, leader: LeaderType.DOT }], indent: { left: (r.level - 1) * 280 }, spacing: { after: r.level === 1 ? 60 : 30, before: r.level === 1 ? 120 : 0 }, children: [new TextRun({ text: r.text + '\t' + (toc[r.text] || ''), bold: r.level === 1, size: r.level === 3 ? 18 : 20 })] }));
  const doc = new Document({
    creator: 'ICONLITE Workshop 2026', title: 'ICONLITE ONT Amplicon Sequencing Handbook',
    styles: { default: { document: { run: { font: 'Arial', size: 21, color: INK } }, heading1: style(40, BLUE, 0, 200), heading2: style(32, BLUE, 360, 140), heading3: style(24, '0F4C7A', 240, 100) } },
    numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }, ...numRefs.map(r => ({ reference: r, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } } } }] }))] },
    sections: [
      { properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1300, left: 1440, right: 1440 } } }, children: cover },
      { properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1300, bottom: 1200, left: 1440, right: 1440 } } },
        headers: { default: new Header({ children: [new Paragraph({ children: [new TextRun({ text: 'ICONLITE 2026 · ONT Amplicon Sequencing Handbook', size: 16, color: GRAY })] })] }) },
        footers: { default: new Footer({ children: [new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: W }], children: [new TextRun({ text: 'v1.0 draft · 8 November 2026\tPage ', size: 16, color: GRAY }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: GRAY }), new TextRun({ text: ' of ', size: 16, color: GRAY }), new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: GRAY })] })] }) },
        children: [...parts.front, new Paragraph({ children: [new TextRun('Contents')], heading: HeadingLevel.HEADING_1, pageBreakBefore: true }), ...tocP, ...parts.body] }]
  });
  return Packer.toBuffer(doc).then(b => fs.writeFileSync(outFile, b));
}
module.exports = { P, PART, CH, SEC, B, N, CALL, T, FIG, PHF, build, reg, cap, runs, head, BLUE, PALE, INK, GRAY, d };
