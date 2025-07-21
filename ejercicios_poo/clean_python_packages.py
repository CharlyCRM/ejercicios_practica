import subprocess
import sys

def get_installed_packages():
    """Obtiene la lista de paquetes instalados"""
    result = subprocess.run([sys.executable, '-m', 'pip', 'freeze'], 
                        capture_output=True, text=True)
    return [line.split('==')[0].lower() for line in result.stdout.split('\n') if line]

def uninstall_package(package):
    """Desinstala un paquete específico"""
    print(f"Desinstalando {package}...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'uninstall', '-y', package], 
                    capture_output=True)
        return True
    except Exception as e:
        print(f"Error al desinstalar {package}: {str(e)}")
        return False

def main():
    # Lista ESTRICTA de paquetes esenciales que queremos mantener
    essential_packages = {
        'certifi',
        'pip',
        'setuptools',
        'wheel',
        'numpy',
        'pandas',
        'python-dateutil',
        'pytz',
        'six'
    }

    print("Obteniendo lista de paquetes instalados...")
    installed_packages = get_installed_packages()
    
    # Filtrar paquetes a desinstalar (ahora más estricto)
    to_uninstall = []
    for pkg in installed_packages:
        pkg_lower = pkg.lower()
        if pkg_lower not in essential_packages and pkg_lower not in ['']:
            to_uninstall.append(pkg)
    
    print(f"\nSe encontraron {len(to_uninstall)} paquetes para desinstalar:")
    for pkg in to_uninstall:
        print(f"- {pkg}")
    
    # Confirmar con el usuario
    response = input("\n¿Deseas continuar con la desinstalación? (s/n): ")
    if response.lower() != 's':
        print("Operación cancelada.")
        return

    # Desinstalar paquetes
    successful = 0
    failed = 0
    
    for package in to_uninstall:
        if uninstall_package(package):
            successful += 1
        else:
            failed += 1

    print("\nResumen:")
    print(f"Paquetes desinstalados exitosamente: {successful}")
    print(f"Paquetes que fallaron: {failed}")
    print("\nProceso completado.")

if __name__ == "__main__":
    main()