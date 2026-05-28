

#link https://regexr.com/



import re

#pattern="and"
pattern=r"[A-Z]+he"
text='''

My name is Odysseas’ he said
but no one ever gives their real name.

‘You’re handsome’ he said.
He seemed like a well-brought-up boy.

When he undressed, his body was unexpectedly beautiful –
it didn’t resemble a porn model’s photograph
not stacked, perfumed, ready.
He wore a pair of nondescript briefs
and gave off a faint trace of sweat.

‘How nice, Odysseas—or whatever your name is’ I told him
‘you could be real, a real human
someone could hold or fall in love with you
one could imagine you writing poems —
how difficult these hookups would be then
how rare and how colourless.’
‘You guessed right, I write poems too’ he replied
‘but my name really is Odysseas
and I do really want you.
Don’t leave, don’t leave me please



'''


match=re.search(pattern,text)
print(match)





















































































