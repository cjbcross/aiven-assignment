# Aiven for Kafka: How to Stream Topic Data with Faker and Deliver Metrics with InfluxDB and Grafana

Details concerning the project and how to run the code in this repo can be found at https://aiven-cjb-blog.herokuapp.com/aiven-for-kafka-how-to-stream-topic-data-with-faker-and-deliver-metrics-with-grafana/

To invoke the main.py Python script (assuming dependencies in the requirements.txt file have been installed) from the project directory commandline, run:



    python main.py
    --security-protocol SSL
    --cert-folder /Users/christopherbutler/Downloads/
    --host kafka-227e26f1-cjbcross-fcdf.aivencloud.com
    --port 21201
    --topic-name jazz-bands
    --nr-messages 1000
    --max-waiting-time 0
    --subject jazz

Important note: the --nr-messages parameter is optional.  However, if this parameter is not used, your main app will run continuously until forcing an exit during the runtime.

These parameters will invoke the JAzzProvider class and send messages to the Kafka service running in Aiven.  JazzProvider code provided below for review:

```
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
```
