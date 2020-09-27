import numpy,collections,pprint,os

encryptedMSG = '''q oseqx inlngnxw gft dzsxj hss nx xto mszb ycnedtr nxgs q cnsx txycsluzt qxr lgssr attg qoqm azse sxt sa gft oncr qxneqcl
qpptqznxw gs gquxg ng qyyszrnxw gs inrts sa gft nxynrtxg qxr gft hss inrtsl lfso gft oseqx lgqxrnxw nx azsxg sa gft cnsx nx gft
qaznyqx cnsx tjfndng dtaszt dztqbnxw nxgs q cnggct rqxyt qxr oqinxw gft cnsx lgqxrl qceslg esgnsxctll lgqznxw qg ftz gft hss ysxanzetr
gft nxynrtxg fqpptxtr sx lqguzrqm dug rnr xsg nrtxgnam gft oseqx gft xto mszb yngm pscnyt rtpqzgetxg lqnr gftm otzt nxitlgnwqgnxw q
ztpszg sa yznenxqc gztlpqll hqwqzn lqnr lft qxr ftz fuldqxr ctag gs wtg qx tepcsmtt dug oftx gftm wsg dqyb gs gft tjfndng gft gztlpqlltz
oql wsxt gfnl qygnsx oql q ltznsul inscqgnsx qxr uxcqoauc gztlpqll gfqg ysucr fqit ztlucgtr nx ltznsul nxvuzm sz rtqgf lqnr q lgqgtetxg
azse gft dzsxj hss dqzzntzl qxr zuctl qzt nx pcqyt gs bttp dsgf inlngszl lgqaa qxr qxneqcl lqat ot fqit q htzs gsctzqxyt pscnym sx gztlpqll
qxr inscqgnsx sa dqzzntzl q hss lpsbtlptzlsx lqnr otrxtlrqm gfqg q ysxyztgt gztxyf oql dtgottx gft oseqx qxr gft cnsx vqxxq hqwqzn oql qg gft
tjfndng ongf ftz aqencm oftx gft nxynrtxg fqpptxtr lft lqnr gft oseqx oql wtlguznxw qxr lqmnxw ftccs gs gft cnsx gft dqr pqzg qdsug gfnl nl na
lsetgfnxw fqpptxtr gft cnsx osucrit dttx pug rsox hqwqzn lqnr ngl qoauc qxr ltcanlf sa lsetdsrm gs rs gfnl nl gft cqgtlg xtol sa gfnl lgszm'''

encryptedMSGlist = encryptedMSG.split()
# Frequency Notes
# ==================================================================================
# singleLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23
# ,'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
#
# trigramLetterFreq = {'THE': 1.81, 'AND': 0.73,'ING': 0.72,'ENT': 0.42,'ION': 0.42,'HER': 0.36,'FOR': 0.34,'THA': 0.33,'NTH': 0.33,'INT': 0.32,
# 'ERE': 0.31,'TIO': 0.31,'TER': 0.30,'EST': 0.28,'ERS': 0.28,'ATI': 0.26,'HAT': 0.26,'ATE': 0.25,'ALL': 0.25,'ETH': 0.24,'HES': 0.24,'VER': 0.24,
# 'HES': 0.24,'VER': 0.24,'HIS': 0.24,'OFT': 0.22,'ITH': 0.21,'FTH': 0.21,'STH': 0.21,'OTH': 0.21, 'RES': 0.21,'ONT': 0.20}
#====================================================================================
 # numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)[source]
 #    Find the unique elements of an array.
 #    Returns the sorted unique elements of an array. There are three optional outputs in addition to the unique elements:
 #        the indices of the input array that give the unique values
 #        the indices of the unique array that reconstruct the input array
 #        the number of times each unique value comes up in the input array


# Break into parts
def getNGrams(message, n):
    ngrams = []
    for i in range(len(message)-(n-1)):
        ngrams.append(message[i:i+n])
    return ngrams

trigrams = getNGrams(encryptedMSGlist,3)
# Use numpy to get some counts by matches
unique, counts = numpy.unique(trigrams, return_counts=True)
# Turn those into one dictionary
trigramDict = dict(zip(unique,counts))
# Order them by frequncy
orderedResults = collections.OrderedDict(sorted(trigramDict.items()))
# Group them by lettercount
sortedResults = sorted(orderedResults.items(), key=lambda kv: kv[1])
# Add some readability for use when comparing and rerunning
cleanedResults = {}
for k,v in sortedResults:
    cleanedResults.setdefault(len(k), []).append({'Group':k,'Freq':v})
pprint.pprint(cleanedResults)
# After much much much!!! trial and error 
os.system('cat encryptedMSG | tr "qdyrtawfnvbcexspkzlguiojmh" "a-z"')
