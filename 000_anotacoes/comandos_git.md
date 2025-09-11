git config --global --list
# Ver usúarios existentes.

git config --global --unset user.name
git config --global --unset user.email
# Remover usuários.

git init
# Inicializar repositório

git config --global user.name "nome do usuário
git config --global user.email "email da conta"
# Configurar credenciais

git status
# Verificar status do repositório

.gitignore
# Arquivo para ignorar arquivos e pastas que não devem ser versionados

git add .
# Adicionar arquivos ao stage

git commit -m "mensagem do commit"
# Commitar as alterações com uma mensagem

git branch -M main
# Cria uma branch chamada main

git remote add origin <url>
# Adicionar repositório remoto

git push -u origin main
# Enviar alterações para o repositório remoto

Repositório > Code > Copiar URL > git clone https://github.com/guilhermededeus/python_developer_qua.491.006.git
# Clonar repositório remoto
