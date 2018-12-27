from sklearn.externals import joblib
import signals, suggestions

clf = joblib.load('model1.pkl')
# classes = joblib.load('classes.pkl')

sample_test = signals.Sample.load_from_file("./test_z.txt")
print sample_test

lin = sample_test.get_linearized(reshape=True)

#Predict the number with the machine learning model
number = clf.predict(lin)


# probs = clf.predict_log_proba(lin)
# ordered = sorted(classes)
# values = {}
# for i in xrange(len(probs[0])):
# 	values[round(probs[0,i], 5)] = classes[ordered[i]]
# ordered = sorted(values, reverse=True)
# letters = []
# for i in ordered:
# 	letters.append(values[i])
#
# print letters

#Convert it to a char
char = chr(ord('a')+number[0])

# hinter = suggestions.Hinter.load_english_dict()
# print hinter.next_letters("")
#
# print hinter.most_probable_letter(clf, classes, lin, "")
#
print number
print char