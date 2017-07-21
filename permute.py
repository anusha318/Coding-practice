class Solution:
  def permute(self, word, rule):
    word=word.lower()
    rule=rule.lower()
    l=[]
    sol=[]
    for i in range(len(word)):
      if((word[i] in rule) and (word[i]>='a' and word[i]<='z')):
        l.append(i)
    x=1<<(len(l))
    for i in range(0,x):
      s=list(word)
      a=bin(i)[2:].zfill(len(l))
      for j in range(0,len(a)):
        if(a[j]=='1'):
          s[l[j]]=s[l[j]].upper()
      sol.append(''.join(s))
    return sol

word="medium-one"
rule="m"
a=Solution()
permute_ul = a.permute
print (permute_ul(word, rule))
print (permute_ul('medium-one', 'me'))
print (permute_ul('m', 'me'))
print (permute_ul('ab-cd', 'ad'))
print (permute_ul('ab-cd', 'a-'))
print (permute_ul('a3b', 'ab'))
print (permute_ul('a3bcdddd', 'acd'))
