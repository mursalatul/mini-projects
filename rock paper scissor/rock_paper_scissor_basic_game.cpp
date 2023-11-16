#include <iostream>
#include <string>

void processResult(int &player_1_score, int &player_2_score, std::string player_1_input, std::jjstring player_2_input)
{
	if (player_1_input == "rock")
	{
		if (player_2_input == "paper")
			player_2_score++;
		else if (player_2_input == "scissor")
			player_1_score++;
	}
	else if (player_1_input == "paper")
	{
		if (player_2_input == "scissor")
			player_2_score++;
		else if (player_2_input == "rock")
			player_1_score++;
	}
	else
	{
		if (player_2_input == "rock")
			player_2_score++;
		else if (player_2_input == "paper")
			player_1_score++;
	}
}

int main()
{
	std::cout << "Rock Paper Scissor\n";
	int player_1_score = 0, player_2_score = 0, rounds = 0;
	std::cout << "Enter number of rounds: ";
	std::cin >> rounds;
	for (int i = 1; i <= rounds; i++)
	{
		std::cout << "\t<Round "<< i << ">\n";
		
		std::cout << "Player 1 (Enter Rock / Paper / Scissor): ";
		std::string player_1_input;
		std::cin >> player_1_input;

		std::cout << "Player 2 (Enter Rock / Paper / Scissor): ";
		std::string player_2_input;
		std::cin >> player_2_input;

		processResult(player_1_score, player_2_score, player_1_input, player_2_input);
	}

	// output result
	if (player_1_score > player_2_score)
		std::cout << "Player 1 won by " << player_1_score - player_2_score << " points.\n";
	else if (player_2_score > player_1_score)
		std::cout << "Player 2 won by " << player_2_score - player_1_score << " points.\n";
	else
		std::cout << "Draw\n";
	return 0;
}