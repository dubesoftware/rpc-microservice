# RPC-Microservice
A Python RPC microservice implemented with [*Nameko*](https://nameko.readthedocs.io/en/stable/).

## Synopsis
The service consists of the AcmeRPCMicroservice class which implements the following three methods:
```
square_odd_numbers: 		- squares each odd number in a given list of integers,
huffman_encode_strings: 	- builds a dictionary of strings - the key being the original string, and the value being a (Huffman) encoded version of that string, and
decode_huffman_encoded_string:	- decodes a given string previously Huffman encoded and latin1 decoded.
```

## Thoughts
The task provides good exposure to the microservice ecosystem and affords the engineer an opportunity to experience and attempt to solve real-world messaging challenges in that space. For the uninitiated to RPC messaging, this provides great opportunities to research solutions to some of the most common pain points, such as handling character encoding.

## Pros (and cons) of technologies used
### [*Nameko*](https://nameko.readthedocs.io/en/stable/), [*RabbitMQ*](https://www.rabbitmq.com/) and [*Docker*](https://www.docker.com/).:
Nameko appears to be the most widely used Python library for RPC microservice implementation. This adoption means that it is actively developed. Nameko keeps the design clean by encouraging dependency injection and providing a simple API. A con of Nameko is that documentation is somewhat sparse at the time of writing. This means lots of Googling and, with more time, one would be diving into the source to see what happens under the hood.

RabbitMQ is a battle-tested message queueing technology with ample documentation, a thriving user community and an abundance of tutorials. From a technical perspective, RabbitMQ is fairly friendly to set up and run and it is capable of handling large volumes of data.

Docker is useful for running lightweight (compared to virtual machines) images in isolated environments. Using it, I could see the benefit in not having a hypervisor policing resource usage between a host operating system and a container. One caveat would be that I found it non-trivial to run an image inside another image (for RabbitMQ) by specifying this in a Dockerfile. This ultimately came down to my relative lack of exposure to Docker at the time of writing, rather than any fault with it.

## Decisions, decisions
Having never implemented an RPC service before, I approached this task as a research project. I Googled a lot for reference implementations and spent a fair amount of time scouring developer forums. Getting feedback was much slower than normal, which could be a result of the worldwide pandemic keeping people busier with other concerns.

Design-wise, I decided to keep the code as modular as possible. This meant defining a single class in a single module with no auxiliary dependency modules and implementing code reuse via object orientation and separation of concerns. This also helped with unit testing. I decided to forego integration testing as I felt that it would introduce cognitive load that would detract from the core requirements within the scope of the project. I kept the code as Pythonic as possible, with adherence to PEP 8 guidelines as much as possible. This helps readability and documentation.

With regards to data formats, JSON is used to send data to and from the service. This is a widely adopted standard for communication between disparate systems and also allows other clients which do not implement the RPC protocol to consume the service. A testing strategy would be to use [*cURL*](https://curl.haxx.se/) to send requests to the containerised service from a terminal.

Please note that the LOC weigh in at ~54, of which ~30 are docstrings. This leaves the actual executable source within the recommended 30 LOC at around ~24. Method chaining delivers a benefit here, although often, especially when debugging, it ought to be used with caution.

Additionally, I kept each method modular and free of side effects by avoiding altering state. Finally, no exception handling is implemented. I believe that this would be for the client of the service to implement, unless the service itself were talking to other services - in which case exception handling and logging could be implemented. I actively worked to stay within the scope of the project and avoided scope creep.

## Timelines
One key takeaway from this project is to always hit the ground running on tasks, especially for unfamiliar technologies. Although I was multiplexing this with study commitments, I did spend ~5 hours researching and implementing the actual service code. All other time (>12 hours) was spent (a) researching a blocker with character encoding, and (b) learning to Dockerize - for my first ever ground-up Docker build. This part of the project is ongoing at the time of writing. In hindsight, I would implement the solution as early as possible and leave ample room to handle unforeseen challenges well within stipulated timelines.
