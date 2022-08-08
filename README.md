Criação de um Blog - Ocean Samsung

Com professores: Guilherme Feulo e Danilo Miguel


Para deploy no Heroku

Fazer login

## cria app
heroku create <nome do app>

## cria Banco
heroku addons:create heroku-postgresql:hobby-dev --app <nome do app>

## config do app
heroku config --app blog

## para atualizar
git push heroku main