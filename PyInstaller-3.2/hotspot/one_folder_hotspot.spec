# -*- mode: python -*-

block_cipher = ''

added_files = [
         ( '..\\..\\res', 'res' ),
		 ('..\\..\\GnuWin32', 'GnuWin32')
         ]

a = Analysis(['..\\..\\hotspot.py'],
             pathex=['..\\modules', 'E:\\git-python\\Hotspot@UPMv2\\PyInstaller-3.2\\hotspot', 'C:\\Program Files (x86)\\Windows Kits\\10\Redist\\ucrt\\DLLs\\x64'],
             binaries=[  ],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
		  a.binaries,
		  a.zipfiles,
		  a.datas
          exclude_binaries=True,
          name='hotspot',
          debug=False,
          strip=False,
          upx=True,
		  onefile=True,
          console=False, 
		  icon='..\\res\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='hotspot')
