'''
Ejemplo de una definición de una herramienta para claude.
tool = {
    "name": "nombre_herramienta",
    "description": "Explicación en inglés simple de lo que hace esta herramienta",
    "input_schema": {
        "type": "object",
        "properties": {
            "nombre_parametro": {
                "type": "string",
                "description": "Qué es este parámetro y qué acepta"
            }
        },
        "required": ["nombre_parametro"]
    }
}
'''

tool = {
    "name": "get_customer_info",
    "description": "This step identifies if the current chat participant is a registered user within our system, based on their email or username.",
    "input_schema": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": "A unique text-based identifier linked to the user. It is a system-wide unique name used for user identification."
            },
            "email": {
                "type": "string",
                "description": "The email address used by the user to register in the system. Type: Text/Email (if supported by the application)."
            }

        },
        "required": ["nombre_parametro"]
    }
}

tool = {
    "name": "lookup_order",
    "description": "This step fetches data regarding a specific order, such as the items purchased, the transaction date, and the current status of both the order and the shipment, including the estimated delivery date.",
    "input_schema": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "string",
                "description": "A unique identifier used to locate and identify a specific order within the system."
            },
            "tracking_number": {
                "type": "string",
                "description": "The tracking label or ID assigned by the shipping carrier to monitor the package's delivery progress"
            },
        },
        "required": ["nombre_parametro"]
    }
}