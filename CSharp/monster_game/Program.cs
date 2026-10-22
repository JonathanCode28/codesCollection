Random random = new Random();

Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine("=== MONSTER BATTLE ===");
Console.ResetColor();

Console.WriteLine($"you enter the arena!");
int monsterHealth = 100;
int playerHealth = 100;

while (monsterHealth > 0 && playerHealth > 0)
{
int playerAttack = random.Next(1, 51);
int specialAttack = random.Next(50, 101);

Console.ForegroundColor = ConsoleColor.Blue;
Console.WriteLine($"Monster health: {monsterHealth}");
Console.WriteLine($"Player health: {playerHealth}");
Console.ResetColor();


int halfAttack = playerAttack / 2;
int doubleAttack = playerAttack * 2;
int strongerAttack = playerAttack + 20;
int drunkAttack = playerAttack / 2;

do {
Console.WriteLine("Choose your attack (1-2):");
Console.WriteLine("1. Normal Attack");
Console.WriteLine("2. Special Attack");
int choice = int.Parse(Console.ReadLine());
while (true);

switch (choice)
{
    case 1:
        Console.WriteLine($"you attack the monster with {playerAttack} power");
        monsterHealth -= playerAttack;
        break;
    case 2:
        Console.WriteLine($"you attack the monster with {specialAttack} power");
        monsterHealth -= specialAttack;
        break;
    default:
        Console.WriteLine("Invalid attack choice");
        break;
}

int monsterAttack = random.Next(1, 51);
Console.WriteLine($"The monster attacks back with {monsterAttack} power");
playerHealth -= monsterAttack;

do {
Console.WriteLine("Choose your attack (3-4):");
Console.WriteLine("3. Half Attack");
Console.WriteLine("4. Double Attack");
choice = int.Parse(Console.ReadLine());
while (true);

switch (choice)
{
    case 3:
        Console.WriteLine($"you attack the monster with {halfAttack} power");
        monsterHealth -= halfAttack;
        break;
    case 4:
        Console.WriteLine($"you attack the monster with {doubleAttack} power");
        monsterHealth -= doubleAttack;
        break;
    default:
        Console.WriteLine("Invalid choice!");
        break;
}

monsterAttack = random.Next(1, 51);
Console.WriteLine($"The monster attack back with {monsterAttack} power");
playerHealth -= monsterAttack;

do {
Console.WriteLine("Choose your attack (5-6):");
Console.WriteLine("5. Strong Attack");
Console.WriteLine("6. Drunk Attack");
choice = int.Parse(Console.ReadLine());
} while (true);

switch (choice)
{
    case 5:
        Console.WriteLine($"you attack the monster with {strongerAttack} power");
        monsterHealth -= strongerAttack;
        break;
    case 6:
        Console.WriteLine($"you attack the monster with {drunkAttack} power");
        monsterHealth -= drunkAttack;
        break;
    default:
        Console.WriteLine("Invalid choice!");
        break;
}

Console.WriteLine($"Monster health: {monsterHealth}");

monsterAttack = random.Next(1, 51);
Console.WriteLine($"The monster attack back with {monsterAttack} power");
playerHealth -= monsterAttack;

int spellAttack = random.Next(1, 51);
int spellHeal = random.Next(1, 21);

int canSpell = random.Next(1, 3);
if (canSpell == 1)
{
Console.ForegroundColor = ConsoleColor.Blue;
Console.WriteLine("You are strong enough to cast a spell and dumbledore teaches you!");
Console.WriteLine($"Choose your spell (1-2):");
Console.ResetColor();

do {
Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine("1. Attack Spell");
Console.ResetColor();

Console.ForegroundColor = ConsoleColor.Green;
Console.WriteLine("2. Heal Spell");
Console.ResetColor();
} while (true);
int spellChoice = int.Parse(Console.ReadLine());

switch (spellChoice)
{
    case 1:
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine($"You cast an attack spell with {spellAttack} power");
        monsterHealth -= spellAttack;
        Console.ResetColor();
        break;
    case 2:
        Console.WriteLine($"You cast a heal spell and recover {spellHeal} health");
        playerHealth += spellHeal;
        break;
    default:
        Console.WriteLine("Invalid spell choice!");
        break;
}
}
else if (canSpell == 2)
{
    Console.ForegroundColor = ConsoleColor.Cyan;
    Console.WriteLine($"You cast an attack spell with {spellAttack} power");
    monsterHealth -= spellAttack;
    Console.WriteLine("Your spell failed to cast!");
    Console.ResetColor();
}

bool monsterDead = monsterHealth <= 0;
bool playerDead = playerHealth <= 0;
bool strongAttack = playerAttack >= 30;
bool weakAttack = playerAttack < 30;

if (monsterDead)
{
    Console.WriteLine("The monster is dead");
    Console.WriteLine("You won");
    Console.WriteLine("Game Over");
}
else
{
    Console.WriteLine("The monster survived, keep attacking!");
}

if (playerDead)
{
    Console.WriteLine("You are dead");
    Console.WriteLine("You lose");
    Console.WriteLine("Game Over");
}
else
{
    Console.WriteLine("You survived");
}

if (strongAttack)
{
    Console.WriteLine("You are a strong player");
}
else
{
    Console.WriteLine("You are a weak player");
}
}