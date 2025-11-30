# Random number generator microservice for CS361 group.

This microservice has the option of generating a random number given a range, or generating a list of random numbers given a range.
ZeroMQ is used for communication.

## Running The Microservice
Install ZeroMQ: 
```
pip install pyzmq
```
+ Run app.py
+ Service runs on tcp://localhost:4000
+ Output should read:
```
"Random number generator microservice running on port 4000"
```

## Communication
1. Generate a Single Random Number
  - Request:
   ```
   {
     "method": "rand",
     "params": {"min": 1, "max": 100}
   }
   ```
  - Response:
  ```
  15
  ```

2. Generate a List of Random Numbers
  - Request:
   ```
   {
     "method": "rand_list",
     "params": {"min": 1, "max": 100, "count": 3}
   }
   ```
  - Response:
  ```
  [9, 78, 52]
  ```
