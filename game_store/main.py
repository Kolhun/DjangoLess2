# Импортируем необходимые модели и классы
from task3.models import Buyer, Game
from decimal import Decimal

# Создаём покупателей
buyer1 = Buyer.objects.create(
    name='young_gamer',
    balance=Decimal('100.00'),
    age=16
)

buyer2 = Buyer.objects.create(
    name='adult_gamer1',
    balance=Decimal('250.50'),
    age=25
)

buyer3 = Buyer.objects.create(
    name='adult_gamer2',
    balance=Decimal('300.75'),
    age=30
)


game1 = Game.objects.create(
    title='Family Fun',
    cost=Decimal('19.99'),
    size=Decimal('2.5'),
    description='A fun game suitable for all ages.',
    age_limited=False
)

game2 = Game.objects.create(
    title='Action Blast',
    cost=Decimal('49.99'),
    size=Decimal('15.0'),
    description='An action-packed shooter game.',
    age_limited=True
)

game3 = Game.objects.create(
    title='Mystery Quest',
    cost=Decimal('29.99'),
    size=Decimal('5.0'),
    description='Solve intriguing mysteries in this adventure game.',
    age_limited=True
)

# Устанавливаем связи между покупателями и играми

# 1. Только один Buyer (buyer3) обладает всеми Game
buyer3.games.set([game1, game2, game3])

# 2. Buyer с возрастом меньше 18 (buyer1) не обладает играми с ограничением по возрасту
buyer1.games.set([game1])

# 3. Остальной Buyer (buyer2) обладает играми с ограничением по возрасту
buyer2.games.set([game2, game3])
