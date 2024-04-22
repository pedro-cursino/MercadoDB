# Versão Beta

### Site de Lista de Compras do Mercado

Dentro deste projeto, foi criado as seguintes colunas:

**Nome do item**: VarChar(Único)
**Quantidade**: int(Opcional)
**Preço**: float(Opcional)
**Onde comprar**: Lista(12 opções)(Opcional)
- Carrefour, Atacadão, Assaí, Tenda, Shibata, Nagumo, Dia, Pão de Açúcar, Itambé, Extra, Compre Bem, Semar


### Bibliotecas para instalar:

Quando for iniciar o projeto, inicie o "interface.py".

```
pip install mysql
pip install customtkinter
```

### Comandos do MySQL:

Foi utilizado o Usuário administrador "**root**" e a senha "**admin**", e o banco de dados foi "**listadecompras**" e a tabela utilizada foi "**lista**", caso queira editar, mudar dentro do "credenciais.py".

```MySQL
CREATE TABLE `listadecompras`.`lista` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL UNIQUE,
  `quantidade` INT NULL,
  `preco` FLOAT NULL,
  `local` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
```

### Referências usadas
 - [CRUD em Python - Python e MySQL](https://youtu.be/_q3j25ACmQ4)
 - [Modern Tkinter Design With CustomTkinter](https://youtube.com/playlist?list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f&si=IHpF7-AuiPNJv7T7)