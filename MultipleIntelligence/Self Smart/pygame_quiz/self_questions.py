from question_object import Question_Object
questions_list = []

temp_question = Question_Object('How in touch with your feelings are you?', ('Not so much, I tend to live more in my head', 'Somewhat, I know when I am having emotions , but I can\'t influence them very much',  'Very in touch, I know what I feel and can experience emotions thoroughly'), (2,1,0) )
questions_list.append(temp_question)

temp_question = Question_Object('Personal beliefs about yourself and your capabilities?',('I don\'t know what I believe. I don\'t think in terms of beliefs about myself',' I understand the concept of personal belief but I couldn\'t necessarily make you a specific list of my positive and negative beliefs' , 'I can make you a list of several beliefs I have about myself and my capabilities in life' ),(2,1,0))
questions_list.append(temp_question)

temp_question =  Question_Object('What role do goals play in your life?',('Hey , I\'m just going with the flow here. Don\'t talk to me about what I really want',' I can\'t say that I intentionally pursue goals on a regular basis', 'Goal-setting is one of the regular tools I use in my life' ),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('Given a choice to work with a group of people and to work alone, what would you choose?' , ( 'Working alone since I believe working alone is most efficient.', 'Working with the group only if I know the members since if I know who I work with will help improve efficiency.', ' Working with the group regardless since I like to work in a group and divide work effectively.'),(2,1,0))
questions_list.append(temp_question)

temp_question =  Question_Object('Life values: What\'s most important to you in life?',('I honestly don\'t know what\'s most important to me in life','I have some ideas about what\'s most important to me in life,but no clarity', 'Yes,I do know my life values. I am very clear on what is most important to me' ),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('Are you a social person that is to say would you willingly attend functions and parties?' , ('Nope, I would like to be left alone.','Depends, with friends, yes, but alone, not really.', 'Definitely, I love attending social gathering.'),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('How important is winning for you?' , ( 'Winning is everything, I like to win everything.','Don\'t mind losing if there is something to gain (lesson,knowledge).', 'I value participation over winning.'),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('Do you introspect yourself?' , ( 'Everytime ','Sometimes, specially when I make mistakes', 'What\'s that.'),(0,1,2))
questions_list.append(temp_question)


temp_question = Question_Object('Do you tend to procrastinate?' , ( 'I\'ll tell you later','Sometimes' , 'Not at all. I like to do my stuff on time.'),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('Do you like to take your own desicions or like someone to make them for you?' , ( 'My own desicions all the way', 'I can take suggestions but prefer to make my own decisions','I would certainly like someone else make them for me'),(0,1,2))
questions_list.append(temp_question)

temp_question = Question_Object('Would you to lead a team if given a choice?' , ( 'No I don\'t like to take responsibilities.', 'Only if there is no volunteer. ', 'Yes, I like being a leader.'),(2,1,0))
questions_list.append(temp_question)

temp_question = Question_Object('How comfortable are you answering such questions' , ( '0','Somewhat' , 'Super'),(2,1,0))
questions_list.append(temp_question)
