# Command line chatbot 

Dataset: https://github.com/nailson/ifood-data-business-analyst-test/blob/master/ml_project1_data.csv

Dictionary: https://github.com/nailson/ifood-data-business-analyst-test/blob/master/dictionary.png

## Set up

Ensure you have python 3.10.3 installed (any version <3.11 should be fine). Then, create a new python virtual env using:

```
python -m venv .venv
```

Then activate the env:

```
source ./.venv/bin/activate
```

### Install dependencies

You can install dependencies using pip from requirement.txt

```
pip install -r requirements.txt
```

### Run the chat

Once all dependencies are installed, you can run the app using python:

```
OPENAI_API_KEY=$YOUR_OPENAI_KEY python run.py
```

### Constraints

1. Note that I have used GPT-4 model for this. If you don't have access to GPT-4, then you can change the code to use GPT-3.5 but in some cases GPT-3.5 performs worse than GPT-4. 
2. I did not keep history of the chat. Kept it simple for this exercise.
3. Chat interface itself is a simple stdin/stdout loop. 

### Some example prompts that I tried with screenshots

1. Which user has spent the most on meat products?

![Which user has spent the most on meat products?](./images/Screenshot%202023-10-16%20at%2014.14.33.png)


2. Who has spent the most on edible products?

![Who has spent the most on edible products?](./images/Screenshot%202023-10-16%20at%2014.16.30.png)


3. Provide list of users who are married and graduates

![Provide list of users who are married and graduates](./images/Screenshot%202023-10-16%20at%2014.18.23.png)


4. Provide some marketing strategies to target the younger users

![Provide some marketing strategies to target the younger users](./images/Screenshot%202023-10-16%20at%2014.23.49.png)

5. Create a bar chart for education. Do not plot it, create a png and save it in current directory


![Create a bar chart for education. Do not plot it, create a png and save it in current directory](./images/Screenshot%202023-10-16%20at%2014.24.57.png)

![Bar chart on education](./images/Screenshot%202023-10-16%20at%2014.42.20.png)










