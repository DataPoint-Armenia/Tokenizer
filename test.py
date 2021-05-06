#import Tokenizer
from tokenizer import Tokenizer

#write some text
text = 'Նա սենյակ մտավ՝ ծածկելու պատուհանները, երբ մենք դեռ անկողնում էինք, ու տեսա, որ տեսքը հիվանդի է 5-ական 5կմ/ժ -5 հեյ~ ՀՀԿ-ական սենյակ։'

#tokenization
T = Tokenizer(text)
T.segmentation().tokenization()

#print result
print(T)
