'''Estrutura do Sistema
# Classe Abstrata Cliente:

# Definirá as características básicas de um cliente e será a classe base para clientes homens e mulheres.
# Classe ClienteMulher e ClienteHomem:

# Herdarão de Cliente e terão características específicas, como o cheque especial para clientes mulheres.
# Classe ContaCorrente:

# Controlará o saldo e as operações de saque e depósito, e manterá uma lista de clientes.
# Classe ChequeEspecial:

# Implementará o comportamento específico do cheque especial para clientes mulheres.
# Classe Cliente:

# É uma classe abstrata com propriedades básicas e um método abstrato cliente_info que deve ser implementado por subclasses.
# Classe ClienteMulher e ClienteHomem:

# Herdam de Cliente. ClienteMulher tem um atributo adicional para o cheque especial.
# Classe ChequeEspecial:

# Gerencia o limite do cheque especial. O limite é definido como a renda mensal do cliente mulher.
# Classe ContaCorrente:

# Gerencia saldo e operações. Faz as verificações de saque levando em consideração o limite do cheque especial se o cliente for mulher.
# Uso de Métodos:

# deposito e saque atualizam o saldo e registram operações.
# exibir_info_clientes mostra informações dos clientes.
# exibir_operacoes lista todas as operações realizadas.