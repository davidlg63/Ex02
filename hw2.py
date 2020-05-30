
def printCompetitor(competitor):
    '''
    Given the data of a competitor, the function prints it in a specific format.
    Arguments:
        competitor: {'competition name': competition_name, 'competition type': competition_type,
                        'competitor id': competitor_id, 'competitor country': competitor_country, 
                        'result': result}
    '''
    competition_name = competitor['competition name']
    competition_type = competitor['competition type']
    competitor_id = competitor['competitor id']
    competitor_country = competitor['competitor country']
    result = competitor['result']
    
    assert(isinstance(result, int)) # Updated. Safety check for the type of result

    print(f'Competitor {competitor_id} from {competitor_country} participated in {competition_name} ({competition_type}) and scored {result}')


def printCompetitionResults(competition_name, winning_gold_country, winning_silver_country, winning_bronze_country):
    '''
    Given a competition name and its champs countries, the function prints the winning countries 
        in that competition in a specific format.
    Arguments:
        competition_name: the competition name
        winning_gold_country, winning_silver_country, winning_bronze_country: the champs countries
    '''
    undef_country = 'undef_country'
    countries = [country for country in [winning_gold_country, winning_silver_country, winning_bronze_country] if country != undef_country]
    print(f'The winning competitors in {competition_name} are from: {countries}')


def key_sort_competitor(competitor):
    '''
    A helper function that creates a special key for sorting competitors.
    Arguments:
        competitor: a dictionary contains the data of a competitor in the following format: 
                    {'competition name': competition_name, 'competition type': competition_type,
                        'competitor id': competitor_id, 'competitor country': competitor_country, 
                        'result': result}
    '''
    competition_name = competitor['competition name']
    result = competitor['result']
    return (competition_name, result)


def readParseData(file_name):
    '''
    Given a file name, the function returns a list of competitors.
    Arguments: 
        file_name: the input file name. Assume that the input file is in the directory of this script.
    Return value:
        A list of competitors, such that every record is a dictionary, in the following format:
            {'competition name': competition_name, 'competition type': competition_type,
                'competitor id': competitor_id, 'competitor country': competitor_country, 
                'result': result}
    '''
    competitors_in_competitions = []
    # TODO Part A, Task 3.4
    with open(file_name, 'r') as file:
        lines = file.readlines()

    competitor_country_dict = {}
    for line in lines:
        words_in_line = line.split()
        if words_in_line[0] == "competitor":
            competitor_country_dict[words_in_line[1]] = words_in_line[2]

    for line in lines:
        words_in_line = line.split()
        if words_in_line[0] == "competition":
            data_dict = {}
            data_dict['competition name'] = words_in_line[1]
            data_dict['competition type'] = words_in_line[3]
            data_dict['competitor id'] = words_in_line[2]
            data_dict['competitor country'] = competitor_country_dict[words_in_line[2]]
            data_dict['result'] = words_in_line[4]
            competitors_in_competitions.append(data_dict)
    # need to check whether the sorting is done by them at the test or by us with their function
    return competitors_in_competitions


def calcCompetitionsResults(competitors_in_competitions):
    '''
    Given the data of the competitors, the function returns the champs countries for each competition.
    Arguments:
        competitors_in_competitions: A list that contains the data of the competitors
                                    (see readParseData return value for more info)
    Retuen value:
        A list of competitions and their champs (list of lists). 
        Every record in the list contains the competition name and the champs, in the following format:
        [competition_name, winning_gold_country, winning_silver_country, winning_bronze_country]
    '''
    competitions_champs = []
    # TODO Part A, Task 3.5
    length = len(competitors_in_competitions)
    competitions_champs = []
    competitions = []
    for dicts in competitors_in_competitions:
        if not dicts[0] in competitions:
            new_dict = {dicts[0], dicts[1]}
            competitions.append(new_dict)

    for competition in competitions:
        competitiors_list = []
        exists = []
        for i in range(length):
            data = competitors_in_competitions[i]
            if data['competition name'] == competition[0]:
                competitor_id = data['competitor id']
                if competitor_id in exists:
                    for entry in competitiors_list:
                        if entry[0] == competitor_id:
                            competitiors_list.remove(competitor_id)
                else:
                    competitor_information = [competitor_id, data['result']]
                    competitiors_list.append(competitor_information)
                    exists += competitor_id
        sorted_list = sorted(competitiors_list, lambda competitor: competitor_information[1])
        sorted_length = len(sorted_list)
        winner_competitions_champs_info = []
        competition_type = competition[1]
        gold_id, silver_id, bronze_id
        gold_country, silver_country, bronze_country
        if sorted_length == 0:
            continue
        elif sorted_length == 1:
            bronze_country = 'undef_country'
            silver_country = 'undef_country'
        elif sorted_length == 2:
            bronze_country == 'undef_country'

        if competition_type == 'untimed':
            gold_id = sorted_list[sorted_length - 1]
            if sorted_length > 1:
                silver_id = sorted_list[sorted_length - 2]
                if sorted_length > 2:
                    bronze_id = sorted_list[sorted_length - 3]
        else:
            gold_id = sorted_list[0]
            if sorted_length > 1:
                silver_id = sorted_list[1]
                if sorted_length > 2:
                    bronze_id = sorted_list[2]

        for competitor in competitors_in_competitions:
            if competitor['competitor id'] == gold_id:
                gold_country = competitor['competitor coutry']
            elif silver_country != 'undef_country' and competitor['competitor id'] == silver_id:
                silver_country = competitor['competitor coutry']
            elif bronze_country != 'undef_country' and competitor['competitor id'] == bronze_id:
                bronze_country = competitor['competitor coutry']

        winner_competitions_champs_info = [competition[0], gold_country, silver_country, bronze_country]
        competitions_champs.append(winner_competitions_champs_info)

    return competitions_champs


def partA(file_name = 'input.txt', allow_prints = True):
    # read and parse the input file
    competitors_in_competitions = readParseData(file_name)
    if allow_prints:
        # competitors_in_competitions are sorted by competition_name (string) and then by result (int)
        for competitor in sorted(competitors_in_competitions, key=key_sort_competitor):
            printCompetitor(competitor)
    
    # calculate competition results
    competitions_results = calcCompetitionsResults(competitors_in_competitions)
    if allow_prints:
        for competition_result_single in sorted(competitions_results):
            printCompetitionResults(*competition_result_single)
    
    return competitions_results


def partB(file_name = 'input.txt'):
    competitions_results = partA(file_name, allow_prints=False)
    # TODO Part B
    o = OlympicsCreate()
    for result in competitions_results:
        OlympicsUpdateCompetitionResults(o, str(result[1]), str(result[2]), str(result[3]))

    OlympicsWinningCountry(o)
    OlympicsDestroy(o)

if __name__ == "__main__":
    '''
    The main part of the script.
    __main__ is the name of the scope in which top-level code executes.
    
    To run only a single part, comment the line below which correspondes to the part you don't want to run.
    '''    
    file_name = 'input.txt'

    partA(file_name)
    partB(file_name)