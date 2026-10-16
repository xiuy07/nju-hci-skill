"""Check distribution invariants with the Python standard library."""
from pathlib import Path
import json
import re


def validate(root):
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    assert re.fullmatch(r'\d+\.\d+\.\d+', version), 'Invalid version'
    assert manifest['version'] == version
    expected_refs = set(manifest['reference_files'])
    language_layouts = []
    for language, relative in manifest['packages'].items():
        package = root / relative
        text = (package / 'SKILL.md').read_text(encoding='utf-8')
        assert re.search(r'^name: ' + re.escape(manifest['name']) + r'$', text, re.M)
        assert f'  version: "{version}"' in text
        assert f'  language: "{language}"' in text
        assert set(p.name for p in (package / 'references').glob('*.md')) == expected_refs
        assert (package / 'agents/openai.yaml').is_file()
        language_layouts.append({p.relative_to(package).as_posix()
                                 for p in package.rglob('*') if p.is_file()})
        for path in package.rglob('*'):
            if not path.is_file():
                continue
            content = path.read_text(encoding='utf-8')
            assert '南京大学' not in content and 'Nanjing University' not in content, path
            assert not re.search(r'https?://', content), f'Source links belong in README: {path}'
            assert 'TODO' not in content and 'TBD' not in content, path
    assert language_layouts[0] == language_layouts[1], 'Language layouts differ'
    for path in root.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):
                continue
            target_path = target.split('#')[0]
            assert (path.parent / target_path).exists(), (path, target)
    assert not list(root.rglob('*.pdf')), 'Original PDF must not be packaged'
    print(f'PASS: {version}, {len(language_layouts)} languages, '
          f'{len(expected_refs)} references per language; links, layout and attribution placement.')


if __name__ == '__main__':
    validate(Path(__file__).resolve().parents[1])
