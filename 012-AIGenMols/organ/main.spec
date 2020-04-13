# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['F:\\workdir\\organ0.19'],
             binaries=[],
             datas=[('organ\\NP_score.pkl.gz', 'organ'), ('organ\\SA_score.pkl.gz', 'organ'), ('organ\\data\\FDA-H.csv', 'organ\\data'), ('organ\\checkpoints\\FDA-H\\FDA-H_99.ckpt.data-00000-of-00001', 'organ\\checkpoints\\FDA-H'), ('organ\\checkpoints\\FDA-H\\FDA-H_99.ckpt.index', 'organ\\checkpoints\\FDA-H'), ('organ\\checkpoints\\FDA-H\\FDA-H_99.ckpt.meta', 'organ\\checkpoints\\FDA-H'), ('organ\\data\\FDA1884.csv', 'organ\\data'), ('organ\\checkpoints\\FDA1884\\FDA1884_119.ckpt.data-00000-of-00001', 'organ\\checkpoints\\FDA1884'), ('organ\\checkpoints\\FDA1884\\FDA1884_119.ckpt.index', 'organ\\checkpoints\\FDA1884'), ('organ\\checkpoints\\FDA1884\\FDA1884_119.ckpt.meta', 'organ\\checkpoints\\FDA1884'), ('organ\\data\\zinc.csv', 'organ\\data'), ('organ\\checkpoints\\ZINC\\ZINC_99.ckpt.data-00000-of-00001', 'organ\\checkpoints\\ZINC'), ('organ\\checkpoints\\ZINC\\ZINC_99.ckpt.index', 'organ\\checkpoints\\ZINC'), ('organ\\checkpoints\\ZINC\\ZINC_99.ckpt.meta', 'organ\\checkpoints\\ZINC')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
