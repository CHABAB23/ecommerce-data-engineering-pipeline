from pathlib import Path
import subprocess
import sys
import logging


# ============================================================
# CONFIGURATION DU PROJET
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

PYTHON_DIR = BASE_DIR / "python"
SQL_DIR = BASE_DIR / "sql"
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"


# ============================================================
# CONFIGURATION DES LOGS
# ============================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# PIPELINE
# ============================================================

logging.info("========== PIPELINE START ==========")

try:

    print()
    print("======================================")
    print("       DATA ENGINEERING PIPELINE")
    print("======================================")

    # --------------------------------------------------------
    # ETAPE 1 : ANALYSE PYTHON
    # --------------------------------------------------------

    analyse_file = PYTHON_DIR / "analyse.py"

    print()
    print("1. Lancement de analyse.py...")
    print(f"   Fichier : {analyse_file}")

    logging.info("Lancement de analyse.py")

    subprocess.run(
        [sys.executable, str(analyse_file)],
        cwd=BASE_DIR,
        check=True
    )

    logging.info("analyse.py termine avec succes")

    print()
    print("2. Analyse terminee avec succes.")

    # --------------------------------------------------------
    # ETAPE 2 : FIN
    # --------------------------------------------------------

    print()
    print("3. Pipeline termine avec succes.")

    logging.info("========== PIPELINE SUCCESS ==========")

except subprocess.CalledProcessError as e:

    logging.error(
        f"Erreur pendant l'execution de analyse.py : {e}",
        exc_info=True
    )

    print()
    print("ERREUR PIPELINE")
    print(e)

    logging.info("========== PIPELINE FAILED ==========")

except Exception as e:

    logging.error(
        f"Pipeline echoue : {e}",
        exc_info=True
    )

    print()
    print("ERREUR PIPELINE")
    print(e)

    logging.info("========== PIPELINE FAILED ==========")