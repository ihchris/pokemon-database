import csv

class Pokemon:
    def __init__(self, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return (f"Name: {self.name}, Type 1: {self.type1}, Type 2: {self.type2}, "
                f"Total: {self.total}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, "
                f"Sp. Atk: {self.sp_atk}, Sp. Def: {self.sp_def}, Speed: {self.speed}, "
                f"Generation: {self.generation}, Legendary: {self.legendary}")

class PokemonDatabase:
    def __init__(self, file_path):
        self.database = []
        self.file_path = file_path

    def add_pokemon(self, pokemon):
        self.database.append(pokemon)
        self.write_to_csv()

    def display_pokemon(self):
        for pokemon in self.database:
            print(pokemon)

    def search_pokemon(self, name):
        for pokemon in self.database:
            if pokemon.name.lower() == name.lower():
                return pokemon
        return None

    def load_from_csv(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_pokemon(Pokemon(
                    row['Name'],
                    row['Type 1'],
                    row['Type 2'],
                    int(row['Total']),
                    int(row['HP']),
                    int(row['Attack']),
                    int(row['Defense']),
                    int(row['Sp. Atk']),
                    int(row['Sp. Def']),
                    int(row['Speed']),
                    int(row['Generation']),
                    row['Legendary'].lower() == 'true'
                ))

    def write_to_csv(self):
        with open(self.file_path, mode='w', newline='') as csvfile:
            fieldnames = ['Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for pokemon in self.database:
                writer.writerow({
                    'Name': pokemon.name,
                    'Type 1': pokemon.type1,
                    'Type 2': pokemon.type2,
                    'Total': pokemon.total,
                    'HP': pokemon.hp,
                    'Attack': pokemon.attack,
                    'Defense': pokemon.defense,
                    'Sp. Atk': pokemon.sp_atk,
                    'Sp. Def': pokemon.sp_def,
                    'Speed': pokemon.speed,
                    'Generation': pokemon.generation,
                    'Legendary': pokemon.legendary
                })

# Creating the database
file_path = 'pokemon_data.csv'
poke_db = PokemonDatabase(file_path)

# Loading Pokémon data from CSV file
poke_db.load_from_csv()

# Function to interact with the user
def main():
    while True:
        action = input("Enter 'add' to add a new Pokémon, 'search' to search for a Pokémon, or 'quit' to exit: ").strip().lower()
        
        if action == 'add':
            name = input("Enter Pokémon name: ").strip()
            type1 = input("Enter Pokémon type 1: ").strip()
            type2 = input("Enter Pokémon type 2: ").strip() or None
            total = int(input("Enter Pokémon total stats: ").strip())
            hp = int(input("Enter Pokémon HP: ").strip())
            attack = int(input("Enter Pokémon attack: ").strip())
            defense = int(input("Enter Pokémon defense: ").strip())
            sp_atk = int(input("Enter Pokémon special attack: ").strip())
            sp_def = int(input("Enter Pokémon special defense: ").strip())
            speed = int(input("Enter Pokémon speed: ").strip())
            generation = int(input("Enter Pokémon generation: ").strip())
            legendary = input("Is Pokémon legendary (True/False): ").strip().lower() == 'true'
            poke_db.add_pokemon(Pokemon(name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary))
            print(f"{name} has been added to the database.")
        
        elif action == 'search':
            name = input("Enter the name of the Pokémon to search: ").strip()
            result = poke_db.search_pokemon(name)
            if result:
                print(result)
            else:
                print(f"{name} not found in the database.")
        
        elif action == 'quit':
            break
        
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
