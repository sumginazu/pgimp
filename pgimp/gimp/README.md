# Purpose

Contains code that is executed within gimp.

## Parameter passing

Parameters are passed to scripts using environment variables and can be retreived as follows:

```
get_parameter('parameter')
```

## Returning values

Values can be returned as follows:

```
return_json(obj)
```

They will be retrieved in the python application by invoking:

```
GimpScriptRunner().execute_and_parse_json(...)
```