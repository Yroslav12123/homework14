car_info = {
    "model": "Toyota Corolla",
    "price": 600000,
    "working volume of the engine": 1.8,
    "full weight": 1800,
    "max speed": 180,
    "features of the interior": [
        "Climate control",
        "Touch display",
        "Leather seats",
            "Multimedia system with Bluetooth"
    ],
    "parameters of the luggage compartment": {
        "trunk volume": 470,
        "trunk volume with folded seat": 1040
    },
    "maximum permissible weight of a trailer with brakes": 1300
}


name_vehicle = car_info.get("model")
price = car_info.get("price")
first_option_interier = car_info.get("features of the interior", [None])[0]
volume_of_trunk_with_folded_seats = car_info.get("parameters of the luggage compartment", {}).get("trunk volume with folded seat")


print("Name of the car:", name_vehicle)
print("price:", price)
print("The first interior option:", first_option_interier)
print("trunk volume with folded seat:", volume_of_trunk_with_folded_seats)


