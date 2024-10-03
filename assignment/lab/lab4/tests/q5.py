from otter.test_files import test_case

OK_FORMAT = False

name = "q5"
points = None

@test_case(points=None, hidden=False)
def test1_aisles_both(aisles_both):
    import pandas as pd
    from pandas.testing import assert_frame_equal
    from io import StringIO
    q5CORRECT_ANSWER = """,aisle_id,num_items_org,num_items_conv,aisle
0,1,895,2679,prepared soups salads
1,2,36,3801,specialty cheeses
2,3,2289,15134,energy granola bars
3,4,1320,8539,instant foods
4,5,191,2623,marinades meat preparation
5,6,271,1703,other
6,7,160,1079,packaged meat
7,8,34,1498,bakery desserts
8,9,2452,7984,pasta sauce
9,11,4,1342,cold flu allergy
10,12,378,1437,fresh pasta
11,13,147,4010,prepared meals
12,14,2556,2546,tofu meat alternatives
13,16,8467,5339,fresh herbs
14,17,2275,10529,baking ingredients
15,18,76,585,bulk dried fruits vegetables
16,19,2725,7852,oils vinegars
17,20,16,3056,oral hygiene
18,21,7007,34326,packaged cheese
19,22,7,1462,hair care
20,23,567,6350,popcorn jerky
21,24,64076,75696,fresh fruits
22,25,54,2711,soap
23,26,593,7790,coffee
24,27,11,1828,beers coolers
25,28,8,1235,red wines
26,29,1229,1574,honeys syrups nectars
27,30,527,3212,latino foods
28,31,5757,18701,refrigerated
29,32,6363,13252,packaged produce
30,33,3,628,kosher foods
31,34,136,2830,frozen meat seafood
32,35,1232,3926,poultry counter
33,36,1606,8975,butter
34,37,1249,21419,ice cream ice
35,38,1201,16350,frozen meals
36,40,43,1569,dog food care
37,41,9,2876,cat food care
38,42,76,4651,frozen vegan vegetarian
39,43,103,4951,buns rolls
40,44,1,547,eye ear care
41,45,2318,9171,candy chocolate
42,46,5,959,mint gum
43,47,188,1826,vitamins supplements
44,48,228,2916,breakfast bars pastries
45,49,1067,5321,packaged poultry
46,50,2384,4340,fruit vegetable snacks
47,51,968,4210,preserved dips spreads
48,52,2493,7236,frozen breakfast
49,53,3891,8465,cream
50,55,5,527,shave needs
51,57,938,2835,granola
52,58,77,1455,frozen breads doughs
53,59,4868,6595,canned meals beans
54,61,171,9853,cookies cakes
55,62,4,1084,white wines
56,63,4168,2976,grains rice dried goods
57,64,158,4536,energy sports drinks
58,65,263,1363,protein meal replacements
59,66,2843,5688,asian foods
60,67,1356,13965,fresh dips tapenades
61,68,413,144,bulk grains rice dried goods
62,69,7778,6906,soup broth bouillon
63,70,187,1018,digestion
64,71,154,1575,refrigerated pudding desserts
65,72,2602,7111,condiments
66,73,2,744,facial care
67,76,67,719,indian foods
68,77,147,16147,soft drinks
69,78,3012,16543,crackers
70,79,699,6962,frozen pizza
71,80,17,841,deodorants
72,81,4993,7147,canned jarred vegetables
73,83,72194,77468,fresh vegetables
74,84,17594,15315,milk
75,85,194,2906,food storage
76,86,10047,9828,eggs
77,87,1,890,more household
78,88,2367,9762,spreads
79,89,803,3916,salad dressing toppings
80,90,20,1043,cocoa drink mixes
81,91,5246,19272,soy lactosefree
82,92,5983,7215,baby food formula
83,93,1327,8524,breakfast bakery
84,94,2215,7159,tea
85,95,22,3219,canned meat seafood
86,96,2916,14044,lunch meat
87,97,115,1036,baking supplies decor
88,98,3082,9987,juice nectars
89,99,1418,2650,canned fruit applesauce
90,100,7531,5060,missing
91,101,3,1065,air fresheners candles
92,102,3,325,baby bath body care
93,103,137,391,ice cream toppings
94,104,6407,7282,spices seasonings
95,105,205,4624,doughs gelatins bake mixes
96,106,2458,10327,hot dogs bacon sausage
97,107,3345,27930,chips pretzels
98,108,3032,9907,other creams cheeses
99,109,17,528,skin care
100,110,353,4267,pickled goods olives
101,112,5448,18154,bread
102,113,56,238,frozen juice
103,114,8,5886,cleaning products
104,115,27,36377,water seltzer sparkling water
105,116,12852,13237,frozen produce
106,117,2796,9173,nuts seeds dried fruit
107,118,46,534,first aid
108,119,23,900,frozen dessert
109,120,10659,44710,yogurt
110,121,2870,13369,cereal
111,122,152,3122,meat counter
112,123,43794,30363,packaged vegetables fruits
113,124,1,966,spirits
114,125,347,1116,trail mix snack mix
115,126,153,895,feminine care
116,127,13,2134,body lotions soap
117,128,1089,7296,tortillas flat bread
118,129,496,8228,frozen appetizers sides
119,130,1528,4848,hot cereal pancake mixes
120,131,2613,8498,dry pasta
121,132,2,244,beauty
122,133,2,895,muscles joints pain relief"""
    q5CORRECT_ANSWER = pd.read_csv(StringIO(q5CORRECT_ANSWER), index_col=0)
    q5STUDENT_ANSWER = aisles_both()
    
    assert type(q5STUDENT_ANSWER) is pd.DataFrame, f"Error: expected DataFrame, got {type(q5STUDENT_ANSWER)} instead."
    try:
        assert_frame_equal(q5STUDENT_ANSWER, q5CORRECT_ANSWER)
    except AssertionError:
        idx = q5STUDENT_ANSWER != q5CORRECT_ANSWER
        correct = q5CORRECT_ANSWER[idx].dropna().to_string()
        incorrect = q5STUDENT_ANSWER[idx].dropna().to_string()
        raise AssertionError(f"Returned dataframe doesn't match. Mismatches are: \n ===== Correct ===== \n {correct} \n\n ===== Incorrect ===== \n {incorrect}")
        
