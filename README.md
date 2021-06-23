# scratch-api-test
This project contains the mostly working code of a users api, which stores it's data in mysql and uses python as it's endpoint flask api that is deployed out to Kubernetes.

### Thought process
I'm most comfortable building bigger systems, such as APIs, in compiled langauges like C#, and mostly use python for scripting. However due to thinking python would be more relavent for this ask/environment(scratch), it seemed appropriate. However it bit me later on with my lack of request/response experience, and translating the data correctly into json. Unfortunately there's a few small bugs in the get users process that prevent me from correctly processing json response data, and me not fully understanding how tuples work in regards to Ellipses. I'm sure this is easy to figure out, I simply don't have enough time this week. Enough excuses, you be the judge.

### Components:
The project is made up of 3 main components:

* compose: The api and db portions were originally scripting out in docker compose, and the tweaked to work independently and become deployable to kubernetes.
* test: A simple test.py script that accepts the data.csv input. It expects the input format to always match the data.csv example input format: 
   $ python3 test.py data.csv
* k8s: Basic kubernetes manifest files to deploy the built dockerhub images to an existing kubernetes cluster.
