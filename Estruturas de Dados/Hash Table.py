# A solucao deve estar implementada dentro da função abaixo.
# Dica: Você pode criar outras funções e classes se quiser mas esta é a função principal que será usada.


def calc_hash(item, item_count):
    hash = 0
    for i in item:
        hash += ord(i)
        return hash % item_count


print(calc_hash("job", len("job")))
print(calc_hash("ana", len("ana")))
print(calc_hash("mia", len("mia")))
print(calc_hash("mal", len("mal")))
print(calc_hash("cov", len("cov")))
print(calc_hash("apn", len("apn")))
print(calc_hash("alo", len("alo")))
print(calc_hash("seg", len("seg")))
print(calc_hash("ter", len("ter")))
print(calc_hash("qar", len("qar")))
print(calc_hash("che", len("che")))
print(calc_hash("ola", len("ola")))
print(calc_hash("bob", len("bob")))
print(calc_hash("ted", len("ted")))
print(calc_hash("doc", len("doc")))
