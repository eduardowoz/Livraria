import shutil
from pathlib import Path
from datetime import datetime


def fazer_backup():
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_backup = f"meu_sistema_livraria/backups/backup_livraria_{data_hora}.db"
    shutil.copy("meu_sistema_livraria/data/livraria.db", caminho_backup)
    print(f"Backup criado: {caminho_backup}")


def limpar_backups():
    backups_dir = Path("meu_sistema_livraria/backups")
    backups = sorted(backups_dir.glob("*.db"), key=lambda x: x.stat().st_mtime, reverse=True)

    # Mantendo apenas os 5 mais recentes
    for backup in backups[5:]:
        backup.unlink()
        print(f"Backup removido: {backup}")
