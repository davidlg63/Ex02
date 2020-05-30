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
    for competitor in competitors_in_competitions:
        print(competitor['competition name'], competitor['competition type'], competitor['competitor id'],
              competitor['competitor country'], competitor['result'])
    #return competitors_in_competitions

if __name__ == "__main__":
    readParseData('test1.txt')