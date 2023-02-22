# the problem is to write a source program that, when compiled and executed, will produce as output an exact copy of its source
# Source: https://research.swtch.com/zip
s = 's = %s; print (s %% repr(s))'; print (s % repr(s))
