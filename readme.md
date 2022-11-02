# Basic interpreter

## GRAMMAR
### evaluator grammar rules:
```
expr => term | expr + term | expr - term
term => factor | term * factor | term / factor
factor => INT | FLOAT | ( expr )
```

### commands grammar rules

```
expr -> command id value image
command -> upd | del | retr | add
id -> INT
value -> str
```