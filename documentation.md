# Recipes API
Recipes API is a service the cookbook


# Chef


## Create chef

```http
  POST /api/v1/chef
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes for creating the chef
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name of chef |

+ Request

    + Body
           
            {
                "name": "Savio Silva "
            }


+ Response 201 Created (application/json)
  
    + Body
           
           {
                "id": 1,
                "name": "Savio Silva "
            }


    
## List All Chefs 

```http
  GET /api/v1/chef/list
  Host:
  Content-Type: application/json
  Accept: application/json
```

####Attributes the chef
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `primary_ky` | **Required**. Id of chef |
| `name`      | `string` | **Required**. Name of chef |

+ Response 200 OK (application/json)
    + Body
  

            [
                {
                    "id": 1,
                    "name": "Savio Silva "
                },
                {
                    "id": 2,
                    "name": "Gustavo",
                }
            ]


## Retrieve Chef 
```http
  GET /api/v1/chef/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes the chef
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `primary_ky` | **Required**. Id of chef |
| `name`      | `string` | **Required**. Name of chef |

+ Parameters
    + id (integer)

+ Response 200 OK (application/json)

    + Body
       
       
        {
            "id": 1,
            "name": "Sávio Silva"
        }

## Update Chef 
```http
  PUT /api/v1/chef/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes the chef
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `primary_ky` | **Required**. Id of chef |
| `name`      | `string` | **Required**. Name of chef |

+ Parameters
    + id (integer)

+ Request

    + Body
  

        {
            "name": "Savio Silva Moreira"
        }
     
    
+ Response 200 OK (application/json)
    
    + Body

          {
              "id": 1,
              "name": "Sávio Silva Moreira"
          }

## Delete Chef
```http
  DELETE /api/v1/chef/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
+ Parameters
    + id (integer)

+ Response 204 No Content





# Recipe


## Create Recipe

```http
  POST /api/v1/recipe
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes for creating the recipe
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required** Name of the recipe. |
| `chef`|`foreign_key`|**Required** Chef who created the recipe.| 
| `description`|`text`|**No Required** Description of the recipe. |
| `ingredients`|`text`|**Required** Ingredients of the recipe. |
| `time`|`integer`|**Required** Recipe preparation time.|
| `difficulty`|`choices`|**Required** Difficulty choices as 1 to 3. |
| `method`|`text`|**Required** Recipe preparation method. | 
| `portions`|`integer`|**Required** Method for the realization of the recipe. | 



 
+ Request

    + Body

           {
                'name': "Empadão de frango",
                "chef": 2,
                "description": "",
                "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
                "time": 90,
                "difficulty": "2",
                "method": "Em ma tigela grande e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
                "portions": 30
           }




+ Response 201 Created (application/json)
  
    + Body
           
            {
                'id': 1,
                'name': "Empadão de frango",
                "chef": 2,
                "description": "",
                "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
                "time": 90,
                "difficulty": "2",
                "method": "Em ma tigela grande e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
                "portions": 30
           }


## Retrieve Recipe 
```http
  GET /api/v1/recipe/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes the recipe
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `primary_ky` | **Required**. Id of recipe |
| `name`      | `string` | **Required** Name of the recipe. |
| `chef`|`foreign_key`|**Required** Chef who created the recipe.| 
| `description`|`text`|**No Required** Description of the recipe. |
| `ingredients`|`text`|**Required** Ingredients of the recipe. |
| `time`|`integer`|**Required** Recipe preparation time.|
| `difficulty`|`choices`|**Required** Difficulty choices as 1 to 3. |
| `method`|`text`|**Required** Recipe preparation method. | 
| `portions`|`integer`|**Required** Method for the realization of the recipe. | 




+ Parameters
    + id (integer)

+ Response 200 OK (application/json)

    + Body
    

        {
                'id': 1,
                'name': "Empadão de frango",
                "chef": 2,
                "description": "",
                "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
                "time": 90,
                "difficulty": "2",
                "method": "Em ma tigela grande e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
                "portions": 30
        }


## Update Recipe 
```http
  PUT /api/v1/recipe/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes the recipe
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `primary_ky` | **Required**. Id of recipe |
| `name`      | `string` | **Required** Name of the recipe. |
| `chef`|`foreign_key`|**Required** Chef who created the recipe.| 
| `description`|`text`|**No Required** Description of the recipe. |
| `ingredients`|`text`|**Required** Ingredients of the recipe. |
| `time`|`integer`|**Required** Recipe preparation time.|
| `difficulty`|`choices`|**Required** Difficulty choices as 1 to 3. |
| `method`|`text`|**Required** Recipe preparation method. | 
| `portions`|`integer`|**Required** Method for the realization of the recipe. | 


+ Parameters
    + id (integer)

+ Request

    + Body
    

        {
            'name': "Empadão d",
            "chef": 1,
            "description": "",
            "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
            "time": 90,
            "difficulty": "2",
            "method": "Em ma tigela pequena e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
            "portions": 30
        }
     
    
+ Response 200 OK (application/json)
    
    + Body
  

          {
              "id": 1,
              'name': "Empadão d",
              "chef": 1,
              "description": "",
              "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
              "time": 90,
              "difficulty": "2",
              "method": "Em ma tigela pequena e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
              "portions": 30
          }


## Delete Recipe
```http
  DELETE /api/v1/recipe/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
+ Parameters
    + id (integer)

+ Response 204 No Content



## Search Recipe 
```http
  PUT /api/v1/recipe/{id}
  Host:
  Content-Type: application/json
  Accept: application/json
```
####Attributes the chef
| Attribute | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `primary_ky` | **Required**. Id of recipe |
| `name`      | `string` | **Required** Name of the recipe. |
| `chef`|`foreign_key`|**Required** Chef who created the recipe.| 
| `description`|`text`|**No Required** Description of the recipe. |
| `ingredients`|`text`|**Required** Ingredients of the recipe. |
| `time`|`integer`|**Required** Recipe preparation time.|
| `difficulty`|`choices`|**Required** Difficulty choices as 1 to 3. |
| `method`|`text`|**Required** Recipe preparation method. | 
| `portions`|`integer`|**Required** Method for the realization of the recipe. | 


+ Parameters
    + name (string)
    + chef (integer)
    + difficulty (choices)
    + time (integer)
    + portions (integer)


        
       
    
+ Response 200 OK (application/json)
    
    + Body
         
            
            [
                {
                    "id": 1,
                    'name': "Empadão d",
                    "chef": 1,
                    "description": "",
                    "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
                    "time": 90,
                    "difficulty": "2",
                    "method": "Em ma tigela pequena e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
                    "portions": 30
                },
            ]




