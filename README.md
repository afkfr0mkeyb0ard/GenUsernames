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


## How to use
`> python3 genusernames.py [-f1/f2/f3/f4] [-es/fr/en]`

```
-en       Use English dictionary only
-fr       Use French dictionary only
-es       Use Spanish dictionary only
-f1       Output format: {firstname}{lastname}
-f2       Output format: {f}{lastname}
-f3       Output format: {firstname}.{lastname}
-f4       Output format: {f}.{lastname}
-h        Display help
```
## Examples

```
#Generate french usernames (format: antoine.dupont)
> python3 genusernames.py -fr -f3

#Generate french usernames (format: adupont)
> python3 genusernames.py -fr -f2

#Generate english usernames (format: c.collins)
> python3 genusernames.py -en -f4

#Generate usernames using all dictionaries (format: javiernunes)
> python3 genusernames.py -f1
```

