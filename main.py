import random

# RAW data
greek_alphabet = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
greek_combinations = [ 'ΑΒ', 'ΑΓ', 'ΑΔ', 'ΑΕ', 'ΑΖ', 'ΑΗ', 'ΑΘ', 'ΑΙ', 'ΑΚ', 'ΑΛ', 'ΑΜ', 'ΑΝ', 'ΑΞ', 'ΑΟ', 'ΑΠ', 'ΑΡ', 'ΑΣ', 'ΑΤ', 'ΑΥ', 'ΑΦ', 'ΑΧ', 'ΑΨ', 'ΑΩ', 'ΒΓ', 'ΒΔ', 'ΒΕ', 'ΒΖ', 'ΒΗ', 'ΒΘ', 'ΒΙ', 'ΒΚ', 'ΒΛ', 'ΒΜ', 'ΒΝ', 'ΒΞ', 'ΒΟ', 'ΒΠ', 'ΒΡ', 'ΒΣ', 'ΒΤ', 'ΒΥ', 'ΒΦ', 'ΒΧ', 'ΒΨ', 'ΒΩ', 'ΓΔ', 'ΓΕ', 'ΓΖ', 'ΓΗ', 'ΓΘ', 'ΓΙ', 'ΓΚ', 'ΓΛ', 'ΓΜ', 'ΓΝ', 'ΓΞ', 'ΓΟ', 'ΓΠ', 'ΓΡ', 'ΓΣ', 'ΓΤ', 'ΓΥ', 'ΓΦ', 'ΓΧ', 'ΓΨ', 'ΓΩ', 'ΔΕ', 'ΔΖ', 'ΔΗ', 'ΔΘ', 'ΔΙ', 'ΔΚ', 'ΔΛ', 'ΔΜ', 'ΔΝ', 'ΔΞ', 'ΔΟ', 'ΔΠ', 'ΔΡ', 'ΔΣ', 'ΔΤ', 'ΔΥ', 'ΔΦ', 'ΔΧ', 'ΔΨ', 'ΔΩ', 'ΕΖ', 'ΕΗ', 'ΕΘ', 'ΕΙ', 'ΕΚ', 'ΕΛ', 'ΕΜ', 'ΕΝ', 'ΕΞ', 'ΕΟ', 'ΕΠ', 'ΕΡ', 'ΕΣ', 'ΕΤ', 'ΕΥ', 'ΕΦ', 'ΕΧ', 'ΕΨ', 'ΕΩ', 'ΖΗ', 'ΖΘ', 'ΖΙ', 'ΖΚ', 'ΖΛ', 'ΖΜ', 'ΖΝ', 'ΖΞ', 'ΖΟ', 'ΖΠ', 'ΖΡ', 'ΖΣ', 'ΖΤ', 'ΖΥ', 'ΖΦ', 'ΖΧ', 'ΖΨ', 'ΖΩ', 'ΗΘ', 'ΗΙ', 'ΗΚ', 'ΗΛ', 'ΗΜ', 'ΗΝ', 'ΗΞ', 'ΗΟ', 'ΗΠ', 'ΗΡ', 'ΗΣ', 'ΗΤ', 'ΗΥ', 'ΗΦ', 'ΗΧ', 'ΗΨ', 'ΗΩ', 'ΘΙ', 'ΘΚ', 'ΘΛ', 'ΘΜ', 'ΘΝ', 'ΘΞ', 'ΘΟ', 'ΘΠ', 'ΘΡ', 'ΘΣ', 'ΘΤ', 'ΘΥ', 'ΘΦ', 'ΘΧ', 'ΘΨ', 'ΘΩ', 'ΙΚ', 'ΙΛ', 'ΙΜ', 'ΙΝ', 'ΙΞ', 'ΙΟ', 'ΙΠ', 'ΙΡ', 'ΙΣ', 'ΙΤ', 'ΙΥ', 'ΙΦ', 'ΙΧ', 'ΙΨ', 'ΙΩ', 'ΚΛ', 'ΚΜ', 'ΚΝ', 'ΚΞ', 'ΚΟ', 'ΚΠ', 'ΚΡ', 'ΚΣ', 'ΚΤ', 'ΚΥ', 'ΚΦ', 'ΚΧ', 'ΚΨ', 'ΚΩ', 'ΛΜ', 'ΛΝ', 'ΛΞ', 'ΛΟ', 'ΛΠ', 'ΛΡ', 'ΛΣ', 'ΛΤ', 'ΛΥ', 'ΛΦ', 'ΛΧ', 'ΛΨ', 'ΛΩ', 'ΜΝ', 'ΜΞ', 'ΜΟ', 'ΜΠ', 'ΜΡ', 'ΜΣ', 'ΜΤ', 'ΜΥ', 'ΜΦ', 'ΜΧ', 'ΜΨ', 'ΜΩ', 'ΝΞ', 'ΝΟ', 'ΝΠ', 'ΝΡ', 'ΝΣ', 'ΝΤ', 'ΝΥ', 'ΝΦ', 'ΝΧ', 'ΝΨ', 'ΝΩ', 'ΞΟ', 'ΞΠ', 'ΞΡ', 'ΞΣ', 'ΞΤ', 'ΞΥ', 'ΞΦ', 'ΞΧ', 'ΞΨ', 'ΞΩ', 'ΟΠ', 'ΟΡ', 'ΟΣ', 'ΟΤ', 'ΟΥ', 'ΟΦ', 'ΟΧ', 'ΟΨ', 'ΟΩ', 'ΠΡ', 'ΠΣ', 'ΠΤ', 'ΠΥ', 'ΠΦ']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def machine(message, key, direction):
    previous_key_index = 0
    current_key_index = 2
    final_message = ''


    if direction == -1:

        # Decrypting    
        mc_key = 2
        mp_key = 0
        for i in range(int(len(message)/2)):
            message_character = message[mp_key:mc_key]
            # Appending SPACE or Symbols to the Final Message
            if not message_character.isalpha():
                final_message += message_character[0]

            else:
                # Seperating Key
                if current_key_index == int(len(key)/2):
                    current_key_index = 2
                    previous_key_index = 0

                key_character = key[previous_key_index : current_key_index]
                current_key_index += 2
                previous_key_index += 2

                diff = greek_combinations.index(key_character)
                index = greek_combinations.index(message_character)
                new_index = (index - diff) % len(greek_combinations)
                final_message += alphabet[new_index]
            mc_key += 2
            mp_key += 2  

    else:
        # Encrypting
        for message_character in message.lower():

            # Appending SPACE or Symbols
            if not message_character.isalpha():
                final_message += message_character*2

            else:
                # Slicing Key
                if current_key_index == int(len(key)/2):
                    current_key_index = 2
                    previous_key_index = 0

                key_character = key[previous_key_index : current_key_index]

                current_key_index += 2
                previous_key_index += 2

                diff = greek_combinations.index(key_character)
                index = alphabet.index(message_character)
                new_index = (index + diff) % len(greek_combinations)
                final_message += greek_combinations[new_index]
                

    print(final_message+'\n')

# Asking whether the user wants to Encrypt or Decrypt, Getting key and message.
while True:

    direction = int(input("\nSelect ECRYPTION (1) / DECRYPTION (-1): "))

    if direction == 1 or direction == -1:
        text = str(input("\nEnter the Message: "))
        key = str(input("Enter Key (type '0' to generate a key): "))
        temp = 0

        # Generating a Key
        if key == '0' :
            key = str() 
            
            for i in range(20):
                temp = random.randint(0,244)
                key += greek_combinations[temp]
            print(f'\nKey : {key}\n')
            break
        
        # Confirming the custom-key
        elif len(key)%2 == 0:
            for i in key:
                if i in greek_alphabet:
                    temp += 1
            if temp == len(key):
                print("\n<-- key Confirmed -->\n")
                break
      
    print("\n**INVALID INPUT**")

machine(text, key, direction)
