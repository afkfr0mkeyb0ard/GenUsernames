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

## Examples
> python3 genusernames.py [-en/fr/es] [-f1/f2/f3/f4]

```
Generate french usernames (format: antoine.dupont)
> python3 genusernames.py -fr -f3

Generate french usernames (format: adupont)
> python3 genusernames.py -fr -f2

Generate english usernames (format: c.collins)
> python3 genusernames.py -en -f4

Generate usernames using all dictionaries (format: javiernunes)
> python3 genusernames.py -f1
```

