from pathlib import Path
root = Path(__file__).resolve().parents[1]
source = root / "src/pe"
html = (source / "index.html").read_text()
html = html.replace('<link rel="stylesheet" href="pe.css">', '<style>' + (source / "pe.css").read_text() + '</style>')
for name in ('model.js', 'dg-assets.js', 'pe.js'):
    html = html.replace('<script src="' + name + '"></script>', '<script>' + (source / name).read_text() + '</script>')
(root / 'docs/windows/pe.html').write_text(html)
(root / 'docs/windows/index.html').write_text((root / 'docs/windows/windows.html').read_text())
print('Built PE page and Windows entry point')
