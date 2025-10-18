
import subprocess
import sys
import os

def install_requirements():
    """Installiert Python-Pakete aus der requirements.txt Datei."""
    requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")

    if not os.path.exists(requirements_file):
        print(f"Fehler: Die Datei '{requirements_file}' wurde nicht gefunden.")
        print("Bitte stellen Sie sicher, dass 'requirements.txt' im selben Verzeichnis wie 'install.py' liegt.")
        sys.exit(1)

    print(f"Installiere Pakete aus {requirements_file}...")
    try:
        # Führe pip install -r requirements.txt aus
        process = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", requirements_file],
            check=True,  # Wirft eine Ausnahme bei Fehlern
            capture_output=True, # Erfasst stdout und stderr
            text=True # Dekodiert stdout/stderr als Text
        )
        print("\nInstallation erfolgreich abgeschlossen!")
        print("\nAusgabe von pip:")
        print(process.stdout)
        if process.stderr:
            print("\nFehler/Warnungen von pip:")
            print(process.stderr)

    except subprocess.CalledProcessError as e:
        print(f"\nFehler bei der Installation der Pakete: {e}")
        print(f"Befehl: {e.cmd}")
        print(f"Statuscode: {e.returncode}")
        print(f"Standardausgabe: {e.stdout}")
        print(f"Fehlerausgabe: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Fehler: 'pip' Befehl nicht gefunden. Stellen Sie sicher, dass Python und pip installiert und im PATH sind.")
        sys.exit(1)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        sys.exit(1)

def main():
    print("Starte die Installation der Projekt-Abhängigkeiten...")
    install_requirements()
    print("\nDie Installation ist abgeschlossen. Sie können nun Ihr Projekt starten.")

if __name__ == "__main__":
    main()

