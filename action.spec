# -*- mode: python ; coding: utf-8 -*-
import os
import re

#Get version from TagVersion
version = os.environ.get("EXTRACTED_VERSION")
if (version is None):
    version = "VersionError"

# Lire le contenu de main.py
with open('main.py', 'r') as main_file:
    main_content = main_file.read()

# Utilisation de regex pour capturer le contenu entre les guillemets simples
pattern = re.compile(r"version = '([^']+)'")

# Recherche de la correspondance
match = pattern.search(main_content)

if match:
    current_version = match.group(1)
    main_content = pattern.sub(f"version = '{version}'", main_content)
    print(f"Version actuelle: {current_version}")
else:
    print("Aucune correspondance trouvée.")

# Écrire le contenu modifié dans main.py
with open('main.py', 'w') as main_file:
    main_file.write(main_content)
a = Analysis(
    ['main.py'],
    pathex=[os.path.join(os.environ['GITHUB_WORKSPACE'], 'OfficeAssistant')],
    binaries=[],
    datas=[(os.path.join(os.environ['GITHUB_WORKSPACE'], 'Pictures'), 'Pictures')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=('OfficeAssistant V'+current_version),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(os.environ['GITHUB_WORKSPACE'], 'Pictures', 'OfficeAssistanticone.ico'),
)
