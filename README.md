# -Office-Jokes---A-RAG-Application-with-Qdrant
# Description:

This project builds a Retrieval-Augmented Generation (RAG) application using the Qdrant vector database. It utilizes a dataset of "The Office" dialogues to train an LLM to generate jokes and text in the style of the show's characters. Retrieval-augmented generation (RAG) is an AI framework for improving the quality of LLM-generated responses by grounding the model on external sources of knowledge to supplement the LLM’s internal representation of information.

"The Office" is renowned for its quirky characters, hilarious dialogues, and memorable jokes. This project leverages advanced technologies to capture the essence of the show's humor and generate new content that mimics the style of the characters.

**Key Features**:

**Langchain**:LangChain is an open source framework that lets software developers working with artificial intelligence (AI) and its machine learning subset combine large language models with other external components to develop LLM-powered applications. The goal of LangChain is to link powerful LLMs, such as OpenAI's GPT-3.5 and GPT-4, to an array of external data sources to create and reap the benefits of natural language processing (NLP) applications.

**Qdrant Cloud**: Qdrant's hosted cloud service is utilized for configuring a free cluster and deploying the vector database to the cloud. Qdrant provides powerful features for efficient storage and retrieval of vector embeddings. Qdrant is a vector database & vector similarity search engine

**RAG**: Retrieval-Augmented Generation. It's a natural language processing (NLP) technique that combines generative- and retrieval-based artificial intelligence (AI) models to improve the output of large language models (LLMs). RAG uses external data sources, like knowledge bases, to generate responses that reference an authoritative source outside of the LLM's training data sources. This can lead to more accurate AI responses that are also context-aware and human-like.

**Gemini Pro API**: This API unlocks the capabilities of Google's advanced large language model (LLM), Gemini Pro. It empowers the project to generate creative text formats and manipulate language in innovative ways.

![image](https://github.com/AKashkv02/-Office-Jokes---A-RAG-Application-with-Qdrant/assets/107745951/d5a04b17-621b-4e19-b412-47d605ca94f7)

![image](https://github.com/AKashkv02/-Office-Jokes---A-RAG-Application-with-Qdrant/assets/107745951/9103590e-5874-4a89-aaf9-0df466779679)


Here's a summary of how retrieval chains from Langchain are used to create Michael Scott-style jokes:

1. **Building the Prompt**:

Prompt Template: A pre-defined text format (ChatPromptTemplate) sets the overall structure and tone for the joke. It includes elements like Michael Scott's personality traits (self-importance, early 2000s pop culture references), desired humor style (inappropriate, cringe-worthy), and placeholders for context and the user's question.

2. **Retrieval Chain**:

User Inquiry: The user enters a topic for the joke.

Document Retrieval: This part leverages Langchain's create_retrieval_chain function. It retrieves relevant documents (likely pre-stored examples of Michael Scott quotes or dialogues) from a vector store based on the user's topic. The vector store uses embeddings to efficiently find documents similar to the topic.

Enriched Prompt: The retrieved documents are combined with the user's question and inserted into the prompt template. This creates a richer context for the Large Language Model (LLM) to understand the desired humor style and topic.

3. **Joke Generation**:

LLM Processing: The enriched prompt is sent to the LLM (e.g., Gemini-Pro). The LLM generates a response based on the prompt's instructions and its knowledge. In this case, it aims to create a joke in Michael Scott's style that's relevant to the user's topic.
Benefits of Retrieval Chains:

Contextual Humor: By providing relevant context through retrieved documents, the LLM can generate jokes more aligned with Michael Scott's character and the user's chosen topic.
Improved Relevance: Retrieval chains ensure that the generated jokes are at least somewhat related to the user's input, avoiding completely off-topic responses.

Overall, retrieval chains enhance the joke generation process by providing the LLM with richer context and relevant information, leading to a higher chance of it creating humor that captures Michael Scott's essence and aligns with the user's chosen theme.

