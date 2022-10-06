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
