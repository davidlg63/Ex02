

def readParseData(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    competitor_country_dict = {}
    for line in lines:
       words_in_line=line.split()
       if words_in_line[0]=="competitor":
            competitor_country_dict[words_in_line[1]] = words_in_line[2]

    olympics_list = []
    for line in lines:
        words_in_line=line.split()
        if words_in_line[0]=="competition":
            data_dict = {}
            data_dict['competition name']=words_in_line[1]
            data_dict['competition type']=words_in_line[3]
            data_dict['competitor id']=words_in_line[2]
            data_dict['competitor country']=competitor_country_dict[words_in_line[2]]
            data_dict['result']=words_in_line[4]
            olympics_list += data_dict
# need to check whether the sorting is done by them at the test or by us with their function
    return olympics_list

1 .timed – המנצח בתחרות הוא המתחרה שהשיג את התוצאה הנמוכה ביותר. למשל, בתחרות
שחייה המתחרה שהשיג את התוצאה בעלת הזמן המועט ביותר לסיום המקצה הוא המנצח.
2 .untimed – המנצח בתחרות הוא המתחרה שהשיג את התוצאה הגבוהה ביותר. למשל,
בתחרות קפיצה לגובה המתחרה שהצליח לעבור את הגובה הגבוה ביותר הוא המנצח.
3 .knockout – תחרויות מסוג זה הן תחרויות טורניר, כמו למשל כדורגל או כדורסל, בהן
התוצאה היא דירוג בטורניר )מקום(. מתחרה ) competitor )בסוג תחרות כז ה נחשב כקבוצה
שלמה המתחרה עבור המדינה אותה מייצגת. לכל תחרות מסוג זה מקומות המתחרים נתונים
באופן רציף, לדוגמא: ב תחרות מסוג basketball ,אם נבחרת ישראל )שמיוצגת ע"י
id_competitor אחד לכל הקבוצה( מדורגת במקום 5 ,אז מובטח כי יהיו נתונות קבוצות
שדורגו במקומות 1 עד 4( אך לאו דווקא לפי סדר מסוים(.


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])

{'competition name': competition_name, 'competition type': competition_type,
'competitor id': competitor_id, 'competitor country': competitor_country,
'result': result}


def calcCompetitionResults(competitors_in_competitions):
    lenght= len(competitors_in_competitions)
    output=[]
    competitions=[]
    for dicts in competitors_in_competitions:
        if not dicts[0] in competitions:
            new_dict={dicts[0],dicts[1]}
            competitions+=new_dict

    for competition in competitions:
        competitiors_list=[]
        exists=[]
        for i in range(lenght):
            data=competitors_in_competitions[i]
            if data['competition name']==competition[0]:
                competitor_id = data['competitor id']
                if competitor_id in exists:
                    for entry in competitiors_list:
                        if entry[0] == competitor_id:
                            competitiors_list.remove(competitor_id)
                else:
                    competitor_information = [competitor_id, data['result']]
                    competitiors_list += competitor_information
                    exists += competitor_id
        sorted_list=sorted(competitiors_list, lambda competitor: competitor_information[1])
        sorted_length=len(sorted_list)
        winner_output_info=[]
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

        if competition_type =='untimed':
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

        winner_output_info = [competition[0], gold_country, silver_country, bronze_country]
        output += winner_output_info

    return  output












def main ():


