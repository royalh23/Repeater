# This program repeats the item you enter as much as you want.

# Choose a language.
prompt = "Please choose one of the languages below:"
prompt += "\nLütfən aşağıdakı dillərdən birini seçin:"
prompt += "\nAzerbaijani"
prompt += "\nEnglish"
prompt += '\n(Write "quit" to quit)'
prompt += '\n(Çıxmaq üçün "quit" yazın.) '

prompten1 = "\nPlease enter what you want to repeat: "

promptaz1 = "\nLütfən təkrarlamaq istədiyinizi daxil edin: "

def repeat(item, prompt):
    """Repeat the entered item in the chosen language."""
    number = int(input(prompt))

    # Create a text file to store the items.
    with open("list.txt", "w") as items:
        i = 1
        while i <= number:
            items.write(f"{item} ")
            i += 1

while True:
    language = input(prompt)
    language = language.strip()

    if language == "English" or language == "english":
        item = input(prompten1)
        prompten2 = f'How many times do you want to repeat "{item}"? '
        repeat(item, prompten2)
        break
        
    elif language == "Azerbaijani" or language == "azerbaijani":
        item = input(promptaz1)
        promptaz2 = f'"{item}"i neçə dəfə təkrarlamaq istəyirsiniz? '
        repeat(item, promptaz2)
        break

    elif language == "quit":
        break
        
    else:
        print("\nPlease enter a valid language.")
        print("Lütfən düzgün dil seçin.\n")
        continue