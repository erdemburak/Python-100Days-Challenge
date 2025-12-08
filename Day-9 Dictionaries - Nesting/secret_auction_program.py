print("----- Welcome To Secret Auction -----\n\n")

print("This auction will be blind so you will type your name and bid. Thats all")

sacret_auction_bids = {
    "participant_name": [],
    "participant_bid": [],
}

there_is_other_participant = True

while there_is_other_participant == True:

    participant_name = input("What is your name: ")
    participant_bid = int(input("What is your bid: "))

    sacret_auction_bids["participant_name"].append(participant_name)
    sacret_auction_bids["participant_bid"].append(participant_bid)

    print("\n" * 20)

    next_participant = input("Is there anyone want to join? Type 'yes' or 'no': ").lower()

    if next_participant == "yes":
        there_is_other_participant = True
    elif next_participant == "no":
        there_is_other_participant = False

print("\n" * 20)
print("------ And the Winner ------\n")

winner_participant = ""
winner_participants_bid = 0

number_of_participants = len(sacret_auction_bids["participant_bid"])

for index in range(0,number_of_participants):
    if sacret_auction_bids["participant_bid"][index] > winner_participants_bid:
        winner_participants_bid = sacret_auction_bids["participant_bid"][index]
        winner_participant = sacret_auction_bids["participant_name"][index]

print(f"{winner_participant} with ${winner_participants_bid} bid")