Console.WriteLine("name:");
string playerName = Console.ReadLine();

Console.WriteLine("age:");
int playerAge = int.Parse(Console.ReadLine());

Console.WriteLine("hours:");
int playerHours = int.Parse(Console.ReadLine());

Console.WriteLine("score:");
int playerScore = int.Parse(Console.ReadLine());

Console.WriteLine($"name: {playerName}");
Console.WriteLine($"age: {playerAge + 5}");
Console.WriteLine($"hours: {playerHours}");
Console.WriteLine($"score: {playerScore + 100}");