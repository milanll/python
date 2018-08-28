
from read_match_result import read_match_result
from soccer_comm import print_help
import odds

print_help()
choice = input('please choice url:')

match_result_dict, match_odds = read_match_result(choice)

final_odds = odds.find_key(match_odds)

print(final_odds)



