
# Arboles de decision

## Resultado de la ejecucion del algoritmo sobre el dataset 'tennis.csv'

### dataset

| outlook   | temp  | humidity  | windy | play  |
| :-------: | :---: | :-------: | :---: | :---: |

| sunny     | hot   | high      | false | no    |
| sunny     | hot   | high      | true  | no    |
| overcast  | hot   | high      | false | yes   |
| rainy     | mild  | high      | false | yes   |
| rainy     | cool  | normal    | false | yes   |
| rainy     | cool  | normal    | true  | no    |
| overcast  | cool  | normal    | true  | yes   |
| sunny     | mild  | high      | false | no    |
| sunny     | cool  | normal    | false | yes   |
| rainy     | mild  | normal    | false | yes   |
| sunny     | mild  | normal    | true  | yes   |
| overcast  | mild  | high      | true  | yes   |
| overcast  | hot   | normal    | false | yes   |
| rainy     | mild  | high      | true  | no    |

### arbol de decision

    *outlook*
            sunny:
                retorna: temp
                    *temp*
                        hot:
                            retorna: False
                        mild:
                            retorna: humidity
                                *humidity*
                                    high:
                                        retorna: False
                                    normal:
                                        retorna: True
                        cool:
                            retorna: True
            overcast:
                retorna: True
            rainy:
                retorna: windy
                    *windy*
                        false:
                            retorna: True
                        true:
                            retorna: False



