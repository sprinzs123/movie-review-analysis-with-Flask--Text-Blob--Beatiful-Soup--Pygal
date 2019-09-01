import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import statistics

# going to make one big function for flask application.
# input for function is URL that input into search bar
# final output is a list that contain different lists
# [[objective], [subjective], [objective], [subjective]]
# in html selecting each particular list and iterate over it

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


def get_all_reviews(input_url):
    initial_page = requests.get(input_url, headers=headers)
    soup = BeautifulSoup(initial_page.content, 'html.parser')
    critic_page = input_url + "/reviews?page="
    full_list = []
    number_of_extremes = 3

    def critic_review(url, head):
    # get number of review pages total
        review_list = []
        page_url = url + '1'
        page_base = requests.get(page_url, headers=head)
        soup_base = BeautifulSoup(page_base.content, 'html.parser')
        number = soup_base.find("span", {"class": "pageInfo"})
        number = str(number.text)
    # number[10:] use this because it is where number of review pages are stored
        number = int(number[10:])
    # this url serves a template to what we are going to iterate to get all review pages
    # review string is a string where we are going to dump all reviews
    # iterate through all pages to get all reviews using 'find_all'
        for page in range(1, number+1):
            iterate_url = url+str(page)+'.html'
            r = requests.get(iterate_url, headers=head)
            soup = BeautifulSoup(r.content, 'html.parser')
            reviews = soup.find_all("div", {"class": "the_review"})
            for one_review in reviews:
                review = str(one_review.text.replace("\n", ""))
                review_list.append(review)
        return review_list
    # return full dictionaries of all polarity and subjectivity scores and reviews
    # keys as scores and values as reviews

    def polarity_dictionary(all_reviews):
        polarity_dict = {}
        for review in all_reviews:
            one_review = TextBlob(review)
            review_polarity = one_review.sentiment.polarity
            polarity_dict.update({review_polarity: review})
        return polarity_dict

    def subjectivity_dictionary(all_reviews):
        subjectivity_dict = {}
        for review in all_reviews:
            one_review = TextBlob(review)
            review_polarity = one_review.sentiment.subjectivity
            subjectivity_dict.update({review_polarity: review})
        return subjectivity_dict

    # call functions to get all reviews and analyze them using TextBlob
    all_reviews_list = critic_review(critic_page, headers)
    polar_dict = polarity_dictionary(all_reviews_list)
    objectivity_dict = subjectivity_dictionary(all_reviews_list)

    # make dictionaries of most positive and most negative polar reviews
    # number is a value we specify and to determine how many most polar reviews to get
    # all these functions going to look the same
    def most_negative(dictionary, number):
        dict_keys = {}
        dict_review = {}
        sorted_keys = list(sorted(dictionary.keys()))
        most_negatives = sorted_keys[0:number]

        for i in most_negatives:
            negative_value = dictionary.get(i)
            dict_keys.update({i: negative_value})

        for i in dict_keys:
            review = dict_keys.get(i)
            review = review.replace('  ', '')
            review = review.strip(' ')
            dict_review.update({i: review})
        return dict_review

    def most_positive(dictionary, number):
        dict_keys = {}
        dict_review = {}
        sorted_keys = list(sorted(dictionary.keys()))
        most_positives = sorted_keys[-1:(-number-1):-1]
        for i in most_positives:
            negative_value = dictionary.get(i)
            dict_keys.update({i: negative_value})

        for i in dict_keys:
            review = dict_keys.get(i)
            review = review.replace('  ', '')
            review = review.strip(' ')
            dict_review.update({i: review})
        return dict_review

    # make dictionaries of most subjective and most objective reviews
    def most_objective(dictionary, number):
        dict_keys = {}
        dict_review = {}
        sorted_keys = list(sorted(dictionary.keys()))
        most_negatives = sorted_keys[-1:(-number-1):-1]

        for i in most_negatives:
            negative_value = dictionary.get(i)
            dict_keys.update({i: negative_value})

        for i in dict_keys:
            review = dict_keys.get(i)
            review = review.replace('  ', '')
            review = review.strip(' ')
            dict_review.update({i: review})
        return dict_review

    def most_subjective(dictionary, number):
        dict_keys = {}
        dict_review = {}
        sorted_keys = list(sorted(dictionary.keys()))
        most_negatives = sorted_keys[0:number]

        for i in most_negatives:
            negative_value = dictionary.get(i)
            dict_keys.update({i: negative_value})

        for i in dict_keys:
            review = dict_keys.get(i)
            review = review.replace('  ', '')
            review = review.strip(' ')
            dict_review.update({i: review})
        return dict_review
    # make dictionaries of extremes as variables
    # number of extremes is number of reviews we want to get for each category

    negatives_dict = most_negative(polar_dict, number_of_extremes)
    positives_dict = most_positive(polar_dict, number_of_extremes)
    objective_dict = most_objective(objectivity_dict, number_of_extremes)
    subjective_dict = most_subjective(objectivity_dict, number_of_extremes)

    def full_negative_list(dictionary):
        final_list = []
        for each in dictionary:
            result = (dictionary.get(each) + ' Score of: ' + str(round(each, 3)))
            final_list.append(result)
        return final_list

    def full_positive_list(dictionary):
        final_list = []
        for each in dictionary:
            result = (dictionary.get(each) + ' Score of: ' + str(round(each, 3)))
            final_list.append(result)
        return final_list

    def full_objective_list(dictionary):
        final_list = []
        for each in dictionary:
            result = (dictionary.get(each) + ' Score of: ' + str(round(each, 3)))
            final_list.append(result)
        return final_list

    def full_subjective_list(dictionary):
        final_list = []
        for each in dictionary:
            result = (dictionary.get(each) + ' Score of: ' + str(round(each, 3)))
            final_list.append(result)
        return final_list

    positive_list = full_negative_list(positives_dict)
    negative_list = full_positive_list(negatives_dict)
    objective_list = full_objective_list(objective_dict)
    subjective_list = full_subjective_list(subjective_dict)


# make list of keys from our dictionary that we are going to use for statistics


# add all reviews that going to be displayed into one list
    full_list.append(positive_list)
    full_list.append(negative_list)
    full_list.append(objective_list)
    full_list.append(subjective_list)

# make list of keys from our dictionary that we are going to use for statistics
    def polarity_keys(dictionary):
        all_keys = []
        for i in dictionary:
            all_keys.append(i)
        return all_keys


    def subjectivity_keys(dictionary):
        all_keys = []
        for i in dictionary:
            all_keys.append(i)
        return all_keys

    full_list.append(list(polarity_keys(polar_dict)))
    full_list.append(list(subjectivity_keys(objectivity_dict)))
    return (full_list)


# print(get_all_reviews('https://www.rottentomatoes.com/m/hobo_with_a_shotgun')[4])







