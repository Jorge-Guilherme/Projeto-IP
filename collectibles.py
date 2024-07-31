class Coletavel:
    def __init__(self, name, type, rare, description, HP, damage):
        self.name = name
        self.type = type
        self.rare = rare
        self.description = description
        self.HP = HP
        self.damage = damage

# Definição de objetos do type Coletavel representando personagens do jogo

personagem1 = Coletavel( # Personagem de Vinícius
    name = "PG", 
    type = "Friendly", 
    rare = 0, 
    description = 1 
)

personagem2 = Coletavel( # Personagem de Hugo
    name = "Herói diferente",
    type = "Friendly",
    rare = 1,
    description = 1
)

personagem3 = Coletavel( # Personagem de Gusto
    name = "Gusto",
    type = "Enemy",
    rare = 2,
    description = "VOU FAZER A CHAMADA!", 
    HP = 1,
    damage = 1
)

personagem4 = Coletavel( # Personagem de Jorge
    name = "Bocudo",
    type = "Friendly",
    rare = 3,
    description = 1
)

personagem5 = Coletavel( # Personagem de Renata
    name = "Renata",
    type = "Friendly",
    rare = 4,
    description = 1
)

personagem6 = Coletavel( # Personagem de Ricardo
    name = "Ricardo",
    type = "Enemy",
    rare = 5,
    description = "TERMINOU A LISTA?", 
    HP = 1,
    damage = 1
)

personagem7 = Coletavel( # Personagem da Greve
    name = "Greve",
    type = "Enemy",
    description = "VOCÊ FICARÁ SEM FÉRIAS!", 
    HP = 2,
    damage = 1
)

personagem8 = Coletavel( # Personagem de Sofia
    name = "Sofia",
    type = "Friendly",
    rare = 7,
    description = 1
)

personagem9 = Coletavel( # Personagem de SérgioAmigo(a)m do RU
    name="Sérgio",
    type="Enemy",
    rare=8,
    description="NÃO ME CHAME DE PROFESSOR!",
    HP=3,
    damage=2
)

personagem10 = Coletavel( # Personagem de Kleberson
    name="Kab esticada",
    type="Friendly",
    name="RU fechado",
    type="Enemy",
    rare=10,
    description="ESTAMOS FECHADOS!", 
    HP=2,
    damage=1
)
