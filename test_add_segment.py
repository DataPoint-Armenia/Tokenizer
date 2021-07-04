#import Tokenizer
from tokenizer import VortanTokenizer

# write some text
text = 'Նա սենյակ մտավ՝ ծածկելու պատուհանները, երբ մենք դեռ '

# tokenization
T = VortanTokenizer(text)
T.add_segment(text).tokenization()

# print result
print(T)
