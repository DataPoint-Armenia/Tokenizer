#import Tokenizer
from tokenizer import VortanTokenizer

# write some text
text = 'Նա սենյակ մտավ՝ ծածկելու պատուհանները, երբ մենք դեռ անկողնում էինք, ու տեսա, որ տեսքը հիվանդի է 5-ական 5կմ/ժ -5 հեյ~ ՀՀԿ-ական սենյակ։'

long_text = """
Նա սենյակ մտավ՝ ծածկելու պատուհանները, երբ մենք դեռ անկողնում էինք, ու տեսա, որ տեսքը հիվանդի է։ Նա դողում էր՝ դեմքը ճեփ֊ճերմակ, քայլում էր հուշիկ, ասես շարժվելը ցավ էր պատճառում։

—Ի՞նչ է եղել, Schatz։

— Գլո՛ւխս է ցավում։
"""

# tokenization
T = VortanTokenizer(long_text)
T.segmentation().tokenization()

# print result
print(T)
