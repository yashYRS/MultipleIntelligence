module = ['You are the manager of a small town travel agency which is having a hard time keeping itself relevant, since the big players like Yatra, Make My Trip are selling everything at substantially lower prices than yours.',
'You are the coach of a very popular football team.', 'You have worked for a company for a very long time, and in that time have served them loyally and put in a lot of effort.', 'You are a teacher in a school. You have just entered the profession and hence have little experince in the field.']
	
Questions ={
	module[0]:
	{	
		'There is new competition in the market, What steps would you take to make sure you don\'t loose your client base.':
			[(
				'Huge demand in market, even if we loose old customers, new people would come in.','Leave the business and start something else','Lower our prices, to keep our clients with us, and once we impress them with our service, prices can be increased gradually.','Go into making niche products, not so easily available on other sites.'
			), (0.5,0,1.5,2) ] , 
		'One of your oldest and most trusted employee\'s mistake has caused you a huge loss, money worth 4 times his/her monthly salary. What action do you take ?':
			[(
				'Fire him/her instantly, and give a clear message that mistakes wouldn\'t be tolerated.','Retrieve the loss money by not giving him/her salary for the next 4 months.','Take the loss into your stride, and not fire the employee, because keeping him/her in the firm is more valuable than the money lost.','Scold him/her in front of everyone but no firing.'
			) , (1,0,2.5,0.5) ] 
	},
	module[1]:
	{	
		'As a football team\'s manager, all the credit for your team\'s win goes to only a few players, What do you do?':
			[(
				'Continue, individual credit doesn\'t matter', 'Give interviews, highlight your importance to the media.','Convince the players to give you credit after winning, since you deserve it.','Take up a job where you are in the limelight'
			) ,(1.5,1,0.5,1)] ,
		'As a manager, your captain although is the greatest player in the world has an attitude problem. What do you do ?':
			[(
				'Talk to him and try to convice him that the players look up to him and so he should take his role seriously.','Tell the management about the problem and recommend a change in captancy.','Continue playing the same way because you are playing with one of the best.','Recommend to fire that player.'
			),(1.5,0.5,1,0.5)]
	},
	module[2]:
	{	
		'You could twist facts to get a relatively new employee at a higher post fired , what would you do?':
			[(
				'Use the information to get the employee fired.','Be indifferent to the situation','Quit the company, and go to a place where old employees have more value.','Wait for people to recognize your loyalty to gain higer posts'
			),(0.5,2.5,0.5,0.5)] , 
		'You got promoted, but you sense that the other people don\'t agree with the promotion. What do you do?':
			[(
				'Fire someone to assert command.','Have a meeting and prove that you are capable of the post.','Ignore and treat it as a minor problem.','Burden them with work so that they won\'t have time to think about it.'
			),(0,1.5,2,0.5)]
	},
	module[3]:
	{	
		'There is a conflict in a class that you teach, how do you resolve that?':
			[(
				'Punish the ones who started it.','Do nothing and let the conflict sort itself out.','Solve the conflict by talking.','Let Principal handle it.'
			),(1.5,0.5,2,0)] , 
		'Except for one, all your students did really badly in an exam you took, what would you do?':
			[(
				'Praise the topper and tell everyone to be like him/her.','Let each student know their own result without mentioning the topper.','Let them know the status and encourage them to do better next time.','Openly distribute marks.'
			),(1,1.5,0.5,1)]
	},
}