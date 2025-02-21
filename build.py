import PyInstaller.__main__
import os
import sys
import shutil

def clean_build():
    """Limpa diretórios de build anteriores"""
    dirs_to_clean = ['build', 'dist']
    files_to_clean = ['SistemaAnaliseVendas.spec']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Diretório {dir_name} removido.")
            
    for file_name in files_to_clean:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Arquivo {file_name} removido.")

def create_assets():
    """Cria diretório de assets se não existir"""
    if not os.path.exists('assets'):
        os.makedirs('assets')
        print("Diretório assets criado.")

def compile_project():
    """Compila o projeto usando PyInstaller"""
    # Limpa builds anteriores
    clean_build()
    
    # Cria diretório de assets
    create_assets()
    
    # Verifica se existe o ícone
    icon_path = os.path.join('assets', 'icon.ico')
    if not os.path.exists(icon_path):
        print("Aviso: arquivo icon.ico não encontrado em assets/")
        icon_path = None
    
    # Argumentos base do PyInstaller
    args = [
        'main.py',
        '--name=SistemaAnaliseVendas',
        '--onefile',
        '--windowed',
        '--noconfirm',
        '--clean',
        '--add-data=assets;assets',
        '--hidden-import=pandas',
        '--hidden-import=tkinter',
        '--hidden-import=ttkthemes',
        '--hidden-import=openpyxl',
        '--hidden-import=xlsxwriter'
    ]
    
    # Adiciona ícone se existir
    if icon_path:
        args.append(f'--icon={icon_path}')
    
    print("Iniciando compilação...")
    try:
        PyInstaller.__main__.run(args)
        print("\nCompilação concluída com sucesso!")
        print("O executável está disponível em: dist/SistemaAnaliseVendas.exe")
    except Exception as e:
        print(f"\nErro durante a compilação: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    compile_project()