https://towardsdatascience.com/question-answering-with-a-fine-tuned-bert-bc4dafd45626

What are Hugging Face and Transformers? 🤔

Hugging Face is an open-source provider of natural language processing (NLP) technologies. You can use hugging face state-of-the-art models to build, train and deploy your own models. Transformers is their NLP library. I highly recommend you to check out the amazing work done by the Hugging Face team and their huge collection of pre-trained NLP models.

What is CoQA? 🤔

CoQA is a Conversational Question Answering dataset released by Stanford NLP in 2019. It is a large-scale dataset for building Conversational Question Answering Systems. This dataset aims to measure the ability of machines to understand a text passage and answer a series of interconnected questions that appear in a conversation. The unique feature about this dataset is that each conversation is collected by pairing two crowd workers to chat about a passage in the form of questions and answers and hence, the questions are conversational. To understand the format of the JSON data, please refer to this link. We will be using the story, question, and answer from the JSON dataset to form our data frame.

What is BERT? 🤔

BERT is a Bidirectional Encoder Representations from Transformers. It is one of the most popular and widely used NLP models. BERT models can consider the full context of a word by looking at the words that come before and after it, which is particularly useful for understanding the intent behind the query asked. Because of its bidirectionality, it has a deeper sense of language context and flow and hence, is used in a lot of NLP tasks nowadays. More details about BERT in the article along with the code.🙃

Transformers library has a lot of different BERT models. It is easy to find a task-specific model from this library and do our task.

## Get Started

What is Conda? Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language.

- `conda create --name ki python=3.9`
- `conda activate ki`
- `conda install -c huggingface transformers`
- Open VSCode, open the command palette (CTRL+SHIFT+P) then select `Python: Select Interpreter` and select the `ki` virtual environment
