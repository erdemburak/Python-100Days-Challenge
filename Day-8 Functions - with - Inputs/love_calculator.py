def calculate_love_score(first_name, second_name):
    true_list = ["t","r","u","e"]
    love_list = ["l","o","v","e"]
    true_count = 0
    love_count = 0

    combined_name = first_name.lower() + second_name.lower()

    for letter in combined_name:
        if letter in true_list:
            true_count += 1
        if letter in love_list:
            love_count += 1
    
    print(str(true_count)+ str(love_count))
        
calculate_love_score("Kanye West", "Kim Kardashian")

