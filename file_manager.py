from pathlib import Path


def criar_diretorios():
    base_dir = Path("meu_sistema_livraria")
    data_dir = base_dir / "data"
    backups_dir = base_dir / "backups"
    exports_dir = base_dir / "exports"

    # Criação dos diretórios
    data_dir.mkdir(parents=True, exist_ok=True)
    backups_dir.mkdir(parents=True, exist_ok=True)
    exports_dir.mkdir(parents=True, exist_ok=True)

    print(f"Diretórios criados: {data_dir}, {backups_dir}, {exports_dir}")
