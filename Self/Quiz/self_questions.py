from question_object import Question_Object
questions_list = []

temp_question = Question_Object('How in touch with your feelings are you?', ('Not so much, I tend to live more in my head', 'Somewhat, aware about my emotions , can\'t influence all that much',  'Generally, I know what I feel and can express them clearly'), (0,2,1) )
questions_list.append(temp_question)

temp_question = Question_Object('Personal beliefs about yourself and your capabilities?',('I don\'t know what I believe. I don\'t think in terms of beliefs about myself','Understand the concept of personal belief but wouldn\'t be able to make a specific list of positive and negative beliefs' , 'Can make an explicit list of several beliefs I have about myself and my capabilities in life' ),(0,1,2))
questions_list.append(temp_question)

temp_question =  Question_Object('What role do goals play in your life?',('Hey , I\'m just going with the flow here. Don\'t talk to me about what I really want',' I can\'t say that I intentionally pursue goals on a regular basis', 'Goal-setting is one of the regular tools I use in my life' ),(0,1,2))
questions_list.append(temp_question)

temp_question = Question_Object('Given a choice to work with a group of people and to work alone, what would you choose?' , ( 'Working alone since I believe working alone is most efficient.', 'Working with the group only if I know the members since if I know who I work with will help improve efficiency.', ' Working with the group regardless since I like to work in a group and divide work effectively.'),(0,2,1))
questions_list.append(temp_question)

temp_question =  Question_Object('Life values: What\'s most important to you in life?',('Am very clear on what is most important to me, and prioritize accordingly'  , 'Haven\t figured it out yet','I have some ideas about what\'s most important to me in life,but no clarity'),(2,0,1))
questions_list.append(temp_question)

temp_question = Question_Object('Are you a social person that is to say would you willingly attend functions and parties?' , ('Nope, I would like to be left alone.','Definitely, I love attending social gathering.', 'Depends, with friends, yes, but alone, not really.' ),(1,0.5,1))
questions_list.append(temp_question)

temp_question = Question_Object('How important is winning for you?' , ( 'Winning is everything, I like to win everything.','Don\'t mind losing if there is something to gain (lesson,knowledge).', 'I value participation over winning.'),(0,1,2))
questions_list.append(temp_question)

temp_question = Question_Object('Do you introspect yourself?' , ( 'Everytime ','Sometimes, specially when I make mistakes', 'What\'s that.'),(2,1.5,0))
questions_list.append(temp_question)


temp_question = Question_Object('Do you tend to procrastinate?' , ( 'I\'ll tell you later','Sometimes' , 'Not at all. I like to do my stuff on time.'),(0,1,2))
questions_list.append(temp_question)

temp_question = Question_Object('Do you like to take your own desicions or like someone to make them for you?' , ( 'My own desicions all the way', 'I can take suggestions but prefer to make my own decisions','I would certainly like someone else make them for me'),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('Would you to lead a team if given a choice?' , ( 'No I don\'t like to take responsibilities.', 'Only if there is no volunteer. ', 'Yes, I like being a leader.'),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('How comfortable are you answering such questions' , ( '0','Somewhat' , 'Super'),(0,1,2))
questions_list.append(temp_question)
