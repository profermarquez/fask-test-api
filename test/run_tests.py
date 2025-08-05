import subprocess

def run_all_tests():
    print("🔍 Ejecutando pruebas de autenticación...")
    subprocess.run(["pytest", "tests/test_auth.py", "-v"])

    print("\n🔍 Ejecutando pruebas de productos...")
    subprocess.run(["pytest", "tests/test_product.py", "-v"])

    print("\n✅ Todas las pruebas han sido ejecutadas.")

if __name__ == "__main__":
    run_all_tests()
