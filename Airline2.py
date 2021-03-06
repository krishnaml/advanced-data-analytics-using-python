from textblob.classifiers import NaiveBayesClassifier

train = [('Air India did a poor job of queue management both times.', 'staff service'),("The 'cleaning' by flight attendants involved regularly spraying air freshener in the lavatories.", 'staff'),('The food tasted decent.', 'food'),('Flew Air India direct from New York to Delhi round trip.', 'route'),('Colombo to Moscow via Delhi.', 'route'),('Flew Birmingham to Delhi with Air India.', 'route'),('Without toilet, food or anything!', 'food'),('Cabin crew announcements included a sincere apology for the delay.', 'cabin flown')]

cl = NaiveBayesClassifier(train)

tests = ['Food is good.', 'Colombo to Moscow via Delhi.']
for c in tests:
	print c,'\t',cl.classify(c)