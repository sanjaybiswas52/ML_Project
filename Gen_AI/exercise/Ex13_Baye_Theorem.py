'''
Baye's Theorem to the resdcue
------------------------------
1. Evemt A = Is a user of the drug,
   Event B = tested positively for th drug.

2. We can work out from that information that 
        P(B) is 1.3% (0.99 * 0.003 + 0.01 * 0.997)
                     - the probability of testing positive if you do use PLUS 
                     - the probability of testing positive if you don't)

3. P(A|B) = P(A)P(B|A) / P(B) = (0.99 * 0.003) / 0.013 = 22.8%
4. So the odds of someone being an actual user of the drug given that they tested positive is only 22.8%
5. Even though P(B|A) is high (99%), it doesn't mean P(A|B) is high.

'''
