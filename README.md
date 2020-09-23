# PSI Test

Write a program to calculate Psi.  It would be a good idea to use dictionaries (in python) and make it able to handle the frequencies of multiple characters.

1) Substitution does not alter the underlying distribution.  Check this by calculating Psi for one of the message texts and corresponding Caesar ciphers.  You'd darned well better get the same answer.

2) Transposition doesn't alter the frequencies of letters, but it does alter the frequencies of pairs, triples, quartets of letters. Try using Psi on triples or quartets of letters to solve the scrambled Alice text (alice_permuted.txt below).   The spaces and punctuation marks are part of the permutation so don't delete them. The permutation (transposition) is in a block of six and the python itertools will generate it along with all other sets.
