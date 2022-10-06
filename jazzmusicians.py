import random
import time
from faker.providers import BaseProvider

# Adding a JazzProvider with 3 methods:
#   * musician_names to retrieve the name of the band leader,
#   * instrument_type for additional musicians axes
#   * jazz_style to retrieve one of the styles available
class JazzProvider(BaseProvider):
    def musician_names(self):
        valid_musician_names = [
            'Miles Davis',
            'Chet Baker',
            'John Coltrane',
            'Wayne Shorter',
            'Sonny Rollins',
            'Stan Getz'
        ]
        return random.choice(valid_musician_names)

    def instrument_type(self):
        available_instrument_type = [
            'saxophone',
            'trumpet',
            'drums',
            'piano',
            'bass',
            'hammond organ',
            'guitar',
            'trombone'
        ]
        return random.choice(available_instrument_type)

    def jazz_style(self):
        jazz_styles = [
            'BeBop',
            'Swing',
            'Modal',
            'Free Jazz',
            'Hard Bop'
        ]
        return random.choice(jazz_styles)
    
    def produce_msg (self, FakerInstance, jazzcount = 1, max_musicians = 5, max_instruments=3):
        style = FakerInstance.jazz_style()
        musicians = []
        for jazz in range(random.randint(1, max_musicians)):
            instruments = []
            for instrument in range(random.randint(0, max_instruments)):
                instruments.append(FakerInstance.instrument_type())
            musicians.append({
                'musicianName': FakerInstance.musician_names(),
                'bandInstruments': instruments
            })
        # message composition
        message = {
            'id': jazzcount,
            'style': style,
            'name': FakerInstance.unique.name(),
            'phoneNumber': FakerInstance.unique.phone_number(),
            'address': FakerInstance.address(),
            'musicians': musicians,
            'timestamp': int(time.time()*1000)
        }
        key = {'style': style}
        return message, key
