"""

这个文件用来根据用户输入来抽取实体、转换向量数据等操作数据库操作前、后的处理工作
也包括prompt设置、让大模型生成知识图谱等操作
但这个文件不直接操作数据库

"""

from ast import List
from transformers import AutoTokenizer, AutoModel
import torch
from huggingface_hub import hf_hub_download
from llmragenv.LLM.llm_base import LLMBase
from database.vector.vector_database import VectorDatabase
from llama_index.core.utils import print_text
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.schema import NodeWithScore, QueryBundle
from llama_index.core.retrievers import (
    # KnowledgeGraphRAGRetriever,
    VectorIndexRetriever,
)
from llama_index.core import (
    VectorStoreIndex,
    # SimpleDirectoryReader,
    # Document,
    StorageContext,
    load_index_from_storage,
)


class RetrieverVector(object):

    def __init__(self, llm: LLMBase, vectordb: VectorDatabase):
        self.vector_database = vectordb
        self._llm = llm

    def format_chunks(self, retrieval_results):
        formatted_string = ""
        for i, chunk in enumerate(retrieval_results, 1):
            formatted_string += f"Chunk{i}: {chunk}\n"
        return formatted_string

    def retrieve(self, question):
        retrieval_result = []
        embedding = self.vector_database.embed_model.get_text_embedding(question)
        nodes = self.vector_database.retrieve_nodes(question, embedding)
        for node in nodes:
            retrieval_result.append(node.text)

        # formatted_string = format_chunks(retrieval_result)
        # print(formatted_string)

        return retrieval_result
