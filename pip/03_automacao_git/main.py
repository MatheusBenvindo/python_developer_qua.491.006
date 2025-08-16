import pyautogui as auto
import time

def tirar_credenciais():
    auto.write("git config --global --unset-all user.name")
    auto.press("enter")
    time.sleep(0.5)
    auto.write("git config --global --unset-all user.email")
    auto.press("enter")
    time.sleep(0.5)

def main():
    auto.PAUSE = 0.5  # Pausa automática entre comandos

    usuario = input("Informe o user.name: ").strip().lower()
    email = input("Informe o user.email: ").strip().lower()
    commit = input("Informe a frase de commit: ")

    tirar_credenciais()

    auto.write('cd ..')  # Corrigido aqui
    auto.press("enter")
    time.sleep(0.5)

    auto.write(f'git config --global user.name "{usuario}"')
    auto.press("enter")
    time.sleep(0.5)

    auto.write(f'git config --global user.email "{email}"')
    auto.press("enter")
    time.sleep(0.5)

    auto.write("git add .")
    auto.press("enter")
    time.sleep(0.5)

    auto.write(f'git commit -m "{commit}"')
    auto.press("enter")
    time.sleep(1)

    auto.write("git push")
    auto.press("enter")
    time.sleep(5)  # espera maior para garantir que o push termine

    tirar_credenciais()

if __name__ == "__main__":
    main()
