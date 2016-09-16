# -*- mode: python -*-

block_cipher = None

added_files = [
         ( '..\\..\\res', 'res' )
         ]

a = Analysis(['..\\..\\hotspot.py'],
             pathex=['..\\modules', 'C:\\Program Files (x86)\\Windows Kits\\10\Redist\\ucrt\\DLLs\\x64', 'E:\\git-python\\Hotspot@UPMv2\\PyInstaller-3.2\\hotspot'],
             binaries=None,
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
          a.datas,
          name='hotspot',
          debug=False,
          strip=False,
          upx=True,
          console=True )
