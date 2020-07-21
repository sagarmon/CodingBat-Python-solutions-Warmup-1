def missing_char(str, n):
  if n == 0:
      return str[1:]
  return str[0:n] + str[n+1:]
