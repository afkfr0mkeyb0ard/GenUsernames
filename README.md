# GenUsernames
A Python script to generate usernames based on firstnames / lastnames

## Available countries 

- USA/UK: `-en`
- France: `-fr`
- Spain: `-es`

## Available formats

- 1: `{firstname}{lastname}`
- 2: `{f}{lastname}`
- 3: `{firstname}.{lastname}` 
- 4: `{f}.{lastname}`
- 5: `{lastname}{firstname}`
- 6: `{l}{firstname}`
- 7: `{lastname}.{firstname}`
- 8: `{l}.{firstname}`
- 9: `{firstname}{l}`
- 10: `{lastname}{f}`
- 11: `{firstname}.{l}`
- 12: `{lastname}.{f}`
- 13: `{firstname}`
- 14: `{lastname}`


## How to use
`> python3 genusernames.py [-f1/f2/f3/f4] [-es/fr/en]`

```
-d        Add a domain to the usernames for email mode (ie: -d google.com)
-en       Use English dictionary only
-fr       Use French dictionary only
-es       Use Spanish dictionary only
-f1       Output format: {firstname}{lastname}
-f2       Output format: {f}{lastname}
-f3       Output format: {firstname}.{lastname}
-f4       Output format: {f}.{lastname}
-f5       Output format: {lastname}{firstname}`
-f6       Output format: {l}{firstname}`
-f7       Output format: {lastname}.{firstname}`
-f8       Output format: {l}.{firstname}`
-f9       Output format: {firstname}{l}`
-f10      Output format: {lastname}{f}`
-f11      Output format: {firstname}.{l}`
-f12      Output format: {lastname}.{f}`
-f13      Output format: {firstname}`
-f14      Output format: {lastname}`
-h        Display help
```
## Examples

```
#Generate french usernames (format: antoine.dupont)
> python3 genusernames.py -fr -f3

#Generate french usernames with emails (format: adupont@google.com)
> python3 genusernames.py -fr -f2 -d google.com

#Generate english usernames (format: c.collins)
> python3 genusernames.py -en -f4

#Generate usernames using all dictionaries (format: javiernunes)
> python3 genusernames.py -f1
```

